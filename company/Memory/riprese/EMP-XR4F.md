# EMP-XR4F — Sito Agency: fase successiva, SOLO AGGIUNTE (mai modificare l'esistente)

- **Codice di ripresa:** `EMP-XR4F`
- **Aperto:** 2026-09-12
- **Stato:** APERTO — sito online com'era (giugno) + 3 sezioni aggiunte; si continua solo aggiungendo
- **Chi riprende:** basta dire `EMP-XR4F` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE
Continuare sul sito dell'agenzia **https://agency-empire-landing.vercel.app** (cartella `agency-empire-landing/`) **aggiungendo
soltanto**: altre sezioni che non duplicano l'esistente, le foto (composizione A) quando Max le dà, e le tre decisioni che spettano a
Max. **Legge di Max (2026-09-12): niente di ciò che è online si modifica, si può solo aggiungere.** Memoria:
`feedback_sito_online_solo_aggiungere.md`.

## 2. DOVE SIAMO — cosa è FATTO davvero (CP-20260912-7ZNY)
- La v2 (riscrittura a 20 sezioni, EMP-2AW3, CP-20260911-92MC) è stata **bocciata da Max dopo un'ora online**. Vive nel commit `6565545f`
  e nel tag `canone-v3-landing`: si può pescare da lì (sezioni, copy, CSS), mai ridistribuirla.
- **Live = sorgente di giugno** (`57a0ba0b`, tag `agency-empire-landing-live-20260912`): verificato testo-identico. Il "restyling F1+F2"
  del 2 settembre (`a745231b`, `84c73c33`) **non è mai stato online**: resta in git, Max non lo ha visto, non si tocca senza chiederglielo.
- **Aggiunte online oggi** (commit `9a1fb92a` e precedenti, deploy `5cgwpu2p2`):
  - `src/sezioni-aggiunte/specchio.tsx` (dopo `<Problems />`), `prove-vere.tsx` (dopo `<Results />`), `cosa-ottieni.tsx` (prima di `<FinalCTA />`),
    `bottone.tsx` (CTA nuova → `/prenota/`).
  - pagine `src/app/prenota/` (Calendly on demand, `?da=`), `privacy/`, `cookie/`.
  - `src/lib/fatti.ts`, `listino.ts`, `contatti.ts` (email vuota: mai inventarla), `legal.ts` (vuoti = riga non renderizzata).
  - `src/app/vivo.css`: **ogni regola scopata sotto `.vivo`** (generata da `scratchpad/scope_css.py` sul vivo.css della v2).
  - `page.tsx` +7 righe (3 import + 3 componenti), `layout.tsx` +1 (`import "./vivo.css"`). **0 righe rimosse.**
- **Prova meccanica usata (da rifare a ogni deploy):** testo del live di prima ⊂ testo nuovo, difflib solo `insert`
  (script inline nel CP-20260912-7ZNY / in questa chat: `testo()` = HTML senza script/style/tag).
- Restano com'erano, per ordine di Max: `robots noindex` (`layout.tsx:22`), CTA vecchie verso `chiamata-formazione.netlify.app`
  (`call-cta.tsx:6`), footer `href="#"`, i 34 file in `src/components/sections/`.

## 3. COSA È RIMASTO A METÀ (la "fase successiva")
1. **Altre sezioni da aggiungere** (candidate del Dossier 37 v2 che NON duplicano l'esistente — controllare prima con Max quali vuole):
   la scala «a mano / tool / sistema tuo» (N7), il conto del canone (parte di N9), le obiezioni «No.» (N16 — ma `objections.tsx` esiste),
   «Cosa NON facciamo» (N12 — `scope-limits` esiste). Copy pronto in `cantieri/agency-empire-landing-vivo/COPY.md`, componenti pronti in
   `git show 6565545f:agency-empire-landing/src/sections-vivo/<file>` → adattare: wrapper `<div className="vivo">`, `BottonePrenota`, niente `Aura`.
2. **Foto (composizione A)**: `aura.tsx`/`aura_prep.py`/manifest della v2 (`6565545f`) NON sono nel sito attuale. Se Max dà ritratti o
   immagini Higgsfield: riportare `components/vivo/aura.tsx` + `scripts/aura_prep.py` + `public/aura/manifest.json` come file NUOVI e usarli
   solo nelle sezioni aggiunte. Still AURA originali mai in `public/`.
3. **Tre decisioni SOLO di Max** (ADR-026, non bloccano): togliere il `noindex`; puntare le CTA vecchie a `/prenota/` (oggi vanno al brand
   del corso in 3 salti); footer con P.IVA/sede/PEC e link a `/privacy/` `/cookie/`. Ognuna modifica l'esistente → serve la sua parola.
4. Fabbrica: B-073…B-079 in BACKLOG (gate porta d'uscita, gate_fatti esteso a email/telefono, `apri_cantiere.py`, pattern, Bibbia →
   `/prenota/`, `offerta.md`, N4 video). Regola **§15 SITO ONLINE = SOLO AGGIUNGERE** da scrivere in `CLAUDE-SITI.md` via ADR.
5. Analytics (`@vercel/analytics`) della v2 NON è nel sito attuale (avrebbe toccato `package.json`): aggiungerlo solo se Max lo vuole.

## 4. IL PROSSIMO PASSO ESATTO
1. Chiedere a Max con una riga: *quali* sezioni aggiungere (lista del §3.1) e se vuole le tre decisioni del §3.3.
2. Per ogni sezione: file nuovo in `src/sezioni-aggiunte/`, inserimento puro in `page.tsx`, `npm run build`, prova difflib "solo insert"
   contro il live corrente (`curl -sL https://agency-empire-landing.vercel.app`), screenshot, `npx vercel --prod --yes` dentro la cartella.
3. Dopo ogni deploy: `git diff --stat` deve mostrare solo `+` sui file esistenti.

## 5. DECISIONI GIÀ PRESE — non ridiscuterle
- Solo aggiunte, CSS scopato `.vivo`, CTA nuove → `/prenota/`, numeri solo da `FATTI.md` (`gate_fatti.py`), contatti/legali vuoti finché
  Max non li dà, il "prima" è il live (verificare `build == live`), riscritture solo su ordine esplicito e **prima in anteprima**
  (`npx vercel` senza `--prod` dà un URL di preview).

## 6. TRAPPOLE — errori già fatti, non rifarli
- **Il «vai» su un piano non è «rifai il sito»** (costo: un'ora di sito rovinato online + rollback). Prima di sostituire qualcosa che Max ha
  visto online: anteprima e sua parola.
- Il sorgente nel repo può non essere il live (restyling del 2 settembre mai deployato): `promote` del deploy vecchio + confronto testo.
- Email/contatti inventati: mai (`info@digitalempire.it` è stato online 10 minuti).
- Heredoc bash lunghi su Windows falliscono: file con `Write`.
- Lighthouse su `python -m http.server` mente (no gzip): usare `npx serve` o il live.
- `ListenUp` e altre sezioni vecchie non hanno `id`: le ancore delle sezioni nuove puntano solo a `id` esistenti (`#risultati`) o nuovi.

## 7. COMANDI PER RIPARTIRE
```bash
cd "C:\Users\Utente\Desktop\qui tutto\Digital Empire"
cat company/Memory/checkpoints/CP-20260912-7ZNY.md
cat agency-empire-landing/src/app/page.tsx                      # ordine attuale: 34 vecchie + 3 aggiunte
ls agency-empire-landing/src/sezioni-aggiunte/
git show 6565545f --stat | head -40                              # la v2 bocciata, da cui pescare pezzi
cat .claude/skills/fabbrica-siti/cantieri/agency-empire-landing-vivo/COPY.md
curl -sL https://agency-empire-landing.vercel.app | grep -c "Automatizziamo la tua"   # deve dare 1
```

## 8. FILE TOCCATI (oggi)
- `agency-empire-landing/` (ripristino a `57a0ba0b` + aggiunte), tag `agency-empire-landing-live-20260912`
- `company/Memory/checkpoints/CP-20260912-7ZNY.md`, `STATO-EMPIRE.md`, `BACKLOG.md` (nota), questa ripresa
- `.claude/skills/fabbrica-siti/cantieri/agency-empire-landing-vivo/LEZIONE.md` (esito in testa), `cantieri/INDICE.md`
- wiki `Progetto_Sito_Agency_Vivo` (Archive), `log.md`, `index.md`; memoria `feedback_sito_online_solo_aggiungere.md`

---
*Chiudi con: `python scripts/checkpoint.py chiudi EMP-XR4F`*
