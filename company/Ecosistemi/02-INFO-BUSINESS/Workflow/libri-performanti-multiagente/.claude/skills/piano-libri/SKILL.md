---
name: piano-libri
description: Genera il piano editoriale settimanale dei libri KDP - 7 righe eseguibili, una per giorno, con nicchie MISURATE su Amazon, premessa, angolo differenziante e comando gia' compilato. Fa girare i 3 agenti KDP-SCOUT, KDP-EDITOR e KDP-GATE in sequenza. Usa questa skill quando Gael dice "/piano-libri", "fai il piano della settimana", "piano editoriale libri", "cosa scrivo questa settimana", o all'inizio di ogni settimana di produzione. NON usarla per aprire un singolo libro - quello e' /libro-del-giorno.
---

# /piano-libri — Il piano della settimana

Un comando. Sette righe. Chi le apre al giorno 5 **non deve decidere niente**.

```bash
cd "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente"
python -m engine.kdp piano                 # la settimana corrente
python -m engine.kdp piano --giorni 7 --dry-run   # valida senza scrivere
```

## Cosa fa, in ordine

Tre agenti, tre mestieri separati (`agenti/`):

| Agente | Mestiere | Se sbaglia |
|---|---|---|
| **KDP-SCOUT** | propone sotto-nicchie e le **misura su Amazon** | salta la keyword e lo dichiara |
| **KDP-EDITOR** | trasforma gli argomenti misurati in 7 righe | il piano esce con meno righe |
| **KDP-GATE** | verifica il piano **prima** che qualcuno lo esegua | **BLOCK: non scrive niente** |

Output:
```
LIBRI/_piani/piano_<lunedì>.json     per il comando /libro-del-giorno
LIBRI/_piani/piano_<lunedì>.md       per una persona
```

## Le regole che questo comando fa rispettare

**Ogni `dati_amazon` viene da un run vero e porta la data.** Nessuna stima, nessun numero
ereditato. Il 2026-09-01 una decisione di catalogo è stata presa su punteggi di 19 giorni
prima: una nicchia era passata da 83,1 a 72,9 e nessuno poteva accorgersene. Da qui
`misurato_il` obbligatorio su ogni riga, e KDP-GATE che blocca senza.

**Se GATE dice BLOCK, non viene scritto niente** ed esce ≠ 0 dicendo cosa manca. Stessa
logica di `kdp copy`: si valida prima di salvare. Un piano scritto a metà sembra valido, ed è
peggio di nessun piano.

**Meno righe vere sono meglio di sette righe finte.** Se la ricerca produce meno argomenti
validi, il piano esce più corto e lo dichiara (Art.2, zero dati finti).

**Una nicchia, un autore.** Le 7 righe stanno dentro la nicchia di catalogo, sotto lo stesso
nome. Sette libri in una nicchia sono un catalogo che si somma; sette in sette nicchie sono
sette esordi che non si aiutano — è esattamente il difetto B-018, chiuso il 2026-09-01.

## Prerequisiti

1. **Nicchia di catalogo scelta** — `kdp nicchia-stato` deve rispondere. Se no:
   `kdp nicchia-scegli --keywords "..."`. È una decisione umana, non del piano.
2. **Magazzino rifornito** — se è vuoto il comando si ferma e rimanda a `kdp scout`, che è
   KDP-SCOUT e gira da solo (~0,20 $, 10 keyword misurate).

## Cosa fare col verdetto

- **PASS** → il piano è su disco. Da domani si lavora con `/libro-del-giorno`.
- **BLOCK** → leggi i bloccanti: ognuno dice **giorno** e **campo**. Correggi la causa e
  rigenera. Non aggirare: se una regola sembra sbagliata si discute la regola e si cambia il
  codice con un test, non la singola esecuzione.

## Costo e tempi

Misurati il 2026-09-02: **0,19 $** e circa un minuto per un piano da 7 righe (più il tempo
della ricerca Amazon, se il magazzino va rifornito).

## Connessioni

- Esegue il piano: `/libro-del-giorno`
- Agenti: `agenti/KDP-SCOUT.md`, `agenti/KDP-EDITOR.md`, `agenti/KDP-GATE.md`
- Motore: `engine/piano.py`, `engine/scout.py`
- Modello copiato: `YOUTUBE-AUTOMATION-FACTORY/memory/piano_editoriale_70.json`
- Procedura completa: `SOP-SCRIVERE-UN-LIBRO.md`
