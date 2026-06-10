import { spawn, ChildProcess } from "child_process";
import path from "path";

// Paths relativi alla root del progetto Next.js (outreach-dashboard-premium/)
const PROJECT_ROOT = process.cwd(); // outreach-dashboard-premium/
const OUTREACH_ROOT = path.resolve(PROJECT_ROOT, ".."); // Outreach/
const OUTREACH_WORKFLOW = path.join(OUTREACH_ROOT, "Outreach Workflow");
const INSTAGRAM_AUTO = path.join(OUTREACH_ROOT, "Instagram Automation");

export const DATA_PATHS = {
  emailLogDir: path.join(OUTREACH_WORKFLOW, "output"),
  igLeads: path.join(INSTAGRAM_AUTO, "instagram_leads.json"),
};

type Status = "idle" | "running" | "done" | "error";
type LogListener = (line: string) => void;

interface State {
  proc: ChildProcess | null;
  mode: string;
  startTime: Date | null;
  status: Status;
  exitCode: number | null;
  logs: string[];
}

// Singleton module-level (funziona in Next.js dev — un solo processo Node)
const state: State = {
  proc: null,
  mode: "",
  startTime: null,
  status: "idle",
  exitCode: null,
  logs: [],
};
const listeners = new Set<LogListener>();
const MAX_LOGS = 800;

function push(line: string) {
  state.logs.push(line);
  if (state.logs.length > MAX_LOGS) state.logs.shift();
  listeners.forEach((fn) => {
    try { fn(line); } catch { /* client disconnesso */ }
  });
}

export function getState() {
  return {
    mode: state.mode,
    startTime: state.startTime?.toISOString() ?? null,
    status: state.status,
    exitCode: state.exitCode,
    logCount: state.logs.length,
  };
}

export function getLogs(): string[] {
  return [...state.logs];
}

export function subscribe(fn: LogListener): () => void {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export function stopProcess() {
  if (state.proc && state.status === "running") {
    state.proc.kill("SIGTERM");
    push("[DASHBOARD] Processo fermato manualmente.");
  }
}

// ── Configurazioni di lancio ──────────────────────────────────────────────────

const CONFIGS: Record<string, { cwd: string; args: string[]; label: string }> = {
  email: {
    cwd: OUTREACH_WORKFLOW,
    args: ["run.py", "--target", "150"],
    label: "EMAIL",
  },
  instagram: {
    cwd: INSTAGRAM_AUTO,
    args: ["run_today.py"],
    label: "INSTAGRAM",
  },
  linkedin: {
    cwd: OUTREACH_ROOT,
    args: ["run_linkedin_only.py"],
    label: "LINKEDIN",
  },
  "email+instagram": {
    cwd: OUTREACH_ROOT,
    args: ["run_ig_email.py"],
    label: "EMAIL + INSTAGRAM",
  },
  all: {
    cwd: OUTREACH_ROOT,
    args: ["run_parallel.py"],
    label: "TUTTO",
  },
};

export function launchProcess(
  mode: string,
  target?: number
): { ok: boolean; error?: string } {
  if (state.status === "running") {
    return { ok: false, error: "Processo già in corso. Fermalo prima." };
  }

  const cfg = CONFIGS[mode];
  if (!cfg) return { ok: false, error: `Modalità sconosciuta: ${mode}` };

  // Override target per email
  const args = [...cfg.args];
  if (mode === "email" && target) {
    const idx = args.indexOf("150");
    if (idx > -1) args[idx] = String(target);
  }

  // Reset stato
  state.logs = [];
  state.mode = mode;
  state.startTime = new Date();
  state.status = "running";
  state.exitCode = null;

  const separator = "═".repeat(56);
  push(separator);
  push(`  MODALITÀ: ${cfg.label}`);
  push(`  START: ${new Date().toLocaleTimeString("it-IT")}`);
  push(`  CMD: python ${args.join(" ")}`);
  push(separator);

  const proc = spawn("python", args, {
    cwd: cfg.cwd,
    shell: true,
    env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUNBUFFERED: "1" },
  });

  state.proc = proc;

  const handleData = (data: Buffer) => {
    const lines = data.toString("utf8").split(/\r?\n/);
    lines.forEach((l) => { if (l.trim()) push(l); });
  };

  proc.stdout?.on("data", handleData);
  proc.stderr?.on("data", handleData);

  proc.on("exit", (code) => {
    state.status = code === 0 ? "done" : "error";
    state.exitCode = code;
    state.proc = null;
    push(separator);
    push(
      code === 0
        ? `  ✓ COMPLETATO con successo — exit 0`
        : `  ✗ TERMINATO con errori — exit ${code}`
    );
    push(separator);
  });

  proc.on("error", (err) => {
    state.status = "error";
    state.proc = null;
    push(`[ERRORE AVVIO] ${err.message}`);
  });

  return { ok: true };
}
