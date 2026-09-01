import { NextRequest, NextResponse } from "next/server";
import { spawn } from "child_process";
import path from "path";
import fs from "fs";

const PROJECT_DIR = path.resolve(process.cwd(), "..");
const LOG_FILE = path.join(PROJECT_DIR, "workflow_live.log");

interface GlobalProcessState {
  activeProcess: any | null;
  processStatus: "idle" | "running" | "setup_arena" | "setup_drive";
  lastTopic: string;
}

const globalState = global as unknown as {
  processState?: GlobalProcessState;
};

if (!globalState.processState) {
  globalState.processState = {
    activeProcess: null,
    processStatus: "idle",
    lastTopic: "",
  };
}

export async function POST(req: NextRequest) {
  const state = globalState.processState!;

  if (state.processStatus !== "idle") {
    return NextResponse.json(
      { error: `Un processo è già in corso: ${state.processStatus}` },
      { status: 400 }
    );
  }

  try {
    const body = await req.json();
    const { target } = body; // 'arena' o 'drive'

    if (target !== "arena" && target !== "drive") {
      return NextResponse.json({ error: "Target non valido. Deve essere 'arena' o 'drive'." }, { status: 400 });
    }

    state.processStatus = target === "arena" ? "setup_arena" : "setup_drive";

    fs.writeFileSync(
      LOG_FILE,
      `--- AVVIO SETUP SESSIONE ${target.toUpperCase()} ---\n` +
      `Apertura del browser in corso...\n` +
      `Si prega di completare l'autenticazione nel browser visualizzato sullo schermo.\n\n`
    );

    const scriptPath = target === "arena"
      ? path.join("ArenaAI", "setup_arena_session.py")
      : path.join("GoogleDrive", "setup_drive_session.py");

    console.log(`[Dashboard Backend] Spawning Setup: python ${scriptPath}`);
    const setupProcess = spawn("python", [scriptPath], {
      cwd: PROJECT_DIR,
      env: { ...process.env, PYTHONUNBUFFERED: "1" },
    });

    state.activeProcess = setupProcess;

    setupProcess.stdout.on("data", (data) => {
      fs.appendFileSync(LOG_FILE, data.toString());
    });

    setupProcess.stderr.on("data", (data) => {
      fs.appendFileSync(LOG_FILE, data.toString());
    });

    setupProcess.on("close", (code) => {
      console.log(`[Dashboard Backend] Setup ${target} terminato con codice: ${code}`);
      fs.appendFileSync(LOG_FILE, `\n--- SETUP SESSIONE TERMINATO CON CODICE: ${code} ---\n`);
      state.activeProcess = null;
      state.processStatus = "idle";
    });

    return NextResponse.json({ success: true, message: `Browser di Setup ${target} aperto sul desktop!` });
  } catch (error: any) {
    state.activeProcess = null;
    state.processStatus = "idle";
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
