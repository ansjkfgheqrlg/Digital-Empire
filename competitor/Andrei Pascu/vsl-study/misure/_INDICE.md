# Misure Fase 1 - indice

Prodotto da `scripts/misura_vsl.py` v1.2.0. Solo numeri.

| slug | durata | fps | tagli | inquadrature | durata media | mediana | moto p90 | sopra soglia | I LUFS | LRA LU | silenzi | pause rel. | cambi regime | frame unici |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| arma-outemail-secondo | 1:46.35 | 29.97003 | 45 | 46 | 2.312 s | 1.675 s | 0.004 | 1.76% | -21.0 | 4.4 | 0 | 0 | 2 | 38/53 |
| arma-outemail-vsl | 2:47.40 | 29.97003 | 51 | 52 | 3.219 s | 2.04 s | 0.0049 | 1.24% | -20.6 | 6.9 | 1 | 2 | 4 | 48/84 |
| arma-outfunnel-vsl | 1:39.14 | 29.97003 | 45 | 46 | 2.155 s | 1.8 s | 0.0126 | 1.88% | -15.2 | 6.4 | 0 | 1 | 4 | 47/50 |
| armageddon-home | 13:28.73 | 25.0 | 266 | 267 | 3.029 s | 1.84 s | 0.0108 | 1.71% | -17.9 | 2.9 | 7 | 7 | 19 | 206/404 |
| claude-speedrun-hero | 1:21.30 | 30.0 | 123 | 124 | 0.656 s | 0.33 s | 0.047 | 11.64% | -12.6 | 8.6 | 1 | 2 | 3 | 41/41 |
| claude-speedrun-sez14 | 5:57.12 | 30.0 | 127 | 128 | 2.79 s | 1.7 s | 0.0076 | 1.65% | -13.0 | 6.8 | 5 | 19 | 10 | 102/179 |
| claude-speedrun-sez9 | 4:45.85 | 30.0 | 117 | 118 | 2.422 s | 1.83 s | 0.0047 | 1.82% | -15.5 | 2.3 | 2 | 3 | 8 | 117/143 |
| outfunnel-vsl-1 | 2:31.28 | 30.0 | 72 | 73 | 2.072 s | 1.84 s | 0.0103 | 1.96% | -16.6 | 3.4 | 0 | 0 | 3 | 60/76 |
| outfunnel-vsl-2 | 1:48.82 | 29.97003 | 52 | 53 | 2.053 s | 1.44 s | 0.0126 | 2.02% | -15.2 | 6.3 | 0 | 0 | 4 | 51/54 |
| outheadline-vsl | 0:46.25 | 24.0 | 68 | 69 | 0.67 s | 0.25 s | 0.0751 | 12.43% | -16.2 | 2.7 | 0 | 0 | 1 | 18/23 |

Soglia scene score usata: 0.040. 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Come leggere le colonne moto p90 e sopra soglia: Su un video di grafica animata continua (griglie che scorrono, zoom permanenti) nessuna soglia per fotogramma separa il movimento dal taglio: verificato all'occhio su outheadline-vsl il 2026-09-10, dove fotogrammi consecutivi contati come tagli distinti appartengono alla stessa animazione, e dove alzare la soglia a 0.100 lascia comunque 60 tagli su 68. Il campo moto_dell_immagine misura il fenomeno. La mediana NON basta a distinguere il caso (0.0040 su outheadline contro 0.0018 su armageddon-home): a distinguerlo sono il percentile 90 e la frazione di fotogrammi sopra soglia. Sui dieci VSL misurati il percentile 90 sta fra 0.0040 e 0.0126 e i fotogrammi sopra soglia fra 1.24% e 2.02% in otto casi su dieci; i due fuori scala sono outheadline-vsl (p90 0.0751, 12.43%) e claude-speedrun-hero (p90 0.0470, 11.64%), ed e' esattamente sui due video dal ritmo dichiarato piu' rapido (0.67 s e 0.66 s di inquadratura media). Su quei due il numero di tagli va letto come limite superiore, non come conteggio.
