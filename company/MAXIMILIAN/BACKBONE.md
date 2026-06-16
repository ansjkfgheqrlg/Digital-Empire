# MAXIMILIAN — BACKBONE (Infrastruttura dell'Organo)

> La spina dorsale dell'organo che È Max: memoria dei verdetti, handoff del 5-bis, relazione col Mandato,
> deleghe (dove MAXIMILIAN decide al posto di Max), ReasoningBank.
> Fonte: [[12-DOSSIER-MAXIMILIAN]] §5 (deleghe) · §6 (relazioni) · §8 (state). Collega: [[ECOSISTEMA.md]]

---

## Namespace memoria — `maximilian/*` (AgentDB)
| Namespace | Contenuto | Test-amnesia (ripresa a freddo) |
|---|---|---|
| `maximilian/verdetti` | ogni review 5-bis `{oggetto, verdetto, motivi, cosa_max_vorrebbe_in_piu, esito}` | da `maximilian/verdetti/<fase-id>` si ricostruisce *perché* una fase fu approvata o rifatta |
| `maximilian/corpus-index` | indice semantico del corpus (chi cita cosa, dove sta ogni direttiva) | MX-MEMORY recupera i precedenti senza rileggere tutto il corpus |
| `maximilian/anticipazioni` | brief WF-ANTICIPAZIONE + flag su quali si sono **avverati** | misura quanto l'organo "vede prima" come Max; alimenta la calibrazione |
| `maximilian/calibrazione` | le correzioni reali di Max ai verdetti dell'organo | affina i test §1 del dossier → l'organo si avvicina a Max nel tempo |

Ogni record è **ripartibile a freddo** (test amnesia, §6 piano V2): un verdetto perso non si rigiudica a
naso, si ricarica da `maximilian/verdetti`.

---

## Handoff in INGRESSO (chi manda l'oggetto da giudicare)
| Da | Handoff | Cosa arriva |
|---|---|---|
| **Conductor di qualsiasi fase** | deliverable di fase | struttura prodotta + SPEC di fase + dossier di riferimento → WF-REVIEW-MAXIMILIAN (5-bis) |
| **FORGE** (a valle del Genesi Core) | artefatto forgiato | output eval-passed → "è all'altezza di Max?" prima della registrazione Identity-HR |
| **Conductor a inizio fase** | scope dichiarato | lo SPEC appena scritto → WF-ANTICIPAZIONE ("cosa vorrà Max DOPO?") |

## Handoff in USCITA (cosa parte, sempre)
| A | Handoff | Cosa parte |
|---|---|---|
| **BUILD (passo 3)** | verdetto **RIFAI** | `{verdetto:"RIFAI", motivi:[…]}` → la fase **torna indietro** (potere di blocco) |
| **COMMIT (passo 7)** | verdetto **APPROVA** | `{verdetto:"APPROVA"}` → la fase procede a CP + STATO + push |
| **SPEC / BACKLOG** | brief di anticipazione | slot pronti nello SPEC + item non urgenti nel BACKLOG (ADR-005) |
| **`maximilian/verdetti`** | record del verdetto | tracciamento obbligatorio: Max può ribaltare a posteriori |

---

## Relazione col Mandato (LEGGE vs STANDARD) — §6
Il **Mandato** e MAXIMILIAN sono **entrambi LX, accanto, e NON si sovrappongono**:
- **Mandato = legge.** Cosa è *lecito* (enforcement, regole, Sentinelle). Risposta binaria: lecito/illecito.
- **MAXIMILIAN = standard e direzione.** Cosa è *all'altezza* di Max (scala, chirurgia, ambizione, voce).

Un output può essere lecito ma non all'altezza (bocciato qui), o all'altezza ma illecito (bloccato dal
Mandato). **In conflitto:** il Mandato prevale sul lecito/illecito; MAXIMILIAN prevale sullo standard/scala.
Verso il Genesi Core sono **gate in serie**: ARCHITETTURA (struttura completa) → FORGE (contenuto +
eval) → MAXIMILIAN (all'altezza) → Mandato (lecito) → Identity-HR (registra) → VIVO.

---

## Deleghe — dove MAXIMILIAN decide AL POSTO di Max (§5)
Max delega per non essere il collo di bottiglia (*"delega aggressiva… lui approva a lotti"*). L'organo
pre-approva **SOLO dove esplicitamente delegato**; tutto il resto resta a Max.
| Ambito | Delega | Vincolo |
|---|---|---|
| **Review di fase (5-bis)** | SÌ — approva/boccia in autonomia | Max può ribaltare a posteriori; verdetto sempre tracciato |
| **Standard / qualità** | SÌ — è l'autorità di standard | si appoggia ai test del corpus, non a opinioni |
| **Prezzi** | NO diretto — passa al team-prezzi (B-003); ok finale del lotto sì | catalogo fisso, mai sconti improvvisati |
| **Strategia / visione nuova** | NO — solo Max apre nuove direzioni | l'organo le ESEGUE e le fa rispettare, non le crea |
| **Spese reali (API/crediti)** | NO — resta ok esplicito (dry-run, pattern #3) | l'organo può solo segnalare se una spesa è "da Max" |

**Confine ferreo:** MAXIMILIAN NON fa il lavoro degli ecosistemi e NON sostituisce il Mandato. È autorità
di STANDARD e DIREZIONE, con potere di **BLOCCO** — niente di più, niente di meno.

---

## ReasoningBank
I pattern di bocciatura ("perché Max boccerebbe questo": *un .md solo per un reparto = INACCETTABILE*;
*v1 grande come un giocattolo*; *fatto solo il chiesto*) alimentano la conoscenza corporate. Gli ecosistemi
**imparano lo standard PRIMA della review 5-bis** → arrivano già all'altezza, l'organo boccia meno nel tempo.
Le correzioni di Max (`maximilian/calibrazione`) chiudono il loop: ogni RIFAI ribaltato affina i test.

---

## Navigazione
- Porta d'ingresso → [[ECOSISTEMA.md]] · Addestramento → [[Corpus-Link.md]]
- Fonte di verità → [[12-DOSSIER-MAXIMILIAN]] · Ciclo → [[10-METODO-CICLO-FASE]] (passo 5-bis)
- Accanto → [[13-DOSSIER-MANDATO-ECOSISTEMA]] (legge) · A monte → ARCHITETTURA→FORGE
