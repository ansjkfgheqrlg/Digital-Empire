# Workflow: Analisi SEO e VidIQ

## Obiettivo
Identificare "Cash Cow Channel" e video performanti, estrarne la struttura e analizzarne gli errori SEO da correggere per posizionarsi meglio rispetto all'originale.

## Triggers (`triggers.md` pattern)
- **Time-based:** Esecuzione settimanale per scansionare nicchie target.
- **Event-based:** Lancio manuale tramite input di una keyword o un link YouTube specifico.

## Stato Iniziale (`state.md` pattern)
- `target_niche`: Definita dall'operatore.
- `search_account`: DEVE essere un account neutro, senza cronologia.

## Steps (`step.md` pattern)
1. **Analisi Metriche Base:** Cerca video con alto VPH (Views Per Hour).
2. **Reverse Engineering VidIQ:** Registra Punteggio Tag, CTR stimato e retention rate (se intuibile dai commenti/curva).
3. **Identificazione Difetti:** Se il video è virale ma con SEO scarsa, segnare "Opportunità Alta".

## Error Handling (`error_handling.md` pattern)
- *Errore:* L'account di ricerca restituisce risultati inquinati. *Fix:* Svuotare la cache e i cookie, usare navigazione in incognito.
