import { NextRequest, NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const PROJECT_DIR = path.resolve(process.cwd(), "..");
const LOG_FILE = path.join(PROJECT_DIR, "workflow_live.log");

export async function GET(req: NextRequest) {
  try {
    if (!fs.existsSync(LOG_FILE)) {
      return NextResponse.json({ logs: "Nessun log disponibile. Avvia un'automazione per iniziare." });
    }

    const logs = fs.readFileSync(LOG_FILE, "utf-8");
    return NextResponse.json({ logs });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// Endpoint opzionale per cancellare i log
export async function DELETE() {
  try {
    if (fs.existsSync(LOG_FILE)) {
      fs.writeFileSync(LOG_FILE, "");
    }
    return NextResponse.json({ success: true, message: "Console ripulita." });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
