import { NextRequest, NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const PROJECT_DIR = path.resolve(process.cwd(), "..");

const ALLOWED_FILES: Record<string, string> = {
  prompt: "Template-prompt.md",
  regole: "REGOLE.md",
  config: "config.py",
};

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const fileKey = searchParams.get("file");

  if (!fileKey || !ALLOWED_FILES[fileKey]) {
    return NextResponse.json({ error: "File richiesto non valido o non consentito." }, { status: 400 });
  }

  try {
    const filePath = path.join(PROJECT_DIR, ALLOWED_FILES[fileKey]);
    if (!fs.existsSync(filePath)) {
      return NextResponse.json({ content: "" });
    }

    const content = fs.readFileSync(filePath, "utf-8");
    return NextResponse.json({ content });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { fileKey, content } = body;

    if (!fileKey || !ALLOWED_FILES[fileKey]) {
      return NextResponse.json({ error: "File non valido o non consentito per il salvataggio." }, { status: 400 });
    }

    if (content === undefined) {
      return NextResponse.json({ error: "Il contenuto non può essere vuoto." }, { status: 400 });
    }

    const filePath = path.join(PROJECT_DIR, ALLOWED_FILES[fileKey]);
    
    // Scrivi e salva il file
    fs.writeFileSync(filePath, content, "utf-8");

    return NextResponse.json({ success: true, message: `File ${ALLOWED_FILES[fileKey]} salvato con successo!` });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
