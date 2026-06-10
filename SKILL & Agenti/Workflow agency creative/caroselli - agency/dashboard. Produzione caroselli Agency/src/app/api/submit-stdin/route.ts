import { NextResponse } from "next/server";

interface GlobalProcessState {
  activeProcess: any | null;
  processStatus: "idle" | "running" | "setup_arena" | "setup_drive";
  lastTopic: string;
}

const globalState = global as unknown as {
  processState?: GlobalProcessState;
};

export async function POST() {
  const state = globalState.processState;

  if (!state || !state.activeProcess) {
    return NextResponse.json({ error: "Nessun processo attivo che richieda input stdin." }, { status: 400 });
  }

  try {
    console.log("[Dashboard Backend] Invio invio (newline) a stdin del processo Python...");
    state.activeProcess.stdin.write("\n");
    return NextResponse.json({ success: true, message: "Comando di completamento inviato!" });
  } catch (error: any) {
    return NextResponse.json({ error: `Impossibile scrivere a stdin: ${error.message}` }, { status: 500 });
  }
}
