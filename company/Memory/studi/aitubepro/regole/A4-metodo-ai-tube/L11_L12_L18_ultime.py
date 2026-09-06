# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L11, L12, L18.

Le tre lezioni che erano rimaste in `1-fallito` per due giorni con la diagnosi sbagliata
«403, gettone scaduto». Il gettone era valido: mancavano le intestazioni verso il CDN. Riparata
l'ingestione, sono arrivate a casa tutte e tre con le durate esatte e sono state lette
integralmente da tre sentinelle.

  L11 «Intelligenza Artificiale con Premiere Pro (SENSEI)» — 22 min — quattro funzioni AI
      dentro un editor. Ne resta un vantaggio nostro che non sapevamo di avere.
  L12 «Video Virali con sottotitoli automatici in 2 minuti» — 9 min — la lezione che poteva
      darci parametri di sottotitoli e non ne contiene UNO. Ne esce il settimo mito.
  L18 «Registrare Voice Over con Audacity» — 17 min — zero numeri di livello audio in tutta
      la lezione. Ne resta una regola sul mestiere di un gate.

Tre lezioni, tre regole. E' un raccolto piccolo, ed e' giusto che sia scritto piccolo.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L11, L12, L18"
LEZIONE = "Premiere SENSEI · sottotitoli automatici · voice over con Audacity"

REGOLE = [
    {
        "id": "A4-L11-01",
        "tipo": "euristica",
        "regola": ("Il formato si GENERA, non si ritaglia: la destinazione (16:9, 9:16, 1:1) si "
                   "dichiara nella configurazione del canale prima di produrre. Chi monta a mano "
                   "deve riquadrare l'orizzontale in verticale inseguendo il soggetto clip per "
                   "clip; noi non abbiamo quel problema, ed e' un vantaggio strutturale da non "
                   "barattare alla prima scorciatoia."),
        "prova": ("solo parlato @ 06:55-07:05 (il soggetto sparisce quando la sequenza passa a "
                  "verticale) e @ 07:47-11:06 (il riquadro automatico come rimedio, anche in "
                  "blocco su tutta la sequenza)"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/video-producer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("video-producer §12 dichiara che il formato si genera e lega la regola al "
                   "formato per canale applicato oggi (A4-L04-02); oggi il vantaggio esisteva ma "
                   "non era scritto da nessuna parte, e i vantaggi non scritti si perdono"),
    },
    {
        "id": "A4-L12-01",
        "tipo": "vincolo",
        "regola": ("Cambiare la voce e aggiungere i sottotitoli NON rende proprio il video di un "
                   "altro: sono uno strato sopra, non toccano l'opera sotto. Settimo dei sette "
                   "miti del camuffamento, e il piu' insidioso perche' il lavoro fatto e' vero — "
                   "ma il lavoro vero su materiale altrui produce un'opera derivata, non un "
                   "titolo."),
        "prova": ("solo parlato @ 08:36-08:50 ('bastera' incollare la voce, o artificiale o la "
                  "vostra, per creare video con sottotitoli, cosi' che diventano video originali, "
                  "unici e che possono senza alcun problema diventare virali')"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 elenca sette miti e il settimo e' 'voce nuova + "
                   "sottotitoli = originale'; il §8.1 registra inoltre che la stessa persona "
                   "reale compare come materiale in due lezioni diverse (L12 @01:36, L15 @11:36) "
                   "senza che copyright o consenso siano mai nominati"),
    },
    {
        "id": "A4-L18-01",
        "tipo": "euristica",
        "regola": ("Un gate audio difende una SOGLIA, non un ideale: ferma l'audio scadente e "
                   "lascia passare quello buono abbastanza. Se stai per bocciare un video e non "
                   "sai dire quale spettatore se ne accorgerebbe, non stai difendendo una soglia "
                   "— scrivilo come osservazione e lascia passare."),
        "prova": ("solo parlato @ 15:38-16:05 ('non e' tanto il fatto di massimizzare la qualita' "
                  "dell'audio ... l'audio fa la differenza nel caso in cui e' scadente')"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("qa-audio-video §11 distingue soglia e ideale e lo lega al §10 (il criterio che "
                   "bocciava su una musica inesistente); oggi il gate non aveva scritto da nessuna "
                   "parte QUANTO deve essere severo, e un gate senza quel limite trova sempre "
                   "qualcosa da bocciare"),
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
        "A4-L11-01": contiene("03-AGENTI-E-RUOLI/operatori/video-producer.md",
                              ["il formato si genera", "non si ritaglia"]),
        "A4-L12-01": contiene("04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
                              ["sette miti", "originali, unici"]),
        "A4-L18-01": contiene("03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
                              ["una soglia, non un ideale"]),
    }
