# -*- coding: utf-8 -*-
"""Test di produci_video_completo.py::consegna_a_max — il brief copertina per Max.

Copre i due rami dichiarati dal task: brief RICCO (testo gia' spezzato riga per riga +
riferimento alla copertina reale del video sorgente) quando brief-miniatura.json c'e' su
disco, brief GENERICO (il testo di sempre, invariato) quando manca — perche' un video che
non si consegna per un file di contorno mancante e' un danno peggiore del brief povero.

Nessuna rete: tutto lavora su una cartella temporanea, con i costanti di modulo
(TEMPLATES_DIR, VIDEO_PRONTI_DIR) rimpiazzati a mano — niente fixture pytest (tmp_path,
monkeypatch), cosi' il runner autonomo in fondo puo' eseguire OGNI test, non solo
"saltarlo" come richiederebbe pytest."""
from __future__ import annotations

import json
import os
import shutil
import tempfile

import produci_video_completo as pvc


# --------------------------------------------------------------------------------------
# Helper: ambiente isolato. Sostituisce TEMPLATES_DIR/VIDEO_PRONTI_DIR del modulo con
# cartelle temporanee e li ripristina sempre, anche se il test fallisce.
# --------------------------------------------------------------------------------------
class _AmbienteIsolato:
    def __enter__(self):
        self._templates_originale = pvc.TEMPLATES_DIR
        self._video_pronti_originale = pvc.VIDEO_PRONTI_DIR
        self._popen_originale = pvc.subprocess.Popen
        self._tmp = tempfile.mkdtemp(prefix="test_consegna_brief_")
        pvc.TEMPLATES_DIR = os.path.join(self._tmp, "05-TEMPLATES-E-KIT")
        pvc.VIDEO_PRONTI_DIR = os.path.join(self._tmp, "VIDEO-PRONTI")
        os.makedirs(pvc.TEMPLATES_DIR, exist_ok=True)
        # explorer non deve aprirsi davvero durante un test automatico.
        pvc.subprocess.Popen = lambda *a, **k: None
        return self._tmp

    def __exit__(self, *exc):
        pvc.TEMPLATES_DIR = self._templates_originale
        pvc.VIDEO_PRONTI_DIR = self._video_pronti_originale
        pvc.subprocess.Popen = self._popen_originale
        shutil.rmtree(self._tmp, ignore_errors=True)
        return False


def _scrivi_brief_ricco(templates_dir: str) -> str:
    """Un brief-miniatura.json come quello reale scritto da apex7_orchestrator.run_phase_5
    (stessi campi verificati in 05-TEMPLATES-E-KIT/brief-miniatura.json su disco), con una
    copertina sorgente VERA presente sul filesystem — non solo dichiarata nel JSON."""
    os.makedirs(os.path.join(templates_dir, "source-thumbnail"), exist_ok=True)
    rel_immagine = os.path.join("source-thumbnail", "canale-XABjAjqfUxw-maxres.jpg")
    with open(os.path.join(templates_dir, rel_immagine), "wb") as f:
        f.write(b"\xff\xd8\xff\xe0fake-jpeg-per-test")
    brief = {
        "title": "Il Trucco Psicologico Che Rende Un Uomo Irresistibile",
        "source_video_id": "XABjAjqfUxw",
        "source_thumbnail": rel_immagine,
        "source_style": "Copertina reale del video sorgente @canale, da adattare mantenendone il linguaggio visivo.",
        "concept": "scene inspired by the real hook (Statement): \"C'e' un dettaglio che decide...\"",
        "text_overlay_lines": [
            "IL TRUCCO PSICOLOGICO CHE RENDE",
            "UN UOMO IRRESISTIBILE FIN DAL",
            "PRIMO SGUARDO",
        ],
        "text_overlay_highlight_lines": [
            "IL TRUCCO PSICOLOGICO CHE RENDE",
            "PRIMO SGUARDO",
        ],
    }
    path = os.path.join(templates_dir, "brief-miniatura.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(brief, f, ensure_ascii=False, indent=2)
    return path


# --------------------------------------------------------------------------------------
# Ramo 1 — brief RICCO: JSON presente, immagine sorgente presente
# --------------------------------------------------------------------------------------
def test_righe_brief_copertina_usa_il_brief_ricco_quando_il_json_ce():
    with _AmbienteIsolato() as tmp:
        _scrivi_brief_ricco(pvc.TEMPLATES_DIR)
        righe = pvc._righe_brief_copertina("Titolo Finale Di Prova")
        testo = "\n".join(righe)

        # le righe di testo sono usate COSI' COME SONO (gia' spezzate), non riscritte
        assert "IL TRUCCO PSICOLOGICO CHE RENDE" in testo
        assert "UN UOMO IRRESISTIBILE FIN DAL" in testo
        assert "PRIMO SGUARDO" in testo
        # le righe evidenziate portano il marcatore, quella centrale (non evidenziata) no
        idx_riga1 = next(i for i, r in enumerate(righe) if "IL TRUCCO PSICOLOGICO" in r)
        idx_riga2 = next(i for i, r in enumerate(righe) if "UN UOMO IRRESISTIBILE" in r)
        assert "<- evidenziata" in righe[idx_riga1]
        assert "<- evidenziata" not in righe[idx_riga2]

        # il riferimento visivo reale porta il percorso ASSOLUTO del file scaricato
        assert "Riferimento visivo reale" in testo
        percorso_atteso = os.path.join(pvc.TEMPLATES_DIR, "source-thumbnail",
                                       "canale-XABjAjqfUxw-maxres.jpg")
        assert percorso_atteso in testo
        assert os.path.exists(percorso_atteso)

        # stile e concept del brief arrivano nel testo consegnato a Max
        assert "Copertina reale del video sorgente @canale" in testo
        assert "C'e' un dettaglio che decide" in testo

        # quello che il brief generico dice gia' oggi non va perso
        assert '**Titolo:** "Titolo Finale Di Prova"' in testo
        assert "stampo Legami d'Amore" in testo
        assert "il titolo deve leggersi anche in miniatura piccola" in testo
        assert "il file .png va messo dentro questa stessa cartella" in testo


def test_righe_brief_copertina_ignora_riferimento_se_il_file_immagine_non_ce():
    """Il JSON dichiara una source_thumbnail ma il file non e' MAI stato scaricato per
    davvero (es. download fallito in F5, apex7_orchestrator._ensure_source_thumbnail lo
    gestisce gia' con un log e un source_thumbnail=None): niente percorso rotto nel brief."""
    with _AmbienteIsolato() as tmp:
        brief = {
            "title": "Titolo",
            "source_video_id": "abc123",
            "source_thumbnail": "source-thumbnail/non-esiste.jpg",
            "source_style": "stile",
            "concept": "concept",
            "text_overlay_lines": ["RIGA UNICA"],
            "text_overlay_highlight_lines": [],
        }
        with open(os.path.join(pvc.TEMPLATES_DIR, "brief-miniatura.json"), "w", encoding="utf-8") as f:
            json.dump(brief, f)
        righe = pvc._righe_brief_copertina("Titolo Finale")
        testo = "\n".join(righe)
        assert "RIGA UNICA" in testo  # il testo c'e' comunque
        assert "Riferimento visivo reale" not in testo  # ma il file non esiste, niente percorso rotto


# --------------------------------------------------------------------------------------
# Ramo 2 — brief GENERICO: JSON assente (produzione lanciata per un'altra strada)
# --------------------------------------------------------------------------------------
def test_righe_brief_copertina_degrada_al_generico_quando_il_json_manca():
    with _AmbienteIsolato() as tmp:
        assert not os.path.exists(os.path.join(pvc.TEMPLATES_DIR, "brief-miniatura.json"))
        righe = pvc._righe_brief_copertina("Titolo Generico")
        testo = "\n".join(righe)

        # il testo di sempre resta tutto presente
        assert '**Titolo:** "Titolo Generico"' in testo
        assert "stampo Legami d'Amore" in testo
        assert "il titolo deve leggersi anche in miniatura piccola" in testo
        assert "il file .png va messo dentro questa stessa cartella" in testo
        assert "upload in privato con le pubblicita' attive" in testo

        # nessuna sezione del brief ricco, perche' non c'e' niente da cui prenderla
        assert "Testo in copertina" not in testo
        assert "Riferimento visivo reale" not in testo
        assert "Stile da mantenere" not in testo


def test_righe_brief_copertina_degrada_al_generico_se_il_json_e_corrotto():
    """Un file presente ma illeggibile (scrittura interrotta, JSON troncato) non deve mai
    far esplodere la consegna: si comporta come se il file non ci fosse."""
    with _AmbienteIsolato() as tmp:
        with open(os.path.join(pvc.TEMPLATES_DIR, "brief-miniatura.json"), "w", encoding="utf-8") as f:
            f.write("{ questo non e' json valido ")
        assert pvc._leggi_brief_miniatura() is None
        righe = pvc._righe_brief_copertina("Titolo")
        assert "Testo in copertina" not in "\n".join(righe)


# --------------------------------------------------------------------------------------
# End-to-end: consegna_a_max scrive davvero copy.md, con lo stesso contenuto verificato sopra
# --------------------------------------------------------------------------------------
def _prepara_mp4_finto(tmp: str) -> str:
    mp4 = os.path.join(tmp, "video-finto.mp4")
    with open(mp4, "wb") as f:
        f.write(b"finto-contenuto-mp4-per-test")
    return mp4


def test_consegna_a_max_scrive_copy_md_con_brief_ricco_end_to_end():
    with _AmbienteIsolato() as tmp:
        _scrivi_brief_ricco(pvc.TEMPLATES_DIR)
        mp4 = _prepara_mp4_finto(tmp)
        lavoro = {"video_id": "XABjAjqfUxw", "canale_origine": "canale", "canale": "canaledest"}
        dest = pvc.consegna_a_max(mp4, "Titolo Video", lavoro)
        assert dest and os.path.isdir(dest)
        with open(os.path.join(dest, "copy.md"), encoding="utf-8") as f:
            copy_md = f.read()
        assert "IL TRUCCO PSICOLOGICO CHE RENDE" in copy_md
        assert "Riferimento visivo reale" in copy_md
        assert os.path.exists(os.path.join(dest, "video.mp4"))


def test_consegna_a_max_scrive_copy_md_generico_end_to_end_senza_json():
    with _AmbienteIsolato() as tmp:
        mp4 = _prepara_mp4_finto(tmp)
        lavoro = {"video_id": "abc", "canale_origine": "canale", "canale": "canaledest"}
        dest = pvc.consegna_a_max(mp4, "Titolo Video", lavoro)
        assert dest and os.path.isdir(dest)
        with open(os.path.join(dest, "copy.md"), encoding="utf-8") as f:
            copy_md = f.read()
        assert "Testo in copertina" not in copy_md
        assert "il titolo deve leggersi anche in miniatura piccola" in copy_md
        assert os.path.exists(os.path.join(dest, "video.mp4"))


# ---------------------------------------------------------------------------
# Runner autonomo (stesso schema di test_verifica_fatti.py): senza questo, `python
# test_<nome>.py` esce 0 SENZA ESEGUIRE NIENTE — un test silente e' peggio di nessun test,
# rassicura senza aver provato nulla. Gira sia con `pytest` sia con `python test_<nome>.py`.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys as _sys, traceback as _tb, inspect as _ins
    _falliti = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]
    _saltati = 0
    for _n, _f in _casi:
        if _ins.signature(_f).parameters:
            _saltati += 1
            print("SALTATO %s  (richiede pytest: %s)"
                  % (_n, ", ".join(_ins.signature(_f).parameters)))
            continue
        try:
            _f()
            print("OK      %s" % _n)
        except Exception:
            _falliti += 1
            print("FALLITO %s" % _n)
            _tb.print_exc()
    _eseguiti = len(_casi) - _saltati
    print("")
    print("%d/%d test passati (%d saltati, girano con: python -m pytest %s)"
          % (_eseguiti - _falliti, _eseguiti, _saltati, __file__.rsplit("\\", 1)[-1]))
    _sys.exit(1 if _falliti else 0)
