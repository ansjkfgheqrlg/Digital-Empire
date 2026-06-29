---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #agency #delivery #autonomia #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# Regole Non Negoziabili — A4 Delivery & Implementazione

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessun handover senza Gate Delivery verde

Nessuna delivery si chiude senza gate verde di AG-A4-QA. Il Gate Delivery non ha deroga
per urgenza, né per pressione commerciale, né per scadenza.

Se il committente ha urgenza → AG-A4-COORD può consegnare un parziale con nota di rischio
esplicita SOLO con approvazione di AG-DIR. AG-A4-QA documenta ogni bypass non autorizzato.

**Perché esiste questa regola:** il Gate Delivery è l'unico punto in cui si verifica che il
cliente sia davvero autonomo. Saltarlo significa consegnare una dipendenza camuffata da prodotto.

---

## R2 — Zero dipendenza residua da DE a fine handover

A fine handover il cliente deve girare i workflow **senza Digital Empire nel runtime**:
nessuna credenziale DE, nessun nodo DE, nessuna API key DE necessaria per una run.

Il Gate Delivery verifica esplicitamente questo: se per girare serve ancora DE, il gate è FAIL.
Questo è il cuore dell'identità "agenzia progettata per essere licenziata" — non è negoziabile
nemmeno se il cliente "preferirebbe" lasciarci dentro.

**Perché esiste questa regola:** la dipendenza residua trasforma una delivery in un vincolo.
Il nostro posizionamento è l'opposto: autonomia totale del cliente.

---

## R3 — Il countdown 7gg parte solo ad ambiente conforme

Il countdown della promessa "≤7 giorni" parte SOLO quando AG-A4-ENV ha verificato che
l'ambiente del cliente è conforme (OS, Python, permessi, rete, secrets). Mai prima.

Se il giorno-1 l'ambiente non è conforme → AG-A4-COORD esegue rollback: countdown fermo,
runbook requisiti al cliente, alert a Max. La promise 7gg è protetta contrattualmente.

**Perché esiste questa regola:** partire su un ambiente non conforme produce delivery che
falliscono a metà, sforano i 7gg e bruciano fiducia. La protezione è scritta nel contratto.

---

## R4 — Tutto gira sul server del cliente, non in locale/staging DE

I 3 prodotti devono girare sul server/macchina del cliente con i suoi dati. Una run in
locale DE o in staging non soddisfa il Gate Delivery: il check "gira sul server del cliente"
è un check separato e bloccante.

Nessun agente di A4 considera "fatto" un setup che gira solo su infrastruttura DE.

**Perché esiste questa regola:** il valore si trasferisce solo nell'ambiente del cliente.
Tutto il resto è una demo.

---

## R5 — Nessun ticket 90gg chiuso senza conferma del cliente

Durante i 90gg di supporto, nessun ticket si chiude senza conferma esplicita del cliente
che il problema è risolto. La SLA (≤24h bug, ≤48h domanda) è sul tempo di risposta, non
sulla chiusura unilaterale.

Ticket fuori scope → risposta standard + proposta estensione a pagamento separato (via A6),
mai chiusura silenziosa.

**Perché esiste questa regola:** chiudere ticket senza conferma gonfia i KPI di SLA e lascia
problemi reali aperti. La conferma cliente è il vero stato di chiusura.

---

## R6 — Nessun secret o PII cliente nel namespace DE

I secrets del cliente (API key, credenziali, token) vivono sul server del cliente, mai nel
namespace `agency/a4/`. Lo state DE contiene solo riferimenti e flag, mai dati personali o
segreti del cliente.

Il profilo ambiente in `agency/a4/environments` registra "Python 3.11 presente: sì",
non registra password, chiavi o dati di clienti finali.

**Perché esiste questa regola:** un leak di secrets cliente dal nostro namespace è un
incidente di sicurezza. Il multi-tenant (pattern 11) impone isolamento, non centralizzazione.

---

## R7 — Wrap, non rewrite durante la delivery (ADR-003)

Nessun agente di A4 riscrive un motore esistente (Outreach, Content Factory, Second Brain)
durante la delivery. Si clona e si parametrizza. Una modifica strutturale necessaria →
handoff al reparto proprietario, fuori dalla finestra dei 7gg.

**Perché esiste questa regola:** riscrivere sotto pressione di tempo crea varianti non testate
e rompe motori che funzionavano. La responsabilità del motore resta del reparto proprietario.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a4-qa]] · `agenti/ag-a4-qa.md` — esecutore del Gate Delivery
- [[ARCHITETTURA]] · `ARCHITETTURA.md §3` — Gate Delivery e confine autonomia in dettaglio
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4` — fonte vincolante
