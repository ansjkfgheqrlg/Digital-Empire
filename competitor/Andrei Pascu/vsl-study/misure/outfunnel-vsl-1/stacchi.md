# Stacchi di montaggio - outfunnel-vsl-1

Misura a macchina. Nessuna interpretazione.

| voce | valore |
|---|---|
| durata video | 2:31.28 (151.275 s) |
| soglia scene score usata | **0.040** |
| tagli rilevati | **72** |
| inquadrature | 73 |
| tagli al minuto | 28.56 |
| durata media inquadratura | 2.072 s |
| durata mediana | 1.84 s |
| minima / massima | 0.2 s / 8.5 s |
| deviazione standard | 1.579 s |
| punteggio di scena mediano (moto dell'immagine) | 0.0017 |
| frame sopra soglia | 1.96% |

Comando: `ffmpeg -v error -nostdin -i "C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\vsl-study\sorgenti\outfunnel-vsl-1\video.mp4" -an -vf "scale=320:-2,select='gte(scene,0)',metadata=print:file=-" -f null -`

## Sensibilita' alla soglia (stessa passata, soglie diverse)

| soglia | tagli | durata media | mediana | inquadrature < 1 s | |
|---|---|---|---|---|---|
| 0.028 | 93 | 1.61 s | 1.17 s | 41 |  |
| 0.040 | 72 | 2.07 s | 1.84 s | 21 | **usata** |
| 0.055 | 53 | 2.8 s | 2.75 s | 5 |  |
| 0.100 | 47 | 3.15 s | 2.75 s | 3 |  |

Perche' questa soglia: 0.040 sullo scene score di ffmpeg calcolato su luma ridotta a 320 px. Calibrata su armageddon-home il 2026-09-10 estraendo il fotogramma prima e dopo un campione di candidati in quattro bande di punteggio e guardandoli: banda 0.028-0.040 = 2-3 tagli veri su 8 candidati (il resto e' movimento del soggetto dentro la stessa inquadratura); banda 0.040-0.055 = 5 su 6 tagli veri; banda 0.055-0.080 = 3 su 5; banda 0.080-0.150 = 4 su 5. Il confine fra movimento e taglio cade a 0.040. Sopra 0.10 si perdono i jump cut su fondo nero identico (misurati a 0.043-0.068), che in questo materiale sono la maggioranza dei tagli.

Limite noto: Un taglio in dissolvenza distribuisce il cambiamento su piu' fotogrammi e resta sotto qualsiasi soglia per fotogramma singolo: a 8.32 s di armageddon-home il passaggio dal parlato al b-roll in bianco e nero segna 0.0312. Questi tagli morbidi sono sotto-contati per costruzione.

## Profilo del ritmo, minuto per minuto

| minuto | tagli | inquadrature iniziate | durata media |
|---|---|---|---|
| 1 | 37 | 38 | 1.65 s |
| 2 | 19 | 19 | 3.06 s |
| 3 | 16 | 16 | 1.89 s |

## Tutte le inquadrature

| n | inizio | fine | durata |
|---|---|---|---|
| 1 | 0.00 | 0.67 | 0.67 |
| 2 | 0.67 | 0.93 | 0.26 |
| 3 | 0.93 | 1.83 | 0.90 |
| 4 | 1.83 | 2.23 | 0.40 |
| 5 | 2.23 | 5.87 | 3.64 |
| 6 | 5.87 | 6.87 | 1.00 |
| 7 | 6.87 | 7.90 | 1.03 |
| 8 | 7.90 | 9.03 | 1.13 |
| 9 | 9.03 | 12.23 | 3.20 |
| 10 | 12.23 | 13.50 | 1.27 |
| 11 | 13.50 | 16.73 | 3.23 |
| 12 | 16.73 | 21.17 | 4.44 |
| 13 | 21.17 | 24.17 | 3.00 |
| 14 | 24.17 | 26.10 | 1.93 |
| 15 | 26.10 | 29.83 | 3.73 |
| 16 | 29.83 | 32.70 | 2.87 |
| 17 | 32.70 | 34.13 | 1.43 |
| 18 | 34.13 | 34.67 | 0.54 |
| 19 | 34.67 | 35.47 | 0.80 |
| 20 | 35.47 | 37.63 | 2.16 |
| 21 | 37.63 | 38.93 | 1.30 |
| 22 | 38.93 | 39.23 | 0.30 |
| 23 | 39.23 | 39.63 | 0.40 |
| 24 | 39.63 | 39.90 | 0.27 |
| 25 | 39.90 | 40.23 | 0.33 |
| 26 | 40.23 | 40.57 | 0.34 |
| 27 | 40.57 | 41.93 | 1.36 |
| 28 | 41.93 | 43.77 | 1.84 |
| 29 | 43.77 | 46.63 | 2.86 |
| 30 | 46.63 | 48.37 | 1.74 |
| 31 | 48.37 | 48.70 | 0.33 |
| 32 | 48.70 | 49.03 | 0.33 |
| 33 | 49.03 | 50.13 | 1.10 |
| 34 | 50.13 | 51.23 | 1.10 |
| 35 | 51.23 | 52.60 | 1.37 |
| 36 | 52.60 | 53.77 | 1.17 |
| 37 | 53.77 | 55.87 | 2.10 |
| 38 | 55.87 | 62.80 | 6.93 |
| 39 | 62.80 | 64.60 | 1.80 |
| 40 | 64.60 | 67.10 | 2.50 |
| 41 | 67.10 | 70.27 | 3.17 |
| 42 | 70.27 | 73.03 | 2.76 |
| 43 | 73.03 | 77.47 | 4.44 |
| 44 | 77.47 | 78.37 | 0.90 |
| 45 | 78.37 | 80.60 | 2.23 |
| 46 | 80.60 | 83.43 | 2.83 |
| 47 | 83.43 | 87.50 | 4.07 |
| 48 | 87.50 | 90.43 | 2.93 |
| 49 | 90.43 | 92.90 | 2.47 |
| 50 | 92.90 | 96.70 | 3.80 |
| 51 | 96.70 | 100.67 | 3.97 |
| 52 | 100.67 | 101.43 | 0.76 |
| 53 | 101.43 | 101.63 | 0.20 |
| 54 | 101.63 | 110.13 | 8.50 |
| 55 | 110.13 | 113.63 | 3.50 |
| 56 | 113.63 | 118.90 | 5.27 |
| 57 | 118.90 | 121.03 | 2.13 |
| 58 | 121.03 | 123.63 | 2.60 |
| 59 | 123.63 | 125.33 | 1.70 |
| 60 | 125.33 | 126.30 | 0.97 |
| 61 | 126.30 | 128.17 | 1.87 |
| 62 | 128.17 | 131.60 | 3.43 |
| 63 | 131.60 | 134.33 | 2.73 |
| 64 | 134.33 | 136.70 | 2.37 |
| 65 | 136.70 | 139.13 | 2.43 |
| 66 | 139.13 | 141.83 | 2.70 |
| 67 | 141.83 | 142.40 | 0.57 |
| 68 | 142.40 | 142.73 | 0.33 |
| 69 | 142.73 | 143.10 | 0.37 |
| 70 | 143.10 | 143.50 | 0.40 |
| 71 | 143.50 | 147.13 | 3.63 |
| 72 | 147.13 | 150.13 | 3.00 |
| 73 | 150.13 | 151.28 | 1.15 |
