# Failure Modes — qa-translation-verifier

| # | Rischio | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Falso positivo tedesco | parola IT scambiata per DE | euristica prudente: morfemi solo se len≥6; stopword mirate |
| 2 | Falso negativo tedesco | termine DE non rilevato | ampliare `GERMAN_STOPWORDS`/`GERMAN_MORPHEMES` |
| 3 | Nome proprio con umlaut | colore/marca marketing flaggati | esclusi a monte (S3 non li mette nelle specs) |
| 4 | Specs numeriche formattate | "78.500 km" vs 78500 | confronto su sole cifre (`\D` rimosse) |
| 5 | Gate troppo permissivo | difetti passano | mai allentare per "far passare": si corregge S3 |

## Tensione nota
Rilevare tedesco in modo perfetto è impossibile senza un dizionario completo. L'euristica è tarata
per **preferire il blocco** (falso positivo) piuttosto che lasciar passare tedesco (falso negativo):
la cura di un falso positivo è comunque migliorare S3/glossario.
