# -*- coding: utf-8 -*-
"""parlato_indice.py -- mette in fila le misure del parlato dei 10 VSL.

Nessun numero nuovo: legge i `ritmo-parlato.json` gia' scritti da `parlato_misura.py`
e li impagina in una tabella sola, per poterli confrontare senza aprire dieci file.
Zero interpretazione, come tutta la Fase 3.

USO
    python parlato_indice.py
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
STUDY = os.path.dirname(HERE)
PARLATO = os.path.join(STUDY, "parlato")


def tc(s):
    return "%d:%02d" % (int(s) // 60, int(s) % 60)


def main():
    righe, tot_video, tot_voce, tot_parole = [], 0.0, 0.0, 0
    for slug in sorted(os.listdir(PARLATO)):
        f = os.path.join(PARLATO, slug, "ritmo-parlato.json")
        if not os.path.exists(f):
            continue
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        L = d.get("loudness") or {}
        pl = max(d["pause_dal_parlato"], key=lambda p: p["durata"]) if d["pause_dal_parlato"] else None
        righe.append({
            "slug": slug,
            "dur": d["durata_video_s"],
            "voce": d["densita"]["secondi_di_parlato"],
            "pct": d["densita"]["percentuale_di_parlato"],
            "seg": d["densita"]["segmenti_vocali"],
            "parole": d["parole_totali"],
            "wpm": d["parole_al_minuto_medie"],
            "wpm_voce": d["parole_al_minuto_sul_solo_parlato"],
            "pause": d["pause_sopra_0_5s"],
            "pl": pl,
            "med": L.get("mediana_segmenti_LUFS_M"),
            "sopra": len(L.get("sopra_mediana_3LU") or []),
            "sil_rel": len(d.get("silenzi_soglia_relativa") or []),
        })
        tot_video += d["durata_video_s"]
        tot_voce += d["densita"]["secondi_di_parlato"]
        tot_parole += d["parole_totali"]

    r = []
    r.append("# Indice del parlato -- 10 VSL di Andrei Pascu\n")
    r.append("FASE 3 di `EMP-DIOEDIT`. Trascrizione **in locale** con `faster-whisper small` "
             "(CPU, int8, `HF_HUB_OFFLINE=1`): nessun secondo di audio ha lasciato questa macchina.\n")
    r.append("Solo misure. Il giudizio arriva in Fase 4.\n")
    r.append("| VSL | durata | parlato | %% voce | segmenti | parole | par/min | par/min sul solo parlato | pause >=0,5 s | pausa piu' lunga | loudness mediana |")
    r.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for x in righe:
        pl = ("%.2f s @ %s" % (x["pl"]["durata"], tc(x["pl"]["inizio"]))) if x["pl"] else "--"
        r.append("| `%s` | %s | %s | %s%% | %d | %d | %s | %s | %d | %s | %s LUFS-M |"
                 % (x["slug"], tc(x["dur"]), tc(x["voce"]), x["pct"], x["seg"], x["parole"],
                    x["wpm"], x["wpm_voce"], x["pause"], pl, x["med"]))
    r.append("")
    r.append("**Totali:** %s di girato, %s di parlato (%.1f%%), %d parole, %.1f parole al minuto "
             "sulla media dei dieci video.\n"
             % (tc(tot_video), tc(tot_voce), 100.0 * tot_voce / tot_video, tot_parole,
                tot_parole * 60.0 / tot_video))
    r.append("## Cosa c'e' in ogni cartella\n")
    r.append("- `trascrizione.json` -- segmenti con inizio/fine **e ogni singola parola col suo tempo**;")
    r.append("- `trascrizione.md` -- lo stesso testo leggibile, `[mm:ss.cc -> mm:ss.cc]`;")
    r.append("- `ritmo-parlato.json` -- pause, parole al minuto minuto per minuto, silenzi grezzi a "
             "tre soglie, profilo di loudness EBU R128 e loudness media di ogni segmento parlato;")
    r.append("- `_SOMMARIO.md` -- il quadro di un video solo: apertura e chiusura testuali, pause piu' "
             "lunghe, dove la voce sale, ritmo minuto per minuto.\n")
    r.append("## Avvertenze di metodo\n")
    r.append("- I confini del parlato vengono dal riconoscitore (VAD attivo, silenzio minimo 400 ms): "
             "sono i confini della **voce**, non dell'onda. Le pause qui sotto sono buchi fra parole, "
             "non silenzi assoluti.")
    r.append("- I silenzi grezzi (`silencedetect`) sono misurati a parte, su tre soglie, e su una base "
             "musicale continua possono legittimamente valere zero: sotto la musica non c'e' silenzio, "
             "c'e' solo assenza di voce.")
    r.append("- La loudness per segmento e' la media aritmetica dei campioni momentanei EBU R128 "
             "(finestra 400 ms) caduti dentro quel segmento: e' una media di valori gia' logaritmici, "
             "confrontabile fra segmenti dello stesso video, non un'energia integrata.")
    r.append("- Il riconoscitore puo' sbagliare una parola. Il **tempo** e' affidabile, la **grafia** di "
             "un nome proprio o di un anglicismo va verificata a orecchio prima di citarla in un rapporto.")
    r.append("")
    r.append("Generato da `scripts/parlato_indice.py`.")

    with open(os.path.join(PARLATO, "_INDICE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(r))
    print("[ok] _INDICE.md -- %d VSL in tabella" % len(righe))


if __name__ == "__main__":
    main()
