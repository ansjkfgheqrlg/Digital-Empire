> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.3 + 6

# Reparto L2 — ECOM-Crescita (`MB-ECOM`) ⚠️ DORMIENTE

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-ECOM-CRES · **Priorità:** MEDIA (struttura minima)
**Stato:** DORMIENTE — attivabile in fase E3 (dopo E2 live + tracking attivo)
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Scalare il business e-commerce tramite ads (strategia con Marketing/04) e monitorare gli
ordini/fulfillment. Non parte prima che E2 abbia unit economics positivi (fase E3 gate).

## Workflow L3 di competenza

| Workflow | Stato | Output |
|---|---|---|
| `WF-ECOM-ADS` | DORMIENTE (attivabile in E3) | Piano ads con Marketing; campagne attive; reportistica ROAS/CPC/CAC |
| `WF-ECOM-FULFILL` | DORMIENTE (attivabile in E3) | Monitor ordini, alert anomalie fulfillment, escalation a fornitore/piattaforma |

## Funzioni L4

| Team | Responsabilità | Stato |
|---|---|---|
| T-ads-liaison | Interfaccia con Marketing (04) per strategia ads; MB decide il budget, Marketing esegue | Dormiente |
| T-fulfillment-monitor | Monitor ordini, anomalie, resi; alert a mb-ecom-coord in caso di problemi | Dormiente |

## Agenti L5 assegnati

- `mb-ecom-coord` (coordinator, Sonnet) — supervisione crescita (dormiente fino a E3)
- `mb-ecom-fulfill-monitor` (worker, WASM/Haiku) — monitor ordini/fulfillment (dormiente)

## Gate di attivazione E3

1. Store E2 live con ≥10 listing pubblicati
2. Tracking e-commerce attivo (pixel, conversion tracking)
3. Prime vendite organiche registrate (unit economics misurabili)
4. Budget ads approvato da Cost-Sentinel (Operations, 09) — dry-run obbligatorio

## Principio ads (da dossier §6 fasi E3-E4)

Il budget ads è un input di MB-ECOM; la strategia e l'esecuzione delle campagne
appartengono a Marketing (04). Il contratto di handoff:
`{brand_kit, icp, budget_max, canali_target, kpi: ROAS minimo, prodotti_prioritari}`.
Marketing restituisce report periodico ROAS/CPC/CAC → input per mb-ecom-coord.

## Sinergia con OPERATIONS (09)

- Dry-run prima di ogni spesa ads
- Cost-Sentinel monitora il budget ads per sessione/settimana/mese
- `WF-ECOM-FULFILL` emette eventi `{ordine, costo_fulfillment, canale}` a OPERATIONS per cost attribution

## KPI (post-attivazione E3-E4)

- ROAS (Return on Ad Spend): > 2x (soglia minima per continuare ads)
- Tasso di fulfillment completato senza anomalie: ≥ 98%
- Unit economics positivi entro 90gg da inizio E3 (gate per passare a E4/scaling)
- Zero scaling senza unit economics verificati (blocco mb-conductor)
