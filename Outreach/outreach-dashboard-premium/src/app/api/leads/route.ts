import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";

const OUTREACH_DIR = path.join(process.cwd(), "..", "Outreach Workflow");

interface RawLead {
  // actual field names from emails_ready.json / emails_b*.json
  page_name?: string;
  nome_attivita?: string; name?: string; azienda?: string;
  email?: string; to?: string;
  citta?: string; city?: string;
  telefono?: string; phone?: string;
  nicchia?: string; settore?: string; niche?: string;
  status?: string;
}

interface Lead {
  id: number; name: string; email: string;
  city: string; phone: string; niche: string; status: string;
}

function parseLeadsFromFiles(): Lead[] {
  const files = ["emails_ready.json", "emails_b4_ready.json", "emails_b6_ready.json"];
  const leads: Lead[] = [];
  let id = 1;

  for (const file of files) {
    const filePath = path.join(OUTREACH_DIR, file);
    if (!fs.existsSync(filePath)) continue;
    try {
      const raw = JSON.parse(fs.readFileSync(filePath, "utf-8"));
      const items: RawLead[] = Array.isArray(raw) ? raw : (raw.emails || raw.leads || []);
      for (const item of items) {
        const email = item.email || item.to || "";
        if (!email) continue;
        leads.push({
          id: id++,
          name: item.page_name || item.nome_attivita || item.name || item.azienda || "N/D",
          email,
          city: item.citta || item.city || "",
          phone: item.telefono || item.phone || "",
          niche: item.nicchia || item.settore || item.niche || "Generico",
          status: item.status === "sent" ? "Sent" : item.status === "error" ? "Failed" : "Ready",
        });
      }
    } catch {}
  }
  return leads;
}

const FALLBACK: Lead[] = [
  { id: 1, name: "Studio Fisioterapico Kinesis",  email: "info@kinesismilano.it",     city: "Milano", phone: "02 1234567",   niche: "Fisioterapista", status: "Ready"  },
  { id: 2, name: "FisioLab Milano",                email: "info@fisiolabmilano.it",    city: "Milano", phone: "02 4129 9227", niche: "Fisioterapista", status: "Sent"   },
  { id: 3, name: "Studio Legale Bianchi",           email: "info@studiobianchiroma.it", city: "Roma",   phone: "06 1234567",   niche: "Avvocato",       status: "Ready"  },
  { id: 4, name: "Studio Legale Rossi & Partners", email: "info@rossipartnersroma.it", city: "Roma",   phone: "06 7654321",   niche: "Avvocato",       status: "Ready"  },
  { id: 5, name: "Studio Legale Esposito",          email: "info@espositonapoli.it",    city: "Napoli", phone: "081 1234567",  niche: "Avvocato",       status: "Failed" },
];

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const search = (searchParams.get("search") || "").toLowerCase();
  const page   = Math.max(1, parseInt(searchParams.get("page")  || "1"));
  const limit  = Math.max(1, parseInt(searchParams.get("limit") || "20"));

  let leads = parseLeadsFromFiles();
  if (leads.length === 0) leads = FALLBACK;

  if (search) {
    leads = leads.filter((l) =>
      [l.name, l.niche, l.city, l.email].some((v) => v.toLowerCase().includes(search))
    );
  }

  const total      = leads.length;
  const totalPages = Math.max(1, Math.ceil(total / limit));
  const paginated  = leads.slice((page - 1) * limit, page * limit);

  return NextResponse.json({ leads: paginated, total, page, totalPages });
}
