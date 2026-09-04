# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L01.

«Scaricare testi gia' pronti per generare video in 3 click» · 7:25 · registrata il 20 aprile
(dichiarato a voce a 01:05 e coerente con la notizia mostrata: la lezione ha ~2 anni e mezzo).

Lezione di approvvigionamento della materia prima. Gli strumenti che insegna (DownSub,
SaveSubs) sono inferiori a quello che abbiamo gia' (yt-dlp automatico, provenienza tracciata).
Il valore sta altrove, in un passaggio detto di sfuggita a 04:58: quando il video sorgente e'
corto, si va a prendere una SECONDA fonte — un articolo di testata — e si salva il link nel
piano editoriale. La nostra fabbrica pretende 2.220 parole da un pacchetto che contiene una
sola fonte, e non conta nemmeno quanto lunga sia: e' il buco che questa lezione tappa.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L01"
LEZIONE = "Scaricare testi gia' pronti per generare video in 3 click"

REGOLE = [
    {
        "id": "A4-L01-01",
        "tipo": "procedura",
        "regola": ("Il pacchetto DA-SCRIVERE deve dichiarare le parole reali del transcript "
                   "sorgente e, se sono meno di quelle che lo script finale pretende, deve "
                   "contenere almeno 2 fonti testuali esterne con link e data. Un ordine di "
                   "2.220 parole servito con 700 parole di materiale e' un invito a inventare."),
        "prova": "solo parlato @ 04:58 ('magari questo qui e' un video abbastanza corto')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("transcript-collector conta le parole e pretende le fonti esterne sotto "
                   "soglia; oggi il brief allega il transcript senza contarlo (verificato: "
                   "apex7_orchestrator.py:1189-1214, nessun conteggio)"),
    },
    {
        "id": "A4-L01-02",
        "tipo": "procedura",
        "regola": ("Se i sottotitoli automatici non escono, prima di scartare il candidato si "
                   "prova la via di riserva (servizi terzi tipo savesubs.com); se fallisce "
                   "anche quella si dichiara QUALE dei due guasti e' accaduto — strumento muto "
                   "o video senza sottotitoli. Sono cause diverse e vanno distinte."),
        "prova": "frame-102.png @ 06:44 (SaveSubs) + parlato @ 06:01",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("transcript-collector nomina la via di riserva e distingue i due guasti nei "
                   "failure modes; oggi dice solo 'fermati, candidato B'"),
    },
    {
        "id": "A4-L01-03",
        "tipo": "vincolo",
        "regola": ("Il piano editoriale deve avere una colonna 'fonti_extra' dove atterrano i "
                   "link del materiale di supporto: una fonte senza un posto dove stare non "
                   "viene mai riusata."),
        "prova": "frame-087.png @ 05:44 (link dell'articolo nella colonna NOTE del foglio)",
        "fonte": "schermo",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/assemble_piano_editoriale.py",
        "azione": "modifica",
        "binario": "B",
        "rischio": "medio",
        "misura": ("campi_csv contiene 'fonti_extra'; oggi sono 13 colonne e nessuna per il "
                   "materiale di supporto (verificato: assemble_piano_editoriale.py:654)"),
    },
    {
        "id": "A4-L01-04",
        "tipo": "euristica",
        "regola": ("Lo stesso video sorgente puo' alimentare un canale in un'altra lingua: la "
                   "trascrizione si traduce in automatico in decine di lingue. E' una leva di "
                   "scala da valutare in sede di strategia, non un'automazione da accendere "
                   "perche' e' possibile."),
        "prova": "frame-056.png @ 03:40 (elenco lingue di auto-traduzione) + parlato @ 03:30",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/capi/capo-strategia.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("capo-strategia elenca la leva multilingua fra le opzioni di scala, con il "
                   "suo costo dichiarato; oggi non e' nominata"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale.

    `fabbrica` e' il percorso della cartella YOUTUBE-AUTOMATION-FACTORY.
    """
    import os

    def contiene(percorso_relativo, aghi):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    esiti = {}
    esiti["A4-L01-01"] = contiene("03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
                                  ["parole del transcript", "fonti esterne"])
    esiti["A4-L01-02"] = contiene("03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
                                  ["via di riserva"])
    esiti["A4-L01-03"] = contiene("02-AUTOMAZIONI-E-SCRIPTS/assemble_piano_editoriale.py",
                                  ["fonti_extra"])
    esiti["A4-L01-04"] = contiene("03-AGENTI-E-RUOLI/capi/capo-strategia.md",
                                  ["multilingua"])
    return esiti
