# Audio - outheadline-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -16.2 LUFS |
| loudness range (LRA) | 2.7 LU (da -17.5 a -14.8 LUFS) |
| true peak | -0.5 dBFS |
| momentary (400 ms) media / min / max | -16.72 / -24.42 / -9.32 LUFS |
| RMS finestre 0,5 s media / min / max | -19.49 / -26.46 / -12.14 dBFS |
| finestre da 0,5 s misurate | 92 |
| RMS mediano del video | -19.25 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia relativa (-31dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 3.0 dB su RMS, 0.0556 su ZCR) | 1 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -vn -af silencedetect=noise=-31dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 3.0 dB, ZCR 0.0556 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 40.00 | 0:40.00 | zcr | -19.92 | -20.45 | -0.53 | 0.0814 | 0.137 | +0.0556 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia relativa - soglia -31dB (mediana RMS del video (-19.25 dBFS) meno 12 dB), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 9.00 | 0:09.00 | -0.51 |
| 31.50 | 0:31.50 | -1.1 |
| 31.00 | 0:31.00 | -1.65 |
| 19.50 | 0:19.50 | -2.1 |
| 9.50 | 0:09.50 | -2.17 |
| 10.00 | 0:10.00 | -2.19 |
| 34.50 | 0:34.50 | -2.78 |
| 28.50 | 0:28.50 | -2.82 |
| 44.50 | 0:44.50 | -3.06 |
| 4.50 | 0:04.50 | -3.16 |
| 29.50 | 0:29.50 | -3.21 |
| 26.00 | 0:26.00 | -3.25 |
| 24.50 | 0:24.50 | -3.32 |
| 3.50 | 0:03.50 | -3.33 |
| 27.50 | 0:27.50 | -3.4 |
| 27.00 | 0:27.00 | -3.54 |
| 30.00 | 0:30.00 | -3.57 |
| 30.50 | 0:30.50 | -3.61 |
| 15.00 | 0:15.00 | -3.68 |
| 42.50 | 0:42.50 | -3.75 |
| 22.00 | 0:22.00 | -3.79 |
| 15.50 | 0:15.50 | -3.83 |
| 28.00 | 0:28.00 | -3.9 |
| 0.00 | 0:00.00 | -3.94 |
| 34.00 | 0:34.00 | -3.98 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -18.66 | 0.0925 |
| 5.00 | -18.64 | 0.1066 |
| 10.00 | -19.99 | 0.0994 |
| 15.00 | -19.0 | 0.1053 |
| 20.00 | -18.55 | 0.1269 |
| 25.00 | -18.98 | 0.1155 |
| 30.00 | -18.96 | 0.1004 |
| 35.00 | -19.92 | 0.0814 |
| 40.00 | -20.45 | 0.137 |
