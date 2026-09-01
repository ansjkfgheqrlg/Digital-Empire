import { NextRequest, NextResponse } from "next/server";
import { spawn } from "child_process";
import path from "path";
import fs from "fs";

const PROJECT_DIR = path.resolve(process.cwd(), "..");
const LOG_FILE = path.join(PROJECT_DIR, "workflow_live.log");

// Definiamo un tipo globale per persistere lo stato del processo
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
    const { topic, visible } = body;

    if (!topic || topic.trim() === "") {
      return NextResponse.json({ error: "L'argomento (topic) è obbligatorio." }, { status: 400 });
    }

    state.processStatus = "running";
    state.lastTopic = topic;

    // Pulisci o prepara il file di log
    fs.writeFileSync(LOG_FILE, `--- AVVIO GENERAZIONE CAROSELLO IN CORSO ---\nArgomento: ${topic}\nBrowser Visibile: ${visible ? "Sì" : "No"}\n\n`);

    const args = ["main_orchestrator.py", "--topic", topic];
    if (visible) {
      args.push("--visible");
    }

    console.log(`[Dashboard Backend] Spawning: python ${args.join(" ")} in ${PROJECT_DIR}`);
    const pyProcess = spawn("python", args, {
      cwd: PROJECT_DIR,
      env: { ...process.env, PYTHONUNBUFFERED: "1" }, // Garantisce flussi live non bufferizzati
    });

    state.activeProcess = pyProcess;

    pyProcess.stdout.on("data", (data) => {
      fs.appendFileSync(LOG_FILE, data.toString());
    });

    pyProcess.stderr.on("data", (data) => {
      fs.appendFileSync(LOG_FILE, data.toString());
    });

    pyProcess.on("close", (code) => {
      console.log(`[Dashboard Backend] Python completato con codice di uscita: ${code}`);
      fs.appendFileSync(LOG_FILE, `\n--- WORKFLOW CONCLUSO CON CODICE: ${code} ---\n`);
      state.activeProcess = null;
      state.processStatus = "idle";
    });

    return NextResponse.json({ success: true, message: "Generazione avviata con successo!" });
  } catch (error: any) {
    state.activeProcess = null;
    state.processStatus = "idle";
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

export async function GET() {
  const state = globalState.processState!;
  return NextResponse.json({
    status: state.processStatus,
    lastTopic: state.lastTopic,
    isRunning: state.activeProcess !== null,
  });
}
