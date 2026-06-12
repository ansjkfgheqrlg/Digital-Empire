> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 · Reparto L2 RESEARCH · WF-CUSTOMER/WF-COMPETITOR/WF-TREND

# T-RESEARCH — Ricerca: Customer / Competitor / Trend

> Funzione L4 · Reparto: L2 RESEARCH · Ecosistema: 08-INTELLIGENCE
> Riferimento ecosistema: `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md`

---

## Scopo

Produrre dossier strutturati di ricerca per gli ecosistemi business: ICP e JTBD per AGENCY
e MARKETING, profili competitor da URL, radar trend mensile per la Board. Tre sotto-funzioni
(Customer, Competitor, Trend) condividono questa scheda; il campo `tipo_ricerca` seleziona
il workflow attivo.

---

## Input

```json
{
  "tipo_ricerca": "customer | competitor | trend",
  "target": "URL competitor | nicchia | keyword mercato",
  "ecosistema_richiedente": "01-AGENCY | 04-MARKETING | ...",
  "icp_ref": "brands/<slug>/icp.json (facoltativo)",
  "deadline": "YYYY-MM-DD"
}
```

## Output

```json
{
  "dossier_path": "knowledge/research/<slug>-<YYYYMMDD>.md",
  "wiki_page": "second-brain-vault/wiki/synthesis/<slug>.md",
  "highlights": ["finding 1", "finding 2"],
  "fonti": ["url1", "url2"],
  "next_action": "aggiorna ICP | crea ADR | brief Board"
}
```

---

## Processo per tipo

### Customer Research (WF-CUSTOMER)
1. Avvia skill `customer-research` con nicchia target.
2. Interviste JTBD (template strutturato): bisogni funzionali, emotivi, sociali.
3. Matrice awareness: cold/warm/hot segmentation.
4. Output → aggiorna `brands/<slug>/icp.json` + pagina wiki `entities/`.

### Competitor Profiling (WF-COMPETITOR)
1. Avvia skill `competitor-profiling` + `market-competitors` con lista URL.
2. Estrae: posizionamento, offerta, pricing, CTA, punti deboli, social proof.
3. Output → pagina wiki `synthesis/Competitor-<Nicchia>.md` con tabella comparativa.
4. Notifica MARKETING per aggiornare copy differenziante.

### Trend Radar (WF-TREND)
1. Scansiona fonti monitorate (RSS, newsletter, AgentDB `intelligence/trend`).
2. Identifica segnali deboli e forti per il mercato DE (AI, piattaforme, offerta).
3. Compila brief mensile (formato fisso: max 1 pagina) per la Board.
4. Archivia fonti in `knowledge/trend/<YYYYMM>/`.

---

## Regole critiche

- Fonti sempre citate e tracciate (no ricerca senza source list).
- Competitor profiling: basato su URL reali forniti, non su conoscenza a priori del modello.
- Trend radar: cadenza mensile schedulata via OPERATIONS (WF-CRON).

---

## Connessioni

- Agenti gestori: `int-customer-researcher` · `int-competitor-analyst` · `int-trend-scout`
- Skill primarie: `customer-research` · `competitor-profiling` · `market-competitors`
- Output verso: AGENCY (ICP) · MARKETING (competitor brief) · Board (trend)
- Cross-link: [[T-INGEST-WEB]] · [[T-WIKI-CONTEXT]] · [[08-INTELLIGENCE/ECOSISTEMA.md]]
