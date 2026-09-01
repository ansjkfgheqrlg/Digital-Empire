"""
Progetto Preventa (Reparto Produzione) - genera un carosello Preventa end-to-end:
copy (Agents/copywriter_agent_preventa.py, nuovo) -> visual (ArenaAI/arena_generator.py
del progetto Agency, RIUSATO via import, non copiato - ADR-003).

Uso:
    python orchestrator_preventa.py                  # topic auto (pain point tempo perso)
    python orchestrator_preventa.py "annunci esteri"  # topic specifico

Nota tecnica (verificata leggendo arena_generator.py, non assunta): la generazione
NON usa una chat Arena persistente - ogni slide riapre https://arena.ai/ da capo e la
continuita' stilistica viene dal ricaricare l'immagine della slide precedente come
allegato. L'unica cosa da isolare da Agency e' DOVE finiscono i file (LOCAL_DOWNLOAD_DIR)
e QUALI immagini di riferimento vengono allegate alla slide 1 (ALLEGATI_DIR) - fatto qui
sovrascrivendo questi due attributi sul modulo `config` condiviso, subito prima della
chiamata (stesso processo, stesso oggetto config in sys.modules).
"""
from __future__ import annotations

import os
import sys

# Console Windows di default e' cp1252 - crasha su emoji (il copywriter le mette
# nella caption apposta, il prompt lo chiede). Stesso bug/fix gia' noto nella
# fabbrica YouTube (vedi CP-20260731-001, "stdout via reconfigure()").
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
sys.path.insert(0, PROJECT_DIR)
sys.path.insert(0, AGENCY_DIR)

from Agents.copywriter_agent_preventa import generate_carousel_copy_preventa  # noqa: E402
import config_preventa  # noqa: E402


def get_final_carousel_plan_preventa(topic: str | None = None):
    print("[Orchestrator Preventa] Avvio generazione copy...")
    res = generate_carousel_copy_preventa(topic)

    if not res or "slides" not in res:
        print("[Orchestrator Preventa] Fallimento critico nella generazione del testo.")
        return None, None, None

    slides = res["slides"]
    descrizione = res.get("descrizione", "")
    print(f"[Orchestrator Preventa] Generato carosello di {len(slides)} slide.")

    import re
    try:
        text_clean = slides[0]["testo_esatto"].replace(" ", "_")
        topic_name = re.sub(r"[^a-zA-Z0-9_]", "", text_clean).strip()[:30] or "Carosello_Preventa"
    except Exception:
        topic_name = "Carosello_Preventa"

    return slides, descrizione, topic_name


def main():
    topic = sys.argv[1] if len(sys.argv) > 1 else None
    slides, descrizione, topic_name = get_final_carousel_plan_preventa(topic)
    if not slides:
        sys.exit(1)

    print(f"\nTopic: {topic_name}\nDescrizione: {descrizione}\nSlide:")
    for s in slides:
        print(f"  {s['slide_numero']}. [{s['titolo_nascosto']}] {s['testo_esatto']}")

    # Isola l'output e i reference Preventa da quelli Agency sul modulo config
    # condiviso (import config al suo interno risolve allo stesso modulo Agency,
    # per come sys.path e' costruito - vedi nota tecnica in cima al file).
    import config as agency_config  # noqa: E402 - stesso modulo usato da arena_generator
    agency_config.LOCAL_DOWNLOAD_DIR = config_preventa.LOCAL_DOWNLOAD_DIR
    agency_config.ALLEGATI_DIR = config_preventa.ALLEGATI_DIR

    from ArenaAI.arena_generator import generate_carousel_visuals  # noqa: E402
    generate_carousel_visuals(slides, topic_name)


if __name__ == "__main__":
    main()
