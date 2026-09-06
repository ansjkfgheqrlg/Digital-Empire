# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L04.

«Editing Video Automatico con AI All in One» · 30:34 · strumento mostrato: **Fliki**
(la trascrizione automatica lo storpia in «flichi», «fligui»; verificato a schermo, frame-050:
la home col claim «Turn text into videos with AI voices»).

E' la prima lezione del corso che insegna LO STRUMENTO CHE USIAMO IN PRODUZIONE. Non ci ha dato
tecniche nuove — su movimento delle scene e sottotitoli siamo gia' oltre cio' che consiglia — ci
ha dato il catalogo completo delle leve di Fliki. Con quel catalogo in mano si vede che
`video-producer.md`, `fliki-produzione.md` e `fliki-avanzato.md` descrivono un montaggio A MANO
nell'interfaccia, mentre la fabbrica genera via API da mesi: quattro ordini dell'agente su sei
sono ineseguibili, e un gate BLOCCANTE (`qa-audio-video`) verifica il volume di una musica che
nel nostro payload non esiste.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L04"
LEZIONE = "Editing Video Automatico con AI All in One"

REGOLE = [
    {
        "id": "A4-L04-01",
        "tipo": "procedura",
        "regola": ("video-producer descrive cio' che la catena fa DAVVERO: produce la spec del "
                   "payload API di Fliki, non le istruzioni per un umano che monta a mano. Un "
                   "agente che ordina operazioni impossibili non e' severo, e' rumore, e insegna "
                   "a ignorarlo."),
        "prova": "frame-224.png @ 18:35 (barra Export/Video settings/Convert/More) + parlato @ 14:24",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-producer.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("video-producer non contiene piu' 'lo fa l'utente in Fliki', 'non chiudere il "
                   "browser' ne' 'anteprima obbligatoria', e nomina i campi reali del payload "
                   "(aspectRatio, visuals, sceneBreakdown, subtitlePresetId, aiVideoModel); oggi "
                   "video-producer.md:20 dichiara che il video lo monta l'utente"),
    },
    {
        "id": "A4-L04-02",
        "tipo": "parametro",
        "regola": ("Il formato del video e' una decisione di destinazione dichiarata per canale "
                   "(landscape YouTube, portrait Shorts/TikTok, square social), non una costante "
                   "scritta a mano nel payload. Finche' e' una costante, la fabbrica non puo' "
                   "produrre Shorts e nessun documento lo dice."),
        "prova": "frame-155.png @ 12:50 (tendina Size: Portrait/Square/Landscape con i social scritti accanto)",
        "fonte": "schermo",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py",
        "azione": "modifica",
        "binario": "B",
        "rischio": "alto",
        "misura": ("aspectRatio arriva da CANALI[canale] o dalla riga di comando con i tre valori "
                   "ammessi e default 16:9 invariato; oggi e' la stringa fissa '16:9' a "
                   "fliki_client.py:258"),
    },
    {
        "id": "A4-L04-03",
        "tipo": "procedura",
        "regola": ("Ogni scheda su Fliki dichiara cosa e' raggiungibile via API e cosa vive solo "
                   "nell'interfaccia. Musica di sottofondo, mappa delle pronunce, pause, "
                   "velocita' e anteprima stanno nell'interfaccia: la nostra catena non le tocca, "
                   "e prescriverle come operazioni nostre e' una bugia scritta in una checklist."),
        "prova": "frame-278.png @ 23:05 (Background music) + frame-224.png @ 18:35 (Pronunciation map nel menu More)",
        "fonte": "schermo",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-produzione.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("fliki-produzione.md e fliki-avanzato.md hanno entrambe una sezione che separa "
                   "cio' che la catena imposta via API da cio' che resta manuale; oggi descrivono "
                   "solo clic nell'interfaccia (registrazione via email, 'non chiudere il "
                   "browser', volume musica 10-15%)"),
    },
    {
        "id": "A4-L04-04",
        "tipo": "vincolo",
        "regola": ("Un gate BLOCCANTE controlla solo cio' che esiste. Il criterio sul volume "
                   "della musica resta sospeso, e dichiarato tale, finche' non e' accertato "
                   "ascoltando un MP4 gia' prodotto se i nostri video contengono musica: un "
                   "criterio che non puo' fallire mai non e' un controllo, e' una formula."),
        "prova": "frame-278.png @ 23:05 (il pannello musica esiste in Fliki, col volume e l'abbassamento automatico) + parlato @ 22:41",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("qa-audio-video segna il criterio musica come DA ACCERTARE con la verifica "
                   "assegnata al gate A4; oggi (qa-audio-video.md:21 e :35) boccia il video per "
                   "'volume della musica troppo alto' mentre il payload non ha alcun campo musica "
                   "(cercati backgroundMusic/musicId/audioTrack in 02-AUTOMAZIONI-E-SCRIPTS: zero "
                   "occorrenze)"),
    },
    {
        "id": "A4-L04-05",
        "tipo": "euristica",
        "regola": ("Le scene si muovono sempre: clip AI al 100% con animazione sulle immagini "
                   "residue. La lezione consiglia di lasciare acceso il Ken Burns 'perche' sembra "
                   "un video e non un'immagine'; noi facciamo un passo oltre, e tornare alle "
                   "immagini ferme e' una regressione, non una semplificazione."),
        "prova": "frame-297.png @ 24:40 (caselle 'Enable Ken Burns effect between sections' e 'Enable zoom effect for images') + parlato @ 25:29",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-producer.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "basso",
        "misura": ("video-producer scrive perche' le scene devono muoversi e cita "
                   "aiVideoClipPercentage=100 + imageAnimationPreset='Mix'; oggi la ragione vive "
                   "solo in un commento di fliki_client.py (riga 172-180, nata dal video v10 "
                   "uscito tutto fermo)"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale."""
    import os

    def leggi(percorso_relativo):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return None
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read().lower()

    def contiene(percorso_relativo, aghi):
        testo = leggi(percorso_relativo)
        if testo is None:
            return False
        return all(a.lower() in testo for a in aghi)

    def non_contiene(percorso_relativo, aghi):
        testo = leggi(percorso_relativo)
        if testo is None:
            return False
        return not any(a.lower() in testo for a in aghi)

    VP = "03-AGENTI-E-RUOLI/operatori/video-producer.md"
    esiti = {}
    # -01: l'agente non descrive piu' il montaggio a mano E nomina i campi veri del payload.
    esiti["A4-L04-01"] = (
        non_contiene(VP, ["lo fa l'utente in fliki", "non chiudere il browser"])
        and contiene(VP, ["aspectratio", "scenebreakdown", "subtitlepresetid"]))
    # -02: binario B — vero solo quando aspectRatio smette di essere una costante.
    # -02: applicata il 2026-09-06 al gate A4. Il controllo cerca la SOSTANZA in entrambi i
    #      posti, non un nome: il canale dichiara il suo formato di destinazione, e il client
    #      lo riceve come parametro con i tre valori ammessi invece della costante scritta a
    #      mano. (Nel codice la chiave del canale si chiama `formato`, in italiano come il
    #      resto di CANALI; il campo del payload resta `aspectRatio`, che e' il nome di Fliki.)
    esiti["A4-L04-02"] = (
        contiene("02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py", ['"formato": "16:9"'])
        and contiene("02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py",
                     ["aspect_ratio", "formati_ammessi", '"aspectratio": aspect_ratio']))
    # -03: entrambe le schede separano API e interfaccia.
    esiti["A4-L04-03"] = (
        contiene("04-SKILLS-E-REFERENCE/references/fliki-produzione.md", ["via api"])
        and contiene("04-SKILLS-E-REFERENCE/references/fliki-avanzato.md", ["via api"]))
    # -04: il criterio musica e' marcato come da accertare, non piu' dato per buono.
    # -04: la verifica e' stata CHIUSA il 2026-09-06 (A4-L20-01): il criterio non e' piu'
    #      "sospeso, da accertare" ma "inapplicabile", perche' i nostri video non hanno
    #      musica. La regola resta soddisfatta — anzi lo e' meglio di prima — quindi il
    #      controllo accetta lo stato di arrivo, non quello di attesa.
    esiti["A4-L04-04"] = contiene("03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
                                  ["inapplicabile"])
    # -05: la ragione del movimento vive nell'agente, non solo in un commento del codice.
    esiti["A4-L04-05"] = contiene(VP, ["aivideoclippercentage", "imageanimationpreset"])
    return esiti
