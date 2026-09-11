# Audio - claude-speedrun-sez14

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -13.0 LUFS |
| loudness range (LRA) | 6.8 LU (da -17.0 a -10.2 LUFS) |
| true peak | 0.8 dBFS |
| momentary (400 ms) media / min / max | -15.04 / -69.93 / -7.08 LUFS |
| RMS finestre 0,5 s media / min / max | -17.51 / -59.44 / -10.45 dBFS |
| finestre da 0,5 s misurate | 714 |
| RMS mediano del video | -16.47 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 5 occorrenze, 2.96 s totali (0.83% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 18 occorrenze, 8.87 s totali (2.48% del video) |
| pausa soglia relativa (-28dB, min 0.25 s) | 19 occorrenze, 9.66 s totali (2.71% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 4.89 dB su RMS, 0.05 su ZCR) | 10 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-28dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 4.89 dB, ZCR 0.05 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 35.00 | 0:35.00 | rms | -15.25 | -20.16 | -4.91 | 0.0825 | 0.0823 | -0.0002 |
| 45.00 | 0:45.00 | rms | -23.95 | -18.49 | +5.46 | 0.1162 | 0.1224 | +0.0062 |
| 115.00 | 1:55.00 | rms | -17.07 | -21.96 | -4.89 | 0.1407 | 0.13 | -0.0107 |
| 130.00 | 2:10.00 | rms | -20.41 | -13.27 | +7.14 | 0.1252 | 0.1024 | -0.0228 |
| 175.00 | 2:55.00 | zcr | -15.83 | -18.8 | -2.97 | 0.0861 | 0.1382 | +0.0521 |
| 180.00 | 3:00.00 | zcr | -18.8 | -14.66 | +4.14 | 0.1382 | 0.0624 | -0.0758 |
| 230.00 | 3:50.00 | zcr | -15.6 | -18.88 | -3.28 | 0.1224 | 0.0688 | -0.0536 |
| 295.00 | 4:55.00 | rms | -13.52 | -19.2 | -5.68 | 0.081 | 0.0822 | +0.0012 |
| 340.00 | 5:40.00 | rms | -13.37 | -22.12 | -8.75 | 0.0657 | 0.0753 | +0.0096 |
| 350.00 | 5:50.00 | rms | -19.54 | -25.88 | -6.34 | 0.1167 | 0.0886 | -0.0281 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

5 occorrenze, 2.96 s totali, 0.83% del video. Media 0.593 s, mediana 0.48 s, max 1.085 s.

| inizio | fine | durata |
|---|---|---|
| 326.541 | 327.021 | 0.480 |
| 340.963 | 341.582 | 0.619 |
| 342.552 | 342.896 | 0.344 |
| 349.065 | 349.502 | 0.437 |
| 353.098 | 354.182 | 1.085 |

### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

18 occorrenze, 8.87 s totali, 2.48% del video. Media 0.493 s, mediana 0.377 s, max 1.276 s.

| inizio | fine | durata |
|---|---|---|
| 18.512 | 18.810 | 0.298 |
| 18.995 | 19.423 | 0.428 |
| 52.778 | 53.371 | 0.593 |
| 298.731 | 299.094 | 0.363 |
| 302.948 | 303.277 | 0.329 |
| 313.154 | 313.499 | 0.345 |
| 317.365 | 317.624 | 0.259 |
| 325.216 | 325.488 | 0.272 |
| 326.525 | 327.021 | 0.496 |
| 340.922 | 341.592 | 0.670 |
| 342.522 | 342.906 | 0.384 |
| 343.734 | 344.164 | 0.430 |
| 345.138 | 345.410 | 0.272 |
| 349.012 | 350.288 | 1.276 |
| 353.051 | 354.289 | 1.238 |
| 355.762 | 356.131 | 0.369 |
| 356.244 | 356.524 | 0.280 |
| 356.550 | 357.120 | 0.570 |

### pausa soglia relativa - soglia -28dB (mediana RMS del video (-16.47 dBFS) meno 12 dB), durata minima 0.25 s

19 occorrenze, 9.66 s totali, 2.71% del video. Media 0.509 s, mediana 0.386 s, max 1.297 s.

| inizio | fine | durata |
|---|---|---|
| 18.512 | 18.811 | 0.299 |
| 18.811 | 19.423 | 0.612 |
| 52.778 | 53.374 | 0.597 |
| 298.731 | 299.094 | 0.363 |
| 302.948 | 303.277 | 0.329 |
| 308.174 | 308.667 | 0.493 |
| 313.150 | 313.499 | 0.349 |
| 317.365 | 317.624 | 0.259 |
| 325.214 | 325.489 | 0.276 |
| 326.509 | 327.021 | 0.512 |
| 340.919 | 341.592 | 0.673 |
| 342.520 | 342.906 | 0.386 |
| 343.730 | 344.164 | 0.434 |
| 345.131 | 345.410 | 0.279 |
| 348.993 | 350.290 | 1.297 |
| 353.005 | 354.289 | 1.284 |
| 355.761 | 356.131 | 0.370 |
| 356.244 | 356.524 | 0.280 |
| 356.550 | 357.120 | 0.570 |

## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 167.50 | 2:47.50 | -0.0 |
| 173.00 | 2:53.00 | 0.0 |
| 211.50 | 3:31.50 | 0.0 |
| 223.50 | 3:43.50 | 0.0 |
| 235.00 | 3:55.00 | 0.0 |
| 271.00 | 4:31.00 | -0.0 |
| 285.50 | 4:45.50 | -0.0 |
| 328.50 | 5:28.50 | 0.0 |
| 346.50 | 5:46.50 | 0.0 |
| 225.50 | 3:45.50 | -0.02 |
| 198.00 | 3:18.00 | -0.05 |
| 27.50 | 0:27.50 | -0.06 |
| 134.50 | 2:14.50 | -0.06 |
| 0.00 | 0:00.00 | -0.08 |
| 332.00 | 5:32.00 | -0.08 |
| 337.00 | 5:37.00 | -0.08 |
| 216.00 | 3:36.00 | -0.09 |
| 222.00 | 3:42.00 | -0.1 |
| 185.00 | 3:05.00 | -0.12 |
| 169.50 | 2:49.50 | -0.13 |
| 267.00 | 4:27.00 | -0.13 |
| 269.00 | 4:29.00 | -0.13 |
| 321.50 | 5:21.50 | -0.14 |
| 64.50 | 1:04.50 | -0.15 |
| 179.00 | 2:59.00 | -0.17 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -16.18 | 0.1184 |
| 5.00 | -17.54 | 0.0948 |
| 10.00 | -18.98 | 0.0757 |
| 15.00 | -18.99 | 0.092 |
| 20.00 | -18.14 | 0.1007 |
| 25.00 | -18.66 | 0.093 |
| 30.00 | -15.25 | 0.0825 |
| 35.00 | -20.16 | 0.0823 |
| 40.00 | -23.95 | 0.1162 |
| 45.00 | -18.49 | 0.1224 |
| 50.00 | -18.6 | 0.0772 |
| 55.00 | -17.85 | 0.106 |
| 60.00 | -17.43 | 0.0904 |
| 65.00 | -15.18 | 0.1063 |
| 70.00 | -18.22 | 0.1074 |
| 75.00 | -16.68 | 0.0925 |
| 80.00 | -17.48 | 0.1239 |
| 85.00 | -16.93 | 0.0793 |
| 90.00 | -16.73 | 0.1064 |
| 95.00 | -18.34 | 0.1154 |
| 100.00 | -15.84 | 0.1624 |
| 105.00 | -16.6 | 0.1153 |
| 110.00 | -17.07 | 0.1407 |
| 115.00 | -21.96 | 0.13 |
| 120.00 | -18.45 | 0.1441 |
| 125.00 | -20.41 | 0.1252 |
| 130.00 | -13.27 | 0.1024 |
| 135.00 | -14.04 | 0.1305 |
| 140.00 | -17.14 | 0.1248 |
| 145.00 | -14.32 | 0.121 |
| 150.00 | -16.41 | 0.1066 |
| 155.00 | -18.87 | 0.112 |
| 160.00 | -16.39 | 0.1075 |
| 165.00 | -18.23 | 0.1098 |
| 170.00 | -15.83 | 0.0861 |
| 175.00 | -18.8 | 0.1382 |
| 180.00 | -14.66 | 0.0624 |
| 185.00 | -14.66 | 0.1003 |
| 190.00 | -13.13 | 0.0826 |
| 195.00 | -13.84 | 0.1043 |
| 200.00 | -14.61 | 0.1069 |
| 205.00 | -13.34 | 0.0917 |
| 210.00 | -13.95 | 0.1162 |
| 215.00 | -14.27 | 0.092 |
| 220.00 | -14.5 | 0.1262 |
| 225.00 | -15.6 | 0.1224 |
| 230.00 | -18.88 | 0.0688 |
| 235.00 | -14.82 | 0.0822 |
| 240.00 | -15.14 | 0.0976 |
| 245.00 | -15.38 | 0.1019 |
| 250.00 | -16.02 | 0.0935 |
| 255.00 | -14.5 | 0.0993 |
| 260.00 | -16.41 | 0.0829 |
| 265.00 | -13.77 | 0.0793 |
| 270.00 | -14.22 | 0.0844 |
| 275.00 | -13.29 | 0.1336 |
| 280.00 | -15.34 | 0.1041 |
| 285.00 | -15.34 | 0.126 |
| 290.00 | -13.52 | 0.081 |
| 295.00 | -19.2 | 0.0822 |
| 300.00 | -20.06 | 0.079 |
| 305.00 | -17.06 | 0.0983 |
| 310.00 | -18.11 | 0.0895 |
| 315.00 | -19.36 | 0.1004 |
| 320.00 | -17.32 | 0.089 |
| 325.00 | -15.12 | 0.1159 |
| 330.00 | -13.27 | 0.1155 |
| 335.00 | -13.37 | 0.0657 |
| 340.00 | -22.12 | 0.0753 |
| 345.00 | -19.54 | 0.1167 |
| 350.00 | -25.88 | 0.0886 |
