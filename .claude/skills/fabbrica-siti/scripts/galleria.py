# -*- coding: utf-8 -*-
"""
galleria.py — genera pattern/GALLERIA.html e controlla i pattern contro il canone.

Perche' esiste (P2 del piano di Fase 2): un indice scritto a mano e' un debito con
una data di scadenza. `section-patterns.md` lo dimostra — 10 puntatori su 17 erano
gia' stale il giorno in cui l'abbiamo letto. Questa galleria si RIGENERA, non si
mantiene.

E fa da controllo: se un pattern usa un colore che il canone non ha, lo dice e
fallisce. E' il gate 1 di `CLAUDE-SITI.md §9`, in versione minima, applicato ai
pattern invece che a un cantiere.

Uso:
  python .claude/skills/fabbrica-siti/scripts/galleria.py

Esce 0 se tutti i pattern sono in canone, 1 altrimenti. Nessuna emoji: console cp1252.
"""
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(QUI)
PATTERN = os.path.join(SKILL, "pattern")
CANONE_JSON = os.path.join(SKILL, "canone", "canone.json")
USCITA = os.path.join(PATTERN, "GALLERIA.html")

HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")


def normalizza(h):
    h = h.lower()
    if len(h) == 4:
        return "#" + h[1] * 2 + h[2] * 2 + h[3] * 2
    return h


def leggi(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def senza_commenti(css):
    """Via i commenti CSS e HTML: li' i colori si citano apposta per vietarli."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"<!--.*?-->", "", css, flags=re.S)
    return css


def scheda_riassunto(testo):
    """Prende dalla scheda la riga di provenienza e il primo capoverso di 'Quando'."""
    origine = ""
    quando = ""
    righe = testo.split("\n")
    for i, r in enumerate(righe):
        if r.startswith("**Corsia") and not origine:
            origine = r.strip()
        if r.strip() == "## Quando" and not quando:
            for succ in righe[i + 1:]:
                if succ.strip():
                    quando = succ.strip()
                    break
    return origine, quando


def ripulisci(md):
    """Markdown minimo -> HTML minimo, per le due righe che finiscono in galleria."""
    md = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", md)
    md = re.sub(r"`(.+?)`", r"<code>\1</code>", md)
    md = md.replace("|", " &middot; ")
    return md


def main():
    if not os.path.isdir(PATTERN):
        print("FAIL - cartella pattern/ assente")
        return 1

    canone = json.loads(leggi(CANONE_JSON))
    ammessi = {normalizza(c) for c in canone["colori"]["ammessi"]}
    vietati = {normalizza(c): m for c, m in canone["colori"]["vietati"].items()}

    cartelle = sorted(
        d for d in os.listdir(PATTERN)
        if os.path.isdir(os.path.join(PATTERN, d))
        and os.path.isfile(os.path.join(PATTERN, d, "pattern.html"))
    )

    errori = []
    voci = []

    for nome in cartelle:
        html = leggi(os.path.join(PATTERN, nome, "pattern.html"))
        scheda_path = os.path.join(PATTERN, nome, "scheda.md")
        scheda = leggi(scheda_path) if os.path.isfile(scheda_path) else ""

        if not scheda:
            errori.append("%s - manca scheda.md (un pattern senza 'quando NO' non e' un pattern)" % nome)

        pulito = senza_commenti(html)
        trovati = {normalizza(h) for h in HEX.findall(pulito)}

        for c in sorted(trovati - ammessi - set(vietati)):
            errori.append("%s - colore %s fuori canone (gate 1)" % (nome, c))
        for c in sorted(trovati & set(vietati)):
            errori.append("%s - colore VIETATO %s - %s" % (nome, c, vietati[c]))

        # gate 5, versione minima: se c'e' un'animazione, ci vuole il ramo reduce
        ha_moto = ("animation" in pulito) or ("transition" in pulito)
        ha_script = "<script" in html
        if ha_script and "prefers-reduced-motion" not in html:
            errori.append("%s - ha JavaScript ma nessun ramo prefers-reduced-motion (gate 5, §7)" % nome)

        origine, quando = scheda_riassunto(scheda)
        voci.append({
            "id": nome,
            "origine": ripulisci(origine),
            "quando": ripulisci(quando),
            "moto": ha_moto,
            "script": ha_script,
            "colori": len(trovati),
        })

    # ------------------------------------------------------------------ HTML
    blocchi = []
    for v in voci:
        segni = []
        if v["moto"]:
            segni.append("moto")
        if v["script"]:
            segni.append("script")
        segni_html = "".join('<span class="tag">%s</span>' % s for s in segni)
        blocchi.append("""
  <section class="voce" id="%(id)s">
    <header class="voce__testa">
      <h2>%(id)s %(segni)s</h2>
      <p class="voce__origine">%(origine)s</p>
      <p class="voce__quando"><strong>Quando:</strong> %(quando)s</p>
      <p class="voce__link">
        <a href="%(id)s/pattern.html" target="_blank" rel="noopener">apri intero</a> &middot;
        <a href="%(id)s/scheda.md" target="_blank" rel="noopener">scheda</a>
      </p>
    </header>
    <div class="voce__vetro">
      <iframe src="%(id)s/pattern.html" title="%(id)s" loading="lazy"></iframe>
    </div>
  </section>""" % {"id": v["id"], "segni": segni_html, "origine": v["origine"], "quando": v["quando"]})

    pagina = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galleria dei pattern &mdash; Fabbrica Siti</title>
<link rel="stylesheet" href="../canone/canone.css">
<style>
/* GENERATA da scripts/galleria.py. Non modificare a mano: la prossima
   esecuzione cancella qualunque modifica. */
body { padding: 0 0 6rem; }
.testa { width: min(1100px, 92vw); margin: 0 auto; padding: 4rem 0 2rem; }
.testa h1 { margin: 0 0 .6rem; font-size: clamp(32px, 5vw, 64px); }
.testa p { margin: 0; max-width: 64ch; color: rgba(249,249,249,.76); line-height: 1.66; }
.conteggio { margin-top: 1.4rem; display: flex; gap: .6rem; flex-wrap: wrap; }
.voce { width: min(1100px, 92vw); margin: 0 auto 4rem; }
.voce__testa { padding: 1.6rem 0 1rem; border-top: 1px solid rgba(249,249,249,.15); }
.voce__testa h2 { margin: 0 0 .4rem; font-size: clamp(20px, 2.6vw, 30px); }
.voce__origine, .voce__quando, .voce__link { margin: .25rem 0; font-size: .9rem;
  color: rgba(249,249,249,.62); line-height: 1.6; }
.voce__quando { color: rgba(249,249,249,.76); max-width: 64ch; }
.voce__link a { color: #fb4604; }
.tag { display: inline-block; margin-left: .5rem; padding: .18em .6em; border-radius: 9999px;
  background: rgba(251,70,4,.16); color: #ff6a2e; font-size: .6em; font-weight: 700;
  letter-spacing: .08em; text-transform: uppercase; vertical-align: middle; }
.voce__vetro { border: 1px solid rgba(249,249,249,.10); border-radius: 20px; overflow: hidden;
  background: #0a0a0a; }
.voce__vetro iframe { display: block; width: 100%%; height: 620px; border: 0; }
code { font-size: .92em; }
</style>
</head>
<body class="grain-fine">
<div class="page">

  <header class="testa">
    <h1><span class="text-silver-white">Galleria dei</span> <span class="text-silver-orange">pattern</span></h1>
    <p>Ogni pattern qui sotto e' <strong>codice che gira</strong>, non una scheda che lo descrive.
    Quello che vedi nel riquadro e' il file vero, aperto in un iframe, che importa lo stesso
    <code>canone.css</code> di qualunque sito dell'Impero.</p>
    <div class="conteggio">
      <span class="bubble-orange">%(n)d pattern</span>
      <span class="bubble-silver">generata da scripts/galleria.py</span>
    </div>
  </header>
%(blocchi)s

</div>
</body>
</html>
""" % {"n": len(voci), "blocchi": "\n".join(blocchi)}

    io.open(USCITA, "w", encoding="utf-8").write(pagina)

    # ----------------------------------------------------------------- esito
    print("GALLERIA - Fabbrica Siti")
    print("  pattern trovati : %d" % len(voci))
    for v in voci:
        print("    - %-24s %2d colori%s%s" % (
            v["id"], v["colori"],
            "  moto" if v["moto"] else "",
            "  script" if v["script"] else ""))
    print("  scritta         : %s" % os.path.relpath(USCITA, os.getcwd()))

    if errori:
        print("\n  FAIL - %d problemi:" % len(errori))
        for e in errori:
            print("    - " + e)
        return 1

    print("\n  PASS - tutti i pattern sono dentro il canone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
