# LEZIONE — cantiere agency-empire-landing-vivo (Dossier 37 v2)

**Data:** 2026-09-12 · **Corsia:** B (Next.js 16, `output: "export"`) · **URL vivo:** https://agency-empire-landing.vercel.app ·
**Misure:** `MISURA-DOPO.md` · **Piano:** `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` (v2, V4 esecutivo) · **Ripresa:** `EMP-2AW3` (chiusa)
**Ritorno:** tag `agency-empire-landing-v1-20260912`.

## Cosa ha funzionato (candidati a pattern, §10)
1. **Seguire ogni CTA fino alla pagina finale prima di pianificare.** La falla più grave del sito (noindex + prenotazione in 3 salti col
   brand del corso) stava in `layout.tsx:31` e in `call-cta.tsx:6`: tre righe di grep che la bozza v2 non aveva fatto. Da oggi il
   gate "porta d'uscita" (`href="#"` = 0, domini terzi col brand sbagliato = 0, ≥ 1 link a una prenotazione nostra) entra in `gate_siti.py` (BACKLOG).
2. **`FATTI.md` + `gate_fatti.py`**: ogni numero del copy con la fonte (file:riga), gate deterministico. Ha bocciato 2 numeri al primo giro
   (`7:40` e «controllo n. 4») e li ha costretti a dichiarare la fonte. Promosso a gate della Fabbrica.
3. **Composizione B statica** (`aura-presenti.json` scritto da `aura_prep.py`, `<Aura/>` rende `null`, `.due-col:has(> .foto)` chiude la
   colonna): il sito è andato online con **zero foto** e nessuna cornice vuota. Le foto arrivano senza toccare un componente. Misura doppia
   (vuoto/pieno) come gate: 14.893 / 17.063 px.
4. **`listino.ts` / `fatti.ts` / `contatti.ts`**: un prezzo in un posto, `data-prezzo` su ogni cifra, grep `€ x.xxx` = 0 nelle sezioni.
5. **Riuso del prototipo sbagliato**: VOCE, vivo.css, aura_prep, analytics, /prenota/, /privacy/, /cookie/ dal branch `agency-empire-vivo-wip`
   hanno tagliato F1 −50%, F3 −70%, F2 −70%. Un cantiere sbagliato ben fatto non è lavoro perso.
6. **Header + sticky al canone PRIMA delle sezioni** (LEZIONE v1 n.4): nessuna sorpresa a fine build.

## Errori fatti (§10: al secondo diventano controllo del gate)
1. **Ho inventato un'email di contatto** (`info@digitalempire.it`) in `contatti.ts` e l'ho deployata per ~10 minuti. Un dato di contatto è
   un fatto come un prezzo: **o sta in FATTI.md o è vuoto e la riga non si renderizza**. Corretto e ridistribuito. Regola: `gate_fatti.py`
   va esteso a email/telefono/P.IVA (stringhe con `@` o `+39`) — BACKLOG.
2. **Lighthouse su `python -m http.server` mente**: senza compressione il perf mobile era 76 (581 KiB "risparmiabili"). Con `npx serve`
   (gzip) 88, sul live 88. Misurare perf solo su un server che comprime, o sul live.
3. **Il gate PROVE di `gate_siti.py` boccia ogni `.prova` senza `data-fonte`**, anche i tre numeri di N3/N6: giusto così — i `data-fonte`
   ora ci sono (FATTI.md). I blocchi `.prova` nascono con `data-fonte`, non lo si aggiunge dopo.
4. **Heredoc bash lunghi su Windows falliscono** (già in LEZIONE v1 n.6): perso un giro su N1/N2/N6. Sezioni con `Write`, sempre.
5. **Lenis + GSAP + framer-motion** erano caricati per un solo effetto (smooth scroll + due barre che scivolano): −130 KB tolti con 6 righe
   di CSS. Prima di aggiungere una libreria di movimento si chiede: cosa muove, e reduced-motion lo spegne?

## Deroghe dichiarate
- **Prenotazione di prova non fatta** (gate F6): avrebbe messo un evento vero sul calendario di Max. Verificato invece che l'iframe Calendly
  si carica (Playwright, `embed_domain` corretto) e che `?da=` arriva a `/prenota/`.
- `canone_sync.py` non si applica a un sito (confronta canone.css↔canone.json della Fabbrica): gate colore = grep hex nelle sezioni = 0.
- `/prenota/` best-practices 75 (terze parti Calendly): fuori obiettivo (perf 97, a11y 100 dentro).
- Il critico indipendente sul copy (apex-critic) non ha consegnato in tempo: la revisione "una voce sola" l'ho fatta io leggendo i 19 file
  di fila; il verdetto, se arriva, va in BACKLOG come correzioni di copy.

## Debito dichiarato (BACKLOG)
- B: gate "porta d'uscita" in `gate_siti.py` · `gate_fatti.py` esteso a email/telefono/P.IVA · `apri_cantiere.py` (PM0) · pattern
  `hero-due-composizioni` e `aura-composizione-b` nella Fabbrica · riga `/prenota/` nella Bibbia dei Messaggi · `company/offerta.md` canonico
  (68 copie del listino) · testimonianze con nome/foto/link in N11 · sezione N4 quando esiste il `src` del video.

## Dipendono da Max (ADR-026, in STATO-EMPIRE), nessuno blocca
ritratto (posto 1, 10) · ritratti Gael/Leonardo (11, 12) · Higgsfield per i 10 posti generati · screenshot dashboard (6) · `src` video (N4) ·
P.IVA/sede/PEC (`legal.ts`) · **email pubblica di contatto** (`contatti.ts`) · consenso Novacar/Preventa per il nome · Vercel Web Analytics acceso.
