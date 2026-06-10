import { NextResponse } from "next/server";
import { spawn } from "child_process";
import fs from "fs";
import path from "path";

const STATE_FILE = path.join(process.cwd(), "process-state.json");
const LOG_FILE   = path.join(process.cwd(), "outreach-live.log");

let activeProcess: ReturnType<typeof spawn> | null = null;

function saveState(state: object) {
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

function getModeScript(mode: string): string {
  const outreachDir = path.join(process.cwd(), "..", "Outreach Workflow");
  const scriptMap: Record<string, string> = {
    email:           path.join(outreachDir, "run.py"),
    instagram:       path.join(outreachDir, "..", "Instagram Automation", "run_today.py"),
    linkedin:        path.join(outreachDir, "..", "LinkedIn Automation", "run_today.py"),
    "email+instagram": path.join(outreachDir, "run_parallel.py"),
    all:             path.join(outreachDir, "run_parallel.py"),
  };
  return scriptMap[mode] || path.join(outreachDir, "run.py");
}

function getModeArgs(mode: string, target: number): string[] {
  if (mode === "email")           return ["--target", String(target)];
  if (mode === "email+instagram") return ["--mode", "email+instagram", "--target", String(target)];
  if (mode === "all")             return ["--mode", "all", "--target", String(target)];
  return [];
}

export async function POST(req: Request) {
  const { mode, target = 150 } = await req.json();

  if (activeProcess && activeProcess.exitCode === null) {
    return NextResponse.json({ error: "Processo già in esecuzione" }, { status: 409 });
  }

  const script = getModeScript(mode);
  const args   = getModeArgs(mode, target);
  const cwd    = path.dirname(script);

  // Clear log
  fs.writeFileSync(LOG_FILE, "");

  const state = {
    process: { mode, status: "running", startTime: new Date().toISOString(), exitCode: null, logFile: LOG_FILE },
    stats: { email: { sent: 0, total: 0 }, ig: { dmToday: 0, f1Today: 0, total: 0 } },
  };
  saveState(state);

  // Demo mode if script doesn't exist
  if (!fs.existsSync(script)) {
    const demoMsgs = [
      `[SYSTEM] ═══════════════════════════════════`,
      `[SYSTEM] Dashboard Outreach Engine v3.0`,
      `[SYSTEM] Modalità: ${mode.toUpperCase()} | Target: ${target}`,
      `[SYSTEM] ═══════════════════════════════════`,
      `[EMAIL-GEN] Avvio scraping Google Maps...`,
      `[SCRAPER] Cercando: fisioterapista Milano`,
      `[EXTRACTOR] Estratto: info@studio-fisio.it (score: 0.85)`,
      `[QUALIFIER] Lead qualificato — fisioterapista ✓ score: 8.4/10`,
      `[WRITER] Generando email APSOC+V personalizzata...`,
      `[EMAIL-INVIA] ✓ Email inviata a: mario.rossi@fisiolab.it`,
      `[EMAIL-GEN] Processando lead 2/${target}...`,
      `[QUALIFIER] Lead qualificato — avvocato ✓ score: 7.9/10`,
      `[WRITER] Email generata con framework Barnum/Rainbow`,
      `[EMAIL-INVIA] ✓ Email inviata a: studio@legalepartners.it`,
      `[SISTEMA] ═══ COMPLETATO ═══ ${target} email processate`,
    ];

    const logStream = fs.createWriteStream(LOG_FILE, { flags: "a" });
    let i = 0;
    const iv = setInterval(() => {
      if (i < demoMsgs.length) {
        logStream.write(demoMsgs[i++] + "\n");
      } else {
        clearInterval(iv);
        logStream.end();
        state.process.status = "done";
        state.process.exitCode = 0;
        saveState(state);
      }
    }, 600);

    return NextResponse.json({ ok: true, demo: true });
  }

  const logStream = fs.createWriteStream(LOG_FILE, { flags: "a" });

  activeProcess = spawn("python", [script, ...args], {
    cwd,
    stdio: ["ignore", "pipe", "pipe"],
    env: { ...process.env, PYTHONUNBUFFERED: "1", PYTHONIOENCODING: "utf-8" },
  });

  activeProcess.stdout?.on("data", (chunk: Buffer) => logStream.write(chunk));
  activeProcess.stderr?.on("data", (chunk: Buffer) => logStream.write(chunk));
  activeProcess.on("close", (code: number | null) => {
    logStream.end();
    state.process.status = code === 0 ? "done" : "error";
    state.process.exitCode = code;
    saveState(state);
    activeProcess = null;
  });

  return NextResponse.json({ ok: true, pid: activeProcess.pid });
}
