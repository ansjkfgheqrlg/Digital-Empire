# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / A6 YouTube Viral Mastery / L02.

«Creiamo la copertina (metodi + A.I)» · 24:54 · la lezione piu' grande della categoria
(172 scene uniche). Letta col mandato nuovo del 2026-09-10: sei domande, non una.

La scoperta piu' importante di questo giro non e' nel corso: e' nel nostro codice. La Fase 5
di `apex7_orchestrator.py` gia' scarica la copertina REALE del video sorgente
(`_ensure_source_thumbnail`, via `i.ytimg.com/vi/<id>/maxresdefault.jpg` — lo stesso trucco
insegnato dal corso, ma nativo) e gia' prepara un `brief-miniatura.json` con testo diviso in
righe leggibili — deciso in casa il 2026-07-31 ("regola di Gael"), indipendentemente dal corso
e coerente con esso. Ma quel brief viene scritto solo per alimentare `arena_thumbnail.py`
(il generatore automatico, fallito tre volte, oggi disattivato di default): quando
`--con-copertina` non e' passato, `consegna_a_max()` scrive un `copy.md` generico
("16:9, testo oro/ambra") e non legge mai `brief-miniatura.json`. Il lavoro buono c'e' gia',
non arriva a chi deve usarlo.

Nessuna regola qui automatizza la resa finale della copertina: la fa sempre Max, a mano
(regola permanente, 2026-08-29/09-04). Tutte preparano solo il materiale che gli arriva.
"""

FONTE = "AI TUBE PRO / A6 YouTube Viral Mastery / L02"
LEZIONE = "Creiamo la copertina (metodi + A.I)"

REGOLE = [
    {
        "id": "A6-L02-01",
        "tipo": "procedura",
        "regola": ("Il font del testo in copertina deve essere UNO SOLO per canale, scelto una "
                   "volta e riusato sempre — mai lasciato alla scelta libera di ogni singola "
                   "copertina. Coerenza di brand, non gusto del momento."),
        "prova": "A6/L02/appunti.md @ 09:58-10:20 «un'altra cosa che dobbiamo fare e' selezionare un font e lasciare sempre lo stesso» — frame-333.png @ 11:04 mostra il pannello font aperto sulla scelta 'Anton'",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/scelta-strumenti.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": "scelta-strumenti.md elenca un font fisso per canale (uno per Legami d'Amore, uno per Dose Mentale); ogni copertina consegnata da Max nell'ultimo mese usa lo stesso font per canale",
    },
    {
        "id": "A6-L02-02",
        "tipo": "parametro",
        "regola": ("La soglia di leggibilita' (luminosita' 40-220, contrasto >=30, gia' scritta "
                   "in thumbnail_analyzer.py) va documentata come standard atteso per OGNI "
                   "copertina, non lasciata solo dentro il codice di un file che oggi nessuno "
                   "chiama: e' la versione numerica dello stesso principio che il corso mostra "
                   "col contorno nero sul testo."),
        "prova": "A6/L02/appunti.md @ 10:58-11:27 «cliccate su effetti [...] contorno [...] ecco qui che gia' cosi' va bene» — frame-341.png @ 11:20 mostra il pannello Effetti aperto sul testo",
        "fonte": "entrambi",
        "tocca": "04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": "youtube-pubblicazione.md riporta le due soglie numeriche come standard di accettazione copertina, citando thumbnail_analyzer.py come fonte",
    },
    {
        "id": "A6-L02-03",
        "tipo": "flusso",
        "regola": ("Il flusso di consegna a Max deve ridisegnarsi per NON ignorare "
                   "`brief-miniatura.json` quando esiste. Oggi la Fase 5 dell'orchestratore lo "
                   "scrive sempre (contiene la copertina reale del competitor gia' scaricata e "
                   "il testo gia' spezzato in righe leggibili), ma `consegna_a_max()` scrive un "
                   "brief hard-coded e generico senza mai leggerlo: il lavoro fatto dalla "
                   "macchina un minuto prima nella stessa run non arriva a chi deve usarlo."),
        "prova": ("A6/L02/report.md §2 — apex7_orchestrator.py:1364 (_ensure_source_thumbnail) "
                  "e :1443-1460 (run_phase_5, scrittura brief-miniatura.json) confrontati con "
                  "produci_video_completo.py:293-366 (consegna_a_max, mai legge quel file). "
                  "Riverificato leggendo il codice il 2026-09-10, non dedotto dai nomi dei file"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "medio",
        "misura": ("un video consegnato a Max con brief-miniatura.json presente su disco porta "
                   "in copy.md il riferimento reale (source_thumbnail) e le righe di testo gia' "
                   "pronte; un video senza quel file consegna il brief generico come oggi, "
                   "nessuna regressione"),
    },
    {
        "id": "A6-L02-04",
        "tipo": "funzione",
        "regola": ("`consegna_a_max()` va riscritta per leggere "
                   "`05-TEMPLATES-E-KIT/brief-miniatura.json` (se presente) e aggiungere al "
                   "blocco 'Copertina' di copy.md: il percorso dell'immagine di riferimento "
                   "reale scaricata (source_thumbnail), le righe di testo gia' spezzate "
                   "(text_overlay_lines) e la fonte (source_style) — arricchendo il brief "
                   "attuale, non sostituendolo. L'immagine di riferimento va aperta insieme "
                   "alla cartella (stesso pattern gia' usato con subprocess.Popen(['explorer', "
                   "dest]))."),
        "prova": ("A6/L02/appunti.md @ 03:18-03:31 «con due clic ho la copertina» (il valore di "
                  "partire da un riferimento reale, non da un canvas bianco) — confrontato con "
                  "produci_video_completo.py righe 335-339, il brief oggi consegnato a Max "
                  "(solo formato/colore generici, nessuna immagine)"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py",
        "azione": "ridisegna",
        "binario": "B",
        "rischio": "medio",
        "misura": ("grep su consegna_a_max() trova una lettura di brief-miniatura.json; il "
                   "copy.md di un video con brief presente riporta un percorso immagine reale "
                   "verificabile su disco, non solo testo generico"),
    },
    {
        "id": "A6-L02-05",
        "tipo": "funzione",
        "regola": ("`thumbnail_analyzer.py` (luminosita'/contrasto/leggibilita' via PIL, 92 "
                   "righe, gia' scritto) va richiamato DAVVERO in un punto della catena — "
                   "candidato naturale: dentro youtube_uploader_playwright.py, appena prima di "
                   "caricare il file passato a --thumbnail. Se fuori soglia, stampa un avviso a "
                   "Max (non blocca l'upload: la macchina misura, Max decide). Oggi il file "
                   "esiste, il criterio e' scritto, thumbnail-designer.md lo cita nel proprio "
                   "playbook (punto 7) come gia' collegato — ma verificato con grep su tutta "
                   "02-AUTOMAZIONI-E-SCRIPTS/: ZERO chiamate reali in tutta la fabbrica."),
        "prova": ("thumbnail-designer.md:37 lo da' per collegato ('Esegui thumbnail_analyzer.py "
                  "--image <miniatura>'), ma grep -rn thumbnail_analyzer "
                  "02-AUTOMAZIONI-E-SCRIPTS/*.py: 0 invocanti reali, solo la definizione in "
                  "thumbnail_analyzer.py stesso. Riverificato 2026-09-10, ore 18:40"),
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "basso",
        "misura": ("grep su youtube_uploader_playwright.py trova una chiamata reale a "
                   "thumbnail_analyzer.analyze_real(); un upload con copertina fuori soglia "
                   "(luminosita' <40 o >220, contrasto <30) stampa l'avviso in console prima di "
                   "procedere"),
    },
]
