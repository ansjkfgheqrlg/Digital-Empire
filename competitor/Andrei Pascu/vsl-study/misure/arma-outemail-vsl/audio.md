# Audio - arma-outemail-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -20.6 LUFS |
| loudness range (LRA) | 6.9 LU (da -24.9 a -18.0 LUFS) |
| true peak | -4.0 dBFS |
| momentary (400 ms) media / min / max | -22.86 / -65.88 / -13.64 LUFS |
| RMS finestre 0,5 s media / min / max | -25.06 / -65.06 / -16.58 dBFS |
| finestre da 0,5 s misurate | 334 |
| RMS mediano del video | -23.84 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 1 occorrenze, 1.21 s totali (0.72% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 8 occorrenze, 6.67 s totali (3.99% del video) |
| pausa soglia relativa (-36dB, min 0.25 s) | 2 occorrenze, 2.12 s totali (1.27% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 4.18 dB su RMS, 0.05 su ZCR) | 4 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -vn -af silencedetect=noise=-36dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 4.18 dB, ZCR 0.05 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 90.00 | 1:30.00 | rms | -23.62 | -19.44 | +4.18 | 0.1048 | 0.0989 | -0.0059 |
| 145.00 | 2:25.00 | rms | -25.33 | -36.87 | -11.54 | 0.121 | 0.1396 | +0.0186 |
| 155.00 | 2:35.00 | rms+zcr | -40.15 | -21.94 | +18.21 | 0.1395 | 0.0297 | -0.1098 |
| 160.00 | 2:40.00 | rms | -21.94 | -31.71 | -9.77 | 0.0297 | 0.0252 | -0.0045 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

1 occorrenze, 1.21 s totali, 0.72% del video. Media 1.207 s, mediana 1.207 s, max 1.207 s.

| inizio | fine | durata |
|---|---|---|
| 166.196 | 167.403 | 1.207 |

### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

8 occorrenze, 6.67 s totali, 3.99% del video. Media 0.834 s, mediana 0.51 s, max 1.935 s.

| inizio | fine | durata |
|---|---|---|
| 135.254 | 135.511 | 0.257 |
| 144.323 | 144.920 | 0.597 |
| 151.315 | 153.250 | 1.935 |
| 153.765 | 154.188 | 0.424 |
| 161.994 | 162.390 | 0.396 |
| 164.276 | 164.592 | 0.316 |
| 164.646 | 165.606 | 0.960 |
| 165.613 | 167.403 | 1.789 |

### pausa soglia relativa - soglia -36dB (mediana RMS del video (-23.84 dBFS) meno 12 dB), durata minima 0.25 s

2 occorrenze, 2.12 s totali, 1.27% del video. Media 1.062 s, mediana 1.062 s, max 1.728 s.

| inizio | fine | durata |
|---|---|---|
| 165.196 | 165.592 | 0.395 |
| 165.674 | 167.403 | 1.728 |

## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 154.00 | 2:34.00 | -3.97 |
| 154.50 | 2:34.50 | -4.3 |
| 92.00 | 1:32.00 | -5.2 |
| 156.00 | 2:36.00 | -5.29 |
| 95.00 | 1:35.00 | -5.49 |
| 94.50 | 1:34.50 | -5.57 |
| 95.50 | 1:35.50 | -5.73 |
| 97.00 | 1:37.00 | -5.73 |
| 85.00 | 1:25.00 | -6.07 |
| 81.00 | 1:21.00 | -6.16 |
| 91.00 | 1:31.00 | -6.25 |
| 81.50 | 1:21.50 | -6.35 |
| 79.50 | 1:19.50 | -6.48 |
| 93.00 | 1:33.00 | -6.52 |
| 96.00 | 1:36.00 | -6.52 |
| 94.00 | 1:34.00 | -6.55 |
| 92.50 | 1:32.50 | -6.69 |
| 101.50 | 1:41.50 | -6.71 |
| 93.50 | 1:33.50 | -6.83 |
| 79.00 | 1:19.00 | -6.85 |
| 80.50 | 1:20.50 | -6.93 |
| 98.50 | 1:38.50 | -7.06 |
| 99.50 | 1:39.50 | -7.26 |
| 100.00 | 1:40.00 | -7.28 |
| 90.00 | 1:30.00 | -7.33 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -24.21 | 0.0682 |
| 5.00 | -22.82 | 0.091 |
| 10.00 | -23.98 | 0.0944 |
| 15.00 | -23.59 | 0.1175 |
| 20.00 | -23.98 | 0.0737 |
| 25.00 | -23.65 | 0.0815 |
| 30.00 | -23.91 | 0.0864 |
| 35.00 | -22.82 | 0.1013 |
| 40.00 | -22.77 | 0.0758 |
| 45.00 | -24.45 | 0.0786 |
| 50.00 | -23.24 | 0.0678 |
| 55.00 | -23.84 | 0.0682 |
| 60.00 | -24.26 | 0.076 |
| 65.00 | -22.95 | 0.0771 |
| 70.00 | -23.61 | 0.0965 |
| 75.00 | -23.67 | 0.0657 |
| 80.00 | -21.82 | 0.0691 |
| 85.00 | -23.62 | 0.1048 |
| 90.00 | -19.44 | 0.0989 |
| 95.00 | -20.71 | 0.0825 |
| 100.00 | -23.16 | 0.0696 |
| 105.00 | -26.86 | 0.1035 |
| 110.00 | -24.46 | 0.0789 |
| 115.00 | -22.8 | 0.0975 |
| 120.00 | -25.38 | 0.0693 |
| 125.00 | -22.04 | 0.0988 |
| 130.00 | -23.39 | 0.1089 |
| 135.00 | -25.39 | 0.0774 |
| 140.00 | -25.33 | 0.121 |
| 145.00 | -36.87 | 0.1396 |
| 150.00 | -40.15 | 0.1395 |
| 155.00 | -21.94 | 0.0297 |
| 160.00 | -31.71 | 0.0252 |
