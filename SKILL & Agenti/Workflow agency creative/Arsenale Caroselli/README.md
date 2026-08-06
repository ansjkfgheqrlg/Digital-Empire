# Arsenale Caroselli — Digital Empire

Libreria dei caroselli **finiti** (PNG + copy.json), separata dalle cartelle
motore (`caroselli - agency/`, `caroselli - preventa/`) dove vive solo il
codice che li genera. Richiesta esplicita di Max (2026-08-06): "un'arsenale
dei caroselli, una cartella per ogni prodotto".

## Struttura
```
Arsenale Caroselli/
├── Preventa/
│   └── 2026-08-06_tempo-perso-import/
│       ├── slide_01.png … slide_08.png
│       ├── copy.json
│       └── Preventa_CAROSELLO_8SLIDE_ULTRA_GRAIN_4K.zip   (locale, *.zip gitignored)
├── Agency/          (futuro — output di caroselli - agency/, non ancora spostato)
└── <ProssimoProdotto>/
```

Una cartella per **prodotto** (non per data, non per campagna), poi una
sottocartella per ogni batch di caroselli generato, datata + nome breve del
topic. `copy.json` dentro ogni batch documenta prodotto/target/prezzo/leve
usate — leggibile senza aprire le immagini.

## Come ci finisce dentro un nuovo carosello
`caroselli - preventa/confirm_and_download.py` salva già qui di default
(vedi il proprio docstring). Per un prodotto diverso da Preventa, passare il
nome prodotto come primo argomento:
```
python confirm_and_download.py NomeProdotto nome-breve-carosello
```

## Note
- Gli ZIP (`*.zip`) sono gitignored a livello di repo (regola generale, non
  specifica di questa cartella) — restano solo in locale. Le PNG estratte +
  `copy.json` sono invece tracciate, sono il contenuto realmente rivedibile.
- I caroselli del progetto Agency (`caroselli - agency/output_caroselli/`,
  se esistono) non sono ancora stati spostati qui — quella cartella ha un
  proprio `REGOLE.md` di confinamento, va verificato prima di toccarla.
