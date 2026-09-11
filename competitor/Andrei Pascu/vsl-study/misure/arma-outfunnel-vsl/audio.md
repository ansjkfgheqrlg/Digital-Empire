# Audio - arma-outfunnel-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -15.2 LUFS |
| loudness range (LRA) | 6.4 LU (da -18.6 a -12.1 LUFS) |
| true peak | -1.3 dBFS |
| momentary (400 ms) media / min / max | -16.75 / -36.2 / -9.88 LUFS |
| RMS finestre 0,5 s media / min / max | -19.17 / -36.67 / -12.9 dBFS |
| finestre da 0,5 s misurate | 198 |
| RMS mediano del video | -18.74 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 1 occorrenze, 0.28 s totali (0.29% del video) |
| pausa soglia relativa (-31dB, min 0.25 s) | 1 occorrenze, 0.27 s totali (0.27% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 3.25 dB su RMS, 0.1051 su ZCR) | 4 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -vn -af silencedetect=noise=-31dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 3.25 dB, ZCR 0.1051 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 10.00 | 0:10.00 | rms | -17.84 | -14.59 | +3.25 | 0.109 | 0.0948 | -0.0142 |
| 15.00 | 0:15.00 | zcr | -14.59 | -15.46 | -0.87 | 0.0948 | 0.1999 | +0.1051 |
| 20.00 | 0:20.00 | zcr | -15.46 | -15.63 | -0.17 | 0.1999 | 0.0648 | -0.1351 |
| 70.00 | 1:10.00 | rms | -17.29 | -21.84 | -4.55 | 0.0642 | 0.1082 | +0.0440 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

1 occorrenze, 0.28 s totali, 0.29% del video. Media 0.284 s, mediana 0.284 s, max 0.284 s.

| inizio | fine | durata |
|---|---|---|
| 98.789 | 99.073 | 0.284 |

### pausa soglia relativa - soglia -31dB (mediana RMS del video (-18.74 dBFS) meno 12 dB), durata minima 0.25 s

1 occorrenze, 0.27 s totali, 0.27% del video. Media 0.271 s, mediana 0.271 s, max 0.271 s.

| inizio | fine | durata |
|---|---|---|
| 98.801 | 99.073 | 0.271 |

## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 13.50 | 0:13.50 | -1.32 |
| 69.50 | 1:09.50 | -1.92 |
| 65.50 | 1:05.50 | -1.99 |
| 76.50 | 1:16.50 | -2.21 |
| 0.00 | 0:00.00 | -2.73 |
| 37.50 | 0:37.50 | -2.75 |
| 0.50 | 0:00.50 | -2.8 |
| 78.50 | 1:18.50 | -2.81 |
| 3.00 | 0:03.00 | -2.85 |
| 39.00 | 0:39.00 | -2.85 |
| 5.00 | 0:05.00 | -2.86 |
| 21.50 | 0:21.50 | -2.86 |
| 7.00 | 0:07.00 | -2.87 |
| 14.50 | 0:14.50 | -2.87 |
| 40.00 | 0:40.00 | -2.88 |
| 39.50 | 0:39.50 | -2.92 |
| 1.00 | 0:01.00 | -2.93 |
| 40.50 | 0:40.50 | -2.95 |
| 14.00 | 0:14.00 | -2.96 |
| 15.00 | 0:15.00 | -2.96 |
| 19.50 | 0:19.50 | -2.96 |
| 68.50 | 1:08.50 | -2.96 |
| 20.00 | 0:20.00 | -2.97 |
| 2.00 | 0:02.00 | -2.98 |
| 38.00 | 0:38.00 | -2.98 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -14.7 | 0.1111 |
| 5.00 | -17.84 | 0.109 |
| 10.00 | -14.59 | 0.0948 |
| 15.00 | -15.46 | 0.1999 |
| 20.00 | -15.63 | 0.0648 |
| 25.00 | -17.08 | 0.1177 |
| 30.00 | -19.02 | 0.1113 |
| 35.00 | -16.66 | 0.0725 |
| 40.00 | -19.0 | 0.1066 |
| 45.00 | -20.48 | 0.0883 |
| 50.00 | -18.16 | 0.0934 |
| 55.00 | -19.36 | 0.1066 |
| 60.00 | -19.41 | 0.0686 |
| 65.00 | -17.29 | 0.0642 |
| 70.00 | -21.84 | 0.1082 |
| 75.00 | -20.41 | 0.0782 |
| 80.00 | -19.01 | 0.1007 |
| 85.00 | -21.52 | 0.0925 |
| 90.00 | -20.95 | 0.1195 |
