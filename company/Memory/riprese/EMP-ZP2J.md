# EMP-ZP2J — Sito Agency Vivo: build del dossier 37

- **Codice di ripresa:** `EMP-ZP2J`
- **Aperto:** 2026-09-11 18:49
- **Stato:** CHIUSO il 2026-09-11 21:59 — **COSTRUITO E DEPLOYATO** (F0-F8 chiuse, F7.5 ponte in backlog B-070)
- **Chi riprende:** basta dire `EMP-ZP2J` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Eseguire il V4 esecutivo di `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` su `agency-empire/`
(Next.js 16.2.3, live `agency-empire-kohl.vercel.app`), fase per fase F0→F8, **solo dopo il «vai»**.

## 2. DOVE SIAMO — cosa è FATTO davvero

- **[2026-09-11 22:00] Build chiuso e deployato:** https://agency-empire-kohl.vercel.app — 19 sezioni, canone v3
  (`src/app/vivo.css`), `<Aura/>` + manifest, gate_voce PASS, gate_siti PASS, MISURA-DOPO.md, LEZIONE.md, CP-20260911-XZCR.
  Restano da Max: 12 foto generate + 2 ritratti in `public/aura/` (B-072), P.IVA in `src/lib/legal.ts`.

- Il dossier 37 è scritto per intero: diagnosi misurata, 3 assi, casting 14/41 immagini, struttura
  19 sezioni, fasi, tre critiche, V4 esecutivo con comandi/gate/forze/ore, pre-mortem, consigli.
- Checkpoint `CP-20260911-D9EP`. Wiki aggiornata.
- **Zero file di `agency-empire/` toccati.**

## 3. COSA È RIMASTO A METÀ

- Niente a metà: il piano è chiuso. Il build è **a zero** per scelta (ordine di Max: prima il piano).

## 4. IL PROSSIMO PASSO ESATTO

1. Leggere `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` **fino al V4 esecutivo** (non fermarsi a P0:
   le critiche cambiano numeri e regole — 10 CTA non 18, hero ≤ 30 parole, canone congelato prima di F4).
2. Scrivere il blocco ⚠️ COORDINAMENTO in cima a `company/Memory/STATO-EMPIRE.md`: perimetro
   `agency-empire/` + `.claude/skills/fabbrica-siti/pattern/` (8 nuovi) + `fabbrica-siti/scripts/gate_voce.py`. Push.
3. F0: `python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" https://agency-empire-kohl.vercel.app --slug 61-agency-baseline`
   → poi `agency-empire/cantiere/BRIEF.md`, `public/aura/manifest.json` (41 righe), analytics + 2 eventi.

## 5. DECISIONI GIÀ PRESE — non ridiscuterle

- **Still AURA originali mai in `public/` né in deploy** (nemmeno preview Vercel): solo dev locale da
  `cantiere/aura-preview/` (gitignored). In produzione: generate (Higgsfield, stesso registro) + ritratto
  di Max (posto 1 hero) + facce team (N11) + screenshot reali dei sistemi.
- **Lista nera** (V10): stronzi, cazzo, cagata, mid, brokie, LOL, JK, daddy. Provocazione sì, insulto no.
- **Ogni provocazione paga con un numero entro 200 caratteri** → `gate_voce.py` (4 controlli, exit 0/1).
- **10 CTA a temperatura** (dopo N1, N4, N5, N7, N8, N10, N12, N14, N16, N18), non 1 ogni 1.100 px.
- **Niente countdown, niente `???`** (curiosity gap totale), niente secondo H1.
- **Ordine di costruzione:** F1a copy N1-N9 → F3 pattern + canone v3 **taggato** → F4 build. Mai F4 prima del tag.
- Scagnozzi toccano **solo** i file di sezione; `globals.css`, `page.tsx`, canone: solo Emperator.
- La pagina-ponte (F7.5) si deploya **solo** se linkata da un template vivo della Bibbia dei Messaggi.

## 6. TRAPPOLE — errori già fatti, non rifarli

- `agency-empire/memory/MEMORY-INDEX.md` parla di **`agency-empire-landing`** (un altro progetto, 10
  sezioni, maggio): è stantio. Il sito vero è `agency-empire/src/sections/` (21 sezioni). Non seguirlo.
- Le "147 immagini" del capture sono icone SVG Lucide: **non** contarle come foto.
- `05b-ascolta-bene` e `11b-carte-scoperte` esistono già: sono E6 ed E17 del piano, si rifanno/spostano.
- `site_capture.py` conta CTA e altezza: rilanciarlo **dopo** ogni fase grossa, non solo alla fine.
- Sub-agenti: l'11/09 11 sentinelle su 11 sono stallate al watchdog (vedi CP-20260911-TVMY). Prompt
  corti, un file per scagnozzo, scrittura incrementale, e se stallano si scrive a mano.

## 7. COMANDI PER RIPARTIRE

```bash
cd "C:\Users\Utente\Desktop\qui tutto\Digital Empire"
sed -n '1,80p' PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md        # ordine + perimetro
grep -n "V4 ESECUTIVO" -A 40 PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md
cat .claude/skills/fabbrica-siti/CLAUDE-SITI.md                     # la legge
ls .claude/skills/fabbrica-siti/pattern/                            # 13 pattern esistenti
python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" https://agency-empire-kohl.vercel.app --slug 61-agency-baseline
```

## 8. FILE TOCCATI (dal piano; dal build ancora nessuno)

- `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` (nuovo)
- `company/Memory/checkpoints/CP-20260911-D9EP.md`, `company/Memory/STATO-EMPIRE.md`
- `second-brain-vault/wiki/projects/Agency/Progetto_Sito_Agency_Vivo.md`, `index.md`, `log.md`

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-ZP2J`*
