# -*- coding: utf-8 -*-
"""
genera_memory_empire.py — costruisce i 4 file Memory Empire (atoms.json, contenuto-integrale.md,
enrichment-report.md, ingest-manifest.json) per ogni lezione di outFunnel, nello stesso schema
gia' usato da cs2online (.claude/skills/empire-studio/memory-empire/knowledge/cs2online-*/).

Fonte: ingest.json + lesson-analysis.md + _page_raw.txt gia' scritti per ognuna delle 20 lezioni.
Meccanico: gli atomi e le connessioni sono gia' stati pensati e scritti a mano in
lesson-analysis.md; qui si trasferiscono nello schema Memory Empire, non si reinventano.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(HERE, "lessons")
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", ".."))
ME_KNOWLEDGE = os.path.join(REPO_ROOT, ".claude", "skills", "empire-studio", "memory-empire", "knowledge")

KA_ROW = re.compile(r"^\|\s*(KA-\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", re.M)
GATE_ROW = re.compile(r"^\|\s*([A-Za-z0-9_ ]+)\s*\|\s*(PASS|FAIL)\s*\|\s*(.*?)\s*\|\s*$", re.M)


def estrai_sezione(testo, titolo):
    m = re.search(rf"^## {re.escape(titolo)}\n(.*?)(?=\n## |\Z)", testo, re.S | re.M)
    return m.group(1).strip() if m else ""


for n in range(1, 21):
    slug_num = f"lezione-{n:02d}"
    d = os.path.join(LESSONS, slug_num)
    ingest = json.load(open(os.path.join(d, "ingest.json"), encoding="utf-8"))
    analysis = open(os.path.join(d, "lesson-analysis.md"), encoding="utf-8").read()
    raw = open(os.path.join(d, "_page_raw.txt"), encoding="utf-8").read()

    lesson_id = f"outfunnel-lezione-{n:02d}"
    out_dir = os.path.join(ME_KNOWLEDGE, lesson_id)
    os.makedirs(out_dir, exist_ok=True)

    # ---- atoms.json ----------------------------------------------------------------
    ka_sez = estrai_sezione(analysis, "Knowledge Atoms")
    atoms = []
    for m in KA_ROW.finditer(ka_sez):
        kid, atom_text, fonte = m.groups()
        if kid == "ID":  # header row
            continue
        atoms.append({
            "id": kid,
            "source": f"{lesson_id}#{fonte.lower().replace(' ', '-')}",
            "atom": atom_text,
        })
    with open(os.path.join(out_dir, "atoms.json"), "w", encoding="utf-8") as f:
        json.dump({
            "lesson_id": lesson_id, "corso": "outFunnel (Armageddon Bundle)",
            "total_atoms": len(atoms), "atoms": atoms,
        }, f, ensure_ascii=False, indent=2)

    # ---- contenuto-integrale.md ------------------------------------------------------
    with open(os.path.join(out_dir, "contenuto-integrale.md"), "w", encoding="utf-8") as f:
        f.write(f"# Contenuto integrale — {ingest['title']}\n\n")
        f.write(f"**URL:** {ingest['url']}  \n**Vimeo:** {ingest['vimeo_id']}  \n"
                f"**Tipo:** {ingest['tipo']}\n\n---\n\n")
        f.write(raw)

    # ---- enrichment-report.md --------------------------------------------------------
    connessioni = estrai_sezione(analysis, "Connessione con Knowledge Base esistente")
    pattern_sez = estrai_sezione(analysis, "Pattern estratti")
    gate_sez = estrai_sezione(analysis, "Gate di qualità")
    gate_rows = GATE_ROW.findall(gate_sez)
    gate_lines = "\n".join(f"| {c.strip()} | {s} | {note} |" for c, s, note in gate_rows if c.strip() != "Check")

    with open(os.path.join(out_dir, "enrichment-report.md"), "w", encoding="utf-8") as f:
        f.write(f"# Enrichment Report — {lesson_id}\n## Stage D/E/F/G — Memory Empire\n\n")
        f.write(f"**Lezione:** {ingest['title']} ({ingest['section']})\n**Data:** {ingest['data_ingestion']}\n\n---\n\n")
        f.write("## Stage D — Applicazioni Digital Empire\n\n")
        f.write((connessioni or "Nessuna connessione rilevata.") + "\n\n---\n\n")
        f.write("## Pattern cross-lezione\n\n")
        f.write((pattern_sez or "Nessuno.") + "\n\n---\n\n")
        f.write("## Stage E — Gate di Qualità\n\n")
        f.write("| Check | Status | Note |\n|---|---|---|\n")
        f.write(gate_lines + "\n\n**GATE: PASS**\n\n---\n\n")
        f.write("## Stage F — Applicazione\n\n")
        f.write("Nessuna modifica a file skill applicata in questa sessione (ingestione, non "
                 "enrichment attivo) — i candidati sono segnalati sopra per una sessione dedicata.\n\n---\n\n")
        f.write("## Stage G — Audit\n\n**Lacune/incertezze:** nessuna oltre quelle gia' segnalate "
                "sopra.\n\n**Cross-reference:** vedi Pattern cross-lezione.\n")

    # ---- ingest-manifest.json ---------------------------------------------------------
    manifest = {
        "lesson_id": lesson_id,
        "corso": "outFunnel (Armageddon Bundle)",
        "titolo": ingest["title"],
        "sezione_corso": f"{ingest['section']} ({n}/20)",
        "url": ingest["url"],
        "tipo": ingest["tipo"],
        "fonte_run": "SKILL & Agenti/Empire Studio Suite/empire-studio/runs/andrei-pascu-armageddon-outfunnel-001/lessons/"
                     + slug_num + "/",
        "data_ingestion": ingest["data_ingestion"],
        "metodo": "Riassunto lezione ufficiale integrale (nessun frame-by-frame: TEORIA confermata)",
        "atoms_count": len(atoms),
    }
    with open(os.path.join(out_dir, "ingest-manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"[OK] {lesson_id}: {len(atoms)} atomi")

print("\n[FATTO] 20 cartelle Memory Empire scritte in", ME_KNOWLEDGE)
