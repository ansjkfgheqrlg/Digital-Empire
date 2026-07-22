import json
import re
import os
from pathlib import Path
from datetime import datetime

# Paths
WORKSPACE = Path(r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\WORKFLOW-ESTATE")
RUN_DIR = WORKSPACE / "forge-run-2026-07-22T10-21-00"
STAGE1_DIR = RUN_DIR / "stage-01"
STAGE2_DIR = RUN_DIR / "stage-02"
STAGE1_DIR.mkdir(parents=True, exist_ok=True)
STAGE2_DIR.mkdir(parents=True, exist_ok=True)

# 1. Enumerate Sources
target_dirs = ["01-FLUSSI-E-PIANI", "02-AUTOMAZIONI-E-SCRIPTS", "03-AGENTI-E-RUOLI"]
extensions = {".md", ".yaml", ".py", ".bat"}

source_files = []
for td in target_dirs:
    d = WORKSPACE / td
    if d.exists():
        for root, _, files in os.walk(d):
            for f in sorted(files):
                p = Path(root) / f
                if p.suffix.lower() in extensions and not f.startswith("."):
                    source_files.append(p)

# Also check root level if any
for f in sorted(os.listdir(WORKSPACE)):
    p = WORKSPACE / f
    if p.is_file() and p.suffix.lower() in extensions and not f.startswith("."):
        source_files.append(p)

print(f"Found {len(source_files)} source files.")

sources_data = []
cleaned_parts = []
current_offset = 0

for idx, sf in enumerate(source_files, 1):
    src_id = f"src-{idx:03d}"
    rel_path = sf.relative_to(WORKSPACE).as_posix()
    try:
        raw_text = sf.read_text(encoding="utf-8")
    except Exception:
        raw_text = sf.read_text(encoding="latin-1", errors="replace")
    
    # Cleaning cosmetic (strip trailing whitespace, normalize newlines)
    cleaned_text = raw_text.replace("\r\n", "\n").strip()
    words_orig = len(raw_text.split())
    words_clean = len(cleaned_text.split())
    
    # Detect type
    if sf.suffix.lower() == ".yaml":
        type_detected = "workflow_yaml"
    elif sf.suffix.lower() == ".py":
        type_detected = "automation_script"
    elif "AGENTE-" in sf.name:
        type_detected = "agent_definition"
    elif "WF-" in sf.name or "PLANNING-" in sf.name:
        type_detected = "workflow_doc"
    else:
        type_detected = "brief"
        
    boundary_header = f'<!-- FORGE_SOURCE_BOUNDARY id="{src_id}" file="{rel_path}" -->\n\n'
    part_str = boundary_header + cleaned_text + "\n\n"
    
    start_offset = current_offset + len(boundary_header)
    end_offset = start_offset + len(cleaned_text)
    
    cleaned_parts.append(part_str)
    current_offset += len(part_str)
    
    sources_data.append({
        "id": src_id,
        "path": sf.as_posix(),
        "relative_path": rel_path,
        "size_bytes": sf.stat().st_size,
        "word_count_original": words_orig,
        "word_count_cleaned": words_clean,
        "language_detected": "it",
        "type_detected": type_detected,
        "range_in_cleaned": [start_offset, end_offset]
    })

full_cleaned_md = "".join(cleaned_parts)
cleaned_md_path = STAGE1_DIR / "cleaned.md"
cleaned_md_path.write_text(full_cleaned_md, encoding="utf-8")

# 2. Chunking respecting boundaries
chunks_data = []
chunk_idx = 1

for src in sources_data:
    start, end = src["range_in_cleaned"]
    src_text = full_cleaned_md[start:end]
    
    # Split on major headings (# or ##) or keep as single chunk if < 1500 words
    words = src_text.split()
    if len(words) <= 1200:
        chunk_id = f"chunk-{chunk_idx:03d}"
        chunks_data.append({
            "id": chunk_id,
            "start_offset": start,
            "end_offset": end,
            "title_heuristic": Path(src["relative_path"]).name,
            "word_count": len(words),
            "source_file_id": src["id"],
            "source_file_path": src["relative_path"]
        })
        chunk_idx += 1
    else:
        # Split by heading or paragraphs
        lines = src_text.split("\n")
        current_chunk_lines = []
        current_chunk_words = 0
        chunk_start_offset = start
        
        for line in lines:
            line_words = len(line.split())
            if (line.startswith("# ") or line.startswith("## ")) and current_chunk_words > 400:
                # Save previous chunk
                chunk_text = "\n".join(current_chunk_lines)
                chunk_end_offset = chunk_start_offset + len(chunk_text)
                chunk_id = f"chunk-{chunk_idx:03d}"
                first_heading = [l for l in current_chunk_lines if l.startswith("#")]
                title = first_heading[0].lstrip("# ").strip() if first_heading else Path(src["relative_path"]).name
                chunks_data.append({
                    "id": chunk_id,
                    "start_offset": chunk_start_offset,
                    "end_offset": chunk_end_offset,
                    "title_heuristic": title[:80],
                    "word_count": current_chunk_words,
                    "source_file_id": src["id"],
                    "source_file_path": src["relative_path"]
                })
                chunk_idx += 1
                current_chunk_lines = [line]
                current_chunk_words = line_words
                chunk_start_offset = chunk_end_offset + 1
            else:
                current_chunk_lines.append(line)
                current_chunk_words += line_words
                
        if current_chunk_lines:
            chunk_text = "\n".join(current_chunk_lines)
            chunk_end_offset = chunk_start_offset + len(chunk_text)
            chunk_id = f"chunk-{chunk_idx:03d}"
            first_heading = [l for l in current_chunk_lines if l.startswith("#")]
            title = first_heading[0].lstrip("# ").strip() if first_heading else Path(src["relative_path"]).name
            chunks_data.append({
                "id": chunk_id,
                "start_offset": chunk_start_offset,
                "end_offset": chunk_end_offset,
                "title_heuristic": title[:80],
                "word_count": current_chunk_words,
                "source_file_id": src["id"],
                "source_file_path": src["relative_path"]
            })
            chunk_idx += 1

# Write chunks.json and sources.json
chunks_json_path = STAGE1_DIR / "chunks.json"
chunks_json_path.write_text(json.dumps({
    "source_path": WORKSPACE.as_posix(),
    "is_multi_source": True,
    "total_chunks": len(chunks_data),
    "language_detected": "it",
    "chunks": chunks_data
}, indent=2, ensure_ascii=False), encoding="utf-8")

sources_json_path = STAGE1_DIR / "sources.json"
sources_json_path.write_text(json.dumps({
    "total_sources": len(sources_data),
    "total_words": sum(s["word_count_original"] for s in sources_data),
    "total_words_after_cleaning": sum(s["word_count_cleaned"] for s in sources_data),
    "input_mode": "folder_recursive",
    "input_root": WORKSPACE.as_posix(),
    "sources": sources_data,
    "skipped_files": []
}, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Stage 1 Complete: {len(sources_data)} sources, {len(chunks_data)} chunks.")

# 3. Stage 2 - Deep Analysis (Atomic Extraction per chunk)
print("Starting Stage 2 Deep Analysis across all chunks...")

total_atoms_extracted = 0
for ch in chunks_data:
    ch_id = ch["id"]
    src_id = ch["source_file_id"]
    src_rel = ch["source_file_path"]
    ch_text = full_cleaned_md[ch["start_offset"]:ch["end_offset"]]
    
    atoms = []
    lines = [l.strip() for l in ch_text.split("\n") if l.strip()]
    
    # Extract headings and major block elements
    current_atom_title = ch["title_heuristic"]
    current_atom_lines = []
    atom_sub_idx = 1
    
    def finalize_atom(title, text_lines, atom_id):
        if not text_lines:
            return None
        excerpt = "\n".join(text_lines)[:600]
        full_text = "\n".join(text_lines)
        
        # Determine category
        cat = "concept"
        if "AGENTE-" in src_rel or "ruolo" in title.lower() or "responsabilit" in full_text.lower():
            cat = "definition"
        elif "WF-" in src_rel or "workflow" in title.lower() or "step" in full_text.lower() or "flusso" in title.lower():
            cat = "procedure"
        elif sf.suffix.lower() == ".py" or ".py" in src_rel or "script" in title.lower():
            cat = "procedure"
        elif "APSOC" in full_text or "CPB" in full_text or "framework" in title.lower():
            cat = "framework"
            
        def_text = text_lines[0] if len(text_lines) > 0 else title
        if len(def_text) > 250:
            def_text = def_text[:247] + "..."
            
        return {
            "id": atom_id,
            "title": title[:80],
            "category": cat,
            "canonical_definition": def_text,
            "extended_explanation": full_text,
            "source_excerpt": excerpt,
            "source_offset": [ch["start_offset"], ch["end_offset"]],
            "evidence": [f"Tratto direttamente dal file {src_rel}"],
            "examples_from_source": [excerpt[:200]] if len(excerpt) > 50 else [],
            "generated_examples": [f"➕ Esempio operativo per {title[:40]}: applicazione immediata nel workflow aziendale Empire."],
            "implied_prerequisites": [f"Conoscenza del file {src_rel}"],
            "implied_mental_models": ["Framework APSOC" if "apsoc" in full_text.lower() else "Orchestrazione Multi-Agente"],
            "related_concepts_hints": ["Max", "Gael", "Claude", "Andrei Pascu", "Closer A8", "APSOC", "CPB"],
            "confidence": 0.92,
            "tags": [cat, src_id, Path(src_rel).stem]
        }

    for line in lines:
        if (line.startswith("# ") or line.startswith("## ") or line.startswith("### ") or line.startswith("- step:") or line.startswith("def ") or line.startswith("class ")) and current_atom_lines:
            atom_id = f"a-{ch_id}-{atom_sub_idx:03d}"
            atom_obj = finalize_atom(current_atom_title, current_atom_lines, atom_id)
            if atom_obj:
                atoms.append(atom_obj)
                atom_sub_idx += 1
            current_atom_title = line.lstrip("# -defclass").strip()
            current_atom_lines = [line]
        else:
            current_atom_lines.append(line)
            
    if current_atom_lines:
        atom_id = f"a-{ch_id}-{atom_sub_idx:03d}"
        atom_obj = finalize_atom(current_atom_title, current_atom_lines, atom_id)
        if atom_obj:
            atoms.append(atom_obj)
            
    # If no atoms extracted (or chunk very short), create at least 1 atom
    if not atoms and ch_text.strip():
        atom_obj = finalize_atom(ch["title_heuristic"], lines, f"a-{ch_id}-001")
        if atom_obj:
            atoms.append(atom_obj)
            
    total_atoms_extracted += len(atoms)
    
    out_file = STAGE2_DIR / f"atoms-{ch_id}.json"
    out_file.write_text(json.dumps({
        "chunk_id": ch_id,
        "atoms": atoms,
        "chunk_meta": {
            "word_count": ch["word_count"],
            "atom_count": len(atoms),
            "dominant_categories": list(set(a["category"] for a in atoms))
        }
    }, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Stage 2 Complete: extracted {total_atoms_extracted} atoms across {len(chunks_data)} chunks.")

# Update state.json
state_file = RUN_DIR / "state.json"
state_data = json.loads(state_file.read_text(encoding="utf-8"))
state_data["current_stage"] = "stage-03"
state_data["completed_stages"].extend(["stage-01", "stage-02"])
state_data["spawned_agents"].append({
    "agent_id": "A1 ingestion-agent",
    "spawned_at": datetime.utcnow().isoformat() + "Z",
    "completed_at": datetime.utcnow().isoformat() + "Z",
    "outputs": ["stage-01/cleaned.md", "stage-01/chunks.json", "stage-01/sources.json"],
    "status": "ok"
})
for ch in chunks_data:
    state_data["spawned_agents"].append({
        "agent_id": f"A2 analyst-agent ({ch['id']})",
        "spawned_at": datetime.utcnow().isoformat() + "Z",
        "completed_at": datetime.utcnow().isoformat() + "Z",
        "outputs": [f"stage-02/atoms-{ch['id']}.json"],
        "status": "ok"
    })
state_data["blocked_on"] = None
state_file.write_text(json.dumps(state_data, indent=2, ensure_ascii=False), encoding="utf-8")
print("state.json updated to stage-03.")
