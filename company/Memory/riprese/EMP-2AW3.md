# EMP-2AW3 — Sito Agency Vivo v2: il sito VERO è agency-empire-landing

- **Codice di ripresa:** `EMP-2AW3`
- **Aperto:** 2026-09-11 22:30
- **Stato:** CHIUSO il 2026-09-11 23:56 — piano v2 CHIUSO (CP-20260911-MX8A), build fermo fino al «vai»
- **Chi riprende:** basta dire `EMP-2AW3` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE
Chiudere il Dossier 37 v2 (`PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md`) sul sito **vero**
`agency-empire-landing/` → https://agency-empire-landing.vercel.app (confermato da Max il 2026-09-11 22:05),
poi costruire **solo su «vai»**. **Mai più toccare `agency-empire/`** (altro sito, ripristinato alla v1).

## 2. DOVE SIAMO — cosa è FATTO davvero
- **L'errore:** l'11/09 ho costruito e deployato il piano sul sito sbagliato (`agency-empire/`,
  agency-empire-kohl.vercel.app). **Riparato:** `agency-empire/` identico al tag `agency-empire-v1-20260911`
  (diff vuoto), ridistribuito in produzione (H1 v1 "Automatizziamo la tua operatività" di nuovo online),
  commit `9a5cc60e` e successivo. Il lavoro vive nel branch `agency-empire-vivo-wip` (origin) = prototipo.
- Sito vero catturato e misurato: `competitor/Andrei Pascu/site-study/capture/63-agency-landing-vero/`
  (38.683 px desktop, 64.255 mobile, 37 sezioni + 5 divider, 10 CTA, 0 foto, 186 dimensioni, 42 sfondi,
  5 famiglie di gradiente, placeholder in `results.tsx`/VSL, Barnum e "12 mesi", footer con href="#").
- Dossier 37 **v2 scritto in bozza** (diagnosi, §0 riuso, 3 assi, mappa 37→20+coda, fasi, decisioni dalle
  critiche abbozzate). La v1 sbagliata è conservata: `37-PIANO-SITO-AGENCY-VIVO-v1-SITO-SBAGLIATO.md`.
- Riusabile dal prototipo (già su main): `gate_voce.py`, 8 pattern vanilla (PASS), `gate_siti.py` fixato,
  `cantieri/agency-empire-vivo/LEZIONE.md`; nel branch wip: `vivo.css`, `aura.tsx`, manifest, `aura_prep.py`,
  `analytics.tsx`, `VOCE.md`, `COPY-V2.md`.

## 2b. FATTO IL 2026-09-12 (chat nuova)
- Dossier 37 v2 **chiuso**: FATTI NUOVI (noindex `layout.tsx:31`; chiamata in 3 salti col brand "Claude Code
  Mastery" → Calendly `max-infoproducer/30min`; `#prenota` = ancora del listino; `output: "export"`; prezzi in 3
  file; `/prenota/`+`/privacy/`+`/cookie/` nel wip), CRITICA 1→P1, 2→P2, 3→P3, V4 (10 fasi, ≈53 h, pesi), politica
  di guasto, PM0-PM12, 9 dipendenze da Max, 4 domande. Nessuna riga di codice toccata.

## 3. COSA È RIMASTO A METÀ
- Niente: il piano è chiuso. Resta solo il «vai» di Max. Memoria di sessione corretta il 12/09.

## 4. IL PROSSIMO PASSO ESATTO
1. Leggere `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` da "# V4 ESECUTIVO" in giù (righe 280-373).
2. Al «vai» di Max: blocco ⚠️ COORDINAMENTO in STATO-EMPIRE + push → **F0** (`cat agency-empire-landing/.vercel/project.json`
   = `agency-empire-landing`; `npx vercel project ls`; curl Calendly; tag `agency-empire-landing-v1-20260912`; zip fuori
   repo; BRIEF con URL + frase di Max delle 22:05; manifest 15 posti; `analytics.tsx` dal wip) → F1 …
3. Senza «vai»: niente. Il piano non si ridiscute; si eseguono le fasi nell'ordine del V4.

## 5. DECISIONI GIÀ PRESE — non ridiscuterle
- **Il sito è `agency-empire-landing`.** `agency-empire/` non si tocca. F7 controlla ANCHE che
  agency-empire-kohl resti intatto.
- **Dal 12/09 (critiche chiuse):** `/prenota/` nostra (Calendly inline dal wip) e tutte e 10 le CTA lì via `<Link>`;
  `#prenota` e `netlify.app` spariscono (grep = 0); noindex tolto nel commit di F7 e legato a `GH_PAGES_BASE`;
  `listino.ts` + `fatti.ts` + `contatti.ts` unici (grep `€ x.xxx` = 0); `FATTI.md` + `gate_fatti.py`; composizione B
  senza foto su ogni posto + gate F5 doppio (manifest pieno/vuoto); prove N11 a 3 livelli, nomi solo con consenso;
  misura servendo `out/` (mai `next dev`); F4 in due metà; 53 h con pesi F0 5·F1 20·F2 5·F3 15·F4a 18·F4b 17·F5 6·F6 5·F7 5·F8 4.
- Tutte quelle della v1 (still originali mai in deploy; lista nera; 10 CTA a temperatura; niente countdown/???)
  + le nuove: VSL solo con video reale; hero a due composizioni (mai segnaposto nell'hero); listino in
  `src/lib/listino.ts` unico; tre sistemi distinti con etichetta mono, non con tre colori; storia in prima
  persona visibile 2 paragrafi + resto apribile; dettagli tecnici delle sezioni "inside" nei `<details>`.
- Via dal copy: «se sei qui è perché senti il peso» (Barnum), «finestra aperta per altri 12 mesi»,
  "312·24·1.4k" finti-live, "99,7%", "decine di implementazioni".

## 6. TRAPPOLE — errori già fatti, non rifarli
- **PM0:** un puntatore in memoria (`agency-empire/memory/MEMORY-INDEX.md` diceva "agency-empire-landing")
  vince sulla deduzione. Se sembra vecchio si verifica con Max, non si scarta. Costo dell'errore: 3 ore.
- `next build` con `distDir` condivisa spegne `next dev` → dev su porta 3012 e distDir diversa.
- `onError` di `<img>` non scatta prima dell'idratazione → controllo al mount (già in `aura.tsx`).
- I componenti condivisi (header/sticky) vanno al canone PRIMA delle sezioni.
- `gate_siti.py` PROVE guarda 1500 char DOPO `class="prova…"`: `data-fonte` va sull'elemento stesso.
- Bash heredoc su Windows: blocchi python lunghi con tripli apici e frecce falliscono → script su file con Write.

## 7. COMANDI PER RIPARTIRE
```bash
cd "C:\Users\Utente\Desktop\qui tutto\Digital Empire"
cat PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md
cat agency-empire-landing/src/app/page.tsx            # le 37 sezioni, nell'ordine attuale
git show agency-empire-vivo-wip:agency-empire/cantiere/VOCE.md > /tmp/VOCE.md
git show agency-empire-vivo-wip:agency-empire/src/app/vivo.css > /tmp/vivo.css
```

## 8. FILE TOCCATI
- `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md` (v2 bozza), `…-v1-SITO-SBAGLIATO.md` (rinominato)
- `agency-empire/` ripristinato; branch `agency-empire-vivo-wip`; `.gitignore` (+ `agency-empire/cantiere/`)
- `company/Memory/STATO-EMPIRE.md`, `checkpoints/CP-20260911-JF6H.md`, questa ripresa, wiki

---
*Chiudi con: `python scripts/checkpoint.py chiudi EMP-2AW3`*
