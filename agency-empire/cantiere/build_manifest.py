"""Costruisce public/aura/manifest.json — il contratto fra copy, immagine e componente (Dossier 37, F0).

Una riga per file della cartella AURA (41) + 3 righe per le immagini che non vengono dalla cartella
(ritratti team, screenshot dashboard). Cambiare corsia (originale -> generata) = cambiare `sorgente`
e `file_pubblico` qui, non un componente.
"""
import json, os, pathlib

SRC = pathlib.Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Caroselli Style\immagini AURA")
OUT = pathlib.Path(__file__).resolve().parents[1] / "public" / "aura" / "manifest.json"

files = sorted(f for f in os.listdir(SRC) if f.lower().endswith((".jpg", ".png")))

# indice nel foglio-contatti (ordine alfabetico) -> (alt, brief luce/taglio)
DESC = {
    0: ("uomo in smoking, papillon, sguardo basso, luce calda di taglio", "ritratto formale, luce calda da sinistra, fondo scuro"),
    1: ("uomo con occhiali che conta banconote dentro un'asciugatrice", "denaro che gira a vuoto, luce fredda, dettaglio mani"),
    2: ("uomo con cappello a tesa larga, sguardo dritto, luce di taglio, sfondo verde sfocato", "ritratto frontale, cappello, luce laterale dura, fondo sfocato"),
    3: ("guerriero in armatura dorata fra le fiamme, fondo nero", "figura in armatura, bagliore arancione dal basso, nero intorno"),
    4: ("uomo in giacca grigia, sigaretta, sguardo in camera, fondo scuro", "ritratto tre quarti, luce fredda, fondo nero"),
    5: ("pugile sul ring, luci dall'alto, pubblico sfocato", "atleta sul ring, controluce, riflettori"),
    6: ("re con maschera d'argento e mantello, citta' sullo sfondo", "figura regale con maschera, luce diffusa, skyline"),
    7: ("uomo in gessato che mostra una banconota da un dollaro", "ritratto con banconota in primo piano, luce calda"),
    8: ("uomo in smoking davanti a una vetrata notturna", "ritratto formale, luce blu da finestra, notte"),
    9: ("uomo con le lacrime agli occhi, primo piano, luce fredda", "primo piano emotivo, luce fredda, fondo neutro"),
    10: ("uomo in giacca su poltrona, bianco e nero, luce da finestra", "ritratto b/n, luce laterale morbida"),
    11: ("figura in armatura dorata che muove una pedina su una scacchiera", "mani su scacchiera, oro e nero, luce di candela"),
    12: ("uomo con occhi rossi luminosi, costume scuro", "scartata: villain"),
    13: ("uomo in cappotto scuro, camicia bianca, sguardo lontano, luce blu", "ritratto tre quarti, luce fredda blu, fondo nero"),
    14: ("uomo in armatura rossa e oro seduto a un tavolo con una ciambella", "figura in armatura a tavola, luce calda interna"),
    15: ("uomo in giacca in mezzo a una folla in strada, tutti in giacca", "folla in strada, luce diurna, un volto a fuoco"),
    16: ("silhouette in controluce davanti a tre finestre bianche", "silhouette totale, controluce bianco, nessun volto"),
    17: ("uomo con occhiali da sole fra la folla che fa il pollice in su", "ritratto in folla, luce interna, gesto di approvazione"),
    18: ("pugile con cinture da campione, guanti rossi, luce dall'alto", "atleta con trofei, luce dall'alto, fondo scuro"),
    19: ("figura incoronata scura su un campo di battaglia, cielo grigio", "figura scura con corona, cielo plumbeo, terreno"),
    20: ("uomo con occhi rossi, fondo nero", "scartata: villain"),
    21: ("uomo con occhiali al lavoro, braccia conserte, luce fredda", "ritratto tre quarti, occhiali, luce fredda da schermo"),
    22: ("uomo in giacca seduto con la mano sul viso", "gesto di stanchezza, luce calda laterale, poltrona"),
    23: ("uomo con occhiali da sole e giacca grigia, cravatta, esterno", "ritratto esterno, occhiali, luce diurna"),
    24: ("uomo seduto in una cabina, sguardo basso, luce fredda", "interno tecnico, luce fredda, volto pensieroso"),
    25: ("elmo da cavaliere medievale, visiera, luce laterale", "elmo in acciaio, luce laterale dura, fondo nero"),
    26: ("uomo in cappotto con camicia bianca, primo piano, luce calda", "ritratto frontale, luce calda, fondo scuro"),
    27: ("uomo con occhi rossi sotto la pioggia, notte", "scartata: villain"),
    28: ("uomo dai capelli grigi che sorride, giacca nera, luce blu", "ritratto sorridente, luce blu, fondo scuro"),
    29: ("uomo con occhiali da sole che saluta dal finestrino di un'auto", "gesto di saluto dall'auto, luce diurna, giacca chiara"),
    30: ("pugile in piedi sopra l'avversario a terra, ring, pubblico", "atleta vincitore sul ring, luce dall'alto"),
    31: ("uomo con cravatta rossa che sorride, corridoio bianco", "ritratto sorridente, luce neutra, corridoio"),
    32: ("uomo in giacca nera, camicia bianca, sguardo serio, fondo scuro", "ritratto frontale serio, luce laterale"),
    33: ("uomo in giacca su poltrona, bianco e nero, mani in grembo", "ritratto b/n seduto, luce da finestra"),
    34: ("figura incoronata scura con mantello rosso su campo di battaglia", "scartata: villain"),
    35: ("uomo con bicchiere di whisky, giacca, luce calda", "ritratto con bicchiere, luce calda, fine giornata"),
    36: ("uomo in camicia a righe e bretelle, mani giunte, ufficio", "ritratto in ufficio, mani giunte, luce da finestra"),
    37: ("uomo con le lacrime agli occhi, primo piano, variante", "primo piano emotivo, luce fredda"),
    38: ("uomo in smoking che sorride, sfondo citta' notturna", "ritratto sorridente, luce blu, citta'"),
    39: ("uomo in camicia azzurra che sorride, luce da finestra", "ritratto sorridente, luce naturale laterale"),
    40: ("uomo con capelli bagnati in un pub, luce calda", "ritratto in interno, luce calda, sguardo di lato"),
}

# indice -> (posto, sezione, ruolo, didascalia = la riga bianca)
CAST = {
    2: (1, "N1", "hero", 'Ho costruito il primo sistema per me. Poi ho smesso di venderlo come "tool".'),
    22: (2, "N2", "specchio", "Ogni mattina. Trenta DM. A mano. Da tre anni."),
    14: (3, "N4", "outreach", "Alle 7:40 ha gia' mandato 300 messaggi. Tu stai facendo colazione."),
    21: (4, "N4", "content", "Un argomento entra. Carosello, reel, caption escono. Senza toccare niente."),
    16: (5, "N6", "fascia", "Non ha un nome. Ha un sistema. E ha i tuoi clienti."),
    # 15 (folla): era il posto 6 sull'asse; tolto in build per la regola "mai due foto di fila" -> riserva
    30: (7, "N8", "ascolta-bene", "Non e' piu' forte. E' arrivato prima."),
    1: (8, "N9", "formula", "Dodici canoni all'anno per un tool che non sa chi sei."),
    35: (9, "N10", "processo", "Il giorno dopo il go-live: 30 giorni di monitoraggio nostri. Le serate tue."),
    36: (11, "N12", "per-chi", "Se vuoi delegare senza capire, non siamo noi. Sul serio."),
    25: (12, "N14", "garanzia", 'Se il sistema non gira come scritto, lo rifacciamo. Non "ti richiamiamo".'),
    29: (13, "N15", "obiezioni", "Ci licenzi quando vuoi. Il codice resta tuo. Ciao."),
}

rows = []
for i, f in enumerate(files):
    alt, brief = DESC[i]
    c = CAST.get(i)
    scartata = brief.startswith("scartata")
    rows.append({
        "id": f.split(".")[0][:8],
        "file_originale": f,
        "indice_foglio": i,
        "posto": c[0] if c else None,
        "sezione": c[1] if c else None,
        "ruolo": c[2] if c else ("scartata" if scartata else "riserva"),
        "alt": alt,
        "didascalia": c[3] if c else None,
        "sorgente": "originale",
        "trattamento": "B" if c else None,
        "brief_generazione": None if scartata else (
            f"Still cinematografico, {brief}; grana pellicola; volto NON riconducibile a persone reali; "
            "palette da desaturare (trattamento B)"),
        "file_pubblico": f"aura/{c[1].lower()}-{c[2]}.webp" if c else None,
        "nota": ("in produzione: ritratto di Max con la stessa luce" if i == 2
                 else "originale 400x400: rigenerare a 1200" if i == 22 else None),
    })

extra = [
    {"id": "team-max", "posto": 10, "sezione": "N11", "ruolo": "chi-siamo", "alt": "Max, ritratto in luce di taglio",
     "didascalia": "Parli con chi ha le mani sui workflow. Per scelta, non per limite.", "sorgente": "team",
     "trattamento": "B", "file_pubblico": "aura/n11-max.webp", "nota": "dipende da Max, non blocca: silhouette con nome finche' manca"},
    {"id": "team-gael", "posto": 10, "sezione": "N11", "ruolo": "chi-siamo", "alt": "Gael, ritratto in luce di taglio",
     "didascalia": None, "sorgente": "team", "trattamento": "B", "file_pubblico": "aura/n11-gael.webp",
     "nota": "dipende da Max, non blocca"},
    {"id": "dash-outreach", "posto": 14, "sezione": "N4/N18", "ruolo": "oggetto-icona",
     "alt": "Dashboard Outreach Factory: invii del giorno, risposte in coda", "didascalia": None,
     "sorgente": "screenshot", "trattamento": "D (richiamo in N18)", "file_pubblico": "aura/oggetto-dashboard.png",
     "nota": "screenshot reale dal sistema; finche' manca, componente disegnato"},
]

manifest = {
    "versione": 1,
    "data": "2026-09-11",
    "regole": {"densita_max_per_1000px": 0.6, "foto_in_pagina": 14, "mai_foto_muta": True,
               "mai_due_di_fila": True, "originali_mai_in_public": True, "contrasto_riga_min": 7.0},
    "trattamenti": {
        "B": "saturate(.78) contrast(1.08) brightness(.9) + vignetta + grana 1.1 overlay .55 + riga su banda scura .86",
        "C": "duotone ink->orange, solo N6",
        "D": "grigio, opacity .16, contrast 1.3, sotto al testo",
    },
    "immagini": rows + extra,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=1)
print(OUT, "|", len(rows), "righe +", len(extra),
      "| in pagina:", sum(1 for r in rows if r["posto"]),
      "| riserva:", sum(1 for r in rows if r["ruolo"] == "riserva"),
      "| scartate:", sum(1 for r in rows if r["ruolo"] == "scartata"))
