# cucitura-fotografica

**Corsia A** | origine: `armageddon.css:186-230` + `356-374` (Andrei Pascu) | canone: `.seam`

## Quando
Ogni volta che **una fotografia deve attraversare due `<section>`** e la giunzione non deve vedersi.

## Quando NO
Fra due sezioni a tinta piatta: li' basta l'alternanza `bg-ink -> bg-paper` con `section-border-t`.
La cucitura serve solo quando c'e' un'immagine da non spezzare.

## Il meccanismo
Non si usa un bordo. Le superfici si **agganciano sullo stesso valore di opacita'**:

```
.sopra::before   0           ->  --consegna (0.992)
.sotto           --consegna  ->  --coda (0.71)  ->  tinta piena
```

Il commento originale: *"the two halves of his one gradient meet without a step."*

**I due numeri sono variabili (`--consegna`, `--coda`) proprio perche' le due meta' devono leggerli
identici.** Scriverli a mano in due punti e' la garanzia che, il giorno che uno cambia, l'altro no:
e' il difetto che l'articolo §8 della legge vieta, applicato a un gradiente.

La fotografia sta in **una sola variabile `--foto`**, riusata da entrambe le sezioni con offset
diversi (`-0.024` e `-0.145` della colonna): e' la stessa immagine che continua, non due immagini
affiancate.

## Cosa cade se sbagli
- **Valori di consegna diversi fra le due meta'** -> compare una banda netta, visibile su ogni schermo.
- **`background-size` diverso fra le due sezioni** -> la foto salta di scala a meta'.
- **Un `border-top` aggiunto per abitudine** -> annulla tutto il lavoro con una riga.
