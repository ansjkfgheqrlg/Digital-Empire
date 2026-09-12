---
Type: TOOL
Status: Active
Tags: #fabbrica-siti #siti #landing #canone #gate #next-js #vercel #agency
Created: 2026-09-12
Last updated: 2026-09-12
---

# Fabbrica Siti — la legge, il canone, le due corsie, i gate

## Overview
Il sistema unico con cui Digital Empire produce qualunque sito o landing page (`.claude/skills/fabbrica-siti/`).
Una **legge** numerata e citabile (`CLAUDE-SITI.md`, 13 articoli), un **canone** in due copie gemelle
(`canone.css` per il browser, `canone.json` per la macchina), **due corsie** (A vanilla ≤3 pagine senza stato ·
B Next.js 16 per tutto il resto — ADR-023), **19 pattern** con scheda «quando sì / quando no» e una galleria
generata, e **gate deterministici** che decidono al posto dell'agente (§9). Nasce il 2026-09-06 dallo studio del
sito `armageddon.bsns.it` di Andrei Pascu, dove il CSS servito in chiaro citava *«CLAUDE.md §4 says his design
wins here»*: il concorrente aveva una legge numerata, noi quattro skill che si contraddicevano.

## Dettagli

### La legge (`CLAUDE-SITI.md`) — vince l'articolo col numero più basso
| § | Articolo | Origine |
|---|---|---|
| 1 | Il canone vince sul gusto | Dossier 32 |
| 2 | La colonna vince sul breakpoint | Dossier 32 |
| 3 | Il copy prima del layout | Dossier 32 |
| 4 | Il design del committente vince sul brand di casa | armageddon §4 |
| 5 | La corsia si sceglie dal lavoro, non dal gusto | ADR-023 |
| 6 | Ogni numero non ovvio dichiara la sua origine | Dossier 32 |
| 7 | Niente animazione senza `prefers-reduced-motion` | Dossier 32 |
| 8 | Nessun dato duplicato in pagina | Dossier 32 |
| 9 | Il gate decide, non l'agente | Dossier 32 |
| 10 | Ogni cantiere lascia una lezione (`LEZIONE.md`; al secondo errore uguale → controllo del gate) | Dossier 32 |
| 11 | La cassa ha un gradino (pre-cassa, 6 elementi, stampo `precassa.py`) | ADR-024 |
| 12 | L'accento si spende una volta (un colore d'azione, una parola) | ADR-024 |
| 13 | **Un sito online si può solo aggiungere** (il «prima» è il live; anteprima prima di `--prod`; gate meccanico) | **ADR-030**, 2026-09-12 |

Si cambia solo con un ADR in `company/Memory/decisions/`. Una deroga senza citazione dell'articolo è un errore.

### I gate (`scripts/`) — exit 0 o non si consegna
- `gate_siti.py` — il giudice che §9 nomina: controlla una consegna contro il canone.
- `gate_fatti.py COPY.md FATTI.md` — ogni cifra del copy deve stare in `FATTI.md` con la fonte (Dossier 37, C2.4).
- `gate_voce.py` — la voce: ogni provocazione paga con un numero/€/%/data entro 200 caratteri (Asse A).
- `gate_solo_aggiunte.py --live <url> --build <out/index.html> --base <tag-del-live>` — §13: il testo del live è
  contenuto, nello stesso ordine, nel testo della build (difflib: solo `equal`/`insert`) **e** dal tag del live nessun file
  esistente ha righe rimosse. `--consenti`/`--ignora` = deroghe da scrivere nel checkpoint.
- `canone_sync.py` — i due canoni non divergono. `galleria.py` — genera `pattern/GALLERIA.html` e controlla i pattern.

### Gli stampi (ciò che si ripete si stampa, non si scrive)
- `precassa.py` — la pre-cassa a 6 elementi (§11); rifiuta un codice sconto senza scadenza.
- `og_stampo.py` — l'immagine di anteprima 1200×630 per la condivisione (fondo ink, grana PNG, argento, un accento,
  font del canone). Primo uso: `agency-empire-landing/public/og.jpg`.

### I pattern (`pattern/<nome>/pattern.html + scheda.md`)
asse-posizionale · coda-legale · contatore-scadenza · cucitura-fotografica · faq-native · fascia-lampo · formula ·
hero-due-strati · micro-sondaggio · mirror-di-lancio · oggetto-che-si-posa · ora-con · pagina-ponte · pre-cassa ·
prova-video · specchio · testata-targa · tipografia-manifesto · vetrina-cliente. Un pattern nasce al **secondo**
cantiere che lo usa (§10), mai al primo.

### I cantieri (`cantieri/<nome>/` + `INDICE.md`)
Ogni cantiere porta `BRIEF, VOCE, FATTI, COPY, MISURA-DOPO, LEZIONE`. Cantieri: `agency-empire-vivo` (prototipo sul
sito sbagliato, riusato), `agency-empire-landing-vivo` (il sito dell'agenzia: v2 bocciata, poi solo aggiunte).

### Regole nate dagli errori (LEZIONE → gate)
- Il sito dell'agenzia è **`agency-empire-landing`**, mai `agency-empire`: il puntatore in memoria vince sulla deduzione,
  l'URL si conferma nel BRIEF prima di ogni deploy.
- Mai inventare un contatto (`info@digitalempire.it` è stato online 10 minuti): contatti vuoti = riga non renderizzata.
- Il compilatore di Next 16 perde lo spazio iniziale di un testo JSX multiriga con `&apos;` → `{" "}` esplicito (B-081).
- Guardare il reso (screenshot desktop+mobile) prima di consegnare, anche per tre sezioni.

## Connessioni
- [[Progetto_Sito_Agency_Vivo]] — il cantiere che ha fatto nascere §11-§13 e i gate `gate_fatti`, `gate_voce`, `gate_solo_aggiunte`
- [[Synthesis_Sistema_Visivo_Andrei_Pascu]] — le misure da cui nasce metà del canone
- [[Source_Andrei_Pascu_Armageddon_Landing_Lancio]] — il sito che ha mostrato la legge numerata del concorrente
- [[Concept_Guardrail_Che_Si_Fanno_Rispettare]] — il principio dietro §9 e dietro ogni gate della Fabbrica: una regola che dipende dalla buona volontà non è un controllo
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` · ADR-023 · ADR-024 · ADR-030
