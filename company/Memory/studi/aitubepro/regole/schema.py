# -*- coding: utf-8 -*-
"""schema.py — il contratto di una regola imparata dal corso.

PERCHE' UN CONTRATTO E NON PROSA LIBERA.
167 lezioni scritte in prosa sono 167 documenti che nessuno rilegge mai. Con un contratto,
ogni regola diventa un oggetto interrogabile: si puo' chiedere quante regole toccano un
certo file, quante ad alto rischio non sono ancora state applicate, quali non hanno una
prova. Senza contratto lo studio resta un archivio; con il contratto diventa un motore.

LA REGOLA PIU' DURA: `prova` non e' facoltativa.
Se una regola non dice DOVE l'ho vista — quale frame, quale minuto — non entra. E' la stessa
legge che governa tutto in questa casa: si riferisce cio' che si e' misurato, mai cio' che
si crede (dottrina §3). Una regola senza prova e' un'opinione con l'uniforme.
"""

CAMPI_OBBLIGATORI = (
    "id",        # <CATEGORIA>-L<NN>-<progressivo>, univoco in tutto lo studio
    "tipo",      # cosa sia questa regola
    "regola",    # la regola in italiano, imperativa, una frase
    "prova",     # dove l'ho vista: "frame-0142.png @ 08:31" oppure "solo parlato @ 08:31"
    "fonte",     # schermo | parlato | entrambi
    "tocca",     # percorso relativo del file della fabbrica che riguarda, o "-" se nessuno
    "azione",    # cosa comporta
    "binario",   # A = si applica subito · B = solo a gate di categoria (tocca la produzione)
    "rischio",   # quanto costa sbagliarla
    "misura",    # come si vede se ha funzionato: senza, non e' verificabile
)

TIPI = ("parametro", "procedura", "vincolo", "euristica", "strumento")
FONTI = ("schermo", "parlato", "entrambi")
AZIONI = ("modifica", "nuovo", "conferma", "scarta")
BINARI = ("A", "B")
RISCHI = ("basso", "medio", "alto")


def valida(regola, contesto=""):
    """Restituisce la lista degli errori. Lista vuota = la regola e' a norma."""
    errori = []
    if not isinstance(regola, dict):
        return ["%s: non e' un dizionario" % contesto]

    for campo in CAMPI_OBBLIGATORI:
        if campo not in regola:
            errori.append("%s: manca il campo obbligatorio '%s'" % (contesto, campo))
        elif not str(regola[campo]).strip():
            errori.append("%s: il campo '%s' e' vuoto" % (contesto, campo))

    def dentro(campo, ammessi):
        v = regola.get(campo)
        if v is not None and v not in ammessi:
            errori.append("%s: '%s' = %r non ammesso (ammessi: %s)"
                          % (contesto, campo, v, ", ".join(ammessi)))

    dentro("tipo", TIPI)
    dentro("fonte", FONTI)
    dentro("azione", AZIONI)
    dentro("binario", BINARI)
    dentro("rischio", RISCHI)

    # Coerenza fra prova e fonte: se la fonte e' lo schermo, la prova deve nominare un frame.
    # E' il punto in cui una regola smette di essere "mi pare di aver visto".
    prova = str(regola.get("prova", ""))
    if regola.get("fonte") in ("schermo", "entrambi") and "frame-" not in prova:
        errori.append("%s: fonte=%s ma la prova non nomina un frame (%r)"
                      % (contesto, regola.get("fonte"), prova))
    if ":" not in prova:
        errori.append("%s: la prova non porta un minuto (%r)" % (contesto, prova))

    # Una regola che tocca il motore in produzione NON puo' stare sul binario A.
    tocca = str(regola.get("tocca", ""))
    if "02-AUTOMAZIONI-E-SCRIPTS" in tocca and regola.get("binario") != "B":
        errori.append("%s: tocca il motore in produzione (%s) ma e' sul binario A. "
                      "Il motore si tocca solo a gate di categoria (ADR-024)." % (contesto, tocca))

    return errori
