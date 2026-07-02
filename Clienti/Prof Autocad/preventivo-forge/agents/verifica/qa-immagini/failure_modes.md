# Failure Modes — qa-immagini

| # | Rischio | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Foto escluse dal PDF | count PDF < count annuncio | il render impagina TUTTE le immagini (nessun cap) |
| 2 | Crop silenzioso | auto tagliata ma count ok | verifica esplicita `contain` / assenza `cover` nell'HTML |
| 3 | Foto grande ma bassa qualità | pixelata | soglia lato ≥ 300px (segnala, non blocca il resto) |
| 4 | Conteggio via HTML impreciso | markup cambia | conta `class="photo-box"` (marcatore stabile del template) |
| 5 | Foto duplicate | count gonfiato | lo scraper deduplica le URL; il gate confronta con `listing.images` |

## Limite noto
Il conteggio è sull'HTML renderizzato (fedele al PDF perché il PDF nasce da quell'HTML). Non
apre il PDF binario: se in futuro il render cambia motore, mantenere il marcatore `photo-box`.
