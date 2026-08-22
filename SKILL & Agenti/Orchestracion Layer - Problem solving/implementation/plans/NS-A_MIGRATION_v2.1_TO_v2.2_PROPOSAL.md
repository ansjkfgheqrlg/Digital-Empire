# NS-A — Proposta di migrazione costituzionale NERVE-SOLVE v2.1 → v2.2

**Data:** 15 agosto 2026  
**Stato:** `PROPOSED_NOT_AUTHORIZED`  
**Baseline attiva locale:** costituzione test-only `2.1.0`  
**Target proposto:** payload `2.2.0` non firmato  
**Produzione:** `BLOCKED`  
**Private key:** non disponibile e non deve essere ricostruita o simulata

## Stato di esecuzione host-controlled — 15 agosto 2026

| Stage | Stato | Evidence / vincolo |
|---|---|---|
| M0 | `PASS` | Ambiente CPython 3.13.14 esatto ripristinato; baseline v2.1 immutata rieseguita a 40 test/100%; validator documentale v2.2 ancora `PASS: 707`. |
| M1 | `OPEN — AUTHORITY UNRESOLVED` | La raccomandazione tecnica è `CONSTITUTIONAL_CHANGE`; decide solo un’autorità costituzionale esterna. Evidence: `../evidence/NS-A-v22-M1-TECHNICAL-RECOMMENDATION.md`. Decision request: `../proposals/authority/NS-A-v22-M1-AUTHORITY-DECISION-REQUEST.md`. |
| M2 | `PREPARATORY CHECKS PASS — GATE BLOCKED BY M1` | L’hardening test-first copre payload strict, diff semantico, isolamento dual-candidate, downgrade/collisione same-version, revoca esplicita e tamper. Gate completo: 48 test, statement/branch coverage 100%. Non è uno stage-pass M2 finché M1 resta aperto. |
| M3–M7 | `BLOCKED` | Non esistono signer, firma di produzione, bundle, nuova trust root, lock v2.2 o activation command. |

Le modifiche bounded introdotte prima della decisione sono fail-closed e version-agnostic: A08 rifiuta versioni non forward prima di authority e side effect; il verifier Ed25519 read-only può escludere esplicitamente key ID revocati. Non rendono v2.2 trusted o attiva.

## 1. Scopo

Governare il delta costituzionale necessario per incorporare struttura del problema e commitment attuativo senza modificare o sostituire in silenzio gli artefatti v2.1 già provati.

Questa proposta non è un comando di attivazione, non è una firma, non è un authority decision e non autorizza Component B.

## 2. Artefatti

| Artefatto | Disposizione |
|---|---|
| `config/constitutions/nerve-solve-2.1.0.payload.json` | immutabile |
| `config/constitutions/nerve-solve-2.1.0.bundle.json` | immutabile |
| `config/constitutions/nerve-solve-2.1.0.lock.json` | immutabile |
| `config/trust/constitutional-test-roots.json` | immutabile; test-only |
| `proposals/constitution/nerve-solve-2.2.0.payload.proposed.json` | nuova proposta non firmata |
| `ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.2.md` | baseline architetturale candidata |
| `SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.2.md` | prompt candidato, non attivo per dichiarazione |

Il digest dell’architettura candidata validata è `d7862b9407ee38e469cfb0d1d1776dd1ee60223bc84eae405ae6546db28cad5b`. È registrato anche nel rapporto di validazione v2.2 e non viene auto-referenziato nel documento architetturale.

## 3. Delta controllato

### Principi

Rimangono esattamente dieci e conservano statement first-person. Cambiano solo falsifier che rendono osservabili:

- struttura minima dopo triage;
- decomposizione esplicita;
- divieto di quota universale per la depth;
- divieto di falsa esaustività e alternative cosmetiche;
- owner proposto e standard fra i costi/condizioni visibili.

### Boundary

Sono aggiunte due capability `IN_LAYER`:

- `nerve.problem_structure`: scelta, versioning e critica di strutture scoped;
- `nerve.execution_commitment`: proposta owner/action/deadline/standard/indicator senza authority o side effect.

Precedence, identity, Layer 2/3 handoff e tutte le capability v2.1 restano conservate.

## 4. Compatibilità attesa

Il modello `ConstitutionPayload` schema `1.0` accetta il delta senza modifica del codice: versione, falsifier e boundary sono già campi tipizzati. Ciò non prova compatibilità operativa completa.

L’adozione richiede test addizionali:

1. payload 2.2 strict validation;
2. diff 2.1→2.2 con soli principle falsifier/boundary attesi;
3. rifiuto di downgrade e same-version hash collision;
4. dual-candidate repository test senza mutare l’active version;
5. binding di un nuovo case al 2.2 e immutabilità dei case già legati al 2.1;
6. revocation/trust replacement/tamper regressions su entrambi i candidati;
7. verifier lock distinto che lega architettura, payload, bundle e trust root 2.2;
8. full Component A gate e architecture validator v2.2.

## 5. Sequenza di migrazione

| Gate | Azione | Exit evidence | Fallimento |
|---|---|---|---|
| M0 | validare architettura/prompt/report/payload proposti | rapporto documentale e digest | correggere proposta; v2.1 invariata |
| M1 | authority decide se il delta è costituzionale o soltanto policy operativa | decision record firmato | mantenere 2.1; adottare solo regole compatibili |
| M2 | introdurre test 2.2 senza active lock | test diff/repository/binding | rollback del solo change set test |
| M3 | ottenere bundle da signer separato e trust root approvata | firma/verifica/provenance | target non attivabile |
| M4 | creare lock 2.2 separato con digest esatti | verifier 2.2 pass | lock respinto; 2.1 invariata |
| M5 | eseguire full A gate e migrazione shadow | zero regressioni e case isolation | target quarantinato |
| M6 | emettere `ActivationCommand` con authority e migration ref | receipt/audit atomici | nessuna attivazione |
| M7 | osservare e autorizzare Component B contro la binding scelta | governance decision | B resta hold |

I gate sono sequenziali. La raccolta di evidence può essere parallela, ma nessun gate futuro viene dichiarato passato prima del precedente.

## 6. Rollback

- Prima di M6: eliminare/quarantinare soltanto artefatti 2.2 proposti; nessun rollback della 2.1 è necessario.
- Dopo M6: vietato riscrivere binding dei case esistenti; disabilitare nuovi binding 2.2, revocare authority e pubblicare — tramite l’intera governance — una nuova versione forward correttiva (`>2.2.0`) che ripristini, se necessario, la semantica 2.1. La riattivazione di un numero di versione inferiore resta vietata perché renderebbe ambigui audit, collision control e monotonicità; i case già legati alla 2.1 restano invariati.
- Eventi, receipt e audit non vengono cancellati.
- Un hash 2.2 già osservato non viene riutilizzato per contenuto differente.

## 7. Decisioni esplicitamente non prese

- nessuna firma generata;
- nessuna trust root aggiunta;
- nessun lock attivo cambiato;
- nessun verifier attivo ripuntato;
- nessun case migrato;
- nessun task B eseguito;
- nessuna production readiness dichiarata.

## 8. Exit della proposta

Questa proposta è completa come piano solo se:

- il validator documentale v2.2 passa;
- il payload proposto è strict-valid;
- gli hash v2.1 continuano a coincidere col lock;
- il rapporto di validazione registra limiti e blocchi;
- la decisione M1 rimane esplicitamente aperta a un’autorità esterna.

Lo stato operativo resta `BLOCKED` fino a M6; Component B resta `HOLD` fino a M7.
