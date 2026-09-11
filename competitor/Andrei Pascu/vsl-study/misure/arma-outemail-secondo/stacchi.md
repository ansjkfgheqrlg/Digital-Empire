# Stacchi di montaggio - arma-outemail-secondo

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| durata video | 1:46.35 (106.347 s) |
| soglia scene score usata | **0.040** |
| tagli rilevati | **45** |
| inquadrature | 46 |
| tagli al minuto | 25.39 |
| durata media inquadratura | 2.312 s |
| durata mediana | 1.675 s |
| minima / massima | 0.03 s / 12.88 s |
| deviazione standard | 2.371 s |
| punteggio di scena mediano (moto dell'immagine) | 0.0006 |
| frame sopra soglia | 1.76% |

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-secondo\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

## Sensibilita' alla soglia (stessa passata, soglie diverse)

| soglia | tagli | durata media | mediana | inquadrature < 1 s | |
|---|---|---|---|---|---|
| 0.028 | 51 | 2.05 s | 1.44 s | 19 |  |
| 0.040 | 45 | 2.31 s | 1.68 s | 15 | **usata** |
| 0.055 | 38 | 2.73 s | 1.97 s | 8 |  |
| 0.100 | 30 | 3.43 s | 2.5 s | 5 |  |

Perche' questa soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

## Profilo del ritmo, minuto per minuto

| minuto | tagli | inquadrature iniziate | durata media |
|---|---|---|---|
| 1 | 29 | 30 | 2.08 s |
| 2 | 16 | 16 | 2.75 s |

## Tutte le inquadrature

| n | inizio | fine | durata |
|---|---|---|---|
| 1 | 0.00 | 0.03 | 0.03 |
| 2 | 0.03 | 1.67 | 1.64 |
| 3 | 1.67 | 2.54 | 0.87 |
| 4 | 2.54 | 4.37 | 1.83 |
| 5 | 4.37 | 7.47 | 3.10 |
| 6 | 7.47 | 12.25 | 4.78 |
| 7 | 12.25 | 14.05 | 1.80 |
| 8 | 14.05 | 16.55 | 2.50 |
| 9 | 16.55 | 19.32 | 2.77 |
| 10 | 19.32 | 20.95 | 1.63 |
| 11 | 20.95 | 22.66 | 1.71 |
| 12 | 22.66 | 24.02 | 1.36 |
| 13 | 24.02 | 36.90 | 12.88 |
| 14 | 36.90 | 37.27 | 0.37 |
| 15 | 37.27 | 38.14 | 0.87 |
| 16 | 38.14 | 38.51 | 0.37 |
| 17 | 38.51 | 39.77 | 1.26 |
| 18 | 39.77 | 40.51 | 0.74 |
| 19 | 40.51 | 41.44 | 0.93 |
| 20 | 41.44 | 42.11 | 0.67 |
| 21 | 42.11 | 42.51 | 0.40 |
| 22 | 42.51 | 42.78 | 0.27 |
| 23 | 42.78 | 43.18 | 0.40 |
| 24 | 43.18 | 43.58 | 0.40 |
| 25 | 43.58 | 43.98 | 0.40 |
| 26 | 43.98 | 45.61 | 1.63 |
| 27 | 45.61 | 54.42 | 8.81 |
| 28 | 54.42 | 57.62 | 3.20 |
| 29 | 57.62 | 59.43 | 1.81 |
| 30 | 59.43 | 62.33 | 2.90 |
| 31 | 62.33 | 65.77 | 3.44 |
| 32 | 65.77 | 66.47 | 0.70 |
| 33 | 66.47 | 69.94 | 3.47 |
| 34 | 69.94 | 71.91 | 1.97 |
| 35 | 71.91 | 77.11 | 5.20 |
| 36 | 77.11 | 81.25 | 4.14 |
| 37 | 81.25 | 84.88 | 3.63 |
| 38 | 84.88 | 85.72 | 0.84 |
| 39 | 85.72 | 88.02 | 2.30 |
| 40 | 88.02 | 89.49 | 1.47 |
| 41 | 89.49 | 90.59 | 1.10 |
| 42 | 90.59 | 91.86 | 1.27 |
| 43 | 91.86 | 95.23 | 3.37 |
| 44 | 95.23 | 97.20 | 1.97 |
| 45 | 97.20 | 99.17 | 1.97 |
| 46 | 99.17 | 106.35 | 7.18 |
