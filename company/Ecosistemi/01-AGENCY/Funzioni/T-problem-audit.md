> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A3 + sez. 5 (market-audit, cro_audit)

# T-PROBLEM-AUDIT — Problem Auditor

> Funzione L4 di A3-PREVENTIVI · Worker · Agente: `AG-A3-AUDIT-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A3

## Cosa fa

Quantifica il problema del cliente partendo dal brief di T-DISCOVERY-BRIEF.
Trasforma "problema vago" in "problema con impatto economico/operativo misurabile" — il preventivo
APRE con questo dato. Skill: `market-audit`, script: `cro_audit.py`.

## Metodo di quantificazione

| Tipo problema | Come si quantifica |
|---|---|
| Outreach manuale | ore/giorno × costo ora + lead persi per volume insufficiente |
| Produzione contenuti lenta | pezzi/settimana attuale vs benchmark settore × valore per pezzo |
| Mancanza di knowledge base | ore perse in ricerca interna × FTE × frequenza |
| Conversione sito bassa | traffico × tasso conversione attuale vs benchmark × valore lead |

**Regola:** si quantifica SOLO con dati forniti dal cliente in call o verificabili pubblicamente.
MAI inventare numeri. Se il cliente non ha dati → si usa il benchmark di settore con disclaimer
esplicito "stima basata su benchmark: verifica con i tuoi dati reali".

## Output schema

```json
{
  "problema_primario": "Outreach manuale: 2h/gg, 20 email/gg",
  "impatto_quantificato": "~€2.000/mese costo opportunità ore + ~€15.000/anno lead non raggiunti",
  "metodologia": "ore fornite dal cliente × costo ora stimato €25/h + benchmark settore",
  "fonte_dati": "chiamata diretta + benchmark e-commerce Italia 2025",
  "prodotto_raccomandato": "Outreach Factory €4.000",
  "payback_stimato": "2 mesi (€4.000 one-time vs €2.000/mese risparmiati)",
  "disclaimer": "il payback usa costi stimati cliente: verifica con CFO"
}
```

## Connessioni

- [`./T-discovery-brief.md`](./T-discovery-brief.md) (fornitore brief) · [`./T-proposal-writer.md`](./T-proposal-writer.md) (cliente: usa l'audit nel preventivo)
- [`../Workflow/WF-PREVENTIVO.md`](../Workflow/WF-PREVENTIVO.md) · [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
