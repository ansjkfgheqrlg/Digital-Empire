# Failure Modes — op-translator-copy

| # | Modo di fallimento | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Termine DE non nel glossario | residuo tedesco in `equipment_it` | Gate B blocca → estendi `glossary_de_it.py` |
| 2 | Umlaut traslitterati (ue/oe/ae) | "Rueckfahrkamera" non tradotto | `_restore_umlauts()` tenta il match con umlaut |
| 3 | Copy inventa un optional | Gate B "fatto non nel sorgente" | descrizione composta SOLO dai campi di listing.json |
| 4 | Prezzo finisce nel titolo IT | Gate B "title_it con prezzo" | `build_title_it` esclude il prezzo per design |
| 5 | `equipment_de` disallineato | `len(it) != len(de)` | `translate_equipment` mappa 1:1 senza aggiungere/togliere |
| 6 | Numero specs alterato | Gate B "specs alterato" | specs presi verbatim da listing.json, mai riscritti |
| 7 | Colore marketing con umlaut | falso residuo (Alpinweiß) | `color_manufacturer` escluso dalle specs |
| 8 | `listing_it.json` sovrascrive price | price perso | `_merge_content` preserva `price` esistente |

## Regola aurea
Un residuo tedesco **non si nasconde allentando il gate**: si risolve estendendo il glossario.
