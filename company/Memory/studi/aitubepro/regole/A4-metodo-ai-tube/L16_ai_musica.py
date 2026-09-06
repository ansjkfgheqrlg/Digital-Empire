# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L16.

«A.I. per canali di Musica: separare voce da audio + nicchia» · ~7 min · 951 parole · BRONZO.

Propone una nicchia costruita su: audio scaricato da YouTube via siti terzi, separato in voce e
base con lalal.ai, ripubblicato. La dichiara «evitando tutti i problemi di copyright» e poi non
spiega alcun meccanismo per evitarli.

Ne escono due regole di natura diversa: una porta chiusa (il materiale in ingresso, non lo
strumento) e un principio generale di scouting che vale ben oltre questa lezione — l'esempio di
successo portato a prova.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L16"
LEZIONE = "A.I. per canali di Musica: separare voce da audio + nicchia"

REGOLE = [
    {
        "id": "A4-L16-01",
        "tipo": "vincolo",
        "regola": ("La separazione audio (source separation) di brani altrui non entra in "
                   "fabbrica, e la nicchia 'canali di musica' costruita su di essa non si apre: "
                   "scaricare l'audio da YouTube via siti terzi viola i ToS, e separare voce e "
                   "base da una registrazione altrui e' elaborazione non autorizzata che tocca "
                   "sia il diritto d'autore sulla composizione sia i diritti connessi sulla "
                   "registrazione. Lo strumento resta legittimo su audio NOSTRO: si separa cio' "
                   "di cui si hanno i diritti."),
        "prova": ("solo parlato @ 03:20 ('evitando tutti i problemi di copyright', senza spiegare "
                  "come) e @ 01:30 (il processo: link YouTube -> sito terzo -> mp3 -> lalal.ai)"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §7 e' la porta chiusa sulla separazione audio, con "
                   "i due passaggi problematici distinti e la linea 'si separa cio' di cui si "
                   "hanno i diritti'; oggi la scheda non nominava ne' l'audio ne' la musica"),
    },
    {
        "id": "A4-L16-02",
        "tipo": "euristica",
        "regola": ("Un canale di successo portato a esempio non e' una prova: risponde solo a "
                   "'e' possibile?'. Prima di aprire una nicchia su un esempio vanno poste due "
                   "domande — su cosa si regge quel successo (se sul riuso di materiale altrui, "
                   "la nicchia e' chiusa) e se e' riproducibile da noi oggi, senza archivio e "
                   "senza base iscritti. Chi guarda solo chi e' rimasto in piedi fa survivorship "
                   "bias: quelli spariti non hanno un canale da mostrare."),
        "prova": "solo parlato @ 03:55 (il canale portato a prova: 544 video, quasi 1.000.000 di iscritti)",
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/niche-scout.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("niche-scout §9 impone le due domande e dichiara l'esempio come candidato mai "
                   "come verdetto; oggi la scheda misurava i numeri di un canale ma non chiedeva "
                   "MAI su cosa si reggessero"),
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

    return {
        "A4-L16-01": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["separazione audio", "source separation"]),
        "A4-L16-02": contiene("03-AGENTI-E-RUOLI/operatori/niche-scout.md",
                              ["survivorship bias", "riproducibile"]),
    }
