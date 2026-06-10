import fs from "fs";
import path from "path";

export const dynamic = "force-dynamic";

const LOG_FILE = path.join(process.cwd(), "outreach-live.log");

export async function GET() {
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    start(controller) {
      controller.enqueue(
        encoder.encode(
          `data: ${JSON.stringify("[SYSTEM] Live Console connessa — in attesa di output...")}\n\n`
        )
      );

      let offset = 0;
      let closed = false;

      if (!fs.existsSync(LOG_FILE)) {
        fs.writeFileSync(LOG_FILE, "");
      }

      const interval = setInterval(() => {
        if (closed) { clearInterval(interval); return; }
        try {
          const stat = fs.statSync(LOG_FILE);
          if (stat.size > offset) {
            const fd = fs.openSync(LOG_FILE, "r");
            const buffer = Buffer.alloc(stat.size - offset);
            fs.readSync(fd, buffer, 0, buffer.length, offset);
            fs.closeSync(fd);
            offset = stat.size;
            const lines = buffer.toString("utf-8").split("\n").filter((l) => l.trim());
            for (const line of lines) {
              if (closed) break;
              controller.enqueue(encoder.encode(`data: ${JSON.stringify(line)}\n\n`));
            }
          }
        } catch {}
      }, 200);

      return () => { closed = true; clearInterval(interval); };
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      "Connection": "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}
