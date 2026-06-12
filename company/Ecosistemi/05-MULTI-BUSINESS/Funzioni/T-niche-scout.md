> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1

# T-niche-scout — Funzione L4 (YT-Strategia)

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Strategia · **Workflow:** WF-YT-NICHE
**Agente assegnato:** `mb-yt-niche-scout` (Sonnet) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Responsabilità

Scansiona categorie YouTube per identificare niche con potenziale per canali full-AI
(voiceover TTS + visual AI + script). Produce la lista preliminare di 10 niche candidate
con dati verificabili per la scorecard di WF-YT-NICHE.

## Criteri di selezione niche

- Volume ricerca: keyword primaria con domanda reale su YouTube
- Competizione: analizzabile dai canali competitor esistenti
- RPM stimato: sopra soglia minima `[da F-MB1]`
- Producibilità AI: solo TTS + visual AI, zero riprese live
- Rischio policy YouTube: basso (no contenuto medico non supportato, no spam, no reused content puro)
- Unicità rispetto al catalogo canali DE: nessun canale DE con stessa niche/angolo

## Input / Output

**Input:** criteri mb-conductor (RPM minimo, lingua, competizione massima)
**Output:** lista 10 niche candidate con dati di base (keyword, n. canali >10k sub, RPM stimato, rischio policy)

## Confini

Non approva la niche (lo fa mb-yt-strategy-coord + mb-conductor). Non esegue keyword research
approfondita (lo fa T-keyword-yt). Non mappa competitor (lo fa T-competitor-map).
