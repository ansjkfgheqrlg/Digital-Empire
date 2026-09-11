# Stacchi di montaggio - arma-outemail-vsl

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| durata video | 2:47.40 (167.403 s) |
| soglia scene score usata | **0.040** |
| tagli rilevati | **51** |
| inquadrature | 52 |
| tagli al minuto | 18.28 |
| durata media inquadratura | 3.219 s |
| durata mediana | 2.04 s |
| minima / massima | 0.2 s / 22.89 s |
| deviazione standard | 4.11 s |
| punteggio di scena mediano (moto dell'immagine) | 0.0006 |
| frame sopra soglia | 1.24% |

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\arma-outemail-vsl\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

## Sensibilita' alla soglia (stessa passata, soglie diverse)

| soglia | tagli | durata media | mediana | inquadrature < 1 s | |
|---|---|---|---|---|---|
| 0.028 | 64 | 2.58 s | 1.63 s | 22 |  |
| 0.040 | 51 | 3.22 s | 2.04 s | 11 | **usata** |
| 0.055 | 41 | 3.99 s | 2.85 s | 6 |  |
| 0.100 | 31 | 5.23 s | 3.37 s | 4 |  |

Perche' questa soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

## Profilo del ritmo, minuto per minuto

| minuto | tagli | inquadrature iniziate | durata media |
|---|---|---|---|
| 1 | 14 | 15 | 4.22 s |
| 2 | 25 | 25 | 2.29 s |
| 3 | 12 | 12 | 3.9 s |

## Tutte le inquadrature

| n | inizio | fine | durata |
|---|---|---|---|
| 1 | 0.00 | 1.37 | 1.37 |
| 2 | 1.37 | 4.47 | 3.10 |
| 3 | 4.47 | 5.34 | 0.87 |
| 4 | 5.34 | 7.67 | 2.33 |
| 5 | 7.67 | 8.27 | 0.60 |
| 6 | 8.27 | 8.74 | 0.47 |
| 7 | 8.74 | 8.94 | 0.20 |
| 8 | 8.94 | 9.14 | 0.20 |
| 9 | 9.14 | 12.91 | 3.77 |
| 10 | 12.91 | 15.78 | 2.87 |
| 11 | 15.78 | 19.39 | 3.61 |
| 12 | 19.39 | 25.93 | 6.54 |
| 13 | 25.93 | 32.67 | 6.74 |
| 14 | 32.67 | 40.41 | 7.74 |
| 15 | 40.41 | 63.30 | 22.89 |
| 16 | 63.30 | 63.60 | 0.30 |
| 17 | 63.60 | 64.03 | 0.43 |
| 18 | 64.03 | 65.43 | 1.40 |
| 19 | 65.43 | 67.30 | 1.87 |
| 20 | 67.30 | 67.63 | 0.33 |
| 21 | 67.63 | 68.84 | 1.21 |
| 22 | 68.84 | 72.41 | 3.57 |
| 23 | 72.41 | 74.94 | 2.53 |
| 24 | 74.94 | 80.25 | 5.31 |
| 25 | 80.25 | 82.05 | 1.80 |
| 26 | 82.05 | 86.39 | 4.34 |
| 27 | 86.39 | 86.72 | 0.33 |
| 28 | 86.72 | 91.66 | 4.94 |
| 29 | 91.66 | 92.53 | 0.87 |
| 30 | 92.53 | 93.46 | 0.93 |
| 31 | 93.46 | 95.60 | 2.14 |
| 32 | 95.60 | 103.94 | 8.34 |
| 33 | 103.94 | 108.04 | 4.10 |
| 34 | 108.04 | 110.34 | 2.30 |
| 35 | 110.34 | 112.11 | 1.77 |
| 36 | 112.11 | 113.51 | 1.40 |
| 37 | 113.51 | 116.08 | 2.57 |
| 38 | 116.08 | 117.15 | 1.07 |
| 39 | 117.15 | 118.99 | 1.84 |
| 40 | 118.99 | 120.62 | 1.63 |
| 41 | 120.62 | 122.76 | 2.14 |
| 42 | 122.76 | 125.59 | 2.83 |
| 43 | 125.59 | 129.80 | 4.21 |
| 44 | 129.80 | 131.10 | 1.30 |
| 45 | 131.10 | 136.20 | 5.10 |
| 46 | 136.20 | 137.24 | 1.04 |
| 47 | 137.24 | 138.37 | 1.13 |
| 48 | 138.37 | 140.31 | 1.94 |
| 49 | 140.31 | 141.98 | 1.67 |
| 50 | 141.98 | 144.51 | 2.53 |
| 51 | 144.51 | 147.65 | 3.14 |
| 52 | 147.65 | 167.40 | 19.75 |
