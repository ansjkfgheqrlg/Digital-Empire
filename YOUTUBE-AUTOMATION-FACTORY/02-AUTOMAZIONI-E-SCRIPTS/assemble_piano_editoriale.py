#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_piano_editoriale.py — Assembla il piano editoriale 70 video / 30 giorni / 3 strategie
per @Legamidiamore, unendo dati REALI (memory/_selected_70_v2.json, derivato dal pool di
build_candidate_pool.py) con il copy adattato (scritto qui, non generato/inventato a caso: ogni
titolo/hook/caption e' una riscrittura del titolo originale reale, non una copia letterale).

Verifica di integrita' bloccante: ogni videoId nel copy DEVE avere una corrispondenza esatta
nella selezione reale — se manca anche uno solo, lo script si ferma (nessuna riga "orfana").

Output:
  memory/piano_editoriale_70.json
  memory/piano_editoriale_70.csv
  01-FLUSSI-E-PIANI/CALENDARIO-70-LEGAMIDIAMORE.md
"""
import csv
import json
import os
from datetime import date, timedelta

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SELEZIONE_PATH = os.path.join(FACTORY_DIR, "memory", "_selected_70_v2.json")
OUT_JSON = os.path.join(FACTORY_DIR, "memory", "piano_editoriale_70.json")
OUT_CSV = os.path.join(FACTORY_DIR, "memory", "piano_editoriale_70.csv")
OUT_MD = os.path.join(FACTORY_DIR, "01-FLUSSI-E-PIANI", "CALENDARIO-70-LEGAMIDIAMORE.md")

STRATEGIE = {
    "A": {
        "nome": "Segnali & Decodifica",
        "canale_sorgente": "PsicologiaFemminile-f8c",
        "target": "Uomini che vogliono capire i segnali (verbali e corporei) che una donna manda "
                  "senza dirli apertamente.",
        "formato": "Lista numerata, 45-90s, voce femminile calma, ritmo alto (1 segnale ogni 8-10s).",
        "frequenza": "~28 video/30gg (volume piu' alto: fonte con 100 candidati reali, il pool piu' ampio).",
        "kpi": "vph medio riga >= mediana del pool A alla generazione (5.1 vph); baseline MIN_VPH=20 di "
               "cashcow_check.py non raggiunta da nessun video reale in questa nicchia oggi, quindi non "
               "usata come soglia assoluta (vedi nota in candidate_pool).",
        "volume": 28,
    },
    "B": {
        "nome": "Tecnica & Comando",
        "canale_sorgente": "PsicologiadellAttrazionee",
        "target": "Uomini che vogliono applicare attivamente una tecnica per aumentare la propria "
                  "attrattivita', non solo riconoscere segnali passivi.",
        "formato": "How-to imperativo, 45-90s, voce femminile diretta, tono da coach.",
        "frequenza": "~14 video/30gg (volume basso DELIBERATAMENTE: il canale reale ha solo 23 "
                     "candidati validi oggi, si usa il 61% del pool per lasciare margine).",
        "kpi": "vph medio riga >= mediana del pool B alla generazione (0.46 vph, pool piu' piccolo e "
               "piu' lento del pool A/C — atteso, non un errore).",
        "volume": 14,
    },
    "C": {
        "nome": "Allarme & Verita' Sociale",
        "canale_sorgente": "DinamicheSocialiAcademy",
        "target": "Uomini disillusi dal dating moderno, in cerca di una spiegazione 'perche' non "
                  "funziona' piu' che di una tecnica.",
        "formato": "Narrativa 'verita' scomoda', 45-90s, tono piu' serio/rivelatorio.",
        "frequenza": "~28 video/30gg. Tono verificato il 2026-08-26 (fresh scrape): critica sociale "
                     "sulla crisi relazionale maschile, NON dark psychology manipolativa come temuto "
                     "nel calendario precedente (CALENDARIO-LEGAMIDIAMORE.md, 05/08) — confermato con "
                     "Max prima di assegnare volume.",
        "kpi": "vph medio riga >= mediana del pool C alla generazione (0.16 vph).",
        "volume": 28,
    },
}

# Copy adattato per ogni videoId reale selezionato. Ogni entry e' una riscrittura del titolo
# originale (vedi 'titolo_originale' nella selezione), mai una copia letterale.
CREATIVO = {
    # ---------------- STRATEGIA A — Segnali & Decodifica ----------------
    "8_RZCbkuIQk": dict(
        titolo="7 Tocchi Che Fanno Innamorare Una Donna Di Te (Funzionano Davvero)",
        hook="Esistono 7 punti del corpo che, se tocchi nel modo giusto, cambiano tutto.",
        caption="Non e' magia, e' psicologia del contatto: 7 tocchi che una donna sente e ricorda. "
                "Guarda fino alla fine per il numero 7.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "linguaggiodelcorpo", "attrazione", "legamidiamore"],
    ),
    "CxdlEsEnZ9g": dict(
        titolo="7 Cose Che Una Donna Dice Solo Quando Sta Iniziando Ad Innamorarsi Di Te",
        hook="Se sente qualcosa per te, lo dice senza accorgersene — in 7 modi precisi.",
        caption="Le parole tradiscono i sentimenti prima dei gesti. Ecco le 7 frasi che segnalano "
                "che sta iniziando a innamorarsi.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "linguaggioverbale", "attrazione", "legamidiamore"],
    ),
    "qHB80wbamBI": dict(
        titolo="4 Segnali Che Lei Ti Desidera In Segreto (E Che Quasi Nessun Uomo Nota)",
        hook="Lei non te lo dira' mai a parole — ma il corpo parla comunque.",
        caption="4 segnali sottili di desiderio che passano inosservati. Riconoscerli prima che sia "
                "troppo tardi.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "desiderio", "attrazione", "legamidiamore"],
    ),
    "XABjAjqfUxw": dict(
        titolo="Il Trucco Psicologico Che Rende Un Uomo Irresistibile Fin Dal Primo Sguardo",
        hook="C'e' un dettaglio che decide l'attrazione nei primi 5 secondi.",
        caption="Non e' l'aspetto fisico: e' un trucco psicologico preciso che puoi applicare da stasera.",
        hashtag=["relazioni", "psicologia", "attrazione", "primaimpressione", "legamidiamore", "psicologiadellamore"],
    ),
    "AXvmuRR4cdY": dict(
        titolo="Perche' Una Donna Torna Da Te Dopo Averti Rifiutato (La Psicologia Dietro)",
        hook="Ti ha rifiutato... eppure torna. Ecco perche' succede davvero.",
        caption="Il rifiuto non e' sempre la fine: la psicologia spiega perche' lei puo' tornare, e quando.",
        hashtag=["relazioni", "psicologia", "rifiuto", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "kY02KtQfyX0": dict(
        titolo="6 Segnali Nascosti Che Una Donna Ti Desidera (Anche Se Non Lo Ammettera' Mai)",
        hook="Non lo dira' mai a voce alta — ma questi 6 segnali la tradiscono.",
        caption="6 segnali nascosti di desiderio femminile che sfuggono alla maggior parte degli uomini.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "desiderio", "attrazione", "legamidiamore"],
    ),
    "IkEmUmnSPI4": dict(
        titolo="Il Trucco Dell'Attrazione Istantanea Che Pochi Uomini Conoscono",
        hook="L'attrazione istantanea non e' fortuna: e' un meccanismo psicologico preciso.",
        caption="Ecco il trucco che genera attrazione istantanea — spiegato passo dopo passo.",
        hashtag=["relazioni", "psicologia", "attrazione", "legamidiamore", "psicologiadellamore", "segnalidilei"],
    ),
    "VejNn26Ndlg": dict(
        titolo="Cosa Succede Nella Mente Di Una Donna Quando Inizia A Sentire La Tua Mancanza",
        hook="C'e' un momento preciso in cui inizia a mancarle — ecco quando.",
        caption="La psicologia dietro il momento esatto in cui una donna inizia a sentire la tua mancanza.",
        hashtag=["relazioni", "psicologia", "mancanza", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "chVKOBlEpDI": dict(
        titolo="Pensi Che Non Sia Interessata? Guarda Questi Segnali Prima Di Arrenderti",
        hook="Prima di pensare che non le interessi, guarda questo.",
        caption="A volte il disinteresse e' solo apparenza. Questi segnali dicono la verita'.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "dubbio", "attrazione", "legamidiamore"],
    ),
    "9UND8IgmOME": dict(
        titolo="Perche' Il 'No Contact' Le Fa Piu' Male Del Tuo Silenzio (Verita' Psicologica)",
        hook="Il silenzio non e' la parte piu' dolorosa — e' quello che viene dopo.",
        caption="La psicologia del no-contact spiegata: perche' fa piu' male di quanto pensi.",
        hashtag=["relazioni", "psicologia", "nocontact", "legamidiamore", "psicologiadellamore", "rottura"],
    ),
    "XHveMwvoB2M": dict(
        titolo="3 Segnali Chiari Che Una Donna Desidera L'Intimita' (Anche Se Non Lo Dice)",
        hook="3 segnali chiari, quasi impossibili da nascondere.",
        caption="Il desiderio di intimita' si manifesta in modi precisi. Ecco i 3 segnali da riconoscere.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "intimita", "attrazione", "legamidiamore"],
    ),
    "VB9Dkd5w1MM": dict(
        titolo="L'Unica Cosa A Cui Una Donna Resta Davvero Fedele (Non E' Quello Che Pensi)",
        hook="Non e' quello che fai per lei. E' qualcos'altro.",
        caption="La fedelta' femminile ha una sola vera radice psicologica — e non e' quella che pensi.",
        hashtag=["relazioni", "psicologia", "fedelta", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "OhbmC_CXL3w": dict(
        titolo="Cosa Significa Davvero Se Una Donna Ti Mostra Questa Parte Del Corpo",
        hook="C'e' un gesto specifico che rivela molto piu' di quanto sembri.",
        caption="Il linguaggio del corpo non mente: ecco cosa significa davvero questo gesto.",
        hashtag=["relazioni", "psicologia", "linguaggiodelcorpo", "segnalidilei", "attrazione", "legamidiamore"],
    ),
    "DktUP9rCN0E": dict(
        titolo="7 Punti Del Corpo Che Le Donne Vogliono Che Tu Tocchi (E Che Ignori)",
        hook="Ci sono 7 punti che la maggior parte degli uomini trascura completamente.",
        caption="7 punti del corpo spesso ignorati, ma decisivi per lei. Guarda fino alla fine.",
        hashtag=["relazioni", "psicologia", "linguaggiodelcorpo", "contatto", "attrazione", "legamidiamore"],
    ),
    "PyUrlzY5xSU": dict(
        titolo="3 Segnali Che Una Donna Rivela Sempre Quando Ti Desidera Davvero",
        hook="Ci sono 3 segnali che rivela sempre, senza eccezioni.",
        caption="Quando il desiderio e' reale, il corpo lo rivela sempre. Ecco i 3 segnali costanti.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "desiderio", "attrazione", "legamidiamore"],
    ),
    "VbVpAli50HU": dict(
        titolo="La Cosa Che, Una Volta Capita, Cambia Per Sempre Il Modo In Cui Corteggi",
        hook="C'e' una cosa che, capita una volta, cambia tutto negli appuntamenti.",
        caption="Un solo concetto psicologico che, capito bene, trasforma ogni primo appuntamento.",
        hashtag=["relazioni", "psicologia", "appuntamenti", "attrazione", "legamidiamore", "psicologiadellamore"],
    ),
    "XuYWVuIRIWM": dict(
        titolo="Come Far Nascere Attrazione In Un'Amica In Pochi Minuti (Psicologia, Non Trucchi)",
        hook="In pochi minuti puoi cambiare il modo in cui ti vede.",
        caption="Passare dalla friendzone all'attrazione e' questione di psicologia, non di fortuna.",
        hashtag=["relazioni", "psicologia", "friendzone", "attrazione", "legamidiamore", "psicologiadellamore"],
    ),
    "n2lhUxDWY0Q": dict(
        titolo="7 Segnali Comportamentali A Cui Prestare Attenzione Dopo Una Lunga Assenza",
        hook="Il comportamento cambia sempre piu' delle parole — ecco cosa notare.",
        caption="Non serve indagare: il comportamento rivela piu' di ogni parola. 7 segnali da "
                "osservare con calma.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "comportamento", "legamidiamore", "psicologiadellamore"],
    ),
    "AzJuqmi7_sY": dict(
        titolo="Come Comportarti (Con Dignita') Con Una Donna Che Ti Ha Ferito",
        hook="Non serve vendicarsi. Serve una strategia migliore.",
        caption="La calma stoica come arma psicologica dopo una ferita d'amore. Ecco come applicarla.",
        hashtag=["relazioni", "psicologia", "stoicismo", "resilienza", "legamidiamore", "crescitapersonale"],
    ),
    "wRepp7aPTcU": dict(
        titolo="Il Punto Esatto Da Baciare Che Accende L'Attrazione (Spiegazione Psicologica)",
        hook="Non tutti i baci sono uguali — la posizione conta piu' di quanto pensi.",
        caption="La psicologia del bacio: un punto preciso che intensifica l'attrazione reciproca.",
        hashtag=["relazioni", "psicologia", "attrazione", "baci", "legamidiamore", "psicologiadellamore"],
    ),
    "FWFGk9fthJ0": dict(
        titolo="7 Abitudini Che Rendono Un Uomo Meno Attraente (Anche Se Non Se Ne Accorge)",
        hook="Ci sono abitudini che tolgono attrazione senza che tu te ne accorga.",
        caption="7 abitudini comuni che spengono l'attrazione — riconoscile prima che sia tardi.",
        hashtag=["relazioni", "psicologia", "attrazione", "abitudini", "legamidiamore", "psicologiadellamore"],
    ),
    "2q8baJHw53M": dict(
        titolo="6 Segnali Che Una Donna Ti Trova Attraente (Anche Se Non Lo Dira' Mai)",
        hook="Non lo dira' mai a voce, ma questi 6 segnali parlano chiaro.",
        caption="L'attrazione femminile si nasconde in gesti piccoli. Ecco i 6 segnali da notare.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "attrazione", "legamidiamore", "psicologiadellamore"],
    ),
    "WCW_GzBEdmE": dict(
        titolo="Una Storia Vera Che Spiega Meglio Di Mille Consigli Cosa Vuole Davvero Una Donna",
        hook="A volte una storia vera insegna piu' di dieci consigli.",
        caption="Una storia vera sul gesto che fa davvero la differenza in una relazione.",
        hashtag=["relazioni", "psicologia", "storievere", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "K_Xvm5xtH5o": dict(
        titolo="Fredda In Apparenza, Ma Questi Segnali Dicono Che In Realta' Pensa Solo A Te",
        hook="La freddezza puo' essere una maschera — questi segnali lo dimostrano.",
        caption="Comportamento freddo non sempre significa disinteresse. Ecco i segnali contraddittori "
                "da leggere.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "contraddizione", "attrazione", "legamidiamore"],
    ),
    "IhCMUfkD_oM": dict(
        titolo="8 Frasi Che Colpiscono Una Donna Molto Piu' Di 'Sei Bellissima'",
        hook="Smetti di dirle che e' bella. Dille questo invece.",
        caption="8 frasi alternative, psicologicamente piu' efficaci del solito complimento sull'aspetto.",
        hashtag=["relazioni", "psicologia", "complimenti", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "cDsuI-bnIAc": dict(
        titolo="10 Cose Che Non Dovresti Mai Fare Per Una Donna (Anche Se Sembrano Romantiche)",
        hook="Alcune cose che fai per amore, in realta', allontanano.",
        caption="10 comportamenti apparentemente romantici che in psicologia fanno l'effetto opposto.",
        hashtag=["relazioni", "psicologia", "erroricomuni", "legamidiamore", "psicologiadellamore", "attrazione"],
    ),
    "1OPc6tk27_Q": dict(
        titolo="4 Segnali Silenziosi Che Rivelano Il Desiderio Di Una Donna (Solo Corpo, Zero Parole)",
        hook="Il corpo comunica desiderio anche quando le parole tacciono.",
        caption="4 segnali di solo linguaggio del corpo — nessuna parola, solo psicologia non verbale.",
        hashtag=["relazioni", "psicologia", "linguaggiodelcorpo", "desiderio", "legamidiamore", "attrazione"],
    ),
    "IWVC1FtczxU": dict(
        titolo="Se Ti Nasconde Qualcosa, Questi Cambiamenti Comportamentali Emergono Per Primi",
        hook="Quando si nasconde qualcosa, il comportamento cambia prima delle parole.",
        caption="I primi segnali comportamentali che emergono quando c'e' qualcosa di non detto.",
        hashtag=["relazioni", "psicologia", "comportamento", "segnalidilei", "legamidiamore", "psicologiadellamore"],
    ),
    # ---------------- STRATEGIA B — Tecnica & Comando ----------------
    "V8m6irmPZmM": dict(
        titolo="7 Segnali Che Dimostrano Che Sei Gia' Un Uomo Attraente (Anche Se Non Lo Sai)",
        hook="Forse sei gia' attraente e non te ne sei accorto. Ecco 7 prove.",
        caption="L'attrattivita' maschile ha segnali precisi — controlla quanti ne riconosci in te.",
        hashtag=["relazioni", "psicologia", "attrazione", "uomoattraente", "legamidiamore", "crescitapersonale"],
    ),
    "l6iiReMUTC4": dict(
        titolo="6 Abilita' Sociali Che Ti Rendono Molto Piu' Attraente (Si Allenano)",
        hook="L'attrazione si allena: ecco 6 abilita' sociali concrete.",
        caption="6 abilita' sociali allenabili che aumentano la tua attrattivita', spiegate passo per passo.",
        hashtag=["relazioni", "psicologia", "abilitasociali", "attrazione", "legamidiamore", "crescitapersonale"],
    ),
    "1nDqK1FUJgs": dict(
        titolo="Quando Lei Fa Questo, L'Attrazione E' Gia' Scattata (Anche Se Non Lo Ammette)",
        hook="C'e' un gesto che rivela l'attrazione prima ancora che lei se ne accorga.",
        caption="Un gesto specifico che tradisce l'attrazione — e che lei non ammettera' mai a parole.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "attrazione", "legamidiamore", "tecnica"],
    ),
    "8kQdIfI4MEc": dict(
        titolo="Come Restare Nei Suoi Pensieri Senza Scriverle Nemmeno Un Messaggio",
        hook="Non serve scrivere per restare nella sua testa. Serve fare questo.",
        caption="La tecnica psicologica per restare presente nei suoi pensieri, senza inviare un solo "
                "messaggio.",
        hashtag=["relazioni", "psicologia", "tecnica", "attrazione", "legamidiamore", "psicologiadellamore"],
    ),
    "If2X61nvDpI": dict(
        titolo="7 Segnali Che Lei E' Gia' Attratta Da Te (Prima Che Lo Dica A Parole)",
        hook="L'attrazione arriva prima delle parole — ecco 7 modi per riconoscerla.",
        caption="7 segnali concreti che l'attrazione e' gia' scattata, anche se lei non lo dira'.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "attrazione", "legamidiamore", "tecnica"],
    ),
    "KmMx0CpFy5Y": dict(
        titolo="Attratta Da Te, Ma Sta Per Perdere Interesse: 7 Segnali Da Non Ignorare",
        hook="L'attrazione c'e' ancora, ma sta per svanire — questi 7 segnali te lo dicono.",
        caption="7 segnali che indicano che l'interesse sta calando, in tempo per intervenire.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "interesse", "legamidiamore", "tecnica"],
    ),
    "5Dq7kG9ORFk": dict(
        titolo="Cosa Crea Un Legame Emotivo Forte Senza Bisogno Di Un Solo Contatto Fisico",
        hook="Il legame piu' forte non nasce dal contatto fisico. Nasce da questo.",
        caption="La tecnica psicologica che crea connessione emotiva profonda, senza toccarla nemmeno "
                "una volta.",
        hashtag=["relazioni", "psicologia", "connessioneemotiva", "tecnica", "legamidiamore", "attrazione"],
    ),
    "7nxChZi90IA": dict(
        titolo="Cosa Rende Davvero Un Uomo Attraente (Non E' Quello Che Pensi)",
        hook="Non e' l'aspetto. Ecco cosa rende davvero un uomo attraente.",
        caption="Il vero motore dell'attrattivita' maschile, spiegato con la psicologia, non con i miti.",
        hashtag=["relazioni", "psicologia", "uomoattraente", "attrazione", "legamidiamore", "crescitapersonale"],
    ),
    "TX42B5ersPw": dict(
        titolo="Pensavo Di Non Essere Attraente, Finche' Non Ho Notato Queste 7 Cose",
        hook="Pensavo di non essere attraente. Poi ho notato 7 cose.",
        caption="Una storia in prima persona su come cambia la percezione di se' notando questi 7 segnali.",
        hashtag=["relazioni", "psicologia", "autostima", "attrazione", "legamidiamore", "crescitapersonale"],
    ),
    "JowWCGsgFeI": dict(
        titolo="Come Capire Se E' Davvero Attratta Da Te (I Segnali Che Non Mentono Mai)",
        hook="Ci sono segnali che il corpo non riesce a nascondere. Mai.",
        caption="I segnali di attrazione che non mentono mai, anche quando le parole dicono altro.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "attrazione", "legamidiamore", "tecnica"],
    ),
    "RliwdVK63TQ": dict(
        titolo="Come Far Cambiare Idea A Una Donna Che All'Inizio Non Era Interessata",
        hook="Il primo 'no' non e' sempre definitivo. Ecco come cambia una prima impressione.",
        caption="La psicologia di come cambia una prima impressione, spiegata passo per passo.",
        hashtag=["relazioni", "psicologia", "primaimpressione", "tecnica", "legamidiamore", "attrazione"],
    ),
    "QrYtxeuxZwk": dict(
        titolo="5 Principi Psicologici Che Aumentano Davvero Il Tuo Fascino",
        hook="5 principi psicologici, non trucchi da manuale — ecco quali sono.",
        caption="5 principi di psicologia dell'attrazione applicabili da subito, spiegati uno per uno.",
        hashtag=["relazioni", "psicologia", "fascino", "tecnica", "legamidiamore", "attrazione"],
    ),
    "AeR7lnC8WA4": dict(
        titolo="7 Errori Che Uccidono L'Attrazione Senza Che Tu Te Ne Accorga",
        hook="Forse stai spegnendo l'attrazione senza saperlo. Ecco 7 errori comuni.",
        caption="7 errori comuni che eliminano l'attrazione — riconoscerli e' il primo passo per smettere.",
        hashtag=["relazioni", "psicologia", "errori", "attrazione", "legamidiamore", "tecnica"],
    ),
    "BRMzetoc3UE": dict(
        titolo="7 Segnali Che Ti Scrive Per Gelosia (Anche Se Dira' Il Contrario)",
        hook="A volte scrive per un motivo che non ammettera' mai: la gelosia.",
        caption="7 segnali che rivelano quando un messaggio nasconde gelosia, non semplice curiosita'.",
        hashtag=["relazioni", "psicologia", "gelosia", "segnalidilei", "legamidiamore", "attrazione"],
    ),
    # ---------------- STRATEGIA C — Allarme & Verita' Sociale ----------------
    "TcKrM6hOctg": dict(
        titolo="Perche' Sempre Piu' Uomini Scompaiono Dal Mercato Degli Appuntamenti (La Verita')",
        hook="Gli uomini non stanno sparendo per caso. C'e' una ragione precisa.",
        caption="La verita' scomoda su perche' sempre piu' uomini si ritirano dagli appuntamenti.",
        hashtag=["relazioni", "psicologia", "veritascomoda", "uomini", "legamidiamore", "societa"],
    ),
    "CzQ9UWUWp3c": dict(
        titolo="Perche' Dopo I 30 Anni Molti Uomini Diventano 'Invisibili' Nel Dating",
        hook="Dopo i 30, qualcosa cambia davvero nel modo in cui vieni notato.",
        caption="La verita' su perche' tanti uomini oltre i 30 anni si sentono invisibili — e cosa fare.",
        hashtag=["relazioni", "psicologia", "uomini", "veritascomoda", "legamidiamore", "societa"],
    ),
    "iCaIzO1VB-I": dict(
        titolo="Il Falso Mito Sulla Solitudine Maschile Che Fa Piu' Danni Della Solitudine Stessa",
        hook="C'e' un mito sulla solitudine maschile che fa piu' male della solitudine stessa.",
        caption="Il mito da sfatare sulla solitudine maschile, e perche' crederci peggiora le cose.",
        hashtag=["relazioni", "psicologia", "solitudine", "uomini", "legamidiamore", "societa"],
    ),
    "RlxkUN3e3pc": dict(
        titolo="Perche' I 'Bravi Ragazzi' Finiscono Per Ritirarsi Dal Gioco (La Verita')",
        hook="I bravi ragazzi non spariscono per caso. Ecco cosa succede davvero.",
        caption="La verita' psicologica dietro il ritiro dei 'bravi ragazzi' dal dating.",
        hashtag=["relazioni", "psicologia", "uomini", "veritascomoda", "legamidiamore", "societa"],
    ),
    "vRHx6bAEHNU": dict(
        titolo="Perche' Sei Single Da Sempre: La Verita' Psicologica Che Ti Blocca",
        hook="Se sei single da sempre, il motivo probabilmente non e' quello che pensi.",
        caption="La vera causa psicologica dietro una lunga serie di 'da solo' — spiegata senza filtri.",
        hashtag=["relazioni", "psicologia", "single", "veritascomoda", "legamidiamore", "crescitapersonale"],
    ),
    "0r_fGgGXspg": dict(
        titolo="5 Segnali Infallibili Di Attrazione Che Continui A Interpretare Male",
        hook="Continui a sbagliare la lettura di questi 5 segnali. Ecco come leggerli davvero.",
        caption="5 segnali infallibili di attrazione, spiegati per smettere di fraintenderli.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "attrazione", "legamidiamore", "veritascomoda"],
    ),
    "Lo9aL7U9F9s": dict(
        titolo="Perche' Nel 2026 Sempre Meno Persone Rispondono Ai Messaggi (La Verita')",
        hook="Non sei tu. E' cambiato il modo in cui le persone rispondono, punto.",
        caption="La verita' sul perche' le risposte ai messaggi sono crollate nel 2026 — e come adattarsi.",
        hashtag=["relazioni", "psicologia", "dating2026", "veritascomoda", "legamidiamore", "societa"],
    ),
    "BZm_ajOnSt0": dict(
        titolo="La Cruda Verita' Sull'Altezza Nel Dating (E Perche' Conta Meno Di Quanto Pensi)",
        hook="L'altezza conta, ma non nel modo in cui pensi che conti.",
        caption="La verita' scomoda sull'altezza nel dating, ridimensionata con dati e psicologia reale.",
        hashtag=["relazioni", "psicologia", "dating", "veritascomoda", "legamidiamore", "societa"],
    ),
    "j3ywIxPFAfo": dict(
        titolo="Come Sapere Se Le Piaci Davvero Senza Fare Il Primo Passo (Segnali Inconsci)",
        hook="Ci sono segnali inconsci che rivelano tutto, prima ancora di parlare.",
        caption="I segnali inconsci che rivelano il suo interesse, senza bisogno di esporti per primo.",
        hashtag=["relazioni", "psicologia", "segnalidilei", "segnaliinconsci", "legamidiamore", "attrazione"],
    ),
    "AiPPUVsy8TY": dict(
        titolo="3 Modi Psicologici Per Capire Se Ti Ama Per Te O Per Altro",
        hook="Ci sono 3 modi per capire cosa cerca davvero in te.",
        caption="3 test psicologici, non accusatori, per leggere le vere motivazioni in una relazione.",
        hashtag=["relazioni", "psicologia", "veritascomoda", "legamidiamore", "societa", "attrazione"],
    ),
    "wvMbDjmq1Tw": dict(
        titolo="5 Motivi Psicologici Per Cui Tante Donne Sono Infelici In Amore Oggi",
        hook="L'infelicita' in amore oggi ha 5 cause psicologiche precise.",
        caption="5 ragioni psicologiche dietro l'infelicita' amorosa moderna, spiegate senza luoghi comuni.",
        hashtag=["relazioni", "psicologia", "societa", "veritascomoda", "legamidiamore", "psicologiadellamore"],
    ),
    "VQTyQXCR8Y8": dict(
        titolo="Come Riconoscere L'Intimita' Finta E I Segnali Di Manipolazione Emotiva",
        hook="Non tutta l'intimita' e' vera. Ecco come riconoscere quella finta.",
        caption="Come distinguere l'intimita' autentica dalla manipolazione emotiva — segnali da "
                "cui proteggersi.",
        hashtag=["relazioni", "psicologia", "manipolazioneemotiva", "consapevolezza", "legamidiamore", "societa"],
    ),
    "02m975jf_5A": dict(
        titolo="Perche' Il No Contact Funziona Davvero Con Chi Ti Manipola Emotivamente",
        hook="Con chi manipola, il silenzio e' la risposta piu' potente.",
        caption="La psicologia del no-contact come strumento di protezione da dinamiche manipolative.",
        hashtag=["relazioni", "psicologia", "nocontact", "manipolazioneemotiva", "legamidiamore", "consapevolezza"],
    ),
    "eYvgLsc47EM": dict(
        titolo="Il Paradosso Psicologico Per Cui A Volte Allontanarsi Avvicina Davvero",
        hook="A volte avvicinarsi allontana. E allontanarsi, paradossalmente, avvicina.",
        caption="Il paradosso psicologico della distanza in amore, spiegato senza trucchi manipolativi.",
        hashtag=["relazioni", "psicologia", "attrazione", "legamidiamore", "psicologiadellamore", "veritascomoda"],
    ),
    "HmGyw0ZMneM": dict(
        titolo="Il Passato Di Una Persona Conta Davvero In Amore? La Verita' Psicologica",
        hook="Il passato conta, ma non nel modo in cui te lo aspetti.",
        caption="Quanto conta davvero il passato di una persona in una relazione — spiegato con la "
                "psicologia.",
        hashtag=["relazioni", "psicologia", "veritascomoda", "legamidiamore", "societa", "psicologiadellamore"],
    ),
    "XKCVkE49eMU": dict(
        titolo="Come Smettere Di Inseguire E Iniziare Ad Essere Desiderato Davvero",
        hook="Smettere di inseguire non e' arrendersi. E' cambiare strategia.",
        caption="La psicologia di come smettere di inseguire e diventare la persona desiderata.",
        hashtag=["relazioni", "psicologia", "desiderio", "legamidiamore", "psicologiadellamore", "crescitapersonale"],
    ),
    "7OyC5rHdvr8": dict(
        titolo="8 Domande Trappola Nelle Conversazioni (E Come Rispondere Senza Perdere Punti)",
        hook="Alcune domande sono trappole psicologiche. Ecco come non caderci.",
        caption="8 domande trappola comuni nelle conversazioni e come gestirle senza sbagliare.",
        hashtag=["relazioni", "psicologia", "conversazione", "legamidiamore", "attrazione", "tecnica"],
    ),
    "YnV7IFkLuUk": dict(
        titolo="L'Errore Che Distrugge Le Possibilita' Di Molti Uomini Dopo I 40 Anni",
        hook="Dopo i 40, un solo errore puo' rovinare tutto. Ecco quale.",
        caption="L'errore psicologico piu' comune dopo i 40 anni — e come smettere di commetterlo.",
        hashtag=["relazioni", "psicologia", "uomini", "veritascomoda", "legamidiamore", "crescitapersonale"],
    ),
    "ZVbafCxosrU": dict(
        titolo="6 Errori Che Distruggono Il Flirt Prima Ancora Che Inizi",
        hook="Il flirt muore spesso nei primi secondi, per 6 errori precisi.",
        caption="6 errori comuni che uccidono il flirt sul nascere — e come evitarli.",
        hashtag=["relazioni", "psicologia", "flirt", "errori", "legamidiamore", "tecnica"],
    ),
    "RrB8zhxomVc": dict(
        titolo="Relazioni Nel 2026: L'Unica Mossa Vincente E' Smettere Di Giocare",
        hook="Nel 2026 la strategia vincente e' una sola: smettere di giocare.",
        caption="Perche' nel 2026 l'autenticita' batte ogni gioco psicologico nelle relazioni.",
        hashtag=["relazioni", "psicologia", "dating2026", "veritascomoda", "legamidiamore", "societa"],
    ),
    "PcQUfbRDZDQ": dict(
        titolo="Smetti Di Essere Solo Gentile: Il Confine Psicologico Che Ti Fa Rispettare",
        hook="La gentilezza senza confini non genera rispetto. Genera l'opposto.",
        caption="Come porre un confine psicologico chiaro senza smettere di essere una brava persona.",
        hashtag=["relazioni", "psicologia", "rispetto", "confini", "legamidiamore", "crescitapersonale"],
    ),
    "35-dXJiLisw": dict(
        titolo="Perche' Essere Sempre Disponibile Ti Rende Meno Attraente (Non Piu')",
        hook="La disponibilita' totale non attira. Fa l'esatto contrario.",
        caption="La psicologia di perche' la disponibilita' costante riduce, invece di aumentare, "
                "l'attrazione.",
        hashtag=["relazioni", "psicologia", "attrazione", "veritascomoda", "legamidiamore", "crescitapersonale"],
    ),
    "HAnjvUyv-nQ": dict(
        titolo="Perche' Le Relazioni Nel 2026 Sembrano Un Gioco Truccato (E Come Muoversi Davvero)",
        hook="Le regole del dating sono cambiate. Ecco come muoversi davvero oggi.",
        caption="Come muoversi con lucidita' in un contesto di dating che sembra cambiato per sempre.",
        hashtag=["relazioni", "psicologia", "dating2026", "societa", "legamidiamore", "veritascomoda"],
    ),
    "NCWBYUCS2KU": dict(
        titolo="5 Segnali Per Capire Se Sei Solo Un Partner Di Transizione (Non Il Vero Obiettivo)",
        hook="A volte non sei l'obiettivo. Sei la transizione verso qualcun altro.",
        caption="5 segnali psicologici per capire se sei un partner di transizione — e proteggerti.",
        hashtag=["relazioni", "psicologia", "consapevolezza", "legamidiamore", "societa", "veritascomoda"],
    ),
    "QMLgtRlczqY": dict(
        titolo="Perche' Il Silenzio, Usato Bene, Genera Piu' Rispetto Di Mille Parole",
        hook="A volte il silenzio comunica piu' di qualsiasi discorso.",
        caption="La psicologia del silenzio come strumento di rispetto reciproco, non come punizione.",
        hashtag=["relazioni", "psicologia", "rispetto", "legamidiamore", "tecnica", "crescitapersonale"],
    ),
    "PEeGQOAKs7U": dict(
        titolo="'Scelto' O Solo 'Selezionato'? La Differenza Psicologica Che Cambia Tutto",
        hook="C'e' una differenza enorme tra essere scelto ed essere solo selezionato.",
        caption="La differenza psicologica, spesso ignorata, tra essere davvero scelti e solo selezionati.",
        hashtag=["relazioni", "psicologia", "veritascomoda", "legamidiamore", "societa", "crescitapersonale"],
    ),
    "GD2g0extf9w": dict(
        titolo="6 Verita' Sulla Psicologia Femminile Che Evitano Gli Errori Piu' Comuni",
        hook="6 verita' che, se le conosci prima, ti evitano gli errori piu' comuni.",
        caption="6 verita' di base sulla psicologia femminile, spiegate per evitare i fallimenti "
                "piu' frequenti.",
        hashtag=["relazioni", "psicologia", "psicologiafemminile", "legamidiamore", "veritascomoda", "crescitapersonale"],
    ),
    "ByvZnDPxqvI": dict(
        titolo="Le Farfalle Nello Stomaco Non Sono Sempre Amore: Ecco Cosa Sono Davvero",
        hook="Le farfalle nello stomaco non sono sempre un buon segno.",
        caption="Cosa dice davvero la psicologia sulle farfalle nello stomaco — non e' sempre amore.",
        hashtag=["relazioni", "psicologia", "veritascomoda", "legamidiamore", "psicologiadellamore", "societa"],
    ),
}

REGOLE_PERMANENTI_CANALE = (
    "voce femminile Fliki tier Ultra; sottotitoli piccoli; SOLO donne o coppia in scena, mai un "
    "uomo da solo; pubblicazione PRIVATA di default; --upload richiede --video-folder con "
    "copertina reale (regola permanente 2026-08-18)."
)


def orario_per_strategia(strategia: str, slot_del_giorno: int) -> str:
    # Prime time IT per contenuti relazioni: sera. Slot multipli distanziati per non
    # cannibalizzarsi in home/shorts feed.
    base = {"A": "19:00", "B": "20:30", "C": "21:30"}
    return base[strategia]


def costruisci_calendario():
    start = date(2026, 8, 27)
    giorni = [start + timedelta(i) for i in range(30)]
    bonus_days = {giorni[0], giorni[14]}  # giorno 1 (lancio) e giorno 15 (metà mese)

    piano_giorni = []
    for d in giorni:
        weekend = d.weekday() >= 5
        n_slot = 3 if (weekend or d in bonus_days) else 2
        piano_giorni.append({"data": d, "n_slot": n_slot, "weekend": weekend, "bonus": d in bonus_days})
    return piano_giorni


def assegna_strategie(piano_giorni):
    """Weekend + bonus days -> 1 A + 1 B + 1 C (mix completo).
    Weekday normali (2 slot) -> pattern fisso per esaurire esattamente 28/14/28 senza sforare."""
    residuo = {"A": STRATEGIE["A"]["volume"], "B": STRATEGIE["B"]["volume"], "C": STRATEGIE["C"]["volume"]}
    normali = [g for g in piano_giorni if g["n_slot"] == 2]
    # 4 giorni normali portano B (1 ogni ~5 giorni feriali), gli altri 16 alternano A/C.
    b_indices = set(idx for pos, idx in enumerate(range(2, len(normali), 5)) if pos < 4)

    assegnazioni = {}
    for g in piano_giorni:
        d = g["data"]
        if g["n_slot"] == 3:
            assegnazioni[d] = ["A", "B", "C"]
            residuo["A"] -= 1
            residuo["B"] -= 1
            residuo["C"] -= 1

    idx_normale = 0
    for g in piano_giorni:
        if g["n_slot"] != 2:
            continue
        d = g["data"]
        if idx_normale in b_indices:
            # giorno con B: l'altro slot va alla strategia con piu' residuo tra A/C
            altra = "A" if residuo["A"] >= residuo["C"] else "C"
            assegnazioni[d] = ["B", altra]
            residuo["B"] -= 1
            residuo[altra] -= 1
        else:
            assegnazioni[d] = ["A", "C"]
            residuo["A"] -= 1
            residuo["C"] -= 1
        idx_normale += 1

    return assegnazioni, residuo


def main():
    with open(SELEZIONE_PATH, "r", encoding="utf-8") as f:
        selezione = json.load(f)

    tutti = []
    for strat, lista in selezione.items():
        for c in lista:
            c2 = dict(c)
            c2["strategia"] = strat
            tutti.append(c2)

    id_selezione = {c["videoId"] for c in tutti}
    id_creativo = set(CREATIVO.keys())
    mancanti_creativo = id_selezione - id_creativo
    extra_creativo = id_creativo - id_selezione
    if mancanti_creativo:
        raise SystemExit(f"[!] {len(mancanti_creativo)} video selezionati senza copy: {mancanti_creativo}")
    if extra_creativo:
        raise SystemExit(f"[!] {len(extra_creativo)} entry di copy senza corrispondenza nella "
                          f"selezione reale (possibile videoId scritto a mano errato): {extra_creativo}")
    assert len(tutti) == 70, f"attesi 70 video selezionati, trovati {len(tutti)}"

    piano_giorni = costruisci_calendario()
    assegnazioni, residuo = assegna_strategie(piano_giorni)
    assert all(v == 0 for v in residuo.values()), f"distribuzione calendario non quadra: {residuo}"

    per_strategia = {"A": [c for c in tutti if c["strategia"] == "A"],
                      "B": [c for c in tutti if c["strategia"] == "B"],
                      "C": [c for c in tutti if c["strategia"] == "C"]}
    for lst in per_strategia.values():
        lst.sort(key=lambda c: -c["vph"])
    cursori = {"A": 0, "B": 0, "C": 0}

    righe = []
    giorno_n = 0
    for g in piano_giorni:
        giorno_n += 1
        for strat in assegnazioni[g["data"]]:
            c = per_strategia[strat][cursori[strat]]
            cursori[strat] += 1
            creativo = CREATIVO[c["videoId"]]
            riga = {
                "giorno": giorno_n,
                "data_pubblicazione": g["data"].isoformat(),
                "orario_pubblicazione": orario_per_strategia(strat, 0),
                "strategia": strat,
                "strategia_nome": STRATEGIE[strat]["nome"],
                "canale_sorgente": c["canale_sorgente"],
                "url_sorgente_reale": c["url"],
                "video_id_sorgente": c["videoId"],
                "titolo_originale": c["title"],
                "vph_sorgente": c["vph"],
                "titolo_adattato": creativo["titolo"],
                "schemi_titolo_applicati": c.get("schemi_titolo", []),
                "hook_3_secondi": creativo["hook"],
                "caption_descrizione": creativo["caption"],
                "hashtag_set": creativo["hashtag"],
                "note_esecuzione": REGOLE_PERMANENTI_CANALE,
                "comando_cli": (
                    f"python apex7_orchestrator.py run --canale legamidiamore "
                    f"--video-sorgente {c['url']} --phase 1"
                ),
            }
            righe.append(riga)

    assert len(righe) == 70
    assert len({r["video_id_sorgente"] for r in righe}) == 70, "duplicati rilevati nel piano finale"

    piano = {
        "generato_il": "2026-08-26",
        "canale": "@Legamidiamore",
        "periodo": {"inizio": piano_giorni[0]["data"].isoformat(), "fine": piano_giorni[-1]["data"].isoformat(),
                    "giorni": 30},
        "totale_video": 70,
        "strategie": STRATEGIE,
        "righe": righe,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(piano, f, ensure_ascii=False, indent=2)

    # `fonti_extra` (A4-L01-03, studio AI TUBE PRO / A4-L01 @ 05:44): la colonna dove atterrano
    # i link del materiale di supporto — l'articolo, il video, la pagina da cui lo script prende
    # i fatti in piu'. Prima non esisteva: una fonte trovata durante la ricerca non aveva un
    # posto dove stare, quindi non veniva mai riusata e si ricercava tutto da capo al video dopo.
    # Piu' fonti nella stessa cella si separano con " | ". Vuota e' legittimo.
    campi_csv = ["giorno", "data_pubblicazione", "orario_pubblicazione", "strategia", "canale_sorgente",
                 "url_sorgente_reale", "titolo_originale", "vph_sorgente", "titolo_adattato",
                 "hook_3_secondi", "caption_descrizione", "hashtag_set", "fonti_extra", "comando_cli"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi_csv, extrasaction="ignore")
        w.writeheader()
        for r in righe:
            r2 = dict(r)
            r2["hashtag_set"] = " ".join(f"#{h}" for h in r["hashtag_set"])
            # La colonna esiste sempre, anche quando non ci sono fonti extra: una colonna che
            # compare solo a volte non e' un posto dove mettere le cose.
            extra = r.get("fonti_extra") or []
            r2["fonti_extra"] = " | ".join(extra) if isinstance(extra, (list, tuple)) else str(extra)
            w.writerow(r2)

    print(f"[+] {OUT_JSON}")
    print(f"[+] {OUT_CSV}")
    print(f"\nDistribuzione finale: A={len(per_strategia['A'])} usati={cursori['A']} · "
          f"B={len(per_strategia['B'])} usati={cursori['B']} · C={len(per_strategia['C'])} usati={cursori['C']}")
    return piano


if __name__ == "__main__":
    main()
