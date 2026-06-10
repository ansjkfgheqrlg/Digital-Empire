# YouTube + Design System Strategy v1.1

**Version**: v1.1 (2026-06-07)  
**Dipartimento**: YouTube Department  
**Content Type**: Design System / Tool Creation  
**Wiki Implementation**: Visual-Heavy Reference + Update-Proposal Integrated

## Trigger di Attivazione
- Input: video o canale YouTube
- Focus dichiarato o dedotto: design, design system, Figma, components, tokens, UI kit, style guide
- Durata tipica: >30 minuti (video lunghi con capitoli)

## Regole Obbligatorie (Non Negoziaibili)
1. **Frame Extraction**: Almeno 1 frame per capitolo + 1 ogni 10-15 minuti. Priorità assoluta su:
   - Creazione componenti
   - Export tokens / JSON
   - UI panels aperti (style guide, properties)
   - Clic su pulsanti chiave (Create, Export, etc.)
2. **Visual Description Depth**: Ogni frame deve avere descrizione ≥ 60 parole che includa:
   - Esatto elemento UI visibile (es. "Figma left sidebar con 12 components listati")
   - Azioni mostrate (es. "cursore clicca su 'Export' → appare JSON preview con color tokens")
   - Risultato visivo (es. "button con shadow blu e corner radius 8px")
3. **Transcript + Visual Sync**: Ogni knowledge atom deve avere sia transcript context che visual evidence.
4. **Trace Rule**: Ogni atomo nella wiki deve avere "Trace: video-ID#timestamp + frame-XXX.png"
5. **Update Proposal**: Obbligatorio generare almeno 1 proposta di miglioramento per workflow esistenti (es. skill creation, master-build, content-forge).

## Decision Tree Interno
```
Input YouTube + Design focus?
├── Capitoli presenti? → Usa capitoli come punti frame prioritari
├── No capitoli? → Frame a 0%, 15%, 30%, 45%, 60%, 75%, 90%, 100% + mid demo
└── Sempre: estrai "passaggi mostrati" (UI actions non detti a voce)
```

## Template di Output per Wiki (da usare in content-forge)
**Nome nota**: `Design-System-[Component/Process]-[Key-Visual]`

**Struttura fissa**:
- ## Visual Evidence (con ref frame)
- ## Step-by-Step (da transcript + visual)
- ## Gotchas mostrati a schermo
- ## Practical Commands / Actions
- **Trace (P12)**: video-xxx#12:34 + frame-003.png

## Performance Goals
- Visual coverage ≥ 85% degli atomi chiave
- Almeno 8-12 frame per video di 1-2 ore
- Minimo 2 update proposal per video lungo

## Esempio di Applicazione
Video "crea design system in 2 ore":
- Frame su: creazione primitives, token export, component variants, style guide panel.
- Descrizione esempio: "A 34:12 si vede Figma canvas con 5 button components. Right panel aperto su 'Variant' properties. Cursore clicca Export → JSON con color e spacing tokens visibile sullo schermo."

**Trace**: Strategia specifica creata per rispondere alla richiesta di "YouTube + Design System Strategy v1.1" con regole precise, decision tree e template.