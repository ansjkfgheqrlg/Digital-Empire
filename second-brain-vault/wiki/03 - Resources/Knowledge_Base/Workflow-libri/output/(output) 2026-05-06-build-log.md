# build_log
            
> Path: [[Map - Workflow-Libri|Workflow-libri > output]]

## Content

Book Factory — Build Log
============================================================
Avvio: 2026-03-21 20:39:58

[2026-03-21 20:39:59] 
[2026-03-21 20:39:59] 🚀 BOOK FACTORY — AVVIO PIPELINE
[2026-03-21 20:39:59] ============================================================
[2026-03-21 20:39:59] 
Step 0: Validazione file di input...
[2026-03-21 20:39:59]   ✅ input\manuscript.md
[2026-03-21 20:39:59]   ✅ input\image_prompts.yaml
[2026-03-21 20:39:59]   ✅ config\book_config.yaml
[2026-03-21 20:39:59] ✅ Tutti i file di input presenti
[2026-03-21 20:39:59] 
Step 0: Verifica dipendenze Python...
[2026-03-21 20:39:59]   ⚠️  WeasyPrint installato ma GTK non disponibile
[2026-03-21 20:39:59]       → Uso ReportLab come backend PDF (fallback automatico)
[2026-03-21 20:39:59]   ✅ ReportLab (backend PDF fallback)
[2026-03-21 20:39:59]   ✅ PyYAML (configurazioni)
[2026-03-21 20:39:59]   ✅ Pillow (immagini)
[2026-03-21 20:39:59] 
Step 1: Generazione immagini SALTATA (--skip-images)
[2026-03-21 20:39:59]   (rimosso book_final.pdf precedente per ricominciare il ciclo QA pulito)
[2026-03-21 20:39:59] 
[2026-03-21 20:39:59] ============================================================
[2026-03-21 20:39:59] CICLO QUALITY 1/3
[2026-03-21 20:39:59] ============================================================
[2026-03-21 20:39:59] 
Step 2 (tentativo 1): Agente 2 — Layout Engine
[2026-03-21 20:39:59] ============================================================
[2026-03-21 20:39:59] INIZIO: AGENTE 2 — Layout Engine
[2026-03-21 20:39:59] ============================================================
[2026-03-21 20:40:41] ✅ COMPLETATO: AGENTE 2 — Layout Engine
[2026-03-21 20:40:41] 
Step 3 (tentativo 1): Agente 3 — Quality Assurance
[2026-03-21 20:40:41] ============================================================
[2026-03-21 20:40:41] INIZIO: AGENTE 3 — Quality Assurance
[2026-03-21 20:40:41] ============================================================
[2026-03-21 20:40:50] ✅ COMPLETATO: AGENTE 3 — Quality Assurance
[2026-03-21 20:40:50] 
✅ QA SUPERATO al tentativo 1/3
[2026-03-21 20:40:50] 
[2026-03-21 20:40:50] ============================================================
[2026-03-21 20:40:50] 🎉 LIBRO COMPLETATO CON SUCCESSO!
[2026-03-21 20:40:50] 📖 File finale: output/book_final.pdf (198.08 MB)
[2026-03-21 20:40:50] 
File generati:
[2026-03-21 20:40:50]   ✅ output/book_draft.pdf (198.08 MB)
[2026-03-21 20:40:50]   ✅ output/book_final.pdf (198.08 MB)
[2026-03-21 20:40:50]   ✅ output/qa_report.md (1.7 KB)
[2026-03-21 20:40:50]   ✅ output/build_log.txt (2.6 KB)
[2026-03-21 20:40:50]   ✅ output/layout_log.txt (161.0 KB)
[2026-03-21 20:40:50]   ✅ output/image_generation_log.txt (27.9 KB)
[2026-03-21 20:40:50]   ✅ output/book_debug.html (266.3 KB)
[2026-03-21 20:40:50] ============================================================

## Collegamenti Correlati
- [[Map - Workflow-Libri|Workflow-Libri Area]]
