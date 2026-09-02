#!/usr/bin/env python3
"""
Empire Studio - wiki_writer.py  (REALE - scrive nella wiki di Digital Empire)

Prende note gia' forgiate (da content-forge --target=wiki) o un singolo file di
conoscenza e le deposita nella wiki di Digital Empire, aggiornando log.md.

Posizione wiki (auto-rilevata risalendo le cartelle fino a trovare
second-brain-vault/wiki, oppure passata con --wiki):
  second-brain-vault/wiki/<subdir>/   (default subdir = sources)

Aggiorna:
  - <wiki>/log.md         (riga "## data" + "- INGEST: ...")
  - copia le note con front-matter coerente

Uso:
  python scripts/wiki_writer.py --note runs/<run>/wiki-notes/ --topic "youtube-design" --source "<url>"
  python scripts/wiki_writer.py --note runs/<run>/video-analysis.md --subdir sources --source "<url>"
  python scripts/wiki_writer.py --dry-run ...    (non scrive, mostra cosa farebbe)

NO API. Solo filesystem.
"""
import argparse
import datetime
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_wiki(explicit=None):
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    # risali dalle cartelle genitore cercando second-brain-vault/wiki
    for base in [ROOT] + list(ROOT.parents):
        cand = base / "second-brain-vault" / "wiki"
        if cand.exists():
            return cand
    return None


def today():
    return datetime.date.today().isoformat()


def gather_notes(note_path: Path):
    if note_path.is_dir():
        return sorted(note_path.glob("*.md"))
    return [note_path] if note_path.exists() else []


def update_log(wiki: Path, topic, n_notes, source, dry):
    log = wiki / "log.md"
    line_header = f"\n## {today()}\n"
    entry = f"- INGEST (Empire Studio): {topic} -> {n_notes} note in wiki. Fonte: {source}\n"
    if dry:
        print(f"[dry-run] log.md += {entry.strip()}")
        return
    txt = log.read_text(encoding="utf-8") if log.exists() else "# Log\n"
    # se la data di oggi non c'e' come ultima sezione, aggiungila
    if f"## {today()}" not in txt:
        txt += line_header
    txt += entry
    log.write_text(txt, encoding="utf-8")
    print(f"[wiki] log aggiornato: {log}")


def main():
    ap = argparse.ArgumentParser(description="Scrive note forgiate nella wiki di Digital Empire")
    ap.add_argument("--note", required=True, help="file .md o cartella di note")
    ap.add_argument("--subdir", default="sources", help="sottocartella wiki (sources|concepts|tools|synthesis)")
    ap.add_argument("--topic", default="empire-ingest", help="etichetta argomento per il log")
    ap.add_argument("--source", default="", help="URL/percorso fonte originale")
    ap.add_argument("--wiki", default=None, help="path esplicito a second-brain-vault/wiki")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    wiki = find_wiki(args.wiki)
    if not wiki:
        print("ERRORE: wiki non trovata (second-brain-vault/wiki). Usa --wiki <path>.")
        sys.exit(1)
    dest_dir = wiki / args.subdir
    notes = gather_notes(Path(args.note))
    if not notes:
        print(f"ERRORE: nessuna nota in {args.note}")
        sys.exit(2)

    print(f"[wiki] destinazione: {dest_dir}")
    if not args.dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for n in notes:
        target = dest_dir / n.name
        header = (f"---\nempire_source: {args.source}\nempire_ingested: {today()}\n"
                  f"empire_topic: {args.topic}\n---\n\n")
        body = n.read_text(encoding="utf-8", errors="replace")
        if args.dry_run:
            print(f"[dry-run] scriverei {target}")
        else:
            target.write_text(header + body, encoding="utf-8")
            written.append(target.name)
    if written:
        print(f"[wiki] scritte {len(written)} note in {dest_dir.relative_to(wiki.parent.parent) if wiki.parent.parent in dest_dir.parents else dest_dir}")
        for w in written:
            print(f"   + {args.subdir}/{w}")

    update_log(wiki, args.topic, len(notes), args.source or "(n/d)", args.dry_run)
    print("[wiki] FATTO." if not args.dry_run else "[wiki] dry-run completato.")


if __name__ == "__main__":
    main()
