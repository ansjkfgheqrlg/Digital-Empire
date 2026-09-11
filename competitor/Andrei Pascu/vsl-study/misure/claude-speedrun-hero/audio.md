# Audio - claude-speedrun-hero

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| loudness integrata | -12.6 LUFS |
| loudness range (LRA) | 8.6 LU (da -16.4 a -7.8 LUFS) |
| true peak | 1.2 dBFS |
| momentary (400 ms) media / min / max | -14.69 / -51.39 / -4.79 LUFS |
| RMS finestre 0,5 s media / min / max | -16.11 / -45.48 / -4.68 dBFS |
| finestre da 0,5 s misurate | 162 |
| RMS mediano del video | -16.40 dBFS |
| silenzio assoluto (-40dB, min 0.3 s) | 1 occorrenze, 0.38 s totali (0.46% del video) |
| pausa soglia fissa (-30dB, min 0.25 s) | 2 occorrenze, 1.41 s totali (1.73% del video) |
| pausa soglia relativa (-28dB, min 0.25 s) | 2 occorrenze, 1.43 s totali (1.76% del video) |
| cambi di regime (blocchi da 5.0 s; soglia 5.71 dB su RMS, 0.05 su ZCR) | 3 |

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-hero\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-hero\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-hero\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-hero\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Comando: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-hero\video.mp4" -vn -af silencedetect=noise=-28dB:d=0.25 -f null -`

## Cambi di regime del volume

Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

Soglie calibrate su questo video: RMS 5.71 dB, ZCR 0.05 (blocchi da 5.0 s).

| t | hh:mm:ss | canale | da dBFS | a dBFS | delta dB | zcr da | zcr a | delta zcr |
|---|---|---|---|---|---|---|---|---|
| 5.00 | 0:05.00 | rms | -7.44 | -13.15 | -5.71 | 0.0528 | 0.0422 | -0.0106 |
| 15.00 | 0:15.00 | rms | -9.94 | -17.27 | -7.33 | 0.0437 | 0.0513 | +0.0076 |
| 55.00 | 0:55.00 | zcr | -18.0 | -17.15 | +0.85 | 0.1187 | 0.0479 | -0.0708 |

## Silenzi

### silenzio assoluto - soglia -40dB (soglia assoluta fissa), durata minima 0.3 s

1 occorrenze, 0.38 s totali, 0.46% del video. Media 0.375 s, mediana 0.375 s, max 0.375 s.

| inizio | fine | durata |
|---|---|---|
| 42.025 | 42.400 | 0.375 |

### pausa soglia fissa - soglia -30dB (soglia assoluta fissa), durata minima 0.25 s

2 occorrenze, 1.41 s totali, 1.73% del video. Media 0.704 s, mediana 0.704 s, max 0.825 s.

| inizio | fine | durata |
|---|---|---|
| 21.259 | 22.083 | 0.825 |
| 41.818 | 42.401 | 0.583 |

### pausa soglia relativa - soglia -28dB (mediana RMS del video (-16.40 dBFS) meno 12 dB), durata minima 0.25 s

2 occorrenze, 1.43 s totali, 1.76% del video. Media 0.714 s, mediana 0.714 s, max 0.846 s.

| inizio | fine | durata |
|---|---|---|
| 21.249 | 22.095 | 0.846 |
| 41.818 | 42.401 | 0.583 |

## Picchi piu' alti (finestre da 0,5 s)

| t | hh:mm:ss | picco dBFS |
|---|---|---|
| 65.00 | 1:05.00 | 0.0 |
| 4.00 | 0:04.00 | -0.17 |
| 1.00 | 0:01.00 | -0.35 |
| 23.50 | 0:23.50 | -0.42 |
| 4.50 | 0:04.50 | -0.43 |
| 47.00 | 0:47.00 | -0.47 |
| 30.00 | 0:30.00 | -0.48 |
| 23.00 | 0:23.00 | -0.5 |
| 71.50 | 1:11.50 | -0.54 |
| 0.00 | 0:00.00 | -0.56 |
| 2.50 | 0:02.50 | -0.57 |
| 3.00 | 0:03.00 | -0.57 |
| 49.50 | 0:49.50 | -0.59 |
| 46.00 | 0:46.00 | -0.63 |
| 54.00 | 0:54.00 | -0.64 |
| 11.50 | 0:11.50 | -0.65 |
| 13.50 | 0:13.50 | -0.67 |
| 12.50 | 0:12.50 | -0.68 |
| 65.50 | 1:05.50 | -0.72 |
| 49.00 | 0:49.00 | -0.73 |
| 46.50 | 0:46.50 | -0.75 |
| 12.00 | 0:12.00 | -0.78 |
| 70.50 | 1:10.50 | -0.8 |
| 31.00 | 0:31.00 | -0.81 |
| 3.50 | 0:03.50 | -0.82 |

## Profilo del volume, blocchi da 5.0 s

(il profilo fitto a 0,5 s sta in audio.json, campo profilo_volume_0_5s)

| t | rms mediano dBFS | zcr mediano |
|---|---|---|
| 0.00 | -7.44 | 0.0528 |
| 5.00 | -13.15 | 0.0422 |
| 10.00 | -9.94 | 0.0437 |
| 15.00 | -17.27 | 0.0513 |
| 20.00 | -14.8 | 0.0678 |
| 25.00 | -16.4 | 0.059 |
| 30.00 | -16.58 | 0.0779 |
| 35.00 | -18.46 | 0.0854 |
| 40.00 | -18.25 | 0.0975 |
| 45.00 | -13.95 | 0.1294 |
| 50.00 | -18.0 | 0.1187 |
| 55.00 | -17.15 | 0.0479 |
| 60.00 | -20.34 | 0.0684 |
| 65.00 | -16.05 | 0.0529 |
| 70.00 | -15.61 | 0.0507 |
| 75.00 | -16.16 | 0.0497 |
