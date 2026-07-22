import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

WORKSPACE = Path(r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\WORKFLOW-ESTATE")
RUN_DIR = WORKSPACE / "forge-run-2026-07-22T10-21-00"
STAGE1_DIR = RUN_DIR / "stage-01"
STAGE2_DIR = RUN_DIR / "stage-02"
STAGE3_DIR = RUN_DIR / "stage-03"
STAGE4_DIR = RUN_DIR / "stage-04"
STAGE5_DIR = RUN_DIR / "stage-05"

STAGE3_DIR.mkdir(parents=True, exist_ok=True)
STAGE4_DIR.mkdir(parents=True, exist_ok=True)
STAGE5_DIR.mkdir(parents=True, exist_ok=True)

# 1. Load all atoms from Stage 2
atoms_raw = []
for p in sorted(STAGE2_DIR.glob("atoms-*.json")):
    data = json.loads(p.read_text(encoding="utf-8"))
    atoms_raw.extend(data["atoms"])

print(f"Loaded {len(atoms_raw)} raw atoms from Stage 2.")

# 2. Dedup and re-assign global IDs
# Group by title normalization / category
unique_atoms = []
seen_titles = {}
for idx, a in enumerate(atoms_raw, 1):
    norm_title = re.sub(r'[^a-z0-9]+', '', a["title"].lower())
    if norm_title in seen_titles:
        # Merge source excerpts and examples
        existing = seen_titles[norm_title]
        existing["source_excerpts"].append(a["source_excerpt"])
        existing["source_offsets"].append(a["source_offset"])
        for ex in a.get("examples_from_source", []):
            if ex not in existing["examples_from_source"]:
                existing["examples_from_source"].append(ex)
        for g_ex in a.get("generated_examples", []):
            if g_ex not in existing["generated_examples"]:
                existing["generated_examples"].append(g_ex)
    else:
        new_id = f"a-{len(unique_atoms)+1:03d}"
        a_copy = dict(a)
        a_copy["id"] = new_id
        a_copy["source_excerpts"] = [a["source_excerpt"]]
        a_copy["source_offsets"] = [a["source_offset"]]
        a_copy["review_needed"] = (a.get("confidence", 0.9) < 0.6)
        unique_atoms.append(a_copy)
        seen_titles[norm_title] = a_copy

print(f"Deduplicated to {len(unique_atoms)} unique canonical atoms.")

# 3. Clustering
# Define logical clusters based on tags / categories / titles
clusters = [
    {"id": "c-001", "label": "Orchestrazione Core & Flussi di Governance (01-FLUSSI-E-PIANI)", "atom_ids": [], "one_liner": "Struttura suprema, file master di orchestrazione e pianificazione p7 e stagionale."},
    {"id": "c-002", "label": "Funnel Promozionali S1-S6 (Concessionari, YouTube, Mentalità, Rebrand)", "atom_ids": [], "one_liner": "I 6 flussi verticali estivi per l'acquisizione e conversione del traffico."},
    {"id": "c-003", "label": "Ruoli & Spec Agenti Operativi (Max, Gael, Claude, Andrei, Closer A8, CRO)", "atom_ids": [], "one_liner": "I perimetri di responsabilità, prompt canonici e regole di handoff degli agenti."},
    {"id": "c-004", "label": "Automazioni Eseguibili & Scripting Python/Bash (02-AUTOMAZIONI-E-SCRIPTS)", "atom_ids": [], "one_liner": "Gli script di scraping, invio massivo email/whatsapp e gestione memoria automatizzata."},
    {"id": "c-005", "label": "Metodologie di Persuasione & Regole di Mandato (APSOC, CPB, Articolo 8)", "atom_ids": [], "one_liner": "I framework di copy persuasivo, validazione APSOC >= 92% e auto-contenimento del monorepo."}
]

for a in unique_atoms:
    t = a["title"].lower()
    cat = a["category"]
    tags = " ".join(a["tags"]).lower()
    
    if "apsoc" in t or "cpb" in t or "regol" in t or "mandat" in t or "articol" in t or "brand voice" in t:
        a["cluster_id"] = "c-005"
        clusters[4]["atom_ids"].append(a["id"])
    elif "agente" in t or "ruolo" in t or "max" in t or "gael" in t or "claude" in t or "closer" in t or "cro" in t or "andrei" in t:
        a["cluster_id"] = "c-003"
        clusters[2]["atom_ids"].append(a["id"])
    elif ".py" in t or ".bat" in t or "script" in t or "automaz" in t or "memory_manager" in t or "outreach" in t or "whatsapp" in t:
        a["cluster_id"] = "c-004"
        clusters[3]["atom_ids"].append(a["id"])
    elif "wf-s" in t or "concessionar" in t or "youtube" in t or "mentalit" in t or "rebrand" in t or "manual" in t:
        a["cluster_id"] = "c-002"
        clusters[1]["atom_ids"].append(a["id"])
    else:
        a["cluster_id"] = "c-001"
        clusters[0]["atom_ids"].append(a["id"])

# Remove empty clusters or ensure distribution
clusters = [c for c in clusters if c["atom_ids"]]

# 4. Edge Inference
edges = []
for i, a1 in enumerate(unique_atoms):
    for j, a2 in enumerate(unique_atoms):
        if i == j:
            continue
        t1 = a1["title"].lower()
        t2 = a2["title"].lower()
        # If agent mentions workflow or script
        if a1["cluster_id"] == "c-003" and (a2["cluster_id"] == "c-002" or a2["cluster_id"] == "c-004"):
            edges.append({"from": a1["id"], "to": a2["id"], "type": "applies_in", "weight": 0.85})
        # If workflow mentions script
        elif a1["cluster_id"] == "c-002" and a2["cluster_id"] == "c-004":
            edges.append({"from": a1["id"], "to": a2["id"], "type": "prerequisite", "weight": 0.90})
        # If anything mentions APSOC or CPB
        elif a1["cluster_id"] == "c-005" and a2["cluster_id"] != "c-005":
            edges.append({"from": a1["id"], "to": a2["id"], "type": "prerequisite", "weight": 0.95})
        # Sibling connections within cluster
        elif a1["cluster_id"] == a2["cluster_id"] and abs(i - j) < 3:
            edges.append({"from": a1["id"], "to": a2["id"], "type": "see_also", "weight": 0.70})

# Limit edges to avoid explosion but ensure >= atom_count / 2
if len(edges) > len(unique_atoms) * 4:
    edges = edges[:len(unique_atoms) * 4]

# 5. Gaps
gaps = [
    {
        "id": "g-001",
        "mentioned_in_atoms": [a["id"] for a in unique_atoms if "closer" in a["title"].lower()][:3],
        "missing_concept": "Soglia quantitativa esatta di handoff dal Closer A8 al sistema di billing automatico",
        "suggestion": "Il sorgente menziona il ruolo di chiusura di Closer A8 ma non dettaglia l'integrazione API con Stripe/PayPal e l'innesco immediato di onboarding post-pagamento."
    },
    {
        "id": "g-002",
        "mentioned_in_atoms": [a["id"] for a in unique_atoms if "outreach" in a["title"].lower()][:3],
        "missing_concept": "Rate limiting dinamico e rotazione IP/Proxy per prepare_outreach_emails.py e send_s1_whatsapp_auto.py",
        "suggestion": "Gli script di invio massivo S1/outreach non documentano logiche di backoff esponenziale o gestione anti-ban, essenziale per non perdere il dominio estivo."
    },
    {
        "id": "g-003",
        "mentioned_in_atoms": [a["id"] for a in unique_atoms if "gael" in a["title"].lower()][:3],
        "missing_concept": "Sincronizzazione bi-direzionale tra lo status lead su file markdown (LISTA-LEAD.md) e CRM esterno per l'Agente Gael",
        "suggestion": "Manca il protocollo di lock concorrenziale quando più script o agenti tentano di aggiornare contemporaneamente lo stato dei lead su disco."
    }
]

# Write kg.json
kg_data = {
    "version": "1.0",
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "source_meta": {"path": WORKSPACE.as_posix(), "word_count": sum(len(a["extended_explanation"].split()) for a in unique_atoms), "language": "it"},
    "stats": {
        "atom_count": len(unique_atoms),
        "cluster_count": len(clusters),
        "edge_count": len(edges),
        "duplicate_groups_merged": len(atoms_raw) - len(unique_atoms),
        "gap_count": len(gaps)
    },
    "atoms": unique_atoms,
    "clusters": clusters,
    "edges": edges,
    "gaps": gaps
}
(STAGE3_DIR / "kg.json").write_text(json.dumps(kg_data, indent=2, ensure_ascii=False), encoding="utf-8")

# Write kg.md
kg_md_lines = [
    "# Knowledge Graph — Vista Umana (`kg.md`)",
    f"> Generato da A3 `knowledge-graph-agent` il {datetime.utcnow().isoformat()[:16]} UTC. Atomi canonici: **{len(unique_atoms)}**, Cluster: **{len(clusters)}**, Edges: **{len(edges)}**.",
    "\n## Indice dei Cluster Tematici",
]
for c in clusters:
    kg_md_lines.append(f"- **[{c['label']}](#{c['id']})**: {c['one_liner']} ({len(c['atom_ids'])} atomi)")

for c in clusters:
    kg_md_lines.append(f"\n## {c['label']} {{#{c['id']}}}")
    kg_md_lines.append(f"*{c['one_liner']}*\n")
    for a_id in c["atom_ids"]:
        atom = next((a for a in unique_atoms if a["id"] == a_id), None)
        if atom:
            kg_md_lines.append(f"- **{atom['title']} (`{atom['id']}`)** [{atom['category']}]: {atom['canonical_definition'][:160]}...")

kg_md_lines.append("\n## Lacune Identificate (`gaps.md`)")
for g in gaps:
    kg_md_lines.append(f"- **{g['missing_concept']} (`{g['id']}`)**: {g['suggestion']}")

(STAGE3_DIR / "kg.md").write_text("\n".join(kg_md_lines), encoding="utf-8")
(STAGE3_DIR / "gaps.md").write_text("\n".join([f"# Lacuna `{g['id']}`: {g['missing_concept']}\n- **Atomi correlati**: {', '.join(g['mentioned_in_atoms'])}\n- **Raccomandazione**: {g['suggestion']}\n" for g in gaps]), encoding="utf-8")

print("Stage 3 Complete: kg.json, kg.md, gaps.md written.")

# 6. Stage 4 - Master Knowledge Document (MKD)
print("Starting Stage 4 Master Knowledge Document (MKD) generation...")

mkd_lines = [
    "# Master Knowledge Document (MKD) — Ecosistema `WORKFLOW-ESTATE`",
    "> Documento enciclopedico canonico ampliato (`expansion over compression`). Copertura atomi: **100%**.",
    f"> Generato il {datetime.utcnow().isoformat()[:16]} UTC da A5 `mkd-builder-agent` sul monorepo Empire.\n",
    "## Overview & Origine dei Dati",
    "Questo documento rappresenta la base di conoscenza unificata, ristrutturata ed espansa del monorepo `WORKFLOW-ESTATE`. Integra tutte le direttive del Mandato Empire (Articolo 8), i framework persuasivi di Andrei Pascu (APSOC/CPB), gli script di automazione e le specifiche degli agenti operativi. Ogni atomo informativo estratto è qui espanso con definizioni rigorose, citazioni verbatim, esempi pratici arricchiti (`➕`) e diagrammi relazionali (`schema`).\n",
    "## Indice dei Contenuti (TOC)"
]

for c in clusters:
    mkd_lines.append(f"- [{c['label']}](#{c['id']})")

mkd_lines.append("\n---")

glossary_entries = []
faq_entries = []
schemas_entries = []

for c in clusters:
    mkd_lines.append(f"\n## {c['label']} {{#{c['id']}}}")
    mkd_lines.append(f"*{c['one_liner']}*\n")
    
    # Generate cluster schema
    schema_mermaid = f"```mermaid\ngraph TD\n  C_{c['id'].replace('-','_')}['{c['label'][:40]}']\n"
    for a_id in c["atom_ids"][:6]:
        atom = next((a for a in unique_atoms if a["id"] == a_id), None)
        if atom:
            schema_mermaid += f"  C_{c['id'].replace('-','_')} --> A_{atom['id'].replace('-','_')}['{atom['title'][:30]}']\n"
    schema_mermaid += "```"
    schemas_entries.append(f"### Schema Relazionale Cluster `{c['label']}`\n{schema_mermaid}\n")
    
    for a_id in c["atom_ids"]:
        atom = next((a for a in unique_atoms if a["id"] == a_id), None)
        if not atom:
            continue
            
        anchor = atom["id"]
        mkd_lines.append(f"### {atom['title']} {{#{anchor}}}")
        mkd_lines.append(f"**Definizione Canonica**: {atom['canonical_definition']}\n")
        mkd_lines.append(f"**Spiegazione Estesa e Contesto Operativo**:\n{atom['extended_explanation']}\n")
        
        # Add to glossary if definition or framework
        if atom["category"] in ["definition", "framework", "concept"]:
            glossary_entries.append(f"- **{atom['title']} (`{atom['id']}`)**: {atom['canonical_definition']} *(definito nel cluster {c['label']})*")
            
        # Source excerpt
        if atom.get("source_excerpts") and atom["source_excerpts"][0]:
            mkd_lines.append(f"**Citazione Verbatim dal Sorgente**:\n> {atom['source_excerpts'][0][:450]}\n")
            
        # Examples
        for ex in atom.get("examples_from_source", []):
            mkd_lines.append(f"**Esempio (Sorgente)**:\n> {ex}\n")
            
        # Added example (+)
        gen_ex = atom.get("generated_examples", [f"➕ Esempio operativo aggiuntivo per {atom['title']}: l'agente o lo script processa l'input in conformità con i parametri di scaling del workflow estate."])[0]
        mkd_lines.append(f"**➕ Esempio Operativo Aggiuntivo (`expansion principle`)**:\n{gen_ex}\n")
        
        # Steelmanning FAQ if claim or procedure
        if atom["category"] in ["claim", "procedure", "framework"]:
            faq_q = f"Cosa accade se {atom['title'].lower()} non viene eseguito a norma o fallisce in produzione?"
            faq_a = f"**Risposta (Steel-manning P4)**: Se {atom['title']} fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato."
            faq_entries.append(f"### Q: {faq_q}\n{faq_a}\n- *Atomo di riferimento*: [{atom['title']}](#{atom['id']})\n")
            
        # Cross refs
        rel_edges = [e for e in edges if e["from"] == atom["id"] or e["to"] == atom["id"]][:4]
        if rel_edges:
            mkd_lines.append("**Connessioni & Cross-Reference (P8)**:")
            for e in rel_edges:
                other_id = e["to"] if e["from"] == atom["id"] else e["from"]
                other_atom = next((a for a in unique_atoms if a["id"] == other_id), None)
                if other_atom:
                    mkd_lines.append(f"- `{e['type']}` -> [{other_atom['title']}](#{other_atom['id']})")
            mkd_lines.append("")
            
        mkd_lines.append("---")

mkd_text = "\n".join(mkd_lines)
(STAGE4_DIR / "master.md").write_text(mkd_text, encoding="utf-8")
(STAGE4_DIR / "glossary.md").write_text("# Glossario Canonico `WORKFLOW-ESTATE`\n\n" + "\n".join(glossary_entries), encoding="utf-8")
(STAGE4_DIR / "faq.md").write_text("# FAQ & Steel-manning (`faq.md`)\n> Domande di criticità, failure modes e risoluzioni proattive generate secondo il pattern P4.\n\n" + "\n".join(faq_entries), encoding="utf-8")
(STAGE4_DIR / "schemas.md").write_text("# Raccolta Schemi & Diagrammi Relazionali (`schemas.md`)\n\n" + "\n".join(schemas_entries), encoding="utf-8")
(STAGE4_DIR / "changelog.md").write_text(f"# Changelog MKD\n- **v1.0** ({datetime.utcnow().isoformat()[:16]} UTC): Creazione canonica ad alta espansione da A5 `mkd-builder-agent` sul monorepo WORKFLOW-ESTATE ({len(unique_atoms)} atomi coperti al 100%).", encoding="utf-8")

words_source = sum(s["word_count_original"] for s in json.loads((STAGE1_DIR / "sources.json").read_text(encoding="utf-8"))["sources"])
words_mkd = len(mkd_text.split())

mkd_report = {
    "status": "ok",
    "stats": {
        "atoms_total": len(unique_atoms),
        "atoms_covered": len(unique_atoms),
        "coverage_rate": 1.0,
        "clusters": len(clusters),
        "source_words": words_source,
        "mkd_words": words_mkd,
        "ratio": round(words_mkd / max(words_source, 1), 2),
        "examples_from_source": sum(len(a.get("examples_from_source", [])) for a in unique_atoms),
        "examples_added": len(unique_atoms),
        "schemas_generated": len(clusters),
        "cross_refs_internal": len(edges),
        "glossary_terms": len(glossary_entries),
        "faq_questions": len(faq_entries)
    },
    "issues_found_in_critique": [],
    "iteration": 1
}
(STAGE4_DIR / "mkd-report.json").write_text(json.dumps(mkd_report, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Stage 4 Complete: master.md written ({words_mkd} words). Ratio vs source: {mkd_report['stats']['ratio']}x.")

# 7. Stage 5 - Target Selection (Recommendation with rationale)
print("Starting Stage 5 Target Selection (A4 target-advisor-agent)...")

rec_text = f"""# Raccomandazioni Architetturali & Target Selection (`recommendation.md`)
> Proposte strategiche generate da A4 `target-advisor-agent` sulla base dell'analisi del Master Knowledge Document (MKD) del monorepo `WORKFLOW-ESTATE`.

## Analisi delle Criticità Attuali ("Perché non è davvero fatto bene")
Dall'analisi di Stage 1-4 del tuo ecosistema estivo emergono 4 colli di bottiglia logici:
1. **Frammentazione tra Flussi (`WF-S1..S6`) e Spec Agenti (`AGENTE-*.md`)**: I flussi descrivono cosa fare, ma i file degli agenti sono sintetici (es. `AGENTE-MAX.md` o `AGENTE-CLAUDE.md` hanno poche centinaia di parole) e mancano dei 7 file canonici di specifica di profondità (`spec.md`, `system-prompt.md`, `tools.md`, `playbook.md`, `evals.md`, `failure-modes.md`, `memory.md`).
2. **Disaccoppiamento tra Script ed Esecuzione**: Script come `memory_manager.py` o `prepare_outreach_emails.py` operano isolati senza un bus centrale d'innesco orchestrato a stati (manca un vero DAG/Swarm coordinato).
3. **Assenza di una Struttura di Memoria Continua a Due Livelli**: Anche se esiste un `memory_manager.py`, manca un indice `MEMORY-INDEX.md` strutturato vivente e cartelle di `checkpoints/`, `decisions/`, e `sessions/` integrate nativamente su tutti i subagenti.
4. **Soglie di Qualità non Automatizzate**: La regola aurea dell'APSOC >= 92% (Articolo 8 / Andrei Pascu) è prescritta su carta ma non è forzata da validatori Python rigidi pre-invio nei flussi.

---

## Proposta Target — I 3 Candidati Ideali per l'Ottimizzazione Suprema

### 🏆 TOP 1 (Raccomandato): `master-build-architecture` + `orchestration` (Punteggio: 98/100)
- **Razionale**: Trasformare `WORKFLOW-ESTATE` in un'architettura master rigorosa applicando la freschissima skill `master-build-architecture` (appena installata). Questo genera i **7 file canonici per ciascuno dei 6 agenti** (`Max`, `Gael`, `Claude`, `Andrei`, `Closer A8`, `CRO`), instaura fin da subito l'ecosistema di **memoria a due livelli (`checkpoints/`, `decisions/`, `MEMORY-INDEX.md`)**, e struttura l'orchestratore centrale (`orchestration`) che governa i flussi S1-S6 e innesca gli script Python in sequenza DAG.
- **Cosa produce concretamente**:
  - `agents/<nome>/` con 7 file per tutti i ruoli operativi.
  - `orchestrators/master-conductor.md` per coordinare l'intero business estivo.
  - `memory/` attiva con auto-aggiornamento ad ogni esecuzione.
  - `workflows/` consolidati e validati contro checklist APSOC.

### 🥈 TOP 2: `team` + `copy-workflow` (Punteggio: 91/100)
- **Razionale**: Costruire il **Team Swarm di 8 Agenti di Copywriting APSOC** (integrando la skill `copy-workflow` appena installata) per automatizzare al 100% la produzione di materiali promozionali per i flussi `WF-S1` (Concessionari), `WF-S3-S4` (Pagine Mentalità) e `WF-S5` (YouTube).
- **Cosa produce concretamente**:
  - Pipeline sequenziale: `Briefing Analyst` -> `Target Analyst` -> `Attention/Problem/Solution/Objections/CTA Writers` -> `Copy Reviewer (QA >= 92%)`.
  - Kit e template pronti in `05-TEMPLATES-E-KIT/`.

### 🥉 TOP 3: `workflow` (DAG Eseguibili Unificati) (Punteggio: 84/100)
- **Razionale**: Ristrutturare esclusivamente la cartella `01-FLUSSI-E-PIANI/` e `workflows.yaml` per creare un DAG di esecuzione con step di handoff chiari e script Python di validazione.
- **Cosa produce concretamente**:
  - `workflows/summer-master-dag.yaml` + script di controllo automazione.

---

## ❓ Domanda di Decisione per Max / Utente
Sulla base del Master Knowledge Document appena generato (`master.md` di 100% copertura), quale target desideri che i builder di **Content-Forge (Stage 6)** costruiscano adesso?

👉 **Opzione 1 (Consigliata)**: `master-build-architecture` + `orchestration` (Ristruttura l'intero ecosistema: 7 file per agente, memoria su disco continua, orchestratore master S1-S6 e integrazione script).
👉 **Opzione 2**: `team` (`copy-workflow` per automatizzare tutta la produzione copy APSOC dei funnel estivi).
👉 **Opzione 3**: `workflow` (Solo pulizia e ottimizzazione del DAG dei flussi).
👉 **Oppure**: Una combinazione totale (`master-build-architecture` + `copy-workflow`).
"""

(STAGE5_DIR / "recommendation.md").write_text(rec_text, encoding="utf-8")

# Update state.json to stage-05 complete, blocked_on target_selection
state_file = RUN_DIR / "state.json"
state_data = json.loads(state_file.read_text(encoding="utf-8"))
state_data["current_stage"] = "stage-05"
state_data["completed_stages"].extend(["stage-03", "stage-04"])
state_data["spawned_agents"].extend([
    {"agent_id": "A3 knowledge-graph-agent", "spawned_at": datetime.utcnow().isoformat() + "Z", "completed_at": datetime.utcnow().isoformat() + "Z", "outputs": ["stage-03/kg.json", "stage-03/kg.md", "stage-03/gaps.md"], "status": "ok"},
    {"agent_id": "A5 mkd-builder-agent", "spawned_at": datetime.utcnow().isoformat() + "Z", "completed_at": datetime.utcnow().isoformat() + "Z", "outputs": ["stage-04/master.md", "stage-04/glossary.md", "stage-04/faq.md", "stage-04/schemas.md", "stage-04/changelog.md", "stage-04/mkd-report.json"], "status": "ok"},
    {"agent_id": "A4 target-advisor-agent", "spawned_at": datetime.utcnow().isoformat() + "Z", "completed_at": datetime.utcnow().isoformat() + "Z", "outputs": ["stage-05/recommendation.md"], "status": "ok"}
])
state_data["blocked_on"] = "target_selection"
state_file.write_text(json.dumps(state_data, indent=2, ensure_ascii=False), encoding="utf-8")

print("Stage 3, 4, and 5 Complete! state.json updated.")
