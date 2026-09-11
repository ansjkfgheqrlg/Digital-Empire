# Stacchi di montaggio - arma-outfunnel-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| durata video | 1:39.14 (99.136 s) |
| soglia scene score usata | **0.040** |
| tagli rilevati | **45** |
| inquadrature | 46 |
| tagli al minuto | 27.24 |
| durata media inquadratura | 2.155 s |
| durata mediana | 1.8 s |
| minima / massima | 0.03 s / 5.54 s |
| deviazione standard | 1.455 s |
| punteggio di scena mediano (moto dell'immagine) | 0.0027 |
| frame sopra soglia | 1.88% |

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outfunnel-vsl\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

## Sensibilita' alla soglia (stessa passata, soglie diverse)

| soglia | tagli | durata media | mediana | inquadrature < 1 s | |
|---|---|---|---|---|---|
| 0.028 | 56 | 1.74 s | 1.37 s | 18 |  |
| 0.040 | 45 | 2.16 s | 1.8 s | 12 | **usata** |
| 0.055 | 42 | 2.31 s | 2.1 s | 10 |  |
| 0.100 | 40 | 2.42 s | 2.3 s | 9 |  |

Perche' questa soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

## Profilo del ritmo, minuto per minuto

| minuto | tagli | inquadrature iniziate | durata media |
|---|---|---|---|
| 1 | 24 | 25 | 2.41 s |
| 2 | 21 | 21 | 1.86 s |

## Tutte le inquadrature

| n | inizio | fine | durata |
|---|---|---|---|
| 1 | 0.00 | 0.03 | 0.03 |
| 2 | 0.03 | 2.04 | 2.01 |
| 3 | 2.04 | 2.84 | 0.80 |
| 4 | 2.84 | 3.94 | 1.10 |
| 5 | 3.94 | 6.87 | 2.93 |
| 6 | 6.87 | 8.88 | 2.01 |
| 7 | 8.88 | 9.61 | 0.73 |
| 8 | 9.61 | 12.01 | 2.40 |
| 9 | 12.01 | 13.58 | 1.57 |
| 10 | 13.58 | 17.62 | 4.04 |
| 11 | 17.62 | 19.59 | 1.97 |
| 12 | 19.59 | 21.69 | 2.10 |
| 13 | 21.69 | 22.96 | 1.27 |
| 14 | 22.96 | 26.69 | 3.73 |
| 15 | 26.69 | 29.50 | 2.81 |
| 16 | 29.50 | 33.27 | 3.77 |
| 17 | 33.27 | 35.37 | 2.10 |
| 18 | 35.37 | 36.74 | 1.37 |
| 19 | 36.74 | 37.67 | 0.93 |
| 20 | 37.67 | 42.98 | 5.31 |
| 21 | 42.98 | 47.98 | 5.00 |
| 22 | 47.98 | 52.15 | 4.17 |
| 23 | 52.15 | 54.99 | 2.84 |
| 24 | 54.99 | 58.69 | 3.70 |
| 25 | 58.69 | 60.13 | 1.44 |
| 26 | 60.13 | 65.67 | 5.54 |
| 27 | 65.67 | 69.27 | 3.60 |
| 28 | 69.27 | 69.77 | 0.50 |
| 29 | 69.77 | 73.67 | 3.90 |
| 30 | 73.67 | 74.27 | 0.60 |
| 31 | 74.27 | 76.81 | 2.54 |
| 32 | 76.81 | 78.18 | 1.37 |
| 33 | 78.18 | 79.38 | 1.20 |
| 34 | 79.38 | 81.01 | 1.63 |
| 35 | 81.01 | 81.82 | 0.81 |
| 36 | 81.82 | 82.15 | 0.33 |
| 37 | 82.15 | 82.88 | 0.73 |
| 38 | 82.88 | 83.82 | 0.94 |
| 39 | 83.82 | 87.45 | 3.63 |
| 40 | 87.45 | 90.59 | 3.14 |
| 41 | 90.59 | 91.12 | 0.53 |
| 42 | 91.12 | 95.43 | 4.31 |
| 43 | 95.43 | 96.46 | 1.03 |
| 44 | 96.46 | 97.46 | 1.00 |
| 45 | 97.46 | 98.83 | 1.37 |
| 46 | 98.83 | 99.14 | 0.31 |
