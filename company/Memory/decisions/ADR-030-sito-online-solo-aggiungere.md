# ADR-030 — Un sito di Max che è online si può solo AGGIUNGERE, mai modificare (CLAUDE-SITI §13 + gate meccanico)

- **Data:** 2026-09-12
- **Stato:** ATTIVO — LEGGE (nasce da un ordine testuale di Max, non da una scelta tecnica)
- **Decisori:** Max (ordine), Emperator (codifica nel canone + gate)
- **Ordinato da Max, testuale (2026-09-12, dopo il deploy del Sito Agency Vivo v2):** *«hai letteralmente rovinato tutto
  il sito. Riporta il sito esattamente com'era prima che lo modificassi. Poi aggiungi le sezioni che vuoi aggiungere
  senza modificare quelle che già ci sono. Non puoi modificare niente di ciò che già c'è, puoi solamente aggiungere.»*

## Contesto

Il 12/09 il piano del Dossier 37 v2 (20 sezioni «al posto di» 37) è stato costruito e messo **in produzione al primo
colpo** su `agency-empire-landing.vercel.app`, letto come conseguenza del «vai» di Max sul piano. Max lo ha visto
online, lo ha bocciato dopo un'ora e ha ordinato il ripristino integrale (CP-20260912-7ZNY). Il costo: un'ora di sito
rovinato online, rollback, e la fiducia. La lezione non è «il piano era brutto»: è che **un sito che il proprietario ha
visto e approvato è suo**, e chi ci lavora sopra non ha licenza di riscriverlo — nemmeno con un piano approvato, perché
il piano lo ha letto lui e il sito lo ha visto lui, e le due cose non coincidono finché non le vede insieme.

Regola già scritta in memoria (`feedback_sito_online_solo_aggiungere.md`) e nel checkpoint; mancava nel **canone della
Fabbrica** (`CLAUDE-SITI.md`), che è ciò che gli agenti leggono quando costruiscono, e mancava **il gate** che la fa
rispettare da una macchina invece che dalla buona volontà (§9: il gate decide, non l'agente).

## Decisione

**§13 di `CLAUDE-SITI.md` — SITO ONLINE = SOLO AGGIUNGERE.** Su un sito pubblicato che il committente ha visto:

1. **Il «prima» è il LIVE**, non il sorgente nel repo: prima di qualunque lavoro si verifica che la build del sorgente
   dia lo stesso testo del live (il repo può contenere restyling mai deployati — è successo il 12/09).
2. **Si aggiunge soltanto**: file nuovi, componenti nuovi, inserimenti puri in `page.tsx`/`layout.tsx` (righe `+`, zero
   righe `-` sui file esistenti), CSS **scopato** sotto un wrapper proprio (`.vivo`), pagine nuove in cartelle nuove.
3. **Non si tocca** ciò che c'era: testo, ordine, CTA, link, `noindex`, footer — anche se sbagliato, anche se «si
   migliorerebbe». Un difetto dell'esistente si **segnala** al committente (ADR-026: in cima a STATO-EMPIRE) e si
   aspetta la sua parola.
4. **Una riscrittura si fa solo se il committente la ordina con quelle parole**, e comunque **prima in anteprima**
   (`npx vercel` senza `--prod` → URL di preview), mai in produzione al primo colpo.
5. **Il gate è meccanico:** `scripts/gate_solo_aggiunte.py --live <url> --build <out/index.html> --base <tag-del-live>`
   deve dare **exit 0** prima di ogni deploy. Parte A: il testo del live è contenuto, nello stesso ordine, nel testo
   della build (difflib: solo `equal`/`insert`). Parte B: `git diff --numstat` dal tag del live: ogni file esistente ha
   0 righe rimosse, nessun file cancellato. Le deroghe (`--ignora` per stringhe che cambiano da sole, `--consenti` per
   correggere un refuso in una sezione **nostra**) si scrivono nel checkpoint, mai date per default.
6. **Un refuso in una sezione aggiunta da noi** si corregge (è nostra, non del committente), con `--consenti` dichiarato
   e mai con un `delete` di testo.

## Alternative scartate

- **Lasciare la regola solo in memoria/checkpoint** — gli agenti della Fabbrica leggono `CLAUDE-SITI.md`, non la
  memoria di Emperator; una regola che vive dove non la si legge non esiste.
- **Fidarsi del `git diff --stat` a occhio** — il 12/09 il sorgente non corrispondeva al live: un diff sul repo non
  prova nulla sul live. Serve il confronto **testo del live vs testo della build**.
- **Confrontare screenshot pixel-per-pixel** — la grana animata e i reveal rendono il confronto rumoroso (3,6/255 su
  `#risultati` era già «uguale»); il testo è la prova stabile, i pixel restano una verifica visiva a campione.

## Conseguenze

- `CLAUDE-SITI.md` guadagna il **§13** (questo ADR è il suo atto di nascita — §"Come si cambia questa legge").
- Nuovo `fabbrica-siti/scripts/gate_solo_aggiunte.py`; `gate_siti.py` lo richiama quando `project.json` dichiara
  `"online": true` (B-080, da fare — finché non c'è, si lancia a mano prima del deploy).
- Ogni cantiere su un sito online apre con il **tag del live** (`<sito>-live-YYYYMMDD`) e con `build == live` provato.
- Il Dossier 37 v2 e ogni piano futuro di «riscrittura» hanno una fase in più, obbligatoria: **anteprima al
  committente** prima di `--prod`.
- Vale per **tutti** i siti dei clienti della Fabbrica (§4: il design del committente vince), non solo per quelli di Max.

## Contradiction-check

- ADR-023 (due corsie), ADR-024 (canone v2): nessun conflitto — §13 non dice come si costruisce, dice cosa non si tocca.
- §1 «il canone vince sul gusto»: un sito online che **non** rispetta il canone resta com'è; il canone vale sulle
  aggiunte (scopate) e sui siti nuovi. Precisazione, non conflitto.
- ADR-028 (niente blocca tutto): il divieto di toccare l'esistente **non ferma** le aggiunte né il lavoro intorno; le
  tre decisioni di Max sul sito agency (noindex · CTA vecchie · footer legale) si segnalano e si lavora intorno.
