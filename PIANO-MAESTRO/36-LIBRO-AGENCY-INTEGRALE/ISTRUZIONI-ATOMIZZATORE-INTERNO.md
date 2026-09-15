# ISTRUZIONI PER L'ATOMIZZATORE DEL MATERIALE INTERNO — Libro I, «Il Metodo Digital Empire»

Lavori in italiano. Il Libro I del Libro dell'Agency parla di COME OPERA DIGITAL EMPIRE: non è
formazione presa da altri, è il nostro metodo. Nessuna fonte esterna può scriverlo. Ma per
passare dallo stesso gate degli altri Libri, anche il materiale interno va ridotto ad
**atomi di conoscenza** con lo stesso schema.

BASE: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\`
USCITA: `PIANO-MAESTRO\36-LIBRO-AGENCY-INTEGRALE\atomi-interni\<GRUPPO>.json`

## Cos'è un atomo

Un'unità di conoscenza autonoma: una regola, un principio, una procedura, una definizione,
una decisione con il suo perché, un numero misurato, un errore commesso e la sua contromisura.
Se una frase insegna qualcosa che si potrebbe applicare da soli, è un atomo. Se è narrazione
di contorno, non lo è.

Ogni atomo ha ESATTAMENTE questi campi:

```json
{
 "id": "KA-001",
 "tipo": "regola | principio | procedura | definizione | decisione | numero | errore | strumento",
 "contenuto": "Cosa dice, in 2-5 frasi complete, comprensibili senza aprire la fonte.",
 "fonte": "percorso/del/file.md § sezione o riga",
 "ancora": "una frase LETTERALE copiata dal file, 8-25 parole, senza modifiche",
 "confidenza": "osservato",
 "capitolo": "I.1 | I.2 | I.3 | I.4 | I.5 | I.6 | I.7",
 "peso": "portante | supporto | contesto",
 "relazioni": [{"verso": "KA-00X", "tipo": "precede | dipende | contraddice | specifica", "perche": "..."}]
}
```

`ancora` è obbligatoria e deve esistere nel file, parola per parola: il gate la cercherà.

## I capitoli del Libro I (scegli SOLO fra questi)

- **I.1** Come nasce una decisione: ADR, memoria, checkpoint
- **I.2** Il ciclo di fase a nove passi
- **I.3** Gate e sentinelle: la macchina che rifiuta
- **I.4** Le skill di produzione dell'Impero
- **I.5** I reparti e i loro BACKBONE
- **I.6** Emperator e la gerarchia delle forze
- **I.7** Ultimo Metro: produrre non è consegnare

## Pesi

- **portante** = merita ≥150 parole nel libro (un principio, una procedura, una decisione con
  le sue ragioni). Atteso 35-50% per il materiale interno, che è denso.
- **supporto** = una citazione dentro un paragrafo.
- **contesto** = solo in appendice (dettagli di percorso, nomi di file secondari, cronologia).

## Regole

- Leggi i file INTERI. Non atomizzare dall'indice o dal titolo.
- Un atomo per idea. Due idee = due atomi con una relazione.
- Nessuna invenzione: se un file dice una cosa, l'atomo dice quella cosa. Se due file si
  contraddicono, due atomi con relazione `contraddice`.
- Nessuna credenziale, nessun nome di cliente reale, nessun numero di conto negli atomi: il
  libro è pubblicabile. Se lo trovi nel materiale, l'atomo dice "esiste una regola su X" senza
  il dato.
- Uscita: `{"gruppo": "<GRUPPO>", "fonti_lette": ["...", "..."], "atoms": [ ... ]}`.
  Prima di consegnare: JSON valido, id progressivi senza buchi, ogni `capitolo` fra I.1-I.7,
  ogni `peso` fra i tre, ogni `ancora` non vuota.

## Cosa rispondi

Quanti atomi, distribuzione per capitolo e per peso, quali file hai letto per intero, e i tre
atomi che ti sembrano più importanti per chi vuole capire come lavora Digital Empire.
