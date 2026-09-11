# Audio - outfunnel-vsl-1

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -16.6 LUFS |
| loudness range (LRA) | 3.4 LU (da -18.3 a -15.0 LUFS) |
| true peak | 0.1 dBFS |
| momentary (400 ms) media / min / max | -17.2 / -29.57 / -8.89 LUFS |
| RMS finestre 0,5 s media / min / max | -20.24 / -28.71 / -10.94 dBFS |
| finestre da 0,5 s misurate | 302 |
| RMS mediano del video | -20.02 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia relativa (-32dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 3.0 dB su RMS, 0.058 su ZCR) | 3 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -vn -af silencedetect=noise=-32dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 3.0 dB, ZCR 0.058 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 20.00 | 0:20.00 | zcr | -19.9 | -19.13 | +0.77 | 0.1925 | 0.1048 | -0.0877 |
| 25.00 | 0:25.00 | zcr | -19.13 | -20.14 | -1.01 | 0.1048 | 0.175 | +0.0702 |
| 50.00 | 0:50.00 | rms | -20.39 | -16.77 | +3.62 | 0.1266 | 0.0852 | -0.0414 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia relativa - soglia -32dB (mediana RMS del video (-20.02 dBFS) meno 12 dB), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 50.00 | 0:50.00 | 0.0 |
| 51.00 | 0:51.00 | 0.0 |
| 50.50 | 0:50.50 | -0.97 |
| 37.50 | 0:37.50 | -1.25 |
| 41.00 | 0:41.00 | -2.54 |
| 87.50 | 1:27.50 | -2.74 |
| 20.00 | 0:20.00 | -2.78 |
| 59.50 | 0:59.50 | -2.78 |
| 93.00 | 1:33.00 | -2.81 |
| 22.00 | 0:22.00 | -2.89 |
| 51.50 | 0:51.50 | -2.93 |
| 81.50 | 1:21.50 | -2.98 |
| 52.50 | 0:52.50 | -3.03 |
| 12.00 | 0:12.00 | -3.05 |
| 40.50 | 0:40.50 | -3.06 |
| 9.00 | 0:09.00 | -3.14 |
| 91.00 | 1:31.00 | -3.14 |
| 39.50 | 0:39.50 | -3.16 |
| 101.50 | 1:41.50 | -3.22 |
| 8.00 | 0:08.00 | -3.24 |
| 90.00 | 1:30.00 | -3.26 |
| 22.50 | 0:22.50 | -3.32 |
| 24.00 | 0:24.00 | -3.34 |
| 42.50 | 0:42.50 | -3.36 |
| 119.00 | 1:59.00 | -3.36 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -18.79 | 0.1459 |
| 5.00 | -19.59 | 0.1246 |
| 10.00 | -19.62 | 0.1366 |
| 15.00 | -19.9 | 0.1925 |
| 20.00 | -19.13 | 0.1048 |
| 25.00 | -20.14 | 0.175 |
| 30.00 | -20.54 | 0.1334 |
| 35.00 | -18.87 | 0.1071 |
| 40.00 | -19.16 | 0.0878 |
| 45.00 | -20.39 | 0.1266 |
| 50.00 | -16.77 | 0.0852 |
| 55.00 | -18.94 | 0.1365 |
| 60.00 | -20.02 | 0.1634 |
| 65.00 | -21.62 | 0.1273 |
| 70.00 | -21.48 | 0.1233 |
| 75.00 | -22.69 | 0.177 |
| 80.00 | -20.25 | 0.1301 |
| 85.00 | -20.3 | 0.1081 |
| 90.00 | -19.22 | 0.1103 |
| 95.00 | -20.44 | 0.096 |
| 100.00 | -20.59 | 0.1326 |
| 105.00 | -20.81 | 0.1462 |
| 110.00 | -19.59 | 0.0917 |
| 115.00 | -21.25 | 0.1497 |
| 120.00 | -19.88 | 0.0975 |
| 125.00 | -21.48 | 0.1119 |
| 130.00 | -21.31 | 0.1298 |
| 135.00 | -18.7 | 0.1284 |
| 140.00 | -18.52 | 0.1178 |
| 145.00 | -19.97 | 0.1193 |
