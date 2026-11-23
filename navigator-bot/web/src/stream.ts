/**
 * Reads the bot's reply as it streams in. The server speaks the AI SDK UI message stream protocol
 * (Server-Sent Events, one JSON chunk per `data:` line); only the text parts matter here.
 */

export interface StreamChunk {
  type: string;
  delta?: string;
  errorText?: string;
}

/** Parse one SSE `data:` payload; undefined for comments, keep-alives and the final [DONE]. */
export function parseLine(line: string): StreamChunk | undefined {
  if (!line.startsWith("data:")) return undefined;
  const payload = line.slice(5).trim();
  if (!payload || payload === "[DONE]") return undefined;
  try {
    const chunk = JSON.parse(payload) as unknown;
    return chunk && typeof chunk === "object" && typeof (chunk as StreamChunk).type === "string"
      ? (chunk as StreamChunk)
      : undefined;
  } catch {
    return undefined;
  }
}

/** Calls onText with the whole reply so far each time more text arrives; returns the full reply. */
export async function readReply(
  body: ReadableStream<Uint8Array>,
  onText: (text: string) => void,
): Promise<string> {
  const reader = body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let text = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";
    for (const line of lines) {
      const chunk = parseLine(line.trimEnd());
      if (chunk?.type === "text-delta" && typeof chunk.delta === "string") {
        text += chunk.delta;
        onText(text);
      } else if (chunk?.type === "error") {
        throw new Error(chunk.errorText || "stream error");
      }
    }
  }
  const last = parseLine(buffer.trimEnd());
  if (last?.type === "text-delta" && typeof last.delta === "string") {
    text += last.delta;
    onText(text);
  }
  return text;
}
