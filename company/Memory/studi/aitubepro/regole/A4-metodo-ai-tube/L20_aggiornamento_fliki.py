# -*- coding: utf-8 -*-
"""Regole imparate da: AI TUBE PRO / Metodo AI Tube / L20.

«Aggiornamento Fliki Luglio 2024» · 76 minuti · ~12.000 parole · la lezione piu' lunga di A4.

E' una live registrata sullo STRUMENTO CHE USIAMO IN PRODUZIONE, quindi vale piu' di qualunque
tutorial di editor altrui. Letta integralmente da una sentinella (solo parlato, zero frame:
profondita' dichiarata BRONZO per COME e' stata letta, non per quanto vale — i frame sulle tre
funzioni candidate all'API restano assegnati al gate A4).

Il risultato piu' importante non e' una novita': e' che questa lezione CHIUDE una verifica aperta
da due giorni. In Fliki la musica non e' automatica (e' una traccia separata da scegliere e
propagare a mano); nel nostro payload non c'e' un campo musica; quindi i nostri video non hanno
musica, e il criterio «Bilanciamento Volumi» del gate qa-audio-video non era sospeso: era
inapplicabile.

Conferma inoltre, senza smentirli, i tre vincoli noti: 16:9 fisso (Shorts mai nominati in 76
minuti), pronunce legate al singolo file, musica non automatica.
"""

FONTE = "AI TUBE PRO / A4 Metodo AI Tube / L20"
LEZIONE = "Aggiornamento Fliki Luglio 2024"

REGOLE = [
    {
        "id": "A4-L20-01",
        "tipo": "vincolo",
        "regola": ("I nostri video NON hanno musica, ed e' accertato: in Fliki la musica e' una "
                   "traccia separata (Background Audio) che va scelta a mano e propagata con "
                   "'Apply to all scenes', e nel nostro payload non esiste un campo musica. "
                   "Quindi il criterio 'Bilanciamento Volumi' di qa-audio-video non e' sospeso: "
                   "e' INAPPLICABILE, non si spunta e non fa bocciare, e torna in vigore solo se "
                   "una traccia entrera' nel payload."),
        "prova": ("solo parlato @ 03:57-05:26 (la musica si sceglie dalla libreria) e @ 07:48-08:10 "
                  "('apply to all scenes', altrimenti resta sulla prima scena) + verifica sul "
                  "codice: fliki_client.py:252 non ha campi musica"),
        "fonte": "parlato",
        "tocca": "03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("qa-audio-video §10 chiude la verifica A4-L04-04 e il criterio in §3 passa da "
                   "SOSPESO a INAPPLICABILE; oggi il gate portava in checklist un controllo su "
                   "una cosa che non esiste, e nessuno se n'era accorto perche' un criterio che "
                   "non puo' fallire non fa rumore"),
    },
    {
        "id": "A4-L20-02",
        "tipo": "parametro",
        "regola": ("Il volume della musica in Fliki sta fra il 5% (tipico, 'gradevole') e il 15% "
                   "(massimo normalmente applicato), non fra il 10 e il 15: il 10% visto a "
                   "schermo in L19 era il default di quel progetto, non una prescrizione. E la "
                   "condizione vale piu' del numero: dipende dalla traccia, dal narratore e dal "
                   "volume del narratore — si regola ascoltando."),
        "prova": ("solo parlato @ 07:13-07:25 (massimo 15) e @ 07:39-07:48 ('gradevole' 5), con la "
                  "condizione @ 07:25-07:39"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-avanzato.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "basso",
        "misura": ("fliki-avanzato §4 riconcilia le tre cifre (10 visto, 15 massimo, 5 tipico) "
                   "spiegando che cosa sia ciascuna; oggi la scheda prescriveva 10-15% con il "
                   "pavimento troppo alto e una sola fonte"),
    },
    {
        "id": "A4-L20-03",
        "tipo": "vincolo",
        "regola": ("La mappa delle pronunce di Fliki si propaga SOLO duplicando un file-modello "
                   "che le contiene gia': non e' una funzione, e' una copia. La nostra catena non "
                   "duplica nulla — crea ogni video da zero con una chiamata — quindi nei nostri "
                   "video una correzione di pronuncia non si applica MAI, nemmeno per eredita'. "
                   "Si corregge nel testo dello script, punto."),
        "prova": ("solo parlato @ 40:54-41:24 ('vi fate un file campione, uno demo, e poi fate "
                  "duplica') e @ 71:52-73:41 (Q&A: la correzione va incollata anche sul file demo, "
                  "altrimenti i prossimi non la ereditano)"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/lessico-pronuncia.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("lessico-pronuncia dichiara che la propagazione e' una duplicazione di "
                   "progetto e che percio' da noi non avviene mai; oggi la scheda diceva 'vale "
                   "per un video solo' senza spiegare come gli altri la ereditino"),
    },
    {
        "id": "A4-L20-04",
        "tipo": "vincolo",
        "regola": ("Il piano base di Fliki ha un secondo tetto oltre ai minuti: 50 SCENE per "
                   "file. Si aggira impacchettando testo in una scena sola e frazionandolo con il "
                   "B-roll, che crea media temporizzati dentro la scena senza contarli come scene "
                   "nuove. Va verificato se il conteggio valga anche via API, prima di alzare i "
                   "volumi di produzione."),
        "prova": ("solo parlato @ 66:59-67:23 (il limite di 50) e @ 67:29-67:53 (40 immagini in "
                  "una scena sola); capacita' caratteri contraddittoria, 'mille' @ 65:29 contro "
                  "'10.000' @ 67:41, non normalizzata"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-produzione.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("fliki-produzione §3 porta il tetto di 50 scene, il modo di aggirarlo e la "
                   "verifica assegnata al gate; oggi la fabbrica conosceva solo il tetto in "
                   "minuti e nessuno sapeva che ne esistesse un secondo"),
    },
    {
        "id": "A4-L20-05",
        "tipo": "strumento",
        "regola": ("Fliki genera effetti sonori da un prompt testuale (Add Layer > Audio > "
                   "Generate) e li si posiziona al secondo col pannello Timing: e' la novita' con "
                   "piu' probabilita' di esistere anche via API, ed e' assegnata al gate A4. "
                   "Attenzione al vuoto: delle tracce musicali di libreria il corso dice che sono "
                   "licenziate, degli SFX generati non dice nulla — il titolo d'uso si legge nei "
                   "termini di Fliki, non si assume per analogia."),
        "prova": "solo parlato @ 44:53-46:04 (generazione da prompt) e @ 46:04-46:56 (sincronizzazione col Timing)",
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-avanzato.md",
        "azione": "nuovo",
        "binario": "A",
        "rischio": "medio",
        "misura": ("fliki-avanzato §4 descrive la generazione degli SFX e dichiara il vuoto di "
                   "licenza; oggi la fabbrica non sapeva che Fliki generasse audio da prompt"),
    },
    {
        "id": "A4-L20-06",
        "tipo": "procedura",
        "regola": ("La difesa dai reclami sulla musica di Fliki si gioca PRIMA, non dopo: si "
                   "registra l'ID del canale nel profilo Fliki (gratis, una volta sola). Il corso "
                   "insegna invece un 'trafiletto' da incollare nella disputa — un processo umano "
                   "fornito dalla sua community, non da Fliki — e in 76 minuti sullo strumento "
                   "non nomina mai il campo YouTube channel ID(s)."),
        "prova": ("solo parlato @ 06:20-06:39 (il trafiletto nella disputa) e @ 06:39-06:48 (lo "
                  "fornisce la community del corso); il campo del profilo Fliki non compare in "
                  "tutta la lezione"),
        "fonte": "parlato",
        "tocca": "04-SKILLS-E-REFERENCE/references/fliki-produzione.md",
        "azione": "modifica",
        "binario": "A",
        "rischio": "medio",
        "misura": ("fliki-produzione §4 mette a confronto la difesa dopo il reclamo e quella "
                   "prima, e dichiara che il corso ignora la seconda; oggi la scheda aveva il "
                   "campo (A4-L19-01) ma non diceva che l'alternativa insegnata altrove e' "
                   "un processo umano che dipende da qualcuno che risponde"),
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

    FP = "04-SKILLS-E-REFERENCE/references/fliki-produzione.md"
    FA = "04-SKILLS-E-REFERENCE/references/fliki-avanzato.md"
    return {
        "A4-L20-01": contiene("03-AGENTI-E-RUOLI/controllo/qa-audio-video.md",
                              ["inapplicabile", "non hanno musica"]),
        "A4-L20-02": contiene(FA, ["5-15%", "gradevole"]),
        "A4-L20-03": contiene("04-SKILLS-E-REFERENCE/references/lessico-pronuncia.md",
                              ["file campione", "duplica"]),
        "A4-L20-04": contiene(FP, ["50 scene", "b-roll"]),
        "A4-L20-05": contiene(FA, ["generate", "effetti sonori"]),
        "A4-L20-06": contiene(FP, ["trafiletto"]),
    }
