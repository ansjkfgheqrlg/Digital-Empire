import { NextResponse } from "next/server";
import { exec } from "child_process";
import fs from "fs";
import path from "path";

const STATE_FILE = path.join(process.cwd(), "process-state.json");

export async function POST() {
  exec("taskkill /F /IM python.exe /T", () => {
    try {
      if (fs.existsSync(STATE_FILE)) {
        const state = JSON.parse(fs.readFileSync(STATE_FILE, "utf-8"));
        state.process.status = "idle";
        state.process.exitCode = -1;
        fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
      }
    } catch {}
  });
  return NextResponse.json({ ok: true });
}
