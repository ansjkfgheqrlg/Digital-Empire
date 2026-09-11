# Audio - arma-outemail-secondo

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -21.0 LUFS |
| loudness range (LRA) | 4.4 LU (da -23.0 a -18.5 LUFS) |
| true peak | 0.0 dBFS |
| momentary (400 ms) media / min / max | -22.05 / -35.85 / -9.14 LUFS |
| RMS finestre 0,5 s media / min / max | -24.09 / -34.42 / -9.46 dBFS |
| finestre da 0,5 s misurate | 212 |
| RMS mediano del video | -24.01 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| pausa soglia relativa (-36dB, min 0.25 s) | 0 occorrenze, 0 s totali (0.0% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 3.51 dB su RMS, 0.05 su ZCR) | 2 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -vn -af silencedetect=noise=-36dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 3.51 dB, ZCR 0.05 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 95.00 | 1:35.00 | rms | -23.65 | -27.16 | -3.51 | 0.0716 | 0.0797 | +0.0081 |
| 100.00 | 1:40.00 | rms | -27.16 | -19.7 | +7.46 | 0.0797 | 0.078 | -0.0017 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


### pausa soglia relativa - soglia -36dB (mediana RMS del video (-24.01 dBFS) meno 12 dB), durata minima 0.25 s

0 occorrenze, 0 s totali, 0.0% del video. Media None s, mediana None s, max None s.


## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 20.50 | 0:20.50 | -0.01 |
| 20.00 | 0:20.00 | -5.1 |
| 43.50 | 0:43.50 | -6.57 |
| 14.00 | 0:14.00 | -7.03 |
| 15.00 | 0:15.00 | -7.51 |
| 16.50 | 0:16.50 | -7.54 |
| 9.00 | 0:09.00 | -7.65 |
| 53.00 | 0:53.00 | -8.44 |
| 22.50 | 0:22.50 | -8.47 |
| 12.00 | 0:12.00 | -8.48 |
| 42.50 | 0:42.50 | -8.7 |
| 14.50 | 0:14.50 | -8.74 |
| 24.00 | 0:24.00 | -8.74 |
| 4.00 | 0:04.00 | -9.04 |
| 91.00 | 1:31.00 | -9.06 |
| 17.50 | 0:17.50 | -9.11 |
| 17.00 | 0:17.00 | -9.23 |
| 0.00 | 0:00.00 | -9.3 |
| 16.00 | 0:16.00 | -9.32 |
| 63.50 | 1:03.50 | -9.35 |
| 84.00 | 1:24.00 | -9.46 |
| 26.00 | 0:26.00 | -9.47 |
| 21.00 | 0:21.00 | -9.48 |
| 76.50 | 1:16.50 | -9.48 |
| 79.00 | 1:19.00 | -9.56 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -23.82 | 0.0622 |
| 5.00 | -23.04 | 0.0658 |
| 10.00 | -22.23 | 0.0607 |
| 15.00 | -20.7 | 0.0511 |
| 20.00 | -23.98 | 0.0495 |
| 25.00 | -24.11 | 0.0948 |
| 30.00 | -24.44 | 0.101 |
| 35.00 | -25.09 | 0.0935 |
| 40.00 | -23.89 | 0.0936 |
| 45.00 | -24.1 | 0.104 |
| 50.00 | -24.64 | 0.0953 |
| 55.00 | -24.44 | 0.1015 |
| 60.00 | -26.06 | 0.0928 |
| 65.00 | -24.31 | 0.084 |
| 70.00 | -24.26 | 0.0725 |
| 75.00 | -24.91 | 0.0693 |
| 80.00 | -24.45 | 0.1176 |
| 85.00 | -23.55 | 0.082 |
| 90.00 | -23.65 | 0.0716 |
| 95.00 | -27.16 | 0.0797 |
| 100.00 | -19.7 | 0.078 |
