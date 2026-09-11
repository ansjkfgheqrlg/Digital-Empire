# claude-speedrun-sez14 - sommario di misura

Fase 1 di EMP-DIOEDIT. Solo numeri: nessun aggettivo, nessuna interpretazione.
Generato il 2026-09-11 00:14 da `scripts/misura_vsl.py` v1.2.0 in 63.2 s.

## Tecnica

| voce | valore |
|---|---|
| durata | 5:57.12 (357.120 s) |
| risoluzione | 1920x1080 |
| fps reale | 30.0 (dichiarato 30/1) |
| frame totali | 10713 (ffprobe stream=nb_frames) |
| codec video | h264 High, yuv420p |
| bitrate video | 2937880 bps |
| codec audio | aac LC, 48000 Hz, 2 canali |
| bitrate audio | 189375 bps |
| bitrate totale | 3135926 bps |
| peso | 133.5 MB |

Come: `ffprobe -v error -show_format -show_streams -of json "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4"`

## Montaggio

| voce | valore |
|---|---|
| soglia scene score usata | **0.040** |
| tagli | **127** |
| inquadrature | 128 |
| tagli al minuto | 21.34 |
| durata media inquadratura | 2.79 s |
| durata mediana | 1.7 s |
| durata minima | 0.23 s |
| durata massima | 31.53 s |
| deviazione standard | 3.74 s |
| moto dell'immagine: punteggio di scena p90 | 0.0076 (mediana 0.0009, p99 0.0778) |
| frame sopra soglia | 1.65% |
| minuto con piu' tagli | minuto 1, 48 tagli |
| minuto con meno tagli | minuto 6, 10 tagli |

Come: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

Soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

Secondo limite noto: Su un video di grafica animata continua (griglie che scorrono, zoom permanenti) nessuna soglia per fotogramma separa il movimento dal taglio: verificato all'occhio su outheadline-vsl il 2026-09-10, dove fotogrammi consecutivi contati come tagli distinti appartengono alla stessa animazione, e dove alzare la soglia a 0.100 lascia comunque 60 tagli su 68. Il campo moto_dell_immagine misura il fenomeno. La mediana NON basta a distinguere il caso (0.0040 su outheadline contro 0.0018 su armageddon-home): a distinguerlo sono il percentile 90 e la frazione di fotogrammi sopra soglia. Sui dieci VSL misurati il percentile 90 sta fra 0.0040 e 0.0126 e i fotogrammi sopra soglia fra 1.24% e 2.02% in otto casi su dieci; i due fuori scala sono outheadline-vsl (p90 0.0751, 12.43%) e claude-speedrun-hero (p90 0.0470, 11.64%), ed e' esattamente sui due video dal ritmo dichiarato piu' rapido (0.67 s e 0.66 s di inquadratura media). Su quei due il numero di tagli va letto come limite superiore, non come conteggio.

Sensibilita' (stessa passata, soglie diverse):

| soglia | tagli | durata media | |
|---|---|---|---|
| 0.028 | 165 | 2.15 s |  |
| 0.040 | 127 | 2.79 s | **usata** |
| 0.055 | 111 | 3.19 s |  |
| 0.100 | 82 | 4.3 s |  |

Tagli per minuto:

| minuto | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| tagli | 48 | 24 | 22 | 13 | 10 | 10 |

## Audio

| voce | valore |
|---|---|
| loudness integrata | -13.0 LUFS |
| loudness range | 6.8 LU |
| true peak | 0.8 dBFS |
| RMS 0,5 s media / min / max | -17.507 / -59.44 / -10.45 dBFS |
| silenzi assoluti (-40dB, min 0.3 s) | 5, 2.96 s totali (0.83%) |
| pause a soglia fissa (-30dB, min 0.25 s) | 18, 8.87 s totali (2.48%) |
| pause a soglia relativa (-28dB = mediana RMS del video (-16.47 dBFS) meno 12 dB, min 0.25 s) | 19, 9.66 s totali (2.71%) |
| cambi di regime del volume | 10 (soglia 4.89 dB su RMS, 0.05 su ZCR) |
| picco piu' alto | -0.0 dBFS a 2:47.50 |

Come: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af ebur128=peak=true:metadata=1,ametadata=print:file=- -f null -`

Come: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -ac 1 -ar 16000 -f s16le -`

Come: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-40dB:d=0.3 -f null -`

Come: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-30dB:d=0.25 -f null -`

Come: `ffmpeg -v info -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vn -af silencedetect=noise=-28dB:d=0.25 -f null -`

Silenzi: Tre configurazioni dichiarate, perche' con la musica sotto la voce il silenzio assoluto quasi non esiste: -40 dB / 0.30 s misura il silenzio vero; -30 dB / 0.25 s la pausa a soglia fissa (confrontabile fra video diversi); e una soglia relativa, 12 dB sotto la mediana RMS di QUESTO video con durata minima 0.25 s, che si adatta a un mix compresso in cui nessuna soglia assoluta bassa scatterebbe mai.

Cambi di regime: Meccanico, nessun giudizio. Su blocchi da 5 s si calcola la mediana di RMS (quanto e' forte) e la mediana dello zero-crossing rate (quanto e' acuto il contenuto: la voce e la musica non hanno lo stesso ZCR anche a pari volume). Si segna ogni blocco che si discosta dal precedente oltre soglia, su almeno uno dei due canali. La soglia NON e' fissa: e' il massimo fra un pavimento (3 dB per l'RMS, 0.05 per lo ZCR) e il percentile 90 dei salti misurati in questo stesso video, perche' un mix compresso a LRA 3 LU non produrra' mai salti da 6 dB e una soglia fissa restituirebbe zero. Che cosa sia entrato (musica, stinger, voce sola) lo dira' l'occhio in Fase 2, non questo script.

| t | canale | delta dB | da | a | delta zcr |
|---|---|---|---|---|---|
| 0:35.00 | rms | -4.91 | -15.25 | -20.16 | -0.0002 |
| 0:45.00 | rms | +5.46 | -23.95 | -18.49 | +0.0062 |
| 1:55.00 | rms | -4.89 | -17.07 | -21.96 | -0.0107 |
| 2:10.00 | rms | +7.14 | -20.41 | -13.27 | -0.0228 |
| 2:55.00 | zcr | -2.97 | -15.83 | -18.8 | +0.0521 |
| 3:00.00 | zcr | +4.14 | -18.8 | -14.66 | -0.0758 |
| 3:50.00 | zcr | -3.28 | -15.6 | -18.88 | -0.0536 |
| 4:55.00 | rms | -5.68 | -13.52 | -19.2 | +0.0012 |
| 5:40.00 | rms | -8.75 | -13.37 | -22.12 | +0.0096 |
| 5:50.00 | rms | -6.34 | -19.54 | -25.88 | -0.0281 |

## Frame

| voce | valore |
|---|---|
| frame densi (uno ogni 2.0 s, 960 px) | 179 |
| frame in cui lo schermo cambia | 102 |
| frame sul primo fotogramma di ogni inquadratura | 128 |
| riduzione | 102 su 179 densi (57.0%) |

Come: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -vf fps=1/2,scale=960:-2 -y "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\misure\claude-speedrun-sez14\frames\frame-%04d.png"`

Come: `ffmpeg -v error -nostdin -ss 0.020 -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\claude-speedrun-sez14\video.mp4" -frames:v 1 -vf scale=960:-2 -y "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\misure\claude-speedrun-sez14\frames\stacchi\stacco-0001.png"   (ripetuto per ogni inquadratura)`

Riduzione: Un frame ogni 2 s a 960 px di larghezza. La riduzione ai soli frame in cui lo schermo cambia usa il metodo di empire-studio/scripts/scene_detector.py: miniatura 64x64 in scala di grigi, differenza media assoluta normalizzata 0-100, soglia 3.0, confronto con l'ultimo frame TENUTO, piu' il presidio che tiene un frame almeno ogni 30 s.

## File

- `tecnica.json`
- `stacchi.json` / `stacchi.md`
- `audio.json` / `audio.md`
- `frames/frame-NNNN.png` + `frames/manifest.json`
- `frames/stacchi/stacco-NNNN.png`
