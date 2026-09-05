# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L06.

«Metodo Copia e Incolla» · 17:07 · strumenti mostrati: vidIQ (funzione «Videos with the highest
velocity»), aTubeCatcher, Envato Elements / Pexels.

E' la lezione piu' delicata del corso: insegna a SCARICARE E RIPUBBLICARE video altrui,
cambiando audio, musica, ordine delle clip e grafica «per non incorrere in strike».
Va divisa in due meta' che non si giudicano insieme:

  (a) il METODO DI RICERCA — ottimo, e ci ha dato l'argomento migliore che avessimo sulla
      maturita' di un video: sulle prime ore le viste arrivano DAGLI ISCRITTI del canale, non
      dall'appeal del contenuto;
  (b) la PROCEDURA DI PRODUZIONE — riuso del materiale visivo altrui: porta chiusa, con tre
      ragioni scritte in CONFLITTI C-004 (difesa contro il Content ID e non contro il diritto,
      «fair use» citato come se fosse una regola di YouTube, ed editing manuale che azzera
      l'automazione).

Nota per chi legge dopo: questa lezione CONTRADDICE L05 sulla freschezza del video sorgente
(L05 sceglie un video di 13 ore, L06 spiega perche' non si deve). Arbitrato in C-005.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L06"
LEZIONE = "Metodo Copia e Incolla"

REGOLE = [
    {
        "id": "A4-L06-01",
        "tipo": "parametro",
        "regola": ("La velocity di un video giovane va rapportata agli ISCRITTI del canale: nelle "
                   "prime ore le viste arrivano dalla base iscritti, che guarda il nuovo "
                   "contenuto perche' e' iscritta, non perche' il contenuto sia forte. Copiare un "
                   "format che ha funzionato grazie a 4 milioni di iscritti altrui significa "
                   "copiare un risultato non riproducibile su un canale piccolo."),
        "prova": "solo parlato @ 07:02 ('e' normale che un video appena pubblicato faccia tante visualizzazioni, soprattutto se ci sono tanti iscritti al canale')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-analyst.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("video-analyst rapporta le viste dei candidati sotto le 24h agli iscritti del "
                   "canale sorgente e lo dichiara; oggi §2 guarda il volume assoluto (A4-L05-01) "
                   "senza chiedersi da dove venga"),
    },
    {
        "id": "A4-L06-02",
        "tipo": "vincolo",
        "regola": ("NON si riusa il materiale visivo di un video altrui. Si replica l'idea "
                   "validata, mai i fotogrammi. Cambiare audio, ordine delle clip e grafica e' "
                   "una difesa contro il Content ID, non conformita': il Content ID identifica, "
                   "non stabilisce chi ha ragione. E il «fair use» e' una dottrina del diritto "
                   "statunitense valutata da un giudice, non un permesso concesso da YouTube."),
        "prova": "solo parlato @ 10:36 ('su YouTube esiste il fair use e ci permette di utilizzare video di altre persone') e @ 04:31 ('il logo del canale lo devo togliere')",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance ha la sezione che vieta il riuso di materiale "
                   "visivo altrui con le tre ragioni; oggi la scheda parla di contenuto "
                   "riutilizzato ma non nomina mai il metodo copia-incolla ne' il Content ID"),
    },
    {
        "id": "A4-L06-03",
        "tipo": "euristica",
        "regola": ("Un format che ha gia' funzionato IN UN'ALTRA LINGUA e' un candidato forte, e "
                   "adesso con una prova misurata: due canali reali pubblicano le stesse identiche "
                   "clip in francese e in italiano (9,42 M contro 1,66 M di iscritti) con video "
                   "gemelli a 63,6k contro 10,4k viste. Si replica l'idea e la struttura, mai il "
                   "materiale."),
        "prova": "frame-205.png @ 13:40 (il video francese di Lama Facha, 63,6k viste, 10:56) + parlato @ 12:07",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-analyst.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("video-analyst segnala i candidati cross-lingua con la prova numerica del caso "
                   "Lama Facha / Famiglia Sfortunata; oggi il cross-lingua e' citato solo come "
                   "'bonus' nello storico video-hunter.md, senza un numero accanto"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale."""
    import os

    def contiene(percorso_relativo, aghi):
        p = os.path.join(fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    VA = "03-AGENTI-E-RUOLI/operatori/video-analyst.md"
    esiti = {}
    esiti["A4-L06-01"] = contiene(VA, ["iscritti del canale", "base iscritti"])
    esiti["A4-L06-02"] = contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                                  ["content id", "copia e incolla"])
    esiti["A4-L06-03"] = contiene(VA, ["cross-lingua", "lama facha"])
    return esiti
