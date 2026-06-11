# Mandato/ — Il Dipartimento Empire (LX, autorità suprema)

> Questa cartella contiene **la costituzione della holding**: `MANDATO-EMPIRE.md`.
> Nessun agente, nessun codice: solo le leggi. Tutto ciò che esce da Digital Empire
> — a qualsiasi livello, L0→L5 — deve rispettarle.

## Cosa c'è qui

| File | Cosa è |
|---|---|
| `MANDATO-EMPIRE.md` | i 7 Articoli: identità/posizionamento, brand voice, offerta/pricing, qualità, memory/wiki-first, multi-tenant, sicurezza |
| `README.md` | questo file: come il Mandato vincola il gruppo e come si modifica |

## Come il Mandato vincola il Board

Il Board/C-Suite (L0) governa la holding, **ma sotto il Mandato**:
- il Board non può deliberare nulla che contraddica un Articolo — una proposta del genere
  è invalida prima ancora del voto (il CEO la respinge in fase di istruttoria);
- l'unica eccezione è la **deroga registrata**: voto hive-mind raft, motivazione scritta,
  deposito in `company/Memory/decisions/` — e vale per il singolo caso, non cambia la legge;
- il Brand-Voice Sentinel risponde a LX (non al Board): può bloccare anche un output
  approvato dal Board se viola il Mandato.

## Come il Mandato vincola gli ecosistemi (L1→L5)

- Ogni ecosistema eredita gli Articoli come **invariant cardinali** (pattern #8): i suoi
  team li copiano nei propri kernel, non li reinterpretano.
- I gate di Governance (`verify-empire`, categorie 2-3) misurano la conformità al Mandato
  su ogni deliverable: brand voce, prove-non-promesse, pricing, APSOC.
- Gli agenti caricano il Mandato compresso via skill `empire-context` (hook pre-task):
  ogni output nasce già dentro le regole, non viene corretto dopo.
- Conflitto tra un ordine di reparto e un Articolo → vince l'Articolo, sempre:
  `Mandato (LX) > Board (L0) > Ecosistema (L1) > Reparto (L2) > Workflow (L3) > Agente (L5)`.

## Chi può modificare il Mandato

**Solo Max (founder), via ADR.** Procedura:

1. Chiunque (Gael, Board, una Guild, un ecosistema) può **proporre** una modifica:
   bozza ADR con contesto → modifica proposta → conseguenze.
2. La proposta passa il **contradiction-check** (`skill-contradiction-analyzer`) contro
   gli ADR attivi e gli altri Articoli: zero contraddizioni bloccanti.
3. **Max approva o respinge.** Nessun altro ha questa autorità — nemmeno il Board all'unanimità.
4. Se approvata: l'ADR si deposita in `company/Memory/decisions/`, l'Articolo si aggiorna
   nello stesso commit, l'operazione si logga (checkpoint + wiki).

Modifiche al Mandato senza ADR = drift: il Drift-Sentinel blocca il merge
("doc normativo modificato senza log" è uno dei suoi trigger).

## Chi lo fa rispettare

| Guardiano | Articoli vigilati |
|---|---|
| Brand-Voice Sentinel | Art.1 (posizionamento), Art.2 (voce, prove), Art.3 (pricing nei copy) |
| Quality Sentinel | Art.4 (gate APSOC, qualità delivery) |
| Drift Sentinel | Art.5 (memory/wiki-first), coerenza ADR, modifiche non loggate |
| Cost Sentinel | Art.4.3 (dry-run prima di spendere) |
| Security Sentinel | Art.7 (segreti, PII, supply-chain) |

Runbook completi: `company/Sentinels/`.

---

*Fonti: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §1-2 · `07-BACKBONE-RUFLO-SKILLS.md` §1.3, §4 ·
ADR-005 (team prezzi). Modello: MANDATO-EXPONIUM (AION GROUP).*
