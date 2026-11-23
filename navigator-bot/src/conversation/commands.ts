/** Fixed commands, matched on the whole message (case and spaces ignored). */

export type Command = "delete" | "reset" | "start";

const COMMANDS: Record<Command, readonly string[]> = {
  delete: ["delete my data", "forget me", "আমার তথ্য মুছে দিন", "/delete"],
  reset: ["reset", "start over", "new question", "নতুন করে শুরু", "/reset"],
  start: ["/start"],
};

const GREETINGS = new Set([
  "hi",
  "hello",
  "hey",
  "salam",
  "assalamualaikum",
  "assalamu alaikum",
  "হাই",
  "হ্যালো",
  "সালাম",
  "আসসালামু আলাইকুম",
]);

function normalise(text: string): string {
  return text
    .normalize("NFC")
    .trim()
    .toLowerCase()
    .replace(/\s+/g, " ")
    .replace(/[!.?।]+$/u, "")
    .replace(/^(\/\w+)@\w+$/, "$1"); // Telegram's "/start@NavigatorBot"
}

export function parseCommand(text: string): Command | undefined {
  const t = normalise(text);
  for (const [command, words] of Object.entries(COMMANDS) as [Command, readonly string[]][]) {
    if (words.includes(t)) return command;
  }
  return undefined;
}

export function isGreeting(text: string): boolean {
  return GREETINGS.has(normalise(text));
}
