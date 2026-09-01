"""Test del comando unico caroselli.py.

Ogni caso qui sotto nasce da un difetto reale visto su questo motore il
2026-08-25, non da una casistica immaginata. Nessuno di questi test apre un
browser o chiama un modello: la parte che parla con la rete e' isolata dietro
`genera_copy`, tutto il resto e' deterministico e si prova a secco.

    python -m pytest "SKILL & Agenti/Workflow agency creative/tests" -q
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import caroselli  # noqa: E402


# --------------------------------------------------------------------------- #
# Il copy passa dai controlli PRIMA di diventare un PNG
# --------------------------------------------------------------------------- #

def _copy_valido(n=3):
    slides = [{"numero": 1, "tipo": "hook-cover", "testo_piccolo": "occhiello",
               "testo_grande": "quanto tempo perdi", "testo_accent": "tempo"}]
    for i in range(2, n):
        slides.append({"numero": i, "tipo": "quote-block", "testo_piccolo": "o",
                       "testo_grande": f"frase numero {i}", "testo_accent": "frase"})
    slides.append({"numero": n, "tipo": "cta-finale", "testo_piccolo": "o",
                   "testo_grande": "scopri preventa", "testo_accent": "scopri"})
    return {"titolo": "titolo breve", "caption": "caption con #hashtag", "slides": slides}


def test_copy_valido_passa():
    assert caroselli.valida_copy(_copy_valido(3), 3) == []


def test_numero_slide_sbagliato_viene_rifiutato():
    problemi = caroselli.valida_copy(_copy_valido(3), 6)
    assert any("attese 6 slide" in p for p in problemi)


def test_lineetta_lunga_nella_caption_viene_rifiutata():
    """Regola di casa: la lineetta lunga e' la firma piu' riconoscibile del testo
    scritto da una macchina. Il prompt la vieta, ma un prompt che chiede una
    regola non e' una regola: qui si controlla davvero."""
    copy = _copy_valido(3)
    copy["caption"] = "risparmia tempo — e vendi di piu"
    problemi = caroselli.valida_copy(copy, 3)
    assert any("lineetta lunga" in p for p in problemi)


def test_lineetta_lunga_in_una_slide_viene_rifiutata():
    copy = _copy_valido(3)
    copy["slides"][0]["testo_grande"] = "venti minuti -- persi"
    assert any("lineetta lunga" in p for p in caroselli.valida_copy(copy, 3))


def test_accent_che_non_esiste_nel_testo_viene_rifiutato():
    """Se la parola accent non compare nel testo grande, il render non colora
    niente e la slide esce piatta senza che nessuno se ne accorga."""
    copy = _copy_valido(3)
    copy["slides"][0]["testo_accent"] = "inesistente"
    assert any("non compare in testo_grande" in p for p in caroselli.valida_copy(copy, 3))


def test_testo_troppo_lungo_viene_rifiutato():
    copy = _copy_valido(3)
    copy["slides"][0]["testo_grande"] = "una frase molto lunga che non entra mai nella slide"
    assert any("max 7" in p for p in caroselli.valida_copy(copy, 3))


def test_tipo_di_slide_inventato_viene_rifiutato():
    copy = _copy_valido(3)
    copy["slides"][1]["tipo"] = "mega-slide"
    assert any("non esiste" in p for p in caroselli.valida_copy(copy, 3))


# --------------------------------------------------------------------------- #
# Il JSON del modello arriva quasi sempre dentro un blocco markdown
# --------------------------------------------------------------------------- #

def test_json_dentro_un_blocco_markdown():
    grezzo = 'Ecco il carosello:\n```json\n{"titolo": "x"}\n```\nSpero vada bene.'
    assert caroselli._estrai_json(grezzo) == {"titolo": "x"}


def test_json_con_chiacchiere_intorno_e_senza_blocco():
    assert caroselli._estrai_json('Certo! {"titolo": "x"} Fammi sapere.') == {"titolo": "x"}


# --------------------------------------------------------------------------- #
# Nomi di cartella
# --------------------------------------------------------------------------- #

def test_slug_toglie_accenti_e_spazi():
    assert caroselli.slug("Perché perdi tempo così") == "perche-perdi-tempo-cosi"


def test_slug_non_finisce_mai_vuoto():
    assert caroselli.slug("!!!???") == "carosello"


def test_piano_mette_in_minuscolo_e_rinumera():
    copy = _copy_valido(3)
    copy["slides"][0]["numero"] = 9
    copy["slides"][0]["testo_grande"] = "QUANTO TEMPO PERDI"
    piano = caroselli.costruisci_piano(copy, "preventa")
    assert [s["numero"] for s in piano["slides"]] == [1, 2, 3]
    assert piano["slides"][-1]["testo_grande"] == "quanto tempo perdi"


# --------------------------------------------------------------------------- #
# GATE: si guardano i file veri, non il log del render
# --------------------------------------------------------------------------- #

def _cartella_finta(tmp_path, n=3, lato=1080, peso=20000):
    from PIL import Image
    for i in range(1, n + 1):
        img = Image.new("RGB", (lato, lato), (16, 30, 62))
        # rumore, altrimenti il PNG di un colore piatto pesa pochi byte e il
        # test del peso minimo scatterebbe per il motivo sbagliato
        px = img.load()
        for x in range(0, lato, 3):
            for y in range(0, lato, 3):
                px[x, y] = ((x * 7) % 255, (y * 13) % 255, 90)
        img.save(tmp_path / f"slide_{i:02d}.png")
    (tmp_path / "caption.txt").write_text("caption vera", encoding="utf-8")
    (tmp_path / "copy.json").write_text(json.dumps({"titolo": "x"}), encoding="utf-8")
    return tmp_path


def test_gate_passa_su_un_carosello_completo(tmp_path):
    assert caroselli.gate(_cartella_finta(tmp_path, 3), 3) == []


def test_gate_prende_una_slide_mancante(tmp_path):
    problemi = caroselli.gate(_cartella_finta(tmp_path, 2), 3)
    assert any("2 PNG invece di 3" in p for p in problemi)


def test_gate_prende_le_dimensioni_sbagliate(tmp_path):
    problemi = caroselli.gate(_cartella_finta(tmp_path, 1, lato=512), 1)
    assert any("512x512" in p for p in problemi)


def test_gate_prende_un_png_praticamente_vuoto(tmp_path):
    """Il difetto che questo motore ha gia' prodotto: run senza eccezioni,
    file creati, contenuto assente."""
    _cartella_finta(tmp_path, 1)
    (tmp_path / "slide_01.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 50)
    assert any("sotto il minimo" in p for p in caroselli.gate(tmp_path, 1))


def test_gate_prende_la_caption_vuota(tmp_path):
    _cartella_finta(tmp_path, 1)
    (tmp_path / "caption.txt").write_text("   ", encoding="utf-8")
    assert any("caption.txt vuoto" in p for p in caroselli.gate(tmp_path, 1))


# --------------------------------------------------------------------------- #
# Prerequisiti del render: errori che si spiegano da soli
# --------------------------------------------------------------------------- #

def test_render_dice_cosa_fare_se_le_dipendenze_sono_a_meta(tmp_path, monkeypatch):
    """Successo reale il 2026-08-25: `npm install` interrotto a meta' lascia
    node_modules/puppeteer SENZA package.json, npm esce 0 e Node non risolve
    piu' il modulo. L'errore grezzo di Node non dice cosa fare."""
    finta = tmp_path / "carousel-factory"
    (finta / "node_modules" / "puppeteer").mkdir(parents=True)
    monkeypatch.setattr(caroselli, "FACTORY_DIR", finta)
    with pytest.raises(RuntimeError, match="npm install"):
        caroselli.render({"brand": "preventa", "slides": [], "titolo": "x", "caption": "y"})


def test_render_dice_se_il_brand_non_esiste(tmp_path, monkeypatch):
    finta = tmp_path / "carousel-factory"
    (finta / "node_modules" / "puppeteer").mkdir(parents=True)
    (finta / "node_modules" / "puppeteer" / "package.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(caroselli, "FACTORY_DIR", finta)
    with pytest.raises(FileNotFoundError, match="Brand 'inesistente'"):
        caroselli.render({"brand": "inesistente", "slides": [], "titolo": "x", "caption": "y"})


def test_prodotto_sconosciuto_elenca_quelli_veri():
    with pytest.raises(KeyError, match="Preventa"):
        caroselli._carica_prodotto("ProdottoCheNonEsiste")


# --------------------------------------------------------------------------- #
# Il ritentativo deve IMPARARE, non ripetere la stessa domanda
# --------------------------------------------------------------------------- #

def _finto_client(risposte: list[str], registro: list):
    """Sostituisce Agents.ai_client.call_ai senza toccare la rete."""
    import types

    def call_ai(messages, **kwargs):
        registro.append(messages)
        return risposte[min(len(registro) - 1, len(risposte) - 1)]

    modulo = types.ModuleType("Agents.ai_client")
    modulo.call_ai = call_ai
    pacchetto = types.ModuleType("Agents")
    pacchetto.ai_client = modulo
    return pacchetto, modulo


def test_il_ritentativo_riporta_al_modello_i_problemi_trovati(monkeypatch):
    """IL difetto, visto al secondo run reale del 2026-08-27: il comando
    ritentava mandando lo stesso identico prompt, il modello sforava di nuovo il
    limite di parole e il run moriva. Un tentativo cieco e' la stessa domanda
    fatta piu' forte."""
    cattivo = json.dumps({
        "titolo": "titolo", "caption": "caption",
        "slides": [
            {"numero": 1, "tipo": "hook-cover", "testo_piccolo": "o",
             "testo_grande": "una frase decisamente troppo lunga per stare in una slide",
             "testo_accent": "frase"},
            {"numero": 2, "tipo": "quote-block", "testo_piccolo": "o",
             "testo_grande": "frase due", "testo_accent": "frase"},
            {"numero": 3, "tipo": "cta-finale", "testo_piccolo": "o",
             "testo_grande": "scopri preventa", "testo_accent": "scopri"},
        ]})
    buono = json.dumps(_copy_valido(3))

    registro: list = []
    pacchetto, modulo = _finto_client([cattivo, buono], registro)
    monkeypatch.setitem(sys.modules, "Agents", pacchetto)
    monkeypatch.setitem(sys.modules, "Agents.ai_client", modulo)

    prodotto = {"brief": "b", "cta": "c", "tono": "t"}
    dati = caroselli.genera_copy(prodotto, "argomento", 3, tentativi=3)

    assert dati["titolo"] == "titolo breve"        # ha usato la seconda risposta
    assert len(registro) == 2                       # e ha ritentato una volta sola
    secondo_giro = registro[1]
    assert secondo_giro[-1]["role"] == "user"
    assert "max 7" in secondo_giro[-1]["content"]   # il difetto e' tornato al modello
    assert secondo_giro[1]["role"] == "assistant"   # con la sua risposta sbagliata


def test_se_il_copy_non_passa_mai_il_comando_lo_dice_e_non_renderizza(monkeypatch):
    cattivo = json.dumps({"titolo": "t", "caption": "c", "slides": []})
    registro: list = []
    pacchetto, modulo = _finto_client([cattivo], registro)
    monkeypatch.setitem(sys.modules, "Agents", pacchetto)
    monkeypatch.setitem(sys.modules, "Agents.ai_client", modulo)

    with pytest.raises(RuntimeError, match="dopo 2 tentativi"):
        caroselli.genera_copy({"brief": "b", "cta": "c", "tono": "t"},
                              "argomento", 3, tentativi=2)
    assert len(registro) == 2
