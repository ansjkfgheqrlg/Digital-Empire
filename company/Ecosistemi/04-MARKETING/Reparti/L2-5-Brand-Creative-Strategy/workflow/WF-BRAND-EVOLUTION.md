---
Type: CONCEPT
Status: Active
Tags: #workflow #brand #evolution #adr #mandato-art2 #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-BRAND-EVOLUTION — Proposta Evolutiva Brand DE

> **Workflow:** WF-BRAND-EVOLUTION · **Reparto:** L2.5 Brand & Creative Strategy
> **Trigger:** segnali di deriva da AN4, richiesta di Max, cambiamento mercato, flag da WF-BRAND-AUDIT
> **Output:** ADR-bozza in `company/Memory/decisions/ADR-DRAFT-BRAND-EVOLUTION-YYYYMMDD.md`
> **Gate di uscita:** nessuna modifica si attua senza approvazione esplicita di Max (Art.5.3 Mandato)
>
> ⚠️ **ATTENZIONE:** questo workflow produce una PROPOSTA, non un'azione. Il brand DE non si
> modifica in autonomia — mai. La proposta scala fino a Max per approvazione formale.

---

## Scopo

Gestire in modo strutturato le evoluzioni dell'identità di brand di Digital Empire. Il Mandato
Art.2 è un invariante operativo: non si tocca senza approvazione esplicita di Max. Quando
emergono segnali che il brand DE potrebbe aver bisogno di evolversi (mercato cambiato,
posizionamento competitor, deriva voce, nuovi prodotti che richiedono nuova identità),
questo workflow costruisce la proposta formale: evidenze, delta proposto, impatto sui kit
esistenti, rischi, e l'ADR-bozza che Max approverà o rifiuterà.

**Questo workflow NON è per aggiornamenti minori** di brand_kit clienti (quello è autonomia
di L2.5). È per modifiche al Mandato Art.2 (la voce DE fondamentale) o al posizionamento
principale di Digital Empire.

---

## Agenti coinvolti

| Agente | Step | Ruolo nel workflow |
|---|---|---|
| `BRAND-LEAD` | 1 + 5 + 6 | Kick-off, costruisce ADR-bozza, scala a Max |
| `BR4` | 2 | Evidenze di contesto: segnali mercato, deriva competitor, dati |
| `BR1` | 3 | Nuova ipotesi di posizionamento (cosa cambierebbe e perché) |
| `BR2` | 4 | Delta voice guide: cosa si modifica nella voce, impatto sui kit esistenti |
| `BR-QA` | 5 | Verifica che la proposta sia coerente con lo spirito del Mandato (anche se propone un cambiamento) |

---

## Passi del workflow

```
[1] BRAND-LEAD — apertura e validazione trigger
  → valuta il trigger: è un segnale reale o interpretazione puntuale?
  → raccoglie evidenze preliminari: quanti output mostrano il segnale? Su quale periodo?
  → decide: il segnale è abbastanza forte da aprire WF-BRAND-EVOLUTION?
     - soglia: 3+ segnali distinti con dati, non impressioni
     - se sotto soglia: log il segnale in state/README.md, non apre il workflow
  → se apre: notifica MKT-Conductor (coordinamento — nessuna evoluzione in silenzio)

[2] BR4 — raccolta evidenze oggettive
  → raccoglie: dati di mercato (competitor hanno cambiato posizionamento? un angolo che
    occupavamo ora è presidiato da 2+ competitor?), feedback ICP (il linguaggio del cliente
    si è spostato?), dati performance (i pattern AN4 mostrano calo di efficacia?)
  → costruisce: dossier_evidenze con fonte per ogni dato (niente "sembra che il mercato...")
  → output: evidenze_drift.md con timeline e dati

[3] BR1 — nuova ipotesi di posizionamento
  → a partire dalle evidenze di BR4, formula l'ipotesi evolutiva:
     - cosa cambierebbe nel positioning statement?
     - l'USP resterebbe "l'agenzia progettata per essere licenziata" o si evolverebbe?
     - quale nuovo angolo si aprirebbe? Perché è meglio del precedente?
  → formula ANCHE il costo: cosa si perde con questo cambio? (brand equity accumulata,
    riconoscibilità, allineamento con la voce attuale)
  → output: positioning_evolution_proposal.md con ipotesi + costo

[4] BR2 — delta voice guide
  → dati BR1: cosa cambierebbe nella voce?
  → produce: diff esplicito (cosa si aggiunge, cosa si rimuove, cosa si modifica)
  → valuta: impatto sui kit clienti esistenti (quanti kit devono essere aggiornati?)
  → produce: migration_plan.md (se approvata, chi fa cosa entro quando per aggiornare i kit)
  → output: voice_delta.md + migration_plan.md

[5] BR-QA — verifica integrità proposta
  → verifica che la proposta stessa rispetti lo spirito del Mandato:
     - la proposta evolutiva mantiene "prove non promesse"?
     - la proposta non introduce dipendency-language o claim senza proof strutturali?
     - il diff è specifico e non ambiguo (può essere applicato deterministicamente)?
  → output: qa_proposta.md con PASS/FAIL + note

[6] BRAND-LEAD — costruzione ADR-bozza e escalation
  → integra tutto: evidenze + ipotesi + delta + migration_plan + QA
  → costruisce ADR-bozza strutturata:
     - Title: "ADR-DRAFT-BRAND-EVOLUTION: [cosa si propone di cambiare]"
     - Contesto: evidenze che hanno motivato la proposta
     - Proposta: delta specifico (cosa cambia nel Mandato Art.2)
     - Alternative considerate: perché non si è scelto di non cambiare niente
     - Conseguenze: cosa cambia nei kit esistenti, nei workflow, nei copy già prodotti
     - Migration plan: chi fa cosa, entro quando
     - Rischi: brand equity persa, confusione per L2.1, tempo di transizione
  → salva ADR-bozza: company/Memory/decisions/ADR-DRAFT-BRAND-EVOLUTION-YYYYMMDD.md
  → scala a MKT-Conductor → escalation a Max

⛔ STOP — nessuna modifica si attua finché Max non ha dato approvazione esplicita

[7] (post-approvazione Max) — BRAND-LEAD esecuzione
  → solo dopo ok formale di Max: modifica il brand_kit DE
  → attiva migration_plan: BR2 aggiorna i kit clienti impattati
  → notifica L2.1/L2.2/L2.3: "brand_kit DE aggiornato, rileggere voice guide prima
    del prossimo run copy"
  → aggiorna state/README.md con nuova versione del kit DE
  → log in wiki/log.md: "WF-BRAND-EVOLUTION approvato da Max: {delta applicato}"
  → salva ADR definitivo in company/Memory/decisions/ADR-NNN-BRAND-EVOLUTION.md
```

---

## Input del workflow

```json
{
  "trigger": "segnale_deriva | richiesta_max | cambio_mercato | flag_audit",
  "descrizione_trigger": "3 output L2.1 nelle ultime 2 settimane usano tono più morbido; pattern deriva potenziale",
  "evidenze_preliminari": ["link o path ai 3 output citati"],
  "urgenza": "standard | urgente",
  "richiedente": "BRAND-LEAD | Max | AN4 via MKT-Conductor"
}
```

---

## Output del workflow

```
company/Memory/decisions/ADR-DRAFT-BRAND-EVOLUTION-YYYYMMDD.md
  ├── Contesto + evidenze (BR4)
  ├── Proposta delta posizionamento (BR1)
  ├── Delta voice guide (BR2)
  ├── Migration plan (BR2)
  ├── QA proposta (BR-QA)
  └── Decisione Max: campo popolato in fase di approvazione (APPROVA / RIFIUTA / RIMANDA + motivo)
```

---

## Gate di uscita

| Gate | Chi | Criteri |
|---|---|---|
| Soglia apertura workflow | BRAND-LEAD | 3+ segnali distinti con dati prima di aprire |
| QA integrità proposta | BR-QA | La proposta rispetta lo spirito del Mandato |
| ⛔ Approvazione Max | Max | L'UNICO gate che sblocca l'attuazione. Senza questo, STOP. |
| Post-approvazione: notifica a L2.1 | BRAND-LEAD | Notifica obbligatoria prima del primo run copy post-evoluzione |

---

## Esempio operativo

**Trigger:** BR4 segnala che 3 nuovi competitor italiani si posizionano tutti su "automazione
outreach" come DE, e il linguaggio "l'agenzia progettata per essere licenziata" inizia a
essere copiato.

**Evidenze:** dossier_competitor aggiornato (BR4) mostra 2 agenzie che hanno usato "autonomia"
come parola chiave nel Q2 2026. Dati AN4: CTR headline "progettata per essere licenziata"
sceso del 12% nel trimestre (possibile saturazione dell'angolo).

**Proposta BR1:** mantenere il posizionamento su autonomia ma aggiornare l'angolo: da
"progettata per essere licenziata" (beneficio finale) a "il tuo sistema, non il nostro
servizio" (possesso immediato — più aggressivo e immediato sull'ownership).

**Delta BR2 (proposta):** voice guide DE + aggiunta regola: ogni output deve avere almeno
una frase che comunica ownership del sistema da parte del cliente, non solo dell'outcome.

**Esito atteso:** ADR-bozza scalata a Max. Max valuta e decide. Il workflow si ferma qui
finché Max non risponde.

---

## Connessioni

- [[brand-lead]] · `agenti/brand-lead.md`
- [[WF-BRAND-AUDIT]] · `workflow/WF-BRAND-AUDIT.md`
- [[WF-BRAND-KIT-BUILD]] · `workflow/WF-BRAND-KIT-BUILD.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 + Art.5.3)
- [[company/Memory/decisions/]] · ADR repository decisioni
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md`
