"""
Test dei controlli e dei formati aggiunti il 2026-08-23.

Ogni caso qui dentro riproduce un difetto REALE trovato leggendo il workflow, non un caso
di scuola:

  - il verdetto usciva `pubblicabile: true` quando le pagine non erano state contate;
  - la regola "niente lineette" non guardava il copy, e tre lineette sono finite nella
    descrizione di un libro consegnato;
  - "mai un capitolo quasi identico a un altro" era una regola senza controllo;
  - il pacchetto non conteneva l'ebook, cioe' il formato che nei nostri generi fa il volume;
  - il libro non chiedeva la recensione a nessuno;
  - i primi tre libri sono usciti in tre nicchie diverse, con il controllo di nicchia gia'
    scritto e mai interrogato;
  - "sposta la cartella a mano quando pubblichi" non e' mai stato fatto.

Come il resto della suite: nessun test apre un browser, chiama un modello o pretende Word.

    python -m pytest tests/test_qualita_pacchetto.py -v
"""
from __future__ import annotations

import json
import sys
import xml.dom.minidom
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import (book_project, config, epub, gate_blocco, kdp, kdp_formatter,  # noqa: E402
                    magazzino, metriche, nicchia_attiva, paratesto, pubblicazione,
                    report_validazione, validators)

LINEETTA = "—"


# --------------------------------------------------------------------------- #
# 1. Capitoli che si ripetono — la regola n.2, che non aveva controllo
# --------------------------------------------------------------------------- #

def _prosa(seme: str, parole: int = 400) -> str:
    """Prosa finta ma con parole diverse per capitolo, come i capitoli veri."""
    return " ".join(f"{seme}{i % 37} parola{i}" for i in range(parole))


def test_capitolo_duplicato_viene_bloccato():
    testo = _prosa("bosco")
    problemi = validators.valida_ripetizioni({"cap_01": testo, "cap_02": testo})
    assert problemi and "si ripetono" in problemi[0]
    assert validators.ripetizioni_bloccanti(problemi) == problemi


def test_capitoli_diversi_non_vengono_segnalati():
    capitoli = {f"cap_{n:02d}": _prosa(f"scena{n}") for n in range(1, 9)}
    assert validators.valida_ripetizioni(capitoli) == []


def test_meta_capitolo_ricopiato_viene_preso():
    """Il caso vero da temere non e' la copia identica, e' la scena rifatta uguale."""
    base = _prosa("porto", 600)
    meta = " ".join(base.split()[:300]) + " " + _prosa("nuovo", 300)
    problemi = validators.valida_ripetizioni({"cap_04": base, "cap_17": meta})
    assert validators.ripetizioni_bloccanti(problemi), problemi


def test_soglie_ripetizione_stanno_larghe_dai_dati_veri():
    """Misurato sui 72 capitoli veri: il massimo legittimo era il 2,72%."""
    assert validators.SOGLIA_RIPETIZIONE_AVVISA > 0.0272
    assert validators.SOGLIA_RIPETIZIONE_BLOCCA >= 3 * 0.0272


# --------------------------------------------------------------------------- #
# 2. Copy KDP — il testo che si legge PRIMA di comprare
# --------------------------------------------------------------------------- #

def test_lineetta_nella_descrizione_viene_bloccata():
    """Difetto reale: 3 lineette nella descrizione di The Ninth Winter, gia' consegnata."""
    copy = {"descrizione": f"Rebecca is a midwife in Willow Creek {LINEETTA} steady hands."}
    problemi = validators.valida_copy_kdp(copy)
    assert len(problemi) == 1 and "lineetta" in problemi[0]


def test_lineetta_trovata_in_ogni_campo_del_copy():
    copy = {"sottotitolo": f"A Novel {LINEETTA} of sorts",
            "bio_autore": f"Vive al nord {LINEETTA} scrive di mare",
            "descrizione_html": f"<p>uno {LINEETTA} due</p>"}
    assert len(validators.valida_copy_kdp(copy)) == 3


def test_copy_pulito_passa():
    assert validators.valida_copy_kdp({
        "descrizione": "Una frase normale, con una virgola.",
        "keywords": ["cozy fantasy bookshop", "gentle fantasy"],
        "sottotitolo": "A Cozy Fantasy Novel"}) == []


def test_limiti_della_form_kdp():
    problemi = validators.valida_copy_kdp({
        "descrizione": "x" * (validators.KDP_MAX_DESCRIZIONE + 1),
        "keywords": ["k"] * (validators.KDP_MAX_KEYWORD + 1)})
    assert any("caratteri" in p for p in problemi)
    assert any("keyword" in p for p in problemi)


def test_copy_assente_non_e_un_difetto_del_copy():
    assert validators.valida_copy_kdp(None) == []
    assert validators.valida_copy_kdp({}) == []


# --------------------------------------------------------------------------- #
# 3. Prezzo contro il prezzo MISURATO della nicchia
# --------------------------------------------------------------------------- #

def test_prezzo_piu_del_doppio_della_nicchia_viene_segnalato():
    """Caso vero: The Ninth Winter a $12.99 con media rilevata $5.95."""
    assert validators.valida_prezzo(12.99, 5.95)


def test_prezzo_in_linea_non_dice_niente():
    assert validators.valida_prezzo(13.99, 21.19) == []


def test_senza_dato_di_nicchia_non_si_inventa_un_giudizio():
    assert validators.valida_prezzo(12.99, None) == []


# --------------------------------------------------------------------------- #
# 4. Verdetto: "non misurato" non e' "a posto"
# --------------------------------------------------------------------------- #

def test_controllo_non_eseguito_non_diventa_un_avviso_qualunque():
    v = report_validazione.ReportValidazione()
    v.aggiungi("Titolo sulla copertina", ["VERIFICA A MANO: manca Tesseract"], "non_verificato")
    d = v.to_dict()
    assert d["verifiche_non_eseguite"] and not d["avvisi"]
    assert d["pubblicabile"] is True     # non blocca...
    assert "NON ESEGUITI" in v.riepilogo()   # ...ma si vede


def test_il_verdetto_porta_con_se_il_numero_su_cui_ha_deciso():
    v = report_validazione.ReportValidazione(pagine_reali=118)
    assert v.to_dict()["pagine_reali"] == 118


@pytest.fixture
def libro_minimo(tmp_path, monkeypatch):
    """Un libro finto completo, con copertina: serve per far girare `assembla` per intero."""
    from PIL import Image

    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path / "in_lavorazione")
    monkeypatch.setattr(config, "LIBRI_PRONTI_DIR", tmp_path / "pronti")
    config.LIBRI_PRONTI_DIR.mkdir(parents=True, exist_ok=True)

    p = book_project.BookProject.crea("Libro Di Prova", "cozy mystery", capitoli=3)
    for n in range(1, 4):
        p.path_capitolo(n).write_text(f"# Cap {n}\n\n{_prosa(f'stanza{n}', 300)}.\n",
                                      encoding="utf-8")
    cover = tmp_path / "cover.png"
    Image.new("RGB", (1800, 2700), (30, 40, 60)).save(cover)
    return p, cover


def test_pagine_non_contate_bloccano_la_consegna(libro_minimo, monkeypatch):
    """IL difetto: con `if pagine_reali and ...`, un PDF non prodotto faceva sparire il
    controllo e il libro usciva pubblicabile senza che nessuno avesse contato una pagina."""
    from engine import book_output_manager

    progetto, cover = libro_minimo
    monkeypatch.setattr(book_output_manager, "converti_in_pdf", lambda *a, **k: None)
    esito = progetto.assembla(cover, forza=True)
    validazione = json.loads(
        (Path(esito["pacchetto"]) / "validazione.json").read_text(encoding="utf-8"))
    assert validazione["pubblicabile"] is False
    assert any("NON CONTATE" in b for b in validazione["bloccanti"])
    assert validazione["pagine_reali"] is None


def test_un_pdf_illeggibile_non_fa_cadere_la_consegna(tmp_path):
    """Prima bastava un PDF troncato e `assembla` moriva con l'eccezione di pdfminer,
    dopo aver fatto tutto il lavoro e senza lasciare un verdetto."""
    rotto = tmp_path / "rotto.pdf"
    rotto.write_bytes(b"%PDF-1.4\nnon sono un pdf vero")
    for esito in (validators.valida_numerazione_pagine(rotto),
                  validators.valida_sillabazione_pdf(rotto)):
        assert esito and esito[0].startswith("VERIFICA A MANO")


def test_pagine_contate_e_sufficienti_non_bloccano(libro_minimo, monkeypatch):
    from engine import book_output_manager

    progetto, cover = libro_minimo
    finto_pdf = progetto.dir / "finto.pdf"
    finto_pdf.write_bytes(b"%PDF-1.4\n" + b"/Type /Page \n" * 130)
    monkeypatch.setattr(book_output_manager, "converti_in_pdf",
                        lambda docx, pdf=None: finto_pdf)
    esito = progetto.assembla(cover, forza=True)
    validazione = json.loads(
        (Path(esito["pacchetto"]) / "validazione.json").read_text(encoding="utf-8"))
    assert validazione["pagine_reali"] == 130
    assert not any("NON CONTATE" in b for b in validazione["bloccanti"])


# --------------------------------------------------------------------------- #
# 5. EPUB — il formato che mancava del tutto
# --------------------------------------------------------------------------- #

@pytest.fixture
def epub_di_prova(tmp_path):
    libro = epub.LibroEpub(
        titolo="The Quiet Test", autore="Rebecca Prova",
        capitoli=[epub.CapitoloEpub(f"Chapter {n}", [_prosa(f"cap{n}", 120), "* * *"])
                  for n in range(1, 4)],
        sottotitolo="A Test Novel",
        pagine_iniziali=[("Copyright", ["Copyright (c) 2026"], False)],
        pagine_finali=[("A Word Before You Go", ["Grazie."], True)],
    )
    return epub.costruisci(libro, tmp_path / "prova.epub")


def test_epub_ha_il_mimetype_per_primo_e_non_compresso(epub_di_prova):
    """L'unica regola del formato che i lettori applicano alla lettera."""
    z = zipfile.ZipFile(epub_di_prova)
    assert z.namelist()[0] == "mimetype"
    assert z.getinfo("mimetype").compress_type == zipfile.ZIP_STORED
    assert z.read("mimetype") == b"application/epub+zip"


def test_epub_e_tutto_xml_valido(epub_di_prova):
    """Un solo file malformato e il lettore rifiuta il libro senza dire perche'."""
    z = zipfile.ZipFile(epub_di_prova)
    for nome in z.namelist():
        if nome.endswith((".xhtml", ".opf", ".ncx", ".xml")):
            xml.dom.minidom.parseString(z.read(nome))
    assert z.testzip() is None


def test_epub_contiene_tutti_i_capitoli_e_le_pagine_di_contorno(epub_di_prova):
    nomi = zipfile.ZipFile(epub_di_prova).namelist()
    assert sum(1 for n in nomi if n.startswith("OEBPS/cap")) == 3
    assert "OEBPS/front01.xhtml" in nomi and "OEBPS/back01.xhtml" in nomi


def test_epub_senza_capitoli_non_si_fa(tmp_path):
    with pytest.raises(ValueError):
        epub.costruisci(epub.LibroEpub(titolo="Vuoto", autore="X", capitoli=[]),
                        tmp_path / "vuoto.epub")


def test_copertina_dell_ebook_viene_alleggerita(tmp_path):
    """Su Kindle la consegna si paga a MB: la copertina del cartaceo pesa 2-6 MB.

    L'immagine di prova e' RUMORE, non un rettangolo pieno: un PNG a tinta unita si
    comprime da solo a pochi KB e non direbbe niente sul caso vero."""
    import io
    import random

    from PIL import Image

    random.seed(7)
    grande = tmp_path / "cover.png"
    rumore = Image.new("RGB", (1800, 2700))
    rumore.putdata([(random.randrange(256), random.randrange(256), random.randrange(256))
                    for _ in range(1800 * 2700)])
    rumore.save(grande)

    nome, byte = epub.copertina_per_ebook(grande)
    assert nome.endswith(".jpg")
    assert len(byte) < grande.stat().st_size / 2, "la copertina ebook deve pesare meno"
    assert max(Image.open(io.BytesIO(byte)).size) <= epub.COPERTINA_EBOOK_LATO_MAX


def test_conta_parole_epub_legge_il_file_non_la_struttura(epub_di_prova):
    assert epub.conta_parole_epub(epub_di_prova) > 300


def test_scarto_di_parole_fra_epub_e_docx_blocca():
    assert book_project.BookProject._controlla_epub(18000, 36000)
    assert book_project.BookProject._controlla_epub(36000, 36000) == []


# --------------------------------------------------------------------------- #
# 6. Paratesto — copyright, recensione, "Also by"
# --------------------------------------------------------------------------- #

def test_la_richiesta_di_recensione_non_usa_lineette():
    _titolo, paragrafi = paratesto.richiesta_recensione("Il Libro", "Autrice")
    assert not any(LINEETTA in p for p in paragrafi)


def test_la_richiesta_di_recensione_e_onesta_come_kdp_pretende():
    """KDP vieta di chiedere SOLO recensioni positive o di offrire qualcosa in cambio."""
    _t, paragrafi = paratesto.richiesta_recensione("Il Libro", "Autrice")
    testo = " ".join(paragrafi).lower()
    assert "honest review" in testo
    assert "five star" not in testo and "free" not in testo


def test_also_by_elenca_solo_i_libri_dello_stesso_autore():
    """E' anche la prova del problema di catalogo: tre nomi d'autore = pagina vuota."""
    catalogo = [{"titolo": "Altro Libro", "autore": "Maren Ashcroft"},
                {"titolo": "Di Un Altro", "autore": "Rebecca Miller"}]
    esito = paratesto.altri_libri("Maren Ashcroft", catalogo, "Questo Libro")
    assert esito is not None
    assert "Altro Libro" in esito[1][0]
    assert paratesto.altri_libri("Nome Solitario", catalogo, "Questo") is None


def test_pagina_copyright_nomina_titolo_e_autore():
    _t, paragrafi = paratesto.pagina_copyright("Il Libro", "Autrice", anno=2026)
    testo = " ".join(paragrafi)
    assert "Il Libro" in testo and "Autrice" in testo and "2026" in testo


def test_il_paratesto_non_conta_nel_numero_di_parole(tmp_path):
    """Se contasse, aggiungere il copyright regalerebbe ~250 parole al controllo che
    decide se il romanzo e' abbastanza lungo."""
    capitoli = [kdp_formatter.Chapter("Uno", ["parola " * 50])]
    senza = kdp_formatter.build_manuscript_docx(
        kdp_formatter.BookManuscript("T", "A", capitoli), tmp_path / "a.docx")
    con = kdp_formatter.build_manuscript_docx(
        kdp_formatter.BookManuscript("T", "A", capitoli,
                                     pagine_iniziali=[("Copyright", ["x " * 200])],
                                     pagine_finali=[("Fine", ["y " * 200])]),
        tmp_path / "b.docx")
    assert con.word_count == senza.word_count


# --------------------------------------------------------------------------- #
# 7. Metriche — il tempo, che non veniva misurato da niente
# --------------------------------------------------------------------------- #

@pytest.fixture
def progetto_per_metriche(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "LIBRI_DIR", tmp_path)
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path / "in_lavorazione")
    (tmp_path / "in_lavorazione" / "prova").mkdir(parents=True)
    return "prova"


def test_le_metriche_contano_bocciature_e_riconsegne(progetto_per_metriche):
    slug = progetto_per_metriche
    metriche.registra(slug, "progetto_creato")
    metriche.registra(slug, "blocco", esito="bocciato", motivi=["capitoli corti"])
    metriche.registra(slug, "blocco", esito="ok")
    metriche.registra(slug, "consegna", esito="non_pubblicabile", con_copertina=True)
    metriche.registra(slug, "consegna", esito="ok", con_copertina=True)
    r = metriche.riepilogo(slug)
    assert (r.blocchi_bocciati, r.blocchi_passati) == (1, 1)
    assert (r.consegne, r.consegne_bloccate) == (2, 1)
    assert "capitoli corti" in r.motivi_bocciatura
    assert r.minuti_attesa_copertina is not None


def test_le_metriche_non_fanno_mai_cadere_un_comando(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "LIBRI_DIR", tmp_path)
    metriche.registra("slug-che-non-esiste", "blocco", esito="ok")  # non deve sollevare
    assert metriche.riepilogo("slug-che-non-esiste").eventi == 0


def test_metriche_illeggibili_non_esplodono(progetto_per_metriche, tmp_path):
    slug = progetto_per_metriche
    (tmp_path / "in_lavorazione" / slug / "metriche.json").write_text("{rotto", encoding="utf-8")
    metriche.registra(slug, "blocco", esito="ok")
    assert metriche.riepilogo(slug).eventi == 1


# --------------------------------------------------------------------------- #
# 8. Disciplina di catalogo — il controllo che c'era e non veniva interrogato
# --------------------------------------------------------------------------- #

@pytest.fixture
def catalogo_con_nicchia(tmp_path, monkeypatch):
    monkeypatch.setattr(nicchia_attiva, "STATO_PATH", tmp_path / "nicchia.json")
    nicchia_attiva.imposta("cozy fantasy bookshop", 83.1, "misurata")
    return tmp_path


def test_libro_fuori_nicchia_viene_rifiutato(catalogo_con_nicchia):
    with pytest.raises(ValueError) as e:
        kdp._controlla_nicchia_catalogo("dark academia mystery", motivo=None)
    assert "nicchia del catalogo" in str(e.value)


def test_libro_nella_nicchia_passa_in_silenzio(catalogo_con_nicchia):
    assert kdp._controlla_nicchia_catalogo("Cozy Fantasy Bookshop", motivo=None) is None


def test_scarto_dichiarato_e_permesso(catalogo_con_nicchia):
    nota = kdp._controlla_nicchia_catalogo("dark academia mystery", motivo="prova di nicchia")
    assert "DICHIARATO" in nota


def test_senza_nicchia_attiva_si_avvisa_ma_non_si_blocca(tmp_path, monkeypatch):
    monkeypatch.setattr(nicchia_attiva, "STATO_PATH", tmp_path / "vuoto.json")
    assert "Nessuna nicchia" in kdp._controlla_nicchia_catalogo("qualsiasi", None)


# --------------------------------------------------------------------------- #
# 9. Pubblicazione — lo step manuale che non e' mai stato eseguito
# --------------------------------------------------------------------------- #

@pytest.fixture
def libro_da_archiviare(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "LIBRI_DIR", tmp_path)
    monkeypatch.setattr(config, "LIBRI_PRONTI_DIR", tmp_path / "pronti")
    monkeypatch.setattr(config, "LIBRI_PUBBLICATI_DIR", tmp_path / "pubblicati")
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path / "in_lavorazione")
    monkeypatch.setattr(magazzino, "MAGAZZINO_PATH", tmp_path / "magazzino.json")
    monkeypatch.setattr(nicchia_attiva, "STATO_PATH", tmp_path / "nicchia.json")

    p = book_project.BookProject.crea("Libro Archiviabile", "cozy mystery", capitoli=2)
    for n in (1, 2):
        p.path_capitolo(n).write_text(f"# Cap {n}\n\n{_prosa(f's{n}', 80)}.\n", encoding="utf-8")
    pacchetto = config.LIBRI_PRONTI_DIR / "Libro_Archiviabile"
    pacchetto.mkdir(parents=True)
    (pacchetto / "validazione.json").write_text(
        json.dumps({"pubblicabile": True, "pagine_reali": 118, "bloccanti": [],
                    "verifiche_non_eseguite": []}), encoding="utf-8")
    (pacchetto / "Libro_Archiviabile.docx").write_bytes(b"finto")
    return p, pacchetto


def test_pubblicato_archivia_registra_e_toglie_i_doppioni(libro_da_archiviare):
    progetto, _pacchetto = libro_da_archiviare
    esito = pubblicazione.pubblica(progetto.slug, asin="B0TEST1234")
    assert esito.cartella.exists() and not progetto.dir.exists()
    scheda = json.loads((esito.cartella / "pubblicazione.json").read_text(encoding="utf-8"))
    assert scheda["asin"] == "B0TEST1234"
    assert scheda["url_amazon"].endswith("B0TEST1234")
    # I sorgenti viaggiano col libro: cancellare la lavorazione non perde niente
    assert (esito.cartella / "sorgenti" / "capitoli" / "cap_01.md").exists()
    assert esito.file_sorgente_copiati >= 3


def test_pubblicato_rifiuta_un_libro_non_pubblicabile(libro_da_archiviare):
    progetto, pacchetto = libro_da_archiviare
    (pacchetto / "validazione.json").write_text(
        json.dumps({"pubblicabile": False, "bloccanti": ["pagine reali 90"]}), encoding="utf-8")
    with pytest.raises(pubblicazione.NonPubblicabile):
        pubblicazione.pubblica(progetto.slug, asin="B0TEST1234")
    assert progetto.dir.exists(), "un rifiuto non deve cancellare niente"


def test_pubblicato_non_sovrascrive_un_archivio_esistente(libro_da_archiviare):
    progetto, _p = libro_da_archiviare
    (config.LIBRI_PUBBLICATI_DIR / "Libro_Archiviabile").mkdir(parents=True)
    with pytest.raises(FileExistsError):
        pubblicazione.pubblica(progetto.slug, asin="B0TEST1234")


def test_tieni_lavorazione_non_cancella(libro_da_archiviare):
    progetto, _p = libro_da_archiviare
    esito = pubblicazione.pubblica(progetto.slug, asin="B0X", tieni_lavorazione=True)
    assert progetto.dir.exists() and not esito.lavorazione_rimossa


def test_il_libro_pubblicato_finisce_nel_catalogo_della_nicchia(libro_da_archiviare):
    progetto, _p = libro_da_archiviare
    nicchia_attiva.imposta("cozy mystery", 70.0, "misurata")
    pubblicazione.pubblica(progetto.slug, asin="B0X")
    assert "Libro Archiviabile" in nicchia_attiva.carica().libri_pubblicati


# --------------------------------------------------------------------------- #
# 10. Il gate rapido prende anche le ripetizioni
# --------------------------------------------------------------------------- #

def test_il_gate_prende_due_capitoli_uguali(tmp_path, monkeypatch):
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    p = book_project.BookProject.crea("Libro Doppio", "cozy mystery")
    for n in range(1, 9):
        seme = "identico" if n in (3, 6) else f"scena{n}"
        p.path_capitolo(n).write_text(f"# Cap {n}\n\n{_prosa(seme, 1600)}.\n", encoding="utf-8")
    p.riassunti_path.write_text(
        "# R\n\n## Fili aperti\n\n## Capitoli\n\n"
        + "\n".join(f"### cap_{n:02d}\n- Succede: cose\n" for n in range(1, 9)),
        encoding="utf-8")
    esito = gate_blocco.controlla(p)
    assert not esito.si_prosegue
    assert any("si ripetono" in b for b in esito.blocchi), esito.blocchi
