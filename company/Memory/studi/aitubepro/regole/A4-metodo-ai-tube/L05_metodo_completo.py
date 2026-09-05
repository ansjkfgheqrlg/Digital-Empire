# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L05.

«Come creare un video da zero con il metodo A.I tube (IL METODO COMPLETO)» · 7:49 ·
lezione madre della categoria: il metodo intero eseguito in diretta col cronometro
(home YouTube -> DownSub -> ChatGPT -> Fliki -> Export, 5 minuti dichiarati).

Datata ad **aprile 2023** dallo schermo, non dal parlato: i file di Fliki sono «Apr 20, 2023»
(frame-042) e ChatGPT gira su Default GPT-3.5 (frame-027).

E' la PRIMA lezione che ci contraddice: tre conflitti, tutti arbitrati in
`company/Memory/studi/aitubepro/CONFLITTI.md` (C-001, C-002, C-003). Il pezzo piu' prezioso non
e' cio' che insegna, e' l'attrito: il corso costruisce l'intera lezione su un video di 13 ore,
che il nostro `video-analyst` scarterebbe — e leggendo la nostra regola si scopre che e' scritta
male, perche' difende dal RUMORE con un vincolo di TEMPO.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L05"
LEZIONE = "Come creare un video da zero con il metodo A.I tube (IL METODO COMPLETO)"

REGOLE = [
    {
        "id": "A4-L05-01",
        "tipo": "parametro",
        "regola": ("Un video giovane si scarta per POCHE VISTE, non per poche ore. Sotto le 24 "
                   "ore un candidato entra se il volume assoluto rende la velocity credibile: "
                   "89.000 viste in 13 ore non sono rumore, 200 viste in 2 ore si'. Un filtro "
                   "solo temporale taglia fuori le nicchie in cui la freschezza E' il prodotto."),
        "prova": "solo parlato @ 01:09 ('5.700 pollici in su, 89.000 visualizzazioni, 13 ore fa')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-analyst.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("video-analyst ammette i candidati sotto le 24h che superano una soglia di "
                   "viste dichiarata nel file; oggi (video-analyst.md:31-32) dice 'scarta tutto "
                   "cio' che e' piu' giovane di 24 ore' e butterebbe il caso del corso"),
    },
    {
        "id": "A4-L05-02",
        "tipo": "euristica",
        "regola": ("La durata di uno script si costruisce AGGIUNGENDO FONTI, mai allungando il "
                   "prompt. 'Scrivi piu' dettagli' gonfia il testo con parole che il modello si "
                   "inventa; altre parti di testo vere lo nutrono. Lo dice il corso stesso, "
                   "subito dopo aver fatto il contrario."),
        "prova": "solo parlato @ 05:39 ('se volessi farlo il doppio piu' lungo, scrivi piu' dettagli') e @ 05:53 ('se io inserissi altre parti di testo sarebbe ancora meglio')",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/script-writer.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("script-writer vieta esplicitamente di allungare chiedendo 'piu' dettagli' e "
                   "rimanda al transcript-collector per altre fonti quando il materiale non basta"),
    },
    {
        "id": "A4-L05-03",
        "tipo": "vincolo",
        "regola": ("Il metodo a FONTE SINGOLA riscritta e' scartato, e la motivazione resta "
                   "scritta: il corso stesso lo dichiara inferiore, il video prodotto cosi' dura "
                   "2:34 contro i 10-20 minuti promessi, e 'rendilo originale' e' un'istruzione a "
                   "un modello, non una proprieta' del contenuto."),
        "prova": "frame-113.png @ 07:28 (il video finito dura 02:34) + parlato @ 01:22 ('non so assolutamente nulla di cosa tratta questo video')",
        "fonte": "entrambi",
        "tocca": "03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
        "azione": "conferma",
        "binario": "A",
        "rischio": "alto",
        "misura": ("transcript-collector cita il metodo a fonte singola come scartato con il "
                   "rimando a CONFLITTI C-002, cosi' che nessuna lezione successiva lo "
                   "reintroduca; oggi la regola delle 2 fonti c'e' ma non dice contro cosa difende"),
    },
    {
        "id": "A4-L05-04",
        "tipo": "procedura",
        "regola": ("Il tempo per video e' una misura di fabbrica: si cronometra una produzione "
                   "vera e si scrive nella baseline, come i test e i difetti. Il corso ha un "
                   "metro (5 minuti); finche' noi non ne abbiamo uno, 'puntiamo sulla qualita'' "
                   "non e' una scelta dichiarata ma una copertura della lentezza."),
        "prova": "solo parlato @ 00:35 ('sono le 13 e 18') e @ 06:48 ('ci ho impiegato veramente 5 minuti per fare tutto')",
        "fonte": "parlato",
        "tocca": "-",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("BASELINE.md dello studio ha la voce 'tempo per video' con il metro del corso "
                   "a confronto e la misura nostra assegnata al gate A4; oggi BASELINE.md misura "
                   "test e difetti ma non un solo minuto di produzione"),
    },
]


def verifica(fabbrica):
    """Dice se la fabbrica rispetta gia' queste regole. Nessun effetto collaterale.

    A4-L05-04 tocca la baseline dello studio (non la fabbrica): si verifica su
    company/Memory/studi/aitubepro/BASELINE.md, che sta due livelli sopra questo file.
    """
    import os

    def contiene(percorso_relativo, aghi, base=None):
        p = os.path.join(base or fabbrica, percorso_relativo)
        if not os.path.exists(p):
            return False
        with open(p, encoding="utf-8", errors="replace") as f:
            testo = f.read().lower()
        return all(a.lower() in testo for a in aghi)

    studio = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    esiti = {}
    esiti["A4-L05-01"] = contiene("03-AGENTI-E-RUOLI/operatori/video-analyst.md",
                                  ["soglia di volume", "13 ore"])
    esiti["A4-L05-02"] = contiene("03-AGENTI-E-RUOLI/operatori/script-writer.md",
                                  ["più dettagli", "fonti"])
    esiti["A4-L05-03"] = contiene("03-AGENTI-E-RUOLI/operatori/transcript-collector.md",
                                  ["c-002"])
    esiti["A4-L05-04"] = contiene("BASELINE.md", ["tempo per video"], base=studio)
    return esiti
