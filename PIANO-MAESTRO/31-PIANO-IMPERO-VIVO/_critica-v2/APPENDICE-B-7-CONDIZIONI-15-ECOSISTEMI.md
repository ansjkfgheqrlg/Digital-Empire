# Appendice B — le 8 condizioni sui 15 ecosistemi

Sentinella indipendente (opus), 2026-09-10 — ricognizione in sola lettura

---

## Cosa è stato fatto, e come

Chiusura di **V3 §7**: le otto condizioni di V2 §4.1 (VIVO: V-a..V-d) e §4.2 (COLLEGATO:
C-a..C-d) sono state provate **una per una sui 15 ecosistemi** di `company/Ecosistemi/`, perché
`empire vivo --json` non deve pubblicare uno stato mai valutato per 15 nodi su 54.

**Le otto condizioni** (testo di V2 §4.1-4.2, non riformulato):

| | Condizione | Come si prova |
|---|---|---|
| V-a | si invoca con un comando dichiarato | il comando esiste ed esce 0 |
| V-b | produce un'uscita conforme a un contratto scritto | l'uscita valida contro lo schema |
| V-c | l'uscita finisce in un posto stabilito | il percorso è dichiarato e il file c'è |
| V-d | un test lo prova, ed è rilanciabile | il test esiste ed è verde |
| C-a | un ingresso dichiarato | il contratto in ingresso esiste |
| C-b | un'uscita dichiarata verso un destinatario che esiste come casella | il contratto nomina il destinatario **e la sua cartella/coda esiste su disco** |
| C-c | la traccia nasce da sola nel formato unico e nel registro dell'Impero | `trace stato --origine hook` la vede |
| C-d | ha servito un consumatore reale almeno una volta | esiste il fatto: file consegnato, lead passato di stato, euro incassato |

**Metodo** (L7 — si scrive ciò che si è misurato):
- Fonti primarie: `Read`/`Grep`/`Glob` su `company/Ecosistemi/<NN>-<nome>/`, `ECOSISTEMA.md`,
  `BACKBONE.md`, `NAMESPACE.md`, il codice dei motori fuori da `company/`, e
  `dati/censimento-01a-ecosistemi.md` (rilevazione del 2026-09-06, 1.256 righe).
- Comandi lanciati: **solo in sola lettura** (`ls`, `find`, `grep -c`, `test -f`). Nessun comando
  che scrive, invia, committa o spende.
- **Nessun test è stato eseguito.** Dove V-d dice PASSA, la prova è *l'esistenza del file di test
  più il verde già registrato da una fonte citata*; dove il verde non è documentato, l'esito è
  NON VALUTATO e lo dichiara la colonna Prova. Un test che esiste ma non è mai stato visto verde
  **non è un PASSA** (V2 §4.1: «il test esiste **ed è verde**»).
- **PASSA** = prova trovata. **NON PASSA** = verificato e manca. **NON VALUTATO** = non
  verificabile con certezza in tempo ragionevole, e il perché è scritto.

**Perimetro:** le 15 cartelle-ecosistema censite in `censimento-01a-ecosistemi.md`. Nota di
perimetro: sul disco oggi le cartelle sono **16** (`ls company/Ecosistemi/` → 16 + `REGISTRO-NUMERI.md`),
perché `15-LANCI` è nata **dopo** il censimento del 06/09 (ADR-025, 08/09). Le 15 schede qui
sotto seguono il censimento; `15-LANCI` è aggiunta come **scheda 16 fuori quota** in coda, per L1
(niente si scarta) e per non falsare il totale di 120 = 15×8 che V3 §7 si aspetta.

---
