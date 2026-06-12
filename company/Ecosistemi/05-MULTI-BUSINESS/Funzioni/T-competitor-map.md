> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1 + 4.0

# T-competitor-map — Funzione L4 (YT-Strategia)

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Strategia · **Workflow:** WF-YT-NICHE
**Agente assegnato:** `mb-yt-competitor-mapper` (Sonnet) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Responsabilità

Per ogni niche candidata in WF-YT-NICHE, analizza i top-3 canali competitor per estrarre
dati verificabili: iscritti, cadenza, formato video, angolo, packaging titolo/thumbnail.

**Dipendenza critica F-MB1:** l'analisi profonda (frame reali + visione Claude) è riservata
ai canali `@Legamidiamore` e `@dosementale` tramite Empire Studio (Intelligence). Prima
di F-MB1, questa funzione opera solo su dati pubblici (iscritti, n. video, cadenza visibile).
Post F-MB1: i pattern estratti dall'ingestione alimentano l'analisi competitor per qualsiasi niche.

## Input / Output

**Input:** lista niche candidate (T-niche-scout); dossier F-MB1 (post ingestione)
**Output:** scheda competitor per niche: top-3 canali con (iscritti, cadenza, formato, RPM stimato, angolo differenziante disponibile)

## Confini

Non produce raccomandazioni strategiche (lo fa mb-yt-strategy-coord). Non esegue
l'ingestione Empire Studio (lo fa Intelligence 08). Non accede a dati privati dei canali.
