---
Type: PROJECT
Status: Archive
Tags: #agency #sito #andrei-pascu #tono #immagini-aura #fabbrica-siti
Created: 2026-09-11
Last updated: 2026-09-12 (sera)
---

# Sito Agency Vivo — dossier 37

## Overview
Piano (non build) per portare nel sito dell'agenzia (`agency-empire/`, live `agency-empire-kohl.vercel.app`)
le tre cose che i lanci di Andrei Pascu hanno e noi no: **il tono** (prima persona, provocazione che paga
con un numero), **gli elementi vivi** (23 mappati, 13 già pattern della Fabbrica Siti) e **le immagini**
(14 su 41 della cartella AURA, con la riga di copy sopra). Ordine di Max del 2026-09-11. Piano scritto in
quattro giri (P0 → tre critiche → V4 esecutivo), ≈70 h stimate, build solo su «vai».

## Dettagli
- **2026-09-13 — Dossier 38 v2 + Tavola v2 + 5 decisioni di Max (CP-20260913-EEV3):** piano riscritto sulle strategie di funneloperator.it
  ([[Source_Funnel_Operator_Sito_2026]]): 24 aggiunte in sei atti (volto 2%, prova 16%, porta nuova 70%), +≤ 8.800 px, 9 schemi in HTML,
  immagini intere al pixel (§14). Tavola v2: https://claude.ai/code/artifact/a7cf07ac-d263-421c-8824-0600b9641384. Decisioni di Max: texture onde = sfondo hero, hero più in alto + funnel a blocchi con
  frecce curve, texture grana = fascia piccola, «Hai competitor» e Specchio della v2 recuperati e migliorati. Texture: file da Max in `public/texture/`.
- **2026-09-13 notte — P4 «la vita» + Tavola Estetica solo-aggiunte (CP-20260913-T3U6):** critica di Max («dove sono le sezioni con le immagini?»):
  il P3 le aveva perse. 13 aggiunte con immagine (firma V0 sotto l'hero, 7 cuciture fotografiche, stanza 3 volti, video, foto nello specchio, 2 fasce-prenota
  con foto, coda legale), casting dal manifest v2, budget +≤ 4.900 px, mai due di fila, `null` senza file. Tavola: https://claude.ai/code/artifact/25405882-779a-43ce-a9a3-91c65c36b34e
- **2026-09-12 notte — DOSSIER 38, il piano «solo aggiunte» (CP-20260912-HTCV):** primo piano con i due vincoli giusti (sito vero + solo
  aggiunte). 11 aggiunte A1-A11 (fascia-lampo, 2 fasce-prenota, misura a 5 eventi, stanza dei 3 volti, video «guardalo girare», immagini vere
  in prove-vere, coda legale, pronto-per-l'indice, AURA nelle sezioni nostre, /prenota/ «prenotato», og fatto), 3 critiche, V4 in 8 fasi con
  gate e pesi (nostra 85% · Max 15%), +≤ 3.000 px, ≈ 20 h. `PIANO-MAESTRO/38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE.md` · artefatto
  https://claude.ai/code/artifact/01019906-18ed-4e27-8cd9-5cc84180f6ca. Il 37 v2 è superato. Build su «vai».
- **2026-09-12 sera — fase «solo aggiunte» n. 2 (CP-20260912-X3A4, ripresa EMP-XR4F aperta):** QA Playwright del live (desktop+mobile,
  8 link, 0 errori console). **Nessuna sezione nuova**: le candidate del dossier (N7, N9, N10, N12, N15, N16) duplicano tutte sezioni già
  online (`hierarchy`, `pricing-roi`, `flow-framework`, `audience`, `my-promise`, `objections`). Fatto invece: 2 refusi nelle sezioni nostre
  («65includono», «Il nostro.L'Outreach» — bug del compilatore Next 16: testo JSX multiriga con `&apos;` perde lo spazio iniziale, rimedio
  `{" "}`); **anteprima di condivisione** (`public/og.jpg` 1200×630 dallo stampo `og_stampo.py` + Open Graph/Twitter in `layout.tsx`, +12
  righe); **`gate_solo_aggiunte.py`** (testo del live ⊂ testo della build + 0 righe rimosse dal tag del live) e **ADR-030 → CLAUDE-SITI
  §13**. Letto nel widget vero: l'unico evento Calendly di Max è «90% formazione 10% Peach · 1 h» → serve un evento agenzia da 30 min
  (gesto di Max). **Deploy prod in attesa di Max** (negato al bot dal classificatore). Build e anteprima Vercel provate.
- **2026-09-12 sera — v2 BOCCIATA da Max, sito ripristinato + solo aggiunte (CP-20260912-7ZNY):** «hai rovinato tutto il sito, riportalo
  esattamente com'era, poi aggiungi senza modificare». Live riportato al deploy di giugno, codice a `57a0ba0b`; aggiunte 3 sezioni
  (`specchio`, `prove-vere`, `cosa-ottieni`) + `/prenota/` `/privacy/` `/cookie/`, CSS scopato `.vivo`, 0 righe esistenti toccate.
  **Legge:** su un sito online di Max si aggiunge soltanto; riscritture solo su ordine esplicito e prima in anteprima. La v2 resta in `6565545f`.
- **2026-09-12 — ONLINE (CP-20260911-92MC, EMP-2AW3 chiusa):** https://agency-empire-landing.vercel.app — 20 sezioni (N4 video esclusa),
  `/prenota/` nostra con Calendly on demand e `?da=` per sezione, noindex tolto, privacy/cookie, sitemap 4 URL. Misure: 38.683 → 14.893 px
  desktop (17.063 con le foto), 64 → 12 dimensioni, 5 → 0 gradienti-card, 0 placeholder, Lighthouse mobile 88/100/96/100. Costruito in una
  sessione dal «vai» (F0-F8), 2 scagnozzi sonnet sulle sezioni di struttura. Nuovo gate `gate_fatti.py`. Composizione B: online senza foto,
  i file di Max (ritratti, Higgsfield, dashboard, P.IVA, email) accendono le parti senza toccare codice. Lezione: mai inventare un contatto.
  `cantieri/agency-empire-landing-vivo/{BRIEF,VOCE,FATTI,COPY,MISURA-DOPO,LEZIONE}.md`.
- **2026-09-12 — v2 CHIUSA (CP-20260911-MX8A):** critiche P1/P2/P3 + V4 esecutivo (10 fasi, ≈53 h, pesi) sul sito vero
  `agency-empire-landing`. Fatti nuovi dal codice: sito **noindex**; CTA chiamata in 3 salti col brand "Claude Code Mastery"
  fino a Calendly `max-infoproducer/30min`; `#prenota` = ancora del listino; `output: "export"`. Decisioni: `/prenota/` nostra
  con Calendly, noindex via in F7 con gate `netlify.app = 0`, listino/fatti/contatti in un file con grep = 0, `gate_fatti.py`,
  composizione B senza foto su ogni posto (gate doppio pieno/vuoto), prove a 3 livelli. Build fermo fino al «vai».
- **⛔ 2026-09-11 22:40 — ERRORE:** il build/deploy delle 22:00 era su `agency-empire/` (sito sbagliato), ripristinato alla v1.
  **Il sito dell'Agenzia è `agency-empire-landing` → https://agency-empire-landing.vercel.app.** Dossier 37 riscritto in v2
  (bozza) sul sito vero; ripresa `EMP-2AW3`; prototipo nel branch `agency-empire-vivo-wip`. CP-20260911-JF6H.
- **2026-09-11 22:00 — COSTRUITO E DEPLOYATO:** https://agency-empire-kohl.vercel.app (CP-20260911-XZCR). 14.798 px, 10 CTA,
  gate_voce/gate_siti PASS, Lighthouse a11y 100. Restano da Max: 12 foto generate + 2 ritratti (B-072), P.IVA. Lezione:
  `.claude/skills/fabbrica-siti/cantieri/agency-empire-vivo/LEZIONE.md`. Versione v1 nel tag `agency-empire-v1-20260911`.
- **Documento:** `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` · ripresa `EMP-ZP2J` · CP-20260911-D9EP
- **Diagnosi misurata** (stesso `site_capture.py` usato su Pascu): noi 43.359 px, 11 CTA (1/3.940 px),
  0 fotografie, 195 dimensioni tipografiche, 48 sfondi; Claude Speedrun 33.756 px / 40 CTA; Armageddon 5.103 px.
- **Voce Digital Empire:** 10 regole (V1-V10) + lista nera; cosa non si copia (parolacce, countdown, `???`).
- **Struttura:** 21 sezioni + 16 divider → 19 sezioni cucite, obiettivo ≤ 28.000 px, 10 CTA a temperatura, 14 foto.
- **Immagini:** due corsie, stesso piano: still originali solo in dev locale; in deploy immagini generate
  nello stesso registro (Higgsfield, dossier 28) + ritratto di Max + facce team + screenshot reali.
- **Tavola estetica (si vede):** https://claude.ai/code/artifact/f3fc31e1-b258-4be6-8074-341c021781c9 — 9 tavole, trattamento B AURA / D filigrana, casting, regole. Asse D del dossier.
- **Cosa nasce oltre al sito:** `gate_voce.py`, `aura_prep.py` + manifest, 8 pattern nuovi in Fabbrica,
  skill `voce-empire` (le 22 formule di Pascu con placeholder).

## Connessioni
- [[Fabbrica_Siti]] — §13 «un sito online si può solo aggiungere» (ADR-030), `gate_solo_aggiunte.py`, `og_stampo.py`
- [[Synthesis_Sistema_Visivo_Andrei_Pascu]] — la temperatura del traffico governa la forma
- [[Concept_CCM_Brand_Guidelines]] — colore dell'azione < 10%, argento + grana
- [[Digital_Empire_6_Phase_Process]] · `../../competitor/Andrei Pascu/site-study/README`
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` · `.claude/skills/fabbrica-siti/CLAUDE-SITI.md`
