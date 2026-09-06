# contatore-scadenza

**Corsia A** | origine: armageddon (il contatore) **+ la correzione del suo difetto n.2**
canone: `--cell`, `--orange`, `.num-tabular`, `.label`, `--t-55`

## Quando
Ogni offerta con una **scadenza vera**. Lanci, promo, iscrizioni che chiudono.

## Quando NO
Se la scadenza non e' vera. Un contatore che riparte da solo e' l'unica cosa che, scoperta, brucia
la fiducia su tutto il resto della pagina.

## Le quattro regole

**1 - La scadenza sta su un attributo solo.** `data-fino="2026-12-31T23:59:59+01:00"` su
`#conto`, **e da nessun'altra parte**. Con il fuso scritto: un lancio italiano che scade a mezzanotte
non scade a mezzanotte per chi legge da Londra, se il fuso non c'e'.

**2 - `tabular-nums`.** Senza, le cifre cambiano larghezza mentre scendono e il contatore trema.

**3 - `aria-label` riscritto ogni secondo.** *"Mancano 4 giorni, 17 ore, 11 minuti e 8 secondi."*
Un contatore accessibile: non se ne vedono molti.

**4 - IL PEZZO CHE ANDREI NON HA.** Il suo si ferma a `00 00 00 00` mentre la pagina **continua a
vendere allo stesso prezzo** e il bottone di pagamento resta vivo: dopo la scadenza la pagina si
contraddice da sola. Qui a scadenza avvenuta il contatore **sparisce**, compare la riga che dice cosa
e' vero adesso, e `documentElement` prende `data-offerta="chiusa"` — un aggancio con cui il resto
della pagina puo' cambiare (prezzo, bottone, testo) con il solo CSS.

**Questo e' il gate 10 del canone**, ed e' nato da un difetto misurato sul sito di un concorrente.

## Il movimento (§7) — trovato dal gate, non a mano
Una cifra che cambia **ogni secondo e' movimento**, e va spenta come qualunque animazione. Con
`prefers-reduced-motion: reduce` il conto **resta** (serve: dice quanto manca) ma si aggiorna **al
minuto**, e la cella dei secondi viene nascosta invece di lampeggiare per sempre.

> Questo ramo non c'era alla prima scrittura. L'ha trovato `galleria.py`, che ha bocciato il pattern
> con *"ha JavaScript ma nessun ramo prefers-reduced-motion"*. E' il gate che fa il suo lavoro il
> giorno stesso in cui nasce.

## Il prezzo che si somma (§8)
`data-prezzo` sulle voci, `data-pack` sul contenitore, e `[data-totale]` / `[data-paghi]` /
`[data-risparmio]` scritti a runtime. **Nessuna cifra e' scritta due volte.** Lo studio dei suoi siti
aveva trovato *otto cifre per quattro metriche* fra pagine dello stesso negozio: si risolve col
codice, non con la disciplina.

## Le misure
cella `var(--cell)` quadrata, raggio `--cell x 0.075`, cifra `--cell x 0.33318` w800 |
spazio fra celle `--cell x 0.27359` | etichette `clamp(9px, --cell x 0.145, 12px)` a opacita' `--t-50`

## Cosa cade se sbagli
- **Scadenza scritta in due posti** -> il giorno che cambia, ne cambi uno solo.
- **Niente fuso nell'ISO** -> scade a un'ora diversa per ogni paese.
- **Nessun comportamento a scaduta** -> la pagina promette una cosa e ne fa un'altra: **FAIL al gate 10**.
- **Cifre non tabellari** -> il contatore trema, e si nota molto piu' di quanto sembri.
