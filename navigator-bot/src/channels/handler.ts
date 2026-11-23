/**
 * The bridge between Chat SDK and the conversation: every channel's messages arrive here.
 *
 * 1. The message is written to the inbox (restart safety), unless it is already there (a repeat delivery).
 * 2. A typing indicator is shown (WhatsApp also marks the message read).
 * 3. The conversation works out the reply, which is posted as Markdown; each adapter converts it.
 * 4. The inbox entry is deleted.
 *
 * Messages that arrive while the previous one is being answered are handed over together by Chat SDK
 * (`context.skipped`); they are answered as one question, so nothing is lost.
 */
import type { Message, MessageContext, Thread } from "chat";
import { detectLang, MESSAGES } from "../conversation/i18n.ts";
import type { Conversation, IncomingMessage } from "../conversation/pipeline.ts";
import type { Inbox } from "../memory/inbox.ts";
import { type Channel, userKey } from "../memory/store.ts";
import { describeError, logger } from "../ops/logger.ts";

export interface HandlerDeps {
  conversation: Conversation;
  inbox: Inbox;
  userHashSecret: string;
  /** Web only: the hashed IP address of the request that carried a message. */
  ipKeyFor?: (threadId: string) => string | undefined;
  onError?: (err: unknown, channel: Channel) => void;
}

export function channelOf(threadId: string): Channel | undefined {
  const prefix = threadId.split(":")[0];
  return prefix === "whatsapp" || prefix === "telegram" || prefix === "web" ? prefix : undefined;
}

/** What the person sent, as the conversation sees it. */
export function toIncoming(
  channel: Channel,
  key: string,
  messages: readonly Pick<Message, "text" | "attachments">[],
  ipKey?: string,
): IncomingMessage {
  const texts = messages.map((m) => m.text.trim()).filter(Boolean);
  const base = { channel, userKey: key, ...(ipKey ? { ipKey } : {}) };
  if (texts.length === 0) return { ...base, kind: "other" };
  return { ...base, kind: "text", text: texts.join("\n") };
}

export class MessageHandler {
  private readonly deps: HandlerDeps;

  constructor(deps: HandlerDeps) {
    this.deps = deps;
  }

  /** Chat SDK's onDirectMessage handler. */
  async onMessage(thread: Thread, message: Message, context?: MessageContext): Promise<void> {
    const channel = channelOf(thread.id);
    if (!channel || message.author.isMe) return;
    const key = userKey(`${channel}:${message.author.userId}`, this.deps.userHashSecret);
    const all = [...(context?.skipped ?? []), message];
    const incoming = toIncoming(channel, key, all, this.deps.ipKeyFor?.(thread.id));
    const inboxId = `${channel}:${message.id}`;
    const fresh = await this.deps.inbox.receive({
      id: inboxId,
      channel,
      threadId: thread.id,
      userKey: key,
      text: incoming.text ?? "",
    });
    if (!fresh) return; // already being answered (a repeat delivery)
    if (channel !== "web") void thread.startTyping().catch(() => undefined);
    await this.answer(thread, incoming, inboxId);
  }

  /** Telegram's /start, /reset and /delete arrive as commands rather than messages. */
  async onCommand(
    post: (text: string) => Promise<unknown>,
    channel: Channel,
    authorId: string,
    command: string,
  ) {
    const key = userKey(`${channel}:${authorId}`, this.deps.userHashSecret);
    const reply = await this.deps.conversation.handle({ channel, userKey: key, kind: "text", text: command });
    if (reply) await post(reply.text);
  }

  /** Answer one incoming message and post the reply. Used live and when replaying after a restart. */
  async answer(thread: Pick<Thread, "post">, incoming: IncomingMessage, inboxId: string): Promise<void> {
    try {
      const reply = await this.deps.conversation.handle(incoming);
      if (reply) await thread.post({ markdown: reply.text });
      await this.deps.inbox.done(inboxId);
    } catch (err) {
      logger.error({ err: describeError(err), channel: incoming.channel }, "Could not answer a message");
      this.deps.onError?.(err, incoming.channel);
      // Tell the person something went wrong, if the channel still works; the inbox keeps the message
      // so it is answered again after a restart.
      const lang = detectLang(incoming.text ?? "");
      await thread.post({ markdown: MESSAGES[lang].error }).catch(() => undefined);
    }
  }
}
