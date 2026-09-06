# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L14.

«Final Cut: Metodo Copia & Incolla Avanzato» · ~50 min · 9.013 parole · BRONZO dichiarata.

E' la lezione piu' lunga del blocco degli editor manuali, e la sola che lasci qualcosa di vero.
Del tutorial non si prende nulla. Si prendono: due principi di script (l'apertura come leva di
ritenzione e la CTA di chiusura), due miti nuovi che portano il catalogo del §5 da quattro a sei,
e un numero che smonta la promessa della lezione madre — il metodo costa ~1 ora a video, non i
5 minuti annunciati in L05.

Nota sul metodo: le due regole di script (L14-01, L14-02) nascono da una lezione che le insegna
per la ragione sbagliata (rendere irriconoscibile un video copiato). Il principio regge anche
senza quella ragione, e si prende dichiarando perche' — piano §6.3.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L14"
LEZIONE = "Final Cut: Metodo Copia & Incolla Avanzato"

REGOLE = [
    {
        "id": "A4-L14-01",
        "tipo": "euristica",
        "regola": ("I primi 30 secondi dello script sono una leva di RITENZIONE, non solo di CTR: "
                   "si scrivono per ultimi, portano una promessa specifica col dettaglio che il "
                   "titolo non conteneva, e non ospitano preamboli ne' presentazioni del canale. "
                   "A 137 parole/minuto sono circa 68 parole: un budget stretto, e va dichiarato "
                   "nella spec."),
        "prova": ("solo parlato @ 09:36 ('cambiare tutte le clip dei primi 30 secondi') e @ 11:35 "
                  "('il tuo obiettivo non e' solo farlo cliccare, ma fargli vedere l'intero video')"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/script-writer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("script-writer §11 tratta l'apertura come blocco a se' con budget di parole e "
                   "rimanda alla ritenzione ai 30s di YouTube Studio; oggi la fabbrica cura "
                   "esplicitamente il clic (titolo, copertina) e non la ritenzione d'apertura"),
    },
    {
        "id": "A4-L14-02",
        "tipo": "procedura",
        "regola": ("Ogni script si chiude con UNA sola CTA esplicita, dichiarata nella spec, col "
                   "motivo accanto e ruotata dal ventaglio del §10. Quattro richieste in fila "
                   "sono zero azioni. La CTA di chiusura e' testo dello script e cambia da video "
                   "a video: non va confusa con l'outro del canale, che invece resta stabile."),
        "prova": ("solo parlato @ 45:35 ('la parte finale va sempre modificata ... e' fondamentale "
                  "che le persone facciano l'azione') e @ 50:33"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/operatori/script-writer.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "basso",
        "misura": ("script-writer §12 impone una CTA sola, motivata e ruotata, e la distingue "
                   "dall'outro; oggi nessun documento diceva come deve finire un video"),
    },
    {
        "id": "A4-L14-03",
        "tipo": "vincolo",
        "regola": ("Nessuna soglia di durata rende lecita una clip protetta, e il fatto che il "
                   "numero cambi da lezione a lezione (5 secondi in L10, 4 secondi in L14) e' la "
                   "prova che nessuno l'ha letto da qualche parte. Quinto dei sei miti del "
                   "camuffamento."),
        "prova": ("solo parlato @ 20:51 ('sono 4 secondi di video che non possono dire nulla "
                  "perche' siamo dentro il fair use, quindi andate super tranquilli')"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 elenca sei miti e il quinto e' la soglia dei "
                   "'4 secondi' messa accanto ai '5 secondi' di L10; oggi la scheda ne portava "
                   "quattro e la contraddizione fra le due soglie non era visibile"),
    },
    {
        "id": "A4-L14-04",
        "tipo": "vincolo",
        "regola": ("«Il fair use decade perche' la clip non e' del canale che la usa» e' falso su "
                   "due piani: confonde chi puo' agire (il titolare, non chi riusa) con la "
                   "liceita' dell'uso, e trasforma una difficolta' di prova in una licenza. "
                   "'Non possono dimostrarlo' non ha mai voluto dire 'si puo' fare'. Sesto dei "
                   "sei miti del camuffamento."),
        "prova": ("solo parlato @ 19:50 ('il canale che la sta utilizzando non e' che l'ha creata "
                  "lui ... quindi in realta' il fair use decade ... noi siamo a posto')"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "alto",
        "misura": ("monetizzazione-compliance §5 porta il sesto mito con la confutazione sui due "
                   "piani; oggi il ragionamento non era registrato da nessuna parte, ed e' quello "
                   "che un collaboratore ripeterebbe con piu' facilita' perche' suona giuridico"),
    },
    {
        "id": "A4-L14-05",
        "tipo": "parametro",
        "regola": ("Il metodo copia-incolla fatto bene costa ~1 ORA a video (5-10 minuti per il "
                   "primo minuto), non i 5 minuti promessi dalla lezione madre L05: un fattore "
                   "12x, e le due cifre stanno nello stesso corso. Il costo dichiarato di un "
                   "metodo si prende dalla lezione che lo mostra dal vivo, non da quella che lo "
                   "vende."),
        "prova": "solo parlato @ 25:23 (5-10 minuti per il primo minuto, circa un'ora per l'intero video)",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("monetizzazione-compliance §4 porta il costo misurato accanto alla terza "
                   "ragione (e' lavoro manuale) e rimanda a CONFLITTI C-006; oggi la porta chiusa "
                   "era argomentata senza un numero"),
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

    SW = "03-AGENTI-E-RUOLI/operatori/script-writer.md"
    MC = "04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md"
    return {
        "A4-L14-01": contiene(SW, ["primi 30 secondi", "ritenzione"]),
        "A4-L14-02": contiene(SW, ["cta di chiusura"]),
        "A4-L14-03": contiene(MC, ["miti del camuffamento", "4 secondi"]),
        "A4-L14-04": contiene(MC, ["fair use decade"]),
        "A4-L14-05": contiene(MC, ["1 ora a video"]),
    }
