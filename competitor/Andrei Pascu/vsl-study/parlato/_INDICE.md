# Indice del parlato -- 10 VSL di Andrei Pascu

FASE 3 di `EMP-DIOEDIT`. Trascrizione **in locale** con `faster-whisper small` (CPU, int8, `HF_HUB_OFFLINE=1`): nessun secondo di audio ha lasciato questa macchina.

Solo misure. Il giudizio arriva in Fase 4.

| VSL | durata | parlato | %% voce | segmenti | parole | par/min | par/min sul solo parlato | pause >=0,5 s | pausa piu' lunga | loudness mediana |
|---|---|---|---|---|---|---|---|---|---|---|
| `arma-outemail-secondo` | 1:46 | 1:36 | 90.7% | 27 | 287 | 161.9 | 178.6 | 1 | 7.51 s @ 1:38 | -24.9 LUFS-M |
| `arma-outemail-vsl` | 2:47 | 2:21 | 84.5% | 32 | 434 | 155.6 | 184.1 | 4 | 23.18 s @ 2:24 | -24.8 LUFS-M |
| `arma-outfunnel-vsl` | 1:39 | 1:36 | 97.8% | 24 | 343 | 207.6 | 212.3 | 1 | 0.66 s @ 1:28 | -20.2 LUFS-M |
| `armageddon-home` | 13:28 | 13:11 | 97.9% | 225 | 2959 | 219.5 | 224.3 | 13 | 3.00 s @ 0:30 | -21.7 LUFS-M |
| `claude-speedrun-hero` | 1:21 | 1:10 | 86.6% | 28 | 210 | 155.0 | 179.0 | 7 | 2.06 s @ 0:11 | -18.4 LUFS-M |
| `claude-speedrun-sez14` | 5:57 | 5:48 | 97.5% | 74 | 1095 | 184.0 | 188.6 | 9 | 4.12 s @ 5:53 | -17.3 LUFS-M |
| `claude-speedrun-sez9` | 4:45 | 4:42 | 98.8% | 53 | 872 | 183.0 | 185.3 | 5 | 2.21 s @ 1:34 | -18.9 LUFS-M |
| `outfunnel-vsl-1` | 2:31 | 2:29 | 99.0% | 39 | 514 | 203.9 | 206.0 | 0 | 0.46 s @ 1:43 | -20.4 LUFS-M |
| `outfunnel-vsl-2` | 1:48 | 1:46 | 98.2% | 26 | 377 | 207.9 | 211.7 | 1 | 0.66 s @ 1:28 | -20.2 LUFS-M |
| `outheadline-vsl` | 0:46 | 0:43 | 94.9% | 11 | 126 | 163.5 | 172.3 | 2 | 1.11 s @ 0:07 | -19.8 LUFS-M |

**Totali:** 36:52 di girato, 35:27 di parlato (96.2%), 7217 parole, 195.7 parole al minuto sulla media dei dieci video.

## Cosa c'e' in ogni cartella

- `trascrizione.json` -- segmenti con inizio/fine **e ogni singola parola col suo tempo**;
- `trascrizione.md` -- lo stesso testo leggibile, `[mm:ss.cc -> mm:ss.cc]`;
- `ritmo-parlato.json` -- pause, parole al minuto minuto per minuto, silenzi grezzi a tre soglie, profilo di loudness EBU R128 e loudness media di ogni segmento parlato;
- `_SOMMARIO.md` -- il quadro di un video solo: apertura e chiusura testuali, pause piu' lunghe, dove la voce sale, ritmo minuto per minuto.

## Avvertenze di metodo

- I confini del parlato vengono dal riconoscitore (VAD attivo, silenzio minimo 400 ms): sono i confini della **voce**, non dell'onda. Le pause qui sotto sono buchi fra parole, non silenzi assoluti.
- I silenzi grezzi (`silencedetect`) sono misurati a parte, su tre soglie, e su una base musicale continua possono legittimamente valere zero: sotto la musica non c'e' silenzio, c'e' solo assenza di voce.
- La loudness per segmento e' la media aritmetica dei campioni momentanei EBU R128 (finestra 400 ms) caduti dentro quel segmento: e' una media di valori gia' logaritmici, confrontabile fra segmenti dello stesso video, non un'energia integrata.
- Il riconoscitore puo' sbagliare una parola. Il **tempo** e' affidabile, la **grafia** di un nome proprio o di un anglicismo va verificata a orecchio prima di citarla in un rapporto.

Generato da `scripts/parlato_indice.py`.