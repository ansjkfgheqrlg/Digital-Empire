# Audio - claude-speedrun-sez9

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -15.5 LUFS |
| loudness range (LRA) | 2.3 LU (da -16.6 a -14.4 LUFS) |
| true peak | -0.5 dBFS |
| momentary (400 ms) media / min / max | -16.21 / -68.77 / -10.87 LUFS |
| RMS finestre 0,5 s media / min / max | -18.8 / -68.1 / -11.12 dBFS |
| finestre da 0,5 s misurate | 571 |
| RMS mediano del video | -18.28 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 2 occorrenze, 1.75 s totali (0.61% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 3 occorrenze, 2.81 s totali (0.98% del video) |
| pausa soglia relativa (-30dB, min 0.25 s) | 3 occorrenze, 2.81 s totali (0.98% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 3.0 dB su RMS, 0.0685 su ZCR) | 8 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez9\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez9\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez9\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez9\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez9\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 3.0 dB, ZCR 0.0685 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 5.00 | 0:05.00 | zcr | -18.79 | -18.0 | +0.79 | 0.1843 | 0.0811 | -0.1032 |
| 110.00 | 1:50.00 | rms | -18.21 | -23.42 | -5.21 | 0.0912 | 0.125 | +0.0338 |
| 115.00 | 1:55.00 | rms | -23.42 | -18.94 | +4.48 | 0.125 | 0.0856 | -0.0394 |
| 120.00 | 2:00.00 | zcr | -18.94 | -18.3 | +0.64 | 0.0856 | 0.1587 | +0.0731 |
| 125.00 | 2:05.00 | zcr | -18.3 | -18.89 | -0.59 | 0.1587 | 0.0902 | -0.0685 |
| 175.00 | 2:55.00 | zcr | -17.77 | -18.37 | -0.60 | 0.0917 | 0.1714 | +0.0797 |
| 215.00 | 3:35.00 | zcr | -18.28 | -19.8 | -1.52 | 0.1066 | 0.1842 | +0.0776 |
| 240.00 | 4:00.00 | zcr | -17.64 | -17.84 | -0.20 | 0.1571 | 0.0851 | -0.0720 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

2 occorrenze, 1.75 s totali, 0.61% del video. Media 0.873 s, mediana 0.873 s, max 1.379 s.

| inizio | fine | durata |
|---|---|---|
| 109.934 | 110.300 | 0.366 |
| 112.368 | 113.747 | 1.379 |

### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

3 occorrenze, 2.81 s totali, 0.98% del video. Media 0.935 s, mediana 0.41 s, max 2.031 s.

| inizio | fine | durata |
|---|---|---|
| 57.356 | 57.721 | 0.365 |
| 109.890 | 110.300 | 0.410 |
| 111.716 | 113.748 | 2.031 |

### pausa soglia relativa - soglia -30dB (mediana RMS del video (-18.28 dBFS) meno 12 dB), durata minima 0.25 s

3 occorrenze, 2.81 s totali, 0.98% del video. Media 0.935 s, mediana 0.41 s, max 2.031 s.

| inizio | fine | durata |
|---|---|---|
| 57.356 | 57.721 | 0.365 |
| 109.890 | 110.300 | 0.410 |
| 111.716 | 113.748 | 2.031 |

## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 62.50 | 1:02.50 | -0.5 |
| 5.00 | 0:05.00 | -0.6 |
| 46.50 | 0:46.50 | -1.11 |
| 94.00 | 1:34.00 | -1.28 |
| 77.00 | 1:17.00 | -1.36 |
| 110.50 | 1:50.50 | -1.37 |
| 47.00 | 0:47.00 | -2.33 |
| 4.50 | 0:04.50 | -2.6 |
| 63.00 | 1:03.00 | -3.46 |
| 50.50 | 0:50.50 | -3.55 |
| 51.00 | 0:51.00 | -3.73 |
| 77.50 | 1:17.50 | -3.76 |
| 47.50 | 0:47.50 | -3.99 |
| 2.00 | 0:02.00 | -4.24 |
| 272.00 | 4:32.00 | -4.41 |
| 242.50 | 4:02.50 | -4.46 |
| 85.50 | 1:25.50 | -4.49 |
| 164.00 | 2:44.00 | -4.49 |
| 236.50 | 3:56.50 | -4.49 |
| 43.50 | 0:43.50 | -4.52 |
| 177.50 | 2:57.50 | -4.53 |
| 198.50 | 3:18.50 | -4.54 |
| 75.50 | 1:15.50 | -4.56 |
| 3.50 | 0:03.50 | -4.57 |
| 78.00 | 1:18.00 | -4.58 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -18.79 | 0.1843 |
| 5.00 | -18.0 | 0.0811 |
| 10.00 | -18.21 | 0.1275 |
| 15.00 | -19.29 | 0.1348 |
| 20.00 | -18.41 | 0.1171 |
| 25.00 | -18.04 | 0.0859 |
| 30.00 | -18.63 | 0.0791 |
| 35.00 | -19.4 | 0.0818 |
| 40.00 | -20.09 | 0.0925 |
| 45.00 | -18.3 | 0.0897 |
| 50.00 | -18.41 | 0.1321 |
| 55.00 | -20.61 | 0.1529 |
| 60.00 | -18.8 | 0.0851 |
| 65.00 | -18.13 | 0.0754 |
| 70.00 | -18.6 | 0.0766 |
| 75.00 | -18.13 | 0.0859 |
| 80.00 | -19.27 | 0.1361 |
| 85.00 | -18.79 | 0.0735 |
| 90.00 | -17.56 | 0.0817 |
| 95.00 | -16.31 | 0.0703 |
| 100.00 | -18.43 | 0.096 |
| 105.00 | -18.21 | 0.0912 |
| 110.00 | -23.42 | 0.125 |
| 115.00 | -18.94 | 0.0856 |
| 120.00 | -18.3 | 0.1587 |
| 125.00 | -18.89 | 0.0902 |
| 130.00 | -18.48 | 0.1285 |
| 135.00 | -17.0 | 0.0716 |
| 140.00 | -18.06 | 0.074 |
| 145.00 | -18.71 | 0.1041 |
| 150.00 | -18.62 | 0.0882 |
| 155.00 | -18.66 | 0.0772 |
| 160.00 | -17.91 | 0.1196 |
| 165.00 | -19.71 | 0.138 |
| 170.00 | -17.77 | 0.0917 |
| 175.00 | -18.37 | 0.1714 |
| 180.00 | -17.3 | 0.1202 |
| 185.00 | -18.12 | 0.156 |
| 190.00 | -17.66 | 0.1175 |
| 195.00 | -17.55 | 0.0824 |
| 200.00 | -17.93 | 0.1161 |
| 205.00 | -17.66 | 0.0943 |
| 210.00 | -18.28 | 0.1066 |
| 215.00 | -19.8 | 0.1842 |
| 220.00 | -17.66 | 0.1646 |
| 225.00 | -18.49 | 0.1379 |
| 230.00 | -17.54 | 0.1255 |
| 235.00 | -17.64 | 0.1571 |
| 240.00 | -17.84 | 0.0851 |
| 245.00 | -17.28 | 0.096 |
| 250.00 | -17.8 | 0.096 |
| 255.00 | -18.59 | 0.1421 |
| 260.00 | -17.89 | 0.1207 |
| 265.00 | -17.13 | 0.1172 |
| 270.00 | -18.03 | 0.1399 |
| 275.00 | -17.59 | 0.0805 |
| 280.00 | -19.41 | 0.1197 |
