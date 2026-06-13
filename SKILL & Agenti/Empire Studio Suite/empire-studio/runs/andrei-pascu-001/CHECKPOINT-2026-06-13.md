# CHECKPOINT — Andrei Pascu Study Run
Data: 2026-06-13
Run: andrei-pascu-001

## RIPRESA DA
**Pipeline fermata a:** Stage 3 VISIONE — video 9CuQI0Cr4Pg
**Prossima azione:** Leggere VTT + tutti i 545 frame PNG del video 9CuQI0Cr4Pg → scrivere video-analysis.md

---

## PROFILI CONFERMATI
| Piattaforma | Handle | URL |
|-------------|--------|-----|
| YouTube | Andrei Pascu | https://www.youtube.com/channel/UCLAag-lcCU9OIIIbLfkAnzA |
| TikTok | @andrei.bsns | https://www.tiktok.com/@andrei.bsns |
| Instagram | @andrei.bsns | https://www.instagram.com/andrei.bsns/ |

**Esclusi:** @SeptemRoptem (vecchio/rumeno), @odoamnelol (altro Andrei Pascu, esports)

---

## LAVORO COMPLETATO

### 1. Estrazione titoli YouTube
- File: `youtube/video-list-raw.txt` — 323 video con ID
- File: `youtube/categories-analysis.md` — 9 categorie analizzate

### 2. Categorizzazione (da studiare: Cat 1-7, skip Cat 8-9)
| Cat | Nome | Video |
|-----|------|-------|
| 1 | Copywriting Tecnico | ~30 |
| 2 | Marketing/Funnel/Ads | ~45 |
| 3 | Freelancer/Business/Vendita | ~60 |
| 4 | AI/ChatGPT/Claude | ~30 |
| 5 | Mindset/Personal Dev | ~45 |
| 6 | Soldi/Business Model | ~30 |
| 7 | Short-form/Viralità | ~25 |

### 3. Pipeline in corso — Cat 1, video 1
- **Video ID:** 9CuQI0Cr4Pg
- **Titolo:** "Copywriter professionista scrive dal vivo (tutorial completo + esercitazione per casa)"
- **Durata:** 1089s (18:09)
- **Capitoli:** 10
  - 0s Introduzione
  - 81s Scrivere il Copy
  - 175s L'ordine delle informazioni
  - 309s La descrizione dell'ad
  - 435s Il target
  - 540s La ricerca
  - 616s Iniziamo la ricerca
  - 673s A cosa servono i pannelli assorbenti?
  - 752s Esempi di copy per pannelli assorbenti
  - 1049s Conclusioni
- **Run folder:** `runs/andrei-pascu-001/cat1-copywriting/9CuQI0Cr4Pg/`
- **Stage 1 (ingest):** ✅ DONE — `ingest.json` creato
- **Stage 2 (frames):** ✅ DONE — 545 frame PNG @ --interval 2 → `frames/`
- **Stage 3 (visione):** ⏸️ FERMATO — VTT disponibile, frame pronti, NON ancora letti
- **Stage 4 (atoms):** ⬜ non iniziato
- **Stage 5 (verifica):** ⬜ non iniziato
- **Stage 6 (forge→wiki):** ⬜ non iniziato
- **Stage 7 (wiki write):** ⬜ non iniziato
- **Memory Empire C-H:** ⬜ non iniziato

### 4. TikTok
- Problema: DPAPI error su Chrome e Edge per cookie auth
- Soluzione da fare: export manuale cookies con estensione "Get cookies.txt LOCALLY"

---

## ORDINE COMPLETO CATEGORIE DA PROCESSARE

### CAT 1 — Copywriting Tecnico (~30 video)
Priorità video (in ordine suggerito):
1. ⏸️ 9CuQI0Cr4Pg — Copywriter professionista scrive dal vivo (pipeline in corso, fermata Stage 3)
2. ⬜ qOK4WP82Bvo — COPYWRITING: cos'è, come funziona e come INIZIARE oggi
3. ⬜ jgIgOPAnYNY — Come diventare un copywriter - tutorial COMPLETO
4. ⬜ hb89lccIacY — 10 strategie PROVATE per EMAIL copywriting
5. ⬜ lQMO0LdeI2c — Copywriter Analyzes Copywriting (Live)
6. ⬜ IWCHN_mE2Vo — Copywriter Analizza Copywriting (Live)
7. ⬜ Ahp_6rHSOsU — Usa Google Docs come un copywriter PRO (8 consigli)
8. ⬜ 6WMkz5Q8g6g — 4 Tips for Writing Persuasive Texts & Copywriting
9. ⬜ nRm7JLsP1bc — Basta usare formule clichè di copywriting
10. ⬜ EBU57iVAutA — Se scrivi QUESTO nel tuo preventivo NON venderai
11. ⬜ 3zJpI8-7TW4 — Buttons that sell: how to make CTAs
12. ⬜ IYd-VOngDog — La parte più importante quando fai copywriting
13. ⬜ t67-j2LiXgQ — Copywriting: How to Start as a Freelance Copywriter
14. ⬜ sTCwYnWmgcQ — How to Become a Copywriter with Zero Experience
15. ⬜ fGpz-uOgr4k — email marketing povero, email marketing ricco
16. ⬜ nP4ojCzvjr8 — L'email marketing dal POV dei lettori
17. ⬜ yX0XZh2PSYo — Merge Tag nell'email marketing
18. ⬜ L5_Z63nxXjI — I reviewed YOUR copies
19. ⬜ Pv5uzIxp96U — I correct your copy
20. ⬜ VbxTgp_fz8Y — Revisione copy oF girl
21. ⬜ uqa06rlgmj4 — Come migliorare con gli hook (1 consiglio)
22. ⬜ PJtGLr-qGTw — Come scrivere pubblicità per i video nel 2022
23. ⬜ wTpfKuHJhOE — Hormozi writes his own copy
24. ⬜ k_DXsUCIkr8 — The real script of the Wolf of Wall Street
25. ⬜ NydMBZ2nUTE — Copione Wolf of Wall Street
26. ⬜ -zUDxSdaKRY — 6 levels of tone of voice
27. ⬜ _yUzEe29aTQ — copy.exe - adesso disponibile
28. ⬜ 6ITBjfPQg3I — scrittore professionale di PDF
29. ⬜ iy13HC9M8z0 — I corrected ChatGPT's copywriting

### CAT 2-7: Iniziare solo dopo completamento Cat 1

---

## PIPELINE CORRETTA (da seguire su ogni video)
```
[EMPIRE STUDIO]
Stage 0  Memory bootstrap + Strategy Manifest
Stage 1  Ingest (yt_ingest.py)
Stage 2  Frame extraction (ffmpeg → PNG, --interval 2)
Stage 3  VISIONE (Claude legge ogni frame PNG via Read nativo)
Stage 4  Knowledge atoms + tracciabilità P12
Stage 5  Verifica (frame reali? niente inventato?)
Stage 6  Forge → wiki
Stage 7  Wiki write

[MEMORY EMPIRE — OBBLIGATORIO post ogni video]
Stage C  Archive INTEGRALE → knowledge/<video-id>/ (MAI riassunti)
Stage D  Enrichment-research: relevance → gap → scout → propose
Stage E  Gate (permission-guard approva/nega)
Stage F  Apply enrichments
Stage G  Audit + rollback se serve
Stage H  Report: cosa archiviato + quali skill arricchite/non arricchite
```

---

## FILE PRODOTTI FINORA
```
runs/andrei-pascu-001/
├── CHECKPOINT-2026-06-13.md          ← questo file
├── youtube/
│   ├── video-list-raw.txt            ← 323 video con ID e titolo
│   └── categories-analysis.md       ← 9 categorie dettagliate
├── tiktok/
│   └── video-list-raw.txt           ← errore DPAPI, da risolvere
└── cat1-copywriting/
    └── 9CuQI0Cr4Pg/
        ├── ingest.json               ← metadata + capitoli + subs
        ├── 9CuQI0Cr4Pg.it.vtt        ← trascritto italiano
        ├── 9CuQI0Cr4Pg.webp          ← thumbnail
        ├── video.mp4                 ← video scaricato (360p)
        └── frames/
            ├── manifest.json         ← mappa frame → timestamp
            └── frame-001.png … frame-545.png  ← 545 frame PNG reali
```
