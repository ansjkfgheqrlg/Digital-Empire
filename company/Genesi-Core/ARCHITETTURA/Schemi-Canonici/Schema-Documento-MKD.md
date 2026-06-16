# SCHEMA CANONICO — Documento / MKD

> Forma MEDIO-PESANTE (knowledge layer). Master Knowledge Document: il "documento perfetto",
> base canonica da cui si derivano altri artefatti. Motore reale: `content-forge` (MKD obbligatorio,
> P03 No-Summary, P10 master-document-intermediate, P12 traceability).

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando hai conoscenza ampia da rendere canonica, navigabile e riusabile: la fonte di
  verità da cui poi nascono skill/agenti/wiki. È il deposito completo, non il riassunto.
- **NO se** è una singola regola → **Principio**. NO se è coerenza visiva/voce → **Stile**. NO se
  va eseguito → **Workflow/Skill/Agente**.
- **REGOLA CARDINALE (P03): MAI riassumere. SEMPRE espandere.** Ogni atomo del sorgente compare
  nel MKD, più ricco — non più povero. Output ≥ sorgente.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Frontmatter/intestazione**: titolo, scopo, fonti (tracciabilità: chi ha detto cosa), data.
2. **Indice / mappa atomica**: l'elenco navigabile di tutti gli atomi informativi coperti.
3. **Corpo ad atomi informativi**: ogni concetto = una sezione auto-contenuta con definizione,
   dettaglio, esempi (espansi, non citati di sfuggita), eventuali schemi/tabelle.
4. **Marcatura della genesi**: ciò che è derivato/aggiunto (non nel sorgente) è etichettato (es. `➕`).
5. **Cross-reference**: link interni tra atomi correlati (il documento è un grafo, non una lista).
6. **Coverage statement**: dichiarazione che il 100% degli atomi del sorgente è presente.
7. **Connessioni** esterne.

## Template vuoto (copiabile)
```markdown
---
Titolo: · Scopo: · Fonti: [src1, src2] · Created: YYYY-MM-DD
---
# <Titolo MKD>
## Mappa atomica
- [Atomo 1](#a1) · [Atomo 2](#a2) ...
## A1 — <Concetto>
<definizione → dettaglio espanso → esempio(i) → schema/tabella>
➕ <materiale derivato etichettato>
→ correlato: [[A2]]
## A2 — <Concetto>
...
## Coverage
100% atomi sorgente presenti: <conteggio o lista>
## Connessioni
```

## Checklist di completezza (per struct-gate)
- [ ] **Intestazione** con scopo + fonti (tracciabilità).
- [ ] **Mappa atomica** navigabile presente.
- [ ] Corpo organizzato in **atomi informativi** auto-contenuti (definizione + dettaglio + esempio).
- [ ] Materiale derivato/aggiunto **etichettato** (distinto dal sorgente).
- [ ] **Cross-reference** interni tra atomi (≥1 ogni atomo dove pertinente).
- [ ] **Coverage statement**: 100% atomi sorgente presenti.
- [ ] Lunghezza output ≥ sorgente (verifica anti-riassunto, P03).
- [ ] **Connessioni** esterne ≥2.

## Esempio minimo compilato
MKD "Outreach v2.0". Fonti: 4 transcript. Mappa atomica: 12 atomi. Atomo A3 "qualifier NVIDIA
Nemotron": definizione + flusso + ➕ esempio di prompt derivato + tabella soglie → correlato [[A7 writer]].
Coverage: 12/12 atomi sorgente, 0 tagliati, output 3.4× il sorgente. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- **Riassumere** invece di espandere (violazione P03) → il MKD vale meno del sorgente. Fatale.
- Atomi non auto-contenuti (rimandano altrove per la definizione) → non è una base canonica.
- Materiale inventato non etichettato → si confonde fonte e derivazione (rompe tracciabilità P12).
- Lista piatta senza cross-reference → è un elenco, non un grafo di conoscenza.
- Nessun coverage statement → impossibile garantire che nulla sia andato perso.

## Connessioni
- [[Schema-Principio]] — quando il sapere è UNA regola, non un corpo ampio
- [[Schema-Skill]] — un MKD spesso è il sorgente da cui si forgia una skill
- [[README]] — principio della FORMA GIUSTA
- 14-DOSSIER-ARCHITETTURA §1 (forma Documento/MKD, "mai riassunto")
