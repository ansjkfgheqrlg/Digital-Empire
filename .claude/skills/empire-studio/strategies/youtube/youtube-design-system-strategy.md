# YouTube + Design System Strategy (v1.1)

**Reparto:** YouTube · **Tipo:** Design System / Tool Creation · **Wiki:** Visual-Heavy Reference + Update-Proposal Integrated

## Trigger
Video/canale YouTube con focus design/Figma/componenti/token/UI kit, tipicamente long-form (>30 min) con capitoli.

## Regole obbligatorie
1. **Frame**: almeno 1 per capitolo + 1 ogni 10-15 min. Priorita' su: creazione componenti, export token/JSON, pannelli proprieta', click su pulsanti chiave.
2. **Descrizione visiva**: ogni frame descritto da Claude con >=60 parole — elemento UI esatto, azione mostrata, risultato visivo.
3. **Sync transcript+visione**: ogni atomo ha sia il contesto del parlato sia l'evidenza visiva.
4. **Trace**: ogni atomo wiki -> `video-id#timestamp + frame-NNN.png`.
5. **Update proposal**: obbligatoria almeno 1 proposta per workflow esistenti (skill-creation, design).

## Decision tree
- Capitoli presenti -> frame ai capitoli (prioritari).
- Niente capitoli -> frame a 0/15/30/45/60/75/90/100% + demo intermedie.
- Sempre: estrai i "passaggi mostrati" (azioni UI non dette a voce).

## Template nota wiki
`Design-System-[Componente/Processo]-[Visual]`: Visual Evidence (frame) | Step-by-Step | Gotchas mostrati | Comandi/Azioni | Trace.

## Performance goal
Coverage visiva >=85% degli atomi chiave; 8-12 frame per video di 1-2h; >=2 update proposal.
