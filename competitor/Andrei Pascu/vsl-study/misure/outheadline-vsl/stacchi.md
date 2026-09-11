# Stacchi di montaggio - outheadline-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| durata video | 0:46.25 (46.251 s) |
| soglia scene score usata | **0.040** |
| tagli rilevati | **68** |
| inquadrature | 69 |
| tagli al minuto | 88.21 |
| durata media inquadratura | 0.67 s |
| durata mediana | 0.25 s |
| minima / massima | 0.04 s / 4.84 s |
| deviazione standard | 1.116 s |
| punteggio di scena mediano (moto dell'immagine) | 0.004 |
| frame sopra soglia | 12.43% |

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outheadline-vsl\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

## Sensibilita' alla soglia (stessa passata, soglie diverse)

| soglia | tagli | durata media | mediana | inquadrature < 1 s | |
|---|---|---|---|---|---|
| 0.028 | 75 | 0.61 s | 0.25 s | 64 |  |
| 0.040 | 68 | 0.67 s | 0.25 s | 59 | **usata** |
| 0.055 | 63 | 0.72 s | 0.25 s | 56 |  |
| 0.100 | 60 | 0.76 s | 0.25 s | 54 |  |

Perche' questa soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

## Profilo del ritmo, minuto per minuto

| minuto | tagli | inquadrature iniziate | durata media |
|---|---|---|---|
| 1 | 68 | 69 | 0.67 s |

## Tutte le inquadrature

| n | inizio | fine | durata |
|---|---|---|---|
| 1 | 0.00 | 0.08 | 0.08 |
| 2 | 0.08 | 0.38 | 0.30 |
| 3 | 0.38 | 0.75 | 0.37 |
| 4 | 0.75 | 1.00 | 0.25 |
| 5 | 1.00 | 1.25 | 0.25 |
| 6 | 1.25 | 1.46 | 0.21 |
| 7 | 1.46 | 1.75 | 0.29 |
| 8 | 1.75 | 2.00 | 0.25 |
| 9 | 2.00 | 2.25 | 0.25 |
| 10 | 2.25 | 2.50 | 0.25 |
| 11 | 2.50 | 2.75 | 0.25 |
| 12 | 2.75 | 3.00 | 0.25 |
| 13 | 3.00 | 3.38 | 0.38 |
| 14 | 3.38 | 3.62 | 0.24 |
| 15 | 3.62 | 3.88 | 0.26 |
| 16 | 3.88 | 4.12 | 0.24 |
| 17 | 4.12 | 4.50 | 0.38 |
| 18 | 4.50 | 4.88 | 0.38 |
| 19 | 4.88 | 5.12 | 0.24 |
| 20 | 5.12 | 5.50 | 0.38 |
| 21 | 5.50 | 5.75 | 0.25 |
| 22 | 5.75 | 6.12 | 0.37 |
| 23 | 6.12 | 6.38 | 0.26 |
| 24 | 6.38 | 6.75 | 0.37 |
| 25 | 6.75 | 7.12 | 0.37 |
| 26 | 7.12 | 7.38 | 0.26 |
| 27 | 7.38 | 7.62 | 0.24 |
| 28 | 7.62 | 8.00 | 0.38 |
| 29 | 8.00 | 8.21 | 0.21 |
| 30 | 8.21 | 8.46 | 0.25 |
| 31 | 8.46 | 8.71 | 0.25 |
| 32 | 8.71 | 8.96 | 0.25 |
| 33 | 8.96 | 9.17 | 0.21 |
| 34 | 9.17 | 9.38 | 0.21 |
| 35 | 9.38 | 9.62 | 0.24 |
| 36 | 9.62 | 9.88 | 0.26 |
| 37 | 9.88 | 10.12 | 0.24 |
| 38 | 10.12 | 14.58 | 4.46 |
| 39 | 14.58 | 14.79 | 0.21 |
| 40 | 14.79 | 15.04 | 0.25 |
| 41 | 15.04 | 15.29 | 0.25 |
| 42 | 15.29 | 15.50 | 0.21 |
| 43 | 15.50 | 15.79 | 0.29 |
| 44 | 15.79 | 16.04 | 0.25 |
| 45 | 16.04 | 16.29 | 0.25 |
| 46 | 16.29 | 16.54 | 0.25 |
| 47 | 16.54 | 16.79 | 0.25 |
| 48 | 16.79 | 17.04 | 0.25 |
| 49 | 17.04 | 17.29 | 0.25 |
| 50 | 17.29 | 17.54 | 0.25 |
| 51 | 17.54 | 17.92 | 0.38 |
| 52 | 17.92 | 18.17 | 0.25 |
| 53 | 18.17 | 18.42 | 0.25 |
| 54 | 18.42 | 18.67 | 0.25 |
| 55 | 18.67 | 18.92 | 0.25 |
| 56 | 18.92 | 19.17 | 0.25 |
| 57 | 19.17 | 19.42 | 0.25 |
| 58 | 19.42 | 19.67 | 0.25 |
| 59 | 19.67 | 23.96 | 4.29 |
| 60 | 23.96 | 25.54 | 1.58 |
| 61 | 25.54 | 27.17 | 1.63 |
| 62 | 27.17 | 29.54 | 2.37 |
| 63 | 29.54 | 34.38 | 4.84 |
| 64 | 34.38 | 37.25 | 2.87 |
| 65 | 37.25 | 41.92 | 4.67 |
| 66 | 41.92 | 43.00 | 1.08 |
| 67 | 43.00 | 43.21 | 0.21 |
| 68 | 43.21 | 46.21 | 3.00 |
| 69 | 46.21 | 46.25 | 0.04 |
