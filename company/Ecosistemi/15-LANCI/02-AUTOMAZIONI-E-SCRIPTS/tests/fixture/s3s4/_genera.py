# -*- coding: utf-8 -*-
"""Genera le fixture di S3/S4 (questa cartella) e l'esempio pubblico
(ECO/05-TEMPLATES-E-KIT/esempio-s3s4). Idempotente: riscrive gli stessi file.

    PYTHONIOENCODING=utf-8 python tests/fixture/s3s4/_genera.py

Perche' un generatore e non file scritti a mano: ricerca.json pretende 15 frasi,
apertura.json 10 voci, e i numeri (pareggio, scarti, ordini) devono tornare fra loro.
Un conto fatto da un programma resta coerente quando si cambia un prezzo; uno fatto a
mano no. I file prodotti restano leggibili e sono quelli che i test usano.

Tutti i dati sono DICHIARATAMENTE finti (`non_misurato` lo dice in ogni artefatto):
nessun numero qui e' stato misurato su un lancio vero.
"""
from __future__ import annotations

import json
import math
import os
import sys
from datetime import date, timedelta

QUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(QUI)))       # 02-AUTOMAZIONI-E-SCRIPTS
ECO = os.path.dirname(SCRIPTS_ROOT)                                          # 15-LANCI
ESEMPIO = os.path.join(ECO, "05-TEMPLATES-E-KIT", "esempio-s3s4")

NOTA_FINTO = "ESEMPIO: nessun numero di questo file e' stato misurato su un lancio vero"


def _scrivi(cartella, nome, dati):
    p = os.path.join(cartella, *nome.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        if isinstance(dati, str):
            f.write(dati)
        else:
            json.dump(dati, f, ensure_ascii=False, indent=2)
            f.write("\n")


def costruisci(lancio_id: str, *, esempio: bool) -> dict:
    """Ritorna {nome_file: contenuto} per un lancio completo e coerente.

    esempio=True: e' il kit pubblico — via_libera NON compilato (REG-1 deve bloccare),
    nessuna affermazione 'prova' (il kit non porta certificato/ricerca), transazione
    di prova dichiaratamente finta.
    """
    apertura = date(2026, 8, 3)
    durata = 7
    chiusura = apertura + timedelta(days=durata - 1)
    prezzo = 47.0
    pubblico = 1000
    scen = {
        "pessimista": (0.20, 0.02, "meta' del pubblico non apre; conversione da lista fredda"),
        "atteso": (0.30, 0.05, "tassi di comodo dichiarati assunti, non misurati"),
        "ottimista": (0.40, 0.08, "se il video di lancio porta traffico caldo"),
    }
    scenari = {}
    for k, (tv, ta, perche) in scen.items():
        copie = round(pubblico * tv * ta)
        scenari[k] = {"tasso_visita": tv, "tasso_acquisto": ta, "copie": copie,
                      "ricavo_lordo": round(copie * prezzo, 2), "perche_questo_scenario": perche}
    costo_pubblicita, costo_strumenti, costo_macchina = 200.0, 50.0, 15.0
    costo_totale = costo_pubblicita + costo_strumenti + costo_macchina
    copie_pareggio = math.ceil(costo_totale / prezzo)

    ordini_reali = 14
    ricavo_reale = ordini_reali * prezzo
    costi_reali = {"totale": 240.0, "macchina": 15.0, "pubblicita": 180.0, "strumenti": 45.0, "altro": 0.0}

    def scarto(prev, reale):
        return None if not prev else round((reale - prev) / prev * 100, 2)

    ts = lambda d, h="10:00:00": "%sT%s+00:00" % (d.isoformat(), h)  # noqa: E731
    giorni = [apertura + timedelta(days=i) for i in range(durata)]
    url = {"vendita": "https://esempio.invalid/manuale",
           "checkout": "https://esempio.invalid/manuale/checkout",
           "grazie": "https://esempio.invalid/manuale/grazie"}

    f = {}

    # --- a monte (S1/S2), minimi ma validi ------------------------------------
    f["pubblico.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "misurato_il": ts(date(2026, 7, 20)), "scade_il": "2026-08-19",
        "canali": [{"id": "lista-email", "tipo": "lista-email", "posseduto": True,
                    "raggiungibili_verificati": pubblico, "raggiungibili_dichiarati": 1200,
                    "prova": {"tipo": "esporto-lista", "riferimento": "esporto-lista-20260720.csv",
                              "data": "2026-07-20"}, "stato_tecnico": "attivo"}],
        "totale_raggiungibile_verificato": pubblico,
        "non_misurato": [NOTA_FINTO],
    }
    f["decisione.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id, "prodotto": "Prodotto di esempio",
        "domande": [
            {"id": "D1-prodotto-esiste", "testo": "Il prodotto esiste?", "risposta": "si", "sostenuta_da": "certificato.json"},
            {"id": "D2-pubblico-esiste", "testo": "Il pubblico esiste?", "risposta": "si", "sostenuta_da": "pubblico.json"},
            {"id": "D3-si-puo-incassare", "testo": "Si puo' incassare?", "risposta": "si", "sostenuta_da": "funnel.json"},
            {"id": "D4-capacita-nel-periodo", "testo": "C'e' capacita' nel periodo?", "risposta": "si", "sostenuta_da": "editoriale.json"},
            {"id": "D5-nessun-lancio-in-conflitto", "testo": "Nessun lancio in conflitto?", "risposta": "si", "sostenuta_da": "stato.json degli altri lanci"},
        ],
        "esito": "si-fa", "ragione_archiviazione": None, "non_misurato": [NOTA_FINTO],
    }
    f["certificato.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id, "modalita": "integrale",
        "file_prodotto": {"percorso": "prodotto/esempio.pdf", "byte": 1024, "formato": "application/pdf", "pagine": 10},
        "bandiere_rosse": [
            {"id": i, "presente": False, "come_verificata": "verifica di esempio, non eseguita davvero", "dettaglio": None}
            for i in ["RF1-nessun-output-pratico", "RF2-template-senza-esempio", "RF3-promessa-non-mantenuta",
                      "RF4-contenuto-non-originale", "RF5-link-morti", "RF6-consegna-non-provata"]],
        "link_testati": [{"url": url["vendita"], "codice": 200}],
        "debito_collaudo": None, "esito": "consegnabile", "non_misurato": [NOTA_FINTO],
    }
    categorie = ["dolore", "desiderio", "obiezione", "linguaggio", "confronto"]
    f["ricerca.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "frasi": [{"testo": "Frase di esempio numero %d, raccolta da nessuna parte" % i,
                   "fonte": {"url": "https://esempio.invalid/frase/%d" % i, "raccolta_il": "2026-07-15", "contesto": None},
                   "categoria": categorie[i % 5]} for i in range(15)],
        "campione_verificato": [{"url": "https://esempio.invalid/frase/%d" % i, "raggiungibile": True,
                                 "testo_ritrovato": True, "verificata_il": ts(date(2026, 7, 16))} for i in range(3)],
        "non_misurato": [NOTA_FINTO],
    }
    f["previsione.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id, "calcolata_il": ts(date(2026, 7, 21)),
        "formula": "ricavo_lordo = pubblico_raggiungibile * tasso_visita * tasso_acquisto * prezzo",
        "ingressi": {"pubblico_raggiungibile": pubblico, "prezzo": prezzo, "fonte_pubblico": "ART-PUB", "fonte_prezzo": "ART-OFF"},
        "scenari": scenari,
        "assunzioni": [{"nome": "tasso_visita", "valore": 0.30, "stato": "assunto", "fonte": None, "da_dove_viene_se_assunto": "numero di comodo"},
                       {"nome": "tasso_acquisto", "valore": 0.05, "stato": "assunto", "fonte": None, "da_dove_viene_se_assunto": "numero di comodo"}],
        "pareggio": {"copie_per_pareggio": copie_pareggio, "costo_totale_previsto": costo_totale, "include_costo_macchina": True},
        "non_misurato": [NOTA_FINTO],
    }
    f["offerta.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id, "ruolo_prodotto": "vendita",
        "prezzo": prezzo, "valuta": "EUR", "data_apertura": apertura.isoformat(),
        "durata_carrello_gg": durata, "data_chiusura": chiusura.isoformat(),
        "struttura": {"valore_dichiarato": 141.0, "rapporto_valore_prezzo": 3.0,
                      "bonus": [{"nome": "Checklist", "valore": 94.0, "fonte_valore": "prezzo-listino-proprio", "riferimento_fonte": "listino di esempio"}],
                      "garanzia": {"giorni": 14, "condizioni": "rimborso entro 14 giorni senza domande", "rinuncia_recesso_raccolta": True},
                      "motivo_per_agire_adesso": "il carrello chiude il %s" % chiusura.isoformat(),
                      "azione_richiesta": "compra il manuale"},
        "previsione_riferimento": {"file": "previsione.json", "ricavo_atteso": scenari["atteso"]["ricavo_lordo"]},
        "firma": {"chi": "ESEMPIO-nessuna-persona", "canale": "file-fuori-agenti",
                  "riferimento": "ESEMPIO: firma finta, nessuna persona ha firmato",
                  "proposta_impronta": "0" * 64, "il": ts(date(2026, 7, 22))},
        "non_misurato": [NOTA_FINTO, "la firma e' finta: serve solo a rendere il file valido per i gate S3/S4"],
    }

    # --- S3 ---------------------------------------------------------------------
    def blocchi(*coppie):
        return [{"nome": n, "punti": p, "punti_massimi": m, "assegnato_da": "giudice", "ancora": None}
                for n, p, m in coppie]
    aff_vendita = [{"testo": "Il carrello chiude il %s" % chiusura.isoformat(), "categoria": "promessa", "riferimento": None},
                   {"testo": "E' il manuale piu' chiaro che abbiamo scritto", "categoria": "opinione", "riferimento": None}]
    aff_email = [{"testo": "Rimborso entro 14 giorni", "categoria": "promessa", "riferimento": None}]
    if not esempio:
        aff_vendita.insert(0, {"testo": "Il manuale contiene output pratici verificati", "categoria": "prova",
                               "riferimento": "certificato.json#bandiere_rosse[0].come_verificata"})
        aff_email.append({"testo": "Lo dice il pubblico stesso", "categoria": "prova",
                          "riferimento": "ricerca.json#frasi[3].testo"})
    f["copy/manifest.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "pezzi": [
            {"id": "pagina-vendita", "tipo": "pagina-vendita", "file": "copy/pagina-vendita.md", "destinazione": "vendita",
             "punteggio": {"totale": 88, "blocchi": blocchi(("titolo", 18, 20), ("promessa", 25, 30), ("prova", 27, 30), ("chiamata", 18, 20))},
             "affermazioni": aff_vendita, "copertina_richiesta": None},
            {"id": "email-1", "tipo": "email", "file": "copy/email-1.md", "destinazione": "vendita",
             "punteggio": {"totale": 82, "blocchi": blocchi(("oggetto", 16, 20), ("corpo", 45, 60), ("chiamata", 16, 20))},
             "affermazioni": aff_email, "copertina_richiesta": None},
        ],
        "punteggio_totale": 85,
        "non_misurato": [NOTA_FINTO, "i punteggi sono di comodo, non assegnati da un giudice vero"]
                        + (["nessuna affermazione 'prova': il kit non porta certificato.json ne' ricerca.json"] if esempio else []),
    }
    f["copy/pagina-vendita.md"] = "# Pagina di vendita (esempio)\n\nTesto di esempio. Il carrello chiude il %s.\n" % chiusura.isoformat()
    f["copy/email-1.md"] = "Oggetto: esempio\n\nTesto di esempio. Rimborso entro 14 giorni.\n"

    rif_tx = "ESEMPIO-nessuna-transazione-vera" if esempio else "tx_prova_0001"
    f["funnel.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "pagine": [{"ruolo": r, "url": u, "codice_http": 200, "verificata_il": ts(date(2026, 7, 30)),
                    "evento_conversione": {"nome": "acquisto" if r == "grazie" else "vista_%s" % r,
                                           "prova": {"origine": "piattaforma-misura", "identificativo_evento": "ev_%s_001" % r,
                                                     "letto_il": ts(date(2026, 7, 30), "11:00:00")}},
                    "tempo_caricamento_ms": 800} for r, u in url.items()],
        "prova_cassa": {"stato": "incassato_e_rimborsato", "fornitore": "fornitore-di-esempio",
                        "riferimento_transazione": rif_tx, "importo": 1.0,
                        "eseguita_il": ts(date(2026, 7, 30), "12:00:00"), "consegna_verificata": True},
        "consenso": {"banner_presente": True, "misura_prima_del_consenso": False, "quota_consenso_stimata": None,
                     "nota": "esempio"},
        "non_misurato": [NOTA_FINTO, "le url sono di esempio: con ReteVera GATE-FNL-1 fallirebbe"],
    }
    f["editoriale.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "contenuti": [{"id": "c-%02d" % i, "data_uscita": g.isoformat(), "canale": "email" if i % 2 == 0 else "instagram",
                       "a_pagamento": False, "formato": "email" if i % 2 == 0 else "post",
                       "destinazione": "vendita" if i % 2 == 0 else url["vendita"], "stato": "pronto",
                       "pubblicato_il": None, "prova_pubblicazione": None, "copertina_richiesta": None,
                       "invio_reale": None} for i, g in enumerate(giorni)],
        "giorni_scoperti": [], "non_misurato": [NOTA_FINTO],
    }
    f["budget.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id, "tetto": 500.0,
        "voci": [{"nome": "pubblicita", "importo": costo_pubblicita, "tipo": "una-tantum", "stato": "previsto", "autorizzato_da": None},
                 {"nome": "strumenti", "importo": costo_strumenti, "tipo": "ricorrente", "stato": "previsto", "autorizzato_da": None},
                 {"nome": "chiamate ai modelli", "importo": costo_macchina, "tipo": "macchina", "stato": "previsto", "autorizzato_da": None}],
        "costo_totale_previsto": costo_totale, "costo_macchina_previsto": costo_macchina, "tetto_macchina": 15.0,
        "pareggio": {"copie": copie_pareggio, "calcolato_da": "previsione.json", "scenario_usato": "atteso"},
        "scarto_corrente": None, "non_misurato": [NOTA_FINTO],
    }
    voci_sync = ["copy approvato", "pagine online", "cassa provata", "calendario pieno", "budget sotto tetto",
                 "lista email caricata", "prezzo firmato", "garanzia scritta", "consegna automatica", "misura attiva"]
    f["apertura.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "lista_sincronizzazione": [{"voce": v, "esito": True, "verificata_il": ts(date(2026, 8, 2)), "come": "esempio"} for v in voci_sync],
        "artefatti_ricalcolati": [{"artefatto": a, "valido": True, "ricalcolato_il": ts(date(2026, 8, 2)), "motivo": None}
                                  for a in ["copy/manifest.json", "funnel.json", "editoriale.json", "budget.json"]],
        "via_libera": ({"chi": "", "canale": "comando-utente", "riferimento": "", "il": ts(date(2026, 8, 2))} if esempio
                       else {"chi": "Persona di prova", "canale": "comando-utente",
                             "riferimento": "lancio via-libera %s" % lancio_id, "il": ts(date(2026, 8, 2), "18:00:00")}),
        "non_misurato": [NOTA_FINTO] + (["via_libera NON compilato di proposito: GATE-REG-1 deve bloccare"] if esempio else []),
    }

    # --- S4 ---------------------------------------------------------------------
    f["consuntivo.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "periodo": {"dal": apertura.isoformat(), "al": chiusura.isoformat()},
        "ricavo_lordo": ricavo_reale, "ricavo_netto": round(ricavo_reale * 0.95, 2),
        "origine": {"tipo": "fornitore-pagamento", "riferimento": "esporto-fornitore-di-esempio-%s" % chiusura.strftime("%Y%m%d"),
                    "letto_il": ts(chiusura + timedelta(days=1))},
        "ordini": {"numero": ordini_reali, "prezzo_medio": prezzo, "rimborsi_numero": 0, "rimborsi_importo": 0.0},
        "per_canale": [{"canale": "email", "a_pagamento": False, "visite": 250, "ordini": 10, "costo": None, "costo_per_acquisto": None},
                       {"canale": "instagram", "a_pagamento": True, "visite": 120, "ordini": 4, "costo": 180.0, "costo_per_acquisto": 45.0}],
        "costi_reali": costi_reali,
        "non_misurato": [NOTA_FINTO],
    }
    prev_att = scenari["atteso"]
    f["debrief.json"] = {
        "schema_version": "1.0.0", "lancio_id": lancio_id,
        "confronto": [{"voce": "ricavo_lordo", "previsto": prev_att["ricavo_lordo"], "reale": ricavo_reale,
                       "scarto_percentuale": scarto(prev_att["ricavo_lordo"], ricavo_reale)},
                      {"voce": "ordini", "previsto": prev_att["copie"], "reale": ordini_reali,
                       "scarto_percentuale": scarto(prev_att["copie"], ordini_reali)}],
        "cause": [{"voce": "ordini", "causa": "un ordine in meno del previsto: scarto sotto il 10%, causa non richiesta ma annotata",
                   "cosa_faremmo_di_diverso": "niente di strutturale: lo scarto e' dentro la banda", "misurata": False}],
        "schemi": [
            {"testo": "La lista email converte piu' dei social a pagamento su un prodotto sotto i 50 euro",
             "forza": "osservazione", "si_applica_quando": "prodotto digitale sotto i 50 euro venduto a una lista propria",
             "conferme": 1, "smentite": 0, "artefatto_di_origine": "consuntivo.json"},
            {"testo": "Un giorno di carrello senza contenuto non produce ordini quel giorno",
             "forza": "indizio", "si_applica_quando": "carrelli di 5-10 giorni con calendario editoriale", "conferme": 1,
             "smentite": 0, "artefatto_di_origine": "editoriale.json"},
            {"testo": "Il costo macchina resta sotto il tetto se si lavora a blocchi e non a unita' minima",
             "forza": "osservazione", "si_applica_quando": "lanci con meno di 10 agenti invocati", "conferme": 1,
             "smentite": 0, "artefatto_di_origine": "budget.json"},
        ],
        "gate_bloccanti_scattati": [{"gate": "GATE-REG-1", "volte": 1, "costo_in_giorni": 1}],
        "punti_umani_scaduti": [],
        "controfirma": {"chi": "ESEMPIO-regia", "il": ts(chiusura + timedelta(days=2)), "obiezioni": None},
    }
    return f


LEGGIMI = """# esempio-s3s4 — kit di esempio per la seconda meta' del lancio (S3/S4)
Un lancio finto, `lancio_id` "esempio", con tutti gli artefatti da `copy/manifest.json` a `debrief.json` VALIDI contro gli schemi.
Nessun numero e' misurato: ogni file lo dichiara in `non_misurato`. Serve a vedere com'e' fatto un lancio, non a farne uno.
Con `ReteFinta` (nei test): GATE-CPY-1, FNL-1, EDT-1, TSR-1, TSR-2, CNS-1, MEM-1 passano; GATE-REG-1 BLOCCA perche' `via_libera.chi` e' vuoto (nessuna persona ha dato il via) e mancano pubblico/decisione/certificato/ricerca.
Con `ReteVera` GATE-FNL-1 fallirebbe: le url `https://esempio.invalid/...` non esistono, e `prova_cassa.riferimento_transazione` = "ESEMPIO-nessuna-transazione-vera" — lo stato `incassato_e_rimborsato` e' ammesso SOLO qui.
La firma in `offerta.json` e' finta (`chi` = "ESEMPIO-nessuna-persona"): GATE-OFF-1 non la accetterebbe, e non deve.
Rigenerare: `PYTHONIOENCODING=utf-8 python tests/fixture/s3s4/_genera.py` da `02-AUTOMAZIONI-E-SCRIPTS` (riscrive gli stessi file).
Provare un gate: `python -c "from scripts.gates import esegui_gate, ReteFinta; print(esegui_gate('GATE-REG-1', r'<questa cartella>', ReteFinta()))"`.
Non copiare questi file in `lanci/<id>/`: un lancio vero nasce con `lancio crea` e i suoi artefatti li producono i reparti.
Schemi: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/`. Contratto dei gate: `02-AUTOMAZIONI-E-SCRIPTS/scripts/gates/_comune.py`.
"""

FILE_ESEMPIO = ["copy/manifest.json", "copy/pagina-vendita.md", "copy/email-1.md", "funnel.json", "editoriale.json",
                "budget.json", "apertura.json", "consuntivo.json", "debrief.json", "offerta.json", "previsione.json"]


def genera():
    fixture = costruisci("prova-s3s4", esempio=False)
    for nome, dati in fixture.items():
        _scrivi(QUI, nome, dati)
    esempio = costruisci("esempio", esempio=True)
    for nome in FILE_ESEMPIO:
        _scrivi(ESEMPIO, nome, esempio[nome])
    _scrivi(ESEMPIO, "LEGGIMI.md", LEGGIMI)
    return len(fixture), len(FILE_ESEMPIO) + 1


if __name__ == "__main__":
    n1, n2 = genera()
    sys.stdout.write("fixture: %d file in %s\nesempio: %d file in %s\n" % (n1, QUI, n2, ESEMPIO))
