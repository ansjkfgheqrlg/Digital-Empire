# 24 — CALENDARIO ESECUTIVO ESTATE V2 + Analisi Stream S7 (NFT/Memecoin bot)

> Creato 2026-07-23, Claude (Opus). Ordine Max: salva tutto, metti le task sui giorni del piano, aggiorna
> workflow + piano, task per Max e Gael, + analizza il report S7 (bot trading NFT/memecoin) e se approvato
> delega l'esecuzione a Gemini. Sostituisce il calendario 21→26 del P7 (superato dai fatti: IG morto,
> Corso parcheggiato, workflow €5-15k = jackpot). Riferimenti: dossier 22 (piano V2), 23 (prodotti).

---

## PARTE A — ANALISI DEL REPORT S7 (bot NFT/Memecoin)

### Verdetto onesto (senza scartarlo, come chiesto)
Il report è **tecnicamente solido e — cosa rara — ONESTO**: ammette capitale a rischio, prime versioni in
perdita, NFT illiquidi, memecoin dominati da MEV bot istituzionali. **La sua stessa conclusione è corretta:
mettere in roadmap autunno, NON distogliere da S1/S2.** Sottoscrivo l'analisi tecnica.

### 3 verità che il report dice e vanno ripetute chiare
1. **NON è entrata estiva.** Richiede capitale da perdere + prime versioni in perdita. Se "servono entrate
   ORA" (parole di Max), S7 è lo strumento SBAGLIATO per quel bisogno. Le entrate estive vengono da S1
   (workflow €5-15k + Preventa outbound) e dai prodotti — non da qui.
2. **Contro gli MEV bot istituzionali noi saremmo la exit-liquidity.** Sul memecoin liquido competi con bot
   ad altissima frequenza con accesso privilegiato al mempool. Il retail lento perde. Questo non è pessimismo:
   è la struttura del mercato descritta nel report stesso.
3. **Errore di premessa nel report:** cita "obiettivo €131.000 trainato da S1+S2 (Manuale Claude)". Framing
   VECCHIO: (a) il prodotto è il **Corso CCM** non il Manuale (dossier 22 §0); (b) €131k non è validato da
   nessun modello nostro — il modello reale (dossier 21/22) dà **€3-6k estate**. Il report va riallineato.

### DECISIONE (D-EST-007): APPROVATO come R&D, con 4 condizioni non negoziabili
Approvo S7 **non come stream revenue estate**, ma come **esperimento R&D delegato**, perché così costa ZERO
focus a noi e non distrae da S1/S2 (che era l'obiezione centrale del report). Condizioni:
1. **PAPER-TRADING PRIMA.** Simulazione su dati reali, **zero capitale**, finché non dimostra *expectancy
   positiva* su ≥3-4 settimane di test. Il paper-trading è il gate che scopre GRATIS se abbiamo un edge
   (quasi certamente contro gli MEV bot non ce l'abbiamo — e lo scopriamo senza perdere un euro).
2. **FUORI dalle proiezioni revenue estate.** S7 = €0 nel piano. Se un giorno rende, è bonus.
3. **Solo capitale-che-puoi-perdere**, e SOLO dopo il gate paper-trading superato. Chain a fee basse
   (Solana/Polygon), mai Ethereum mainnet per i test.
4. **Esecuzione 100% a Gemini/Antigravity.** Claude e Gael NON toccano S7 → zero deviazione da S1/S2.
   Brief pronto: `company/Antigravity-Briefs/S7-NFT-BOT-BRIEF.md`.

Sicurezza (dal report, confermo): nessuna chiave privata hardcoded / nel repo / nello zip → solo
`.env.example` + VPS con variabili d'ambiente; kill-switch manuale; limiti posizione + stop-loss.
Cartella prevista: `company/Ecosistemi/08-TRADING-BOT/` (owner Gemini).

---

## PARTE B — CALENDARIO ESECUTIVO (dal 23/07, Opzione B: tutto outbound freddo)

> Oggi = **giovedì 23/07**. Strategia: costruire le macchine (sett.1) → far girare l'outbound (sett.2).
> Jackpot = 1 workflow €5-15k. Pane = Preventa a volume. Corso parcheggiato. S7 in parallelo su Gemini.

### 🟣 GAEL (build — sequenza rigida, task idempotenti, checkpoint dopo ognuno)
| Data | Task | Output atteso |
|------|------|---------------|
| **23-24/07** | **G-EST-1** sezione Preventa separata su `agency-empire/` (`03b-preventa.tsx` + import) · **G-EST-5** sezione PROVE/case-study Novacar sul sito | sito con Preventa (tier suo) + 1 prova reale · `npm run build` verde |
| **25/07** | **G-EST-3** verifica funnel Corso CCM (checkout €1) → poi **PARCHEGGIA** (no audience). Solo report "cosa è live/rotto" | stato funnel documentato, non riattivato |
| **25-28/07** | **G-EST-2** macchina outreach freddo **2 target** (wrap ADR-003, mai riscrivere): lista A = aziende ICP per workflow €5-15k · lista B = concessionari per Preventa. Due script APSOC | dry-run 5 lead finti per lista, pronto al lancio |
| **29-31/07** | **G-EST-4** riempi zone vuote workflow `DIGITAL-EMPIRE/` (WF-S* stub + gate 07-CONTROL) + integra eventuali zip Arena consegnati | workflow senza buchi, gate verdi |

### 🔵 MAX (business — 90 min/giorno; gli input sbloccano Gael)
| Data | Task | Perché |
|------|------|--------|
| **23/07 (OGGI)** | **M-EST-6** definisci ICP workflow (settore, dimensione, dove trovarli) · **M-EST-7** capacità delivery (quanti workflow consegnabili in estate) · **M-EST-4** veto prezzo Preventa (€490/€149) · **M-EST-5→D-EST-007** NFT: confermi delega a Gemini + paper-trading? | senza ICP+capacità, G-EST-2 spara nel buio |
| **24-25/07** | rivedi sezione Preventa + PROVE sul sito (review 10') · raccogli materiale case-study Novacar (numeri, screenshot) | dà a Gael la prova vera da mettere online |
| **26-27/07** | consegna a Gemini il brief S7 (`S7-NFT-BOT-BRIEF.md`) · prepara eventuale lista contatti tiepidi residui | S7 parte su Gemini senza toccare noi |
| **28/07 →** | quando la macchina outreach è pronta: **avvii l'outbound** su lista A (workflow) + lista B (Preventa) → obiettivo: **prime demo prenotate** | qui inizia il flusso reale di cassa |

### 🟡 GEMINI/ANTIGRAVITY (parallelo, isolato)
| Task | Output |
|------|--------|
| **S7** — costruire bot NFT/memecoin in **paper-trading** (4 layer del report: Data/Analysis/Execution/Risk) su Solana/Polygon, zero capitale reale. Brief: `S7-NFT-BOT-BRIEF.md` | zip con report-studio onesto + bot in simulazione + log expectancy. **Gate:** niente soldi veri finché la simulazione non prova un edge |

---

## PARTE C — REGISTRO DECISIONI DI QUESTO GIRO
- **D-EST-006** (fork) → RISOLTO: IG a zero → Opzione B (outbound freddo). Corso parcheggiato estate.
- **D-EST-007** (S7 NFT bot) → APPROVATO come R&D delegato a Gemini, paper-trading prima, fuori revenue estate.
- **DEC-EST-005** (prezzo Preventa €490/€149) → in attesa veto Max (M-EST-4).
- **Priorità revenue estate:** 🥇 workflow €5-15k (dogfooding outbound) · 🥈 Preventa · 🥉 Content Factory ·
  Corso/Second Brain deprioritizzati · S7 = €0 nel piano.

## PARTE D — AUTOCRITICA
1. Calendario troppo ottimista sulla velocità di build outreach → difesa: G-EST-2 wrappa motore esistente, non da zero.
2. Max non consegna ICP/capacità → Gael bloccato su G-EST-2 → difesa: G-EST-1/5 (sito) non dipendono da input Max, partono comunque.
3. S7 "ruba" attenzione nonostante la delega → difesa: condizione 4 (100% Gemini) + €0 nel piano lo isola.
4. Ancora nessun euro incassato → vero: l'incasso arriva con l'outbound (sett.2), non prima. Onestà mantenuta.
