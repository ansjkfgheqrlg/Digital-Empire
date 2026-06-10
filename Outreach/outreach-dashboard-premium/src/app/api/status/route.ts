import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";

const STATE_FILE = path.join(process.cwd(), "process-state.json");

function readState() {
  try {
    if (fs.existsSync(STATE_FILE)) {
      return JSON.parse(fs.readFileSync(STATE_FILE, "utf-8"));
    }
  } catch {}
  return null;
}

function getDefaultState() {
  return {
    process: { mode: "", status: "idle", startTime: null, exitCode: null },
    stats: {
      email: { sent: 0, total: 0 },
      ig: { dmToday: 0, f1Today: 0, total: 0 },
    },
  };
}

function parseStatsFromLog(logContent: string) {
  const emailMatches = logContent.match(/email.*?inviata|inviata.*?email|✓ Email inviata/gi) || [];
  const igDmMatches = logContent.match(/\[DM\].*?inviato|DM inviato|dm.*?sent/gi) || [];

  let igTotal = 0;
  try {
    const igLeadsPath = path.join(process.cwd(), "..", "Instagram Automation", "instagram_leads.json");
    if (fs.existsSync(igLeadsPath)) {
      const leads = JSON.parse(fs.readFileSync(igLeadsPath, "utf-8"));
      igTotal = Array.isArray(leads) ? leads.length : Object.keys(leads).length;
    }
  } catch {}

  return {
    email: { sent: emailMatches.length, total: 0 },
    ig: { dmToday: igDmMatches.length, f1Today: 0, total: igTotal },
  };
}

export async function GET() {
  const saved = readState();
  if (!saved) return NextResponse.json(getDefaultState());

  if (saved.process?.logFile) {
    try {
      const logContent = fs.readFileSync(saved.process.logFile, "utf-8");
      saved.stats = parseStatsFromLog(logContent);
    } catch {}
  }

  return NextResponse.json(saved);
}
