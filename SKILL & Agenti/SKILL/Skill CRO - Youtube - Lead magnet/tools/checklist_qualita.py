#!/usr/bin/env python3
"""
SKILL 5 — YouTube Script Factory PRO
Checklist Qualità Automatica — 45 punti, 11 sezioni, scoring + report.
"""

import json
from datetime import datetime
from typing import Optional


# ═══════════════════════════════════════════════════
# DATABASE CHECKLIST COMPLETA — 45 PUNTI
# ═══════════════════════════════════════════════════

CHECKLIST = {
    "hook": {
        "nome": "HOOK (0-15s)",
        "peso": 5,  # stelle importanza (1-5)
        "items": [
            {
                "id": "H1",
                "check": "Cattura in meno di 5 secondi?",
                "dettaglio": "Il primo concetto/frase impedisce lo scroll?",
                "red_flag": "Inizia con 'Ciao ragazzi' o intro generica"
            },
            {
                "id": "H2",
                "check": "Crea gap di curiosità o riconoscimento problema?",
                "dettaglio": "Lo spettatore pensa 'devo sapere di più' o 'questo è il mio problema'?",
                "red_flag": "Hook vago che potrebbe applicarsi a qualsiasi video"
            },
            {
                "id": "H3",
                "check": "Contiene un numero specifico?",
                "dettaglio": "Es: 'il 60% dei visitatori', 'in 14 giorni', '3 errori'",
                "red_flag": "Nessun dato concreto, tutto generico"
            },
            {
                "id": "H4",
                "check": "NON dice 'ciao ragazzi benvenuti'?",
                "dettaglio": "Zero intro generiche. Si parte col contenuto.",
                "red_flag": "Qualsiasi forma di saluto generico prima del hook"
            },
            {
                "id": "H5",
                "check": "Ho scritto 3 varianti e scelto la migliore?",
                "dettaglio": "Almeno 3 hook diversi provati.",
                "red_flag": "Primo hook scritto = hook usato, senza alternative"
            }
        ]
    },
    "setup": {
        "nome": "SETUP (15-45s)",
        "peso": 3,
        "items": [
            {
                "id": "S1",
                "check": "Lo spettatore sa ESATTAMENTE cosa otterrà?",
                "dettaglio": "Roadmap chiara: 'vedrai X, Y, Z'",
                "red_flag": "Setup vago: 'in questo video parliamo di...'"
            },
            {
                "id": "S2",
                "check": "Elenca 3-4 punti specifici (non di più)?",
                "dettaglio": "Max 4 punti. Ogni punto è un loop aperto.",
                "red_flag": "Troppi punti (>5) o nessun punto specifico"
            },
            {
                "id": "S3",
                "check": "Include menzione preview della CTA?",
                "dettaglio": "Menzione 1/3: 'Ho preparato [lead magnet], link in descrizione.'",
                "red_flag": "Nessuna menzione CTA nel setup"
            },
            {
                "id": "S4",
                "check": "Dura meno di 30 secondi?",
                "dettaglio": "Il setup deve essere conciso.",
                "red_flag": "Setup che dura >45 secondi"
            }
        ]
    },
    "credibilita": {
        "nome": "CREDIBILITÀ",
        "peso": 2,
        "items": [
            {
                "id": "CR1",
                "check": "C'è un motivo per cui ascoltare ME?",
                "dettaglio": "Perché TU sei qualificato su questo topic?",
                "red_flag": "Nessun elemento di credibilità"
            },
            {
                "id": "CR2",
                "check": "Mostro, non dico? (risultato, non curriculum)",
                "dettaglio": "✅ 'Ho ottimizzato 20+ funnel' ❌ 'Ho 5 anni di esperienza'",
                "red_flag": "Elenco di certificazioni o anni di esperienza"
            },
            {
                "id": "CR3",
                "check": "È sotto i 60 secondi?",
                "dettaglio": "La credibilità migliore è implicita.",
                "red_flag": "Monologo di auto-promozione >60 sec"
            }
        ]
    },
    "contenuto": {
        "nome": "CONTENUTO CORE",
        "peso": 4,
        "items": [
            {
                "id": "CO1",
                "check": "C'è UNA SOLA idea centrale?",
                "dettaglio": "Un video = un concetto principale.",
                "red_flag": "5 strategie + 3 tool + 2 case study nello stesso video"
            },
            {
                "id": "CO2",
                "check": "È organizzato in punti/step chiari?",
                "dettaglio": "Lo spettatore sa sempre 'dove siamo' nel video.",
                "red_flag": "Flusso di coscienza senza struttura"
            },
            {
                "id": "CO3",
                "check": "Ogni punto ha: affermazione + spiegazione + esempio + azione?",
                "dettaglio": "Struttura completa per ogni punto (Anchor) o atto (Shift/Conversion).",
                "red_flag": "Punti con solo affermazione, senza esempio o azione"
            },
            {
                "id": "CO4",
                "check": "Ci sono screencast/visual dove possibile?",
                "dettaglio": "MOSTRA > DICI. Alterna FACCIA e SCHERMO.",
                "red_flag": "Tutto parlato in camera, nessun visual"
            },
            {
                "id": "CO5",
                "check": "Retention hooks ogni 2-3 minuti?",
                "dettaglio": "Almeno 1 open loop + 1 pattern interrupt ogni 2-3 min.",
                "red_flag": "Nessun retention hook nell'intero contenuto"
            },
            {
                "id": "CO6",
                "check": "Open loops posizionati strategicamente?",
                "dettaglio": "'Tra poco ti mostro [cosa grave] — ma prima...'",
                "red_flag": "Nessun open loop, contenuto lineare senza suspense"
            },
            {
                "id": "CO7",
                "check": "Transizioni fluide tra punti?",
                "dettaglio": "Ogni punto 'vende' il successivo.",
                "red_flag": "'Ok, passiamo al punto successivo' senza collegamento"
            },
            {
                "id": "CO8",
                "check": "Il linguaggio è quello del TARGET?",
                "dettaglio": "Parole dell'imprenditore, non gergo tecnico.",
                "red_flag": "Linguaggio da manuale universitario"
            }
        ]
    },
    "ricap": {
        "nome": "RICAP",
        "peso": 2,
        "items": [
            {
                "id": "R1",
                "check": "Riassume i punti in <60 secondi?",
                "dettaglio": "1 frase per punto, non un'altra spiegazione.",
                "red_flag": "Ricap che dura >90 sec o riprende le spiegazioni"
            },
            {
                "id": "R2",
                "check": "C'è UN takeaway memorabile?",
                "dettaglio": "1 frase che lo spettatore porterà a casa.",
                "red_flag": "Nessuna frase conclusiva forte"
            }
        ]
    },
    "cta": {
        "nome": "CTA",
        "peso": 4,
        "items": [
            {
                "id": "CTA1",
                "check": "3 menzioni: preview, reminder, finale?",
                "dettaglio": "Menzione 1 nel setup, 2 a metà video, 3 dopo il ricap.",
                "red_flag": "Solo 1 CTA alla fine del video"
            },
            {
                "id": "CTA2",
                "check": "La CTA finale è specifica + beneficio?",
                "dettaglio": "Non 'clicca il link' → 'Scarica [nome] per applicare tutto da solo.'",
                "red_flag": "'Link in descrizione' senza contesto"
            },
            {
                "id": "CTA3",
                "check": "Include de-risking ('gratis', 'senza impegno')?",
                "dettaglio": "Rimuovi il rischio percepito dall'azione.",
                "red_flag": "CTA che sembra un impegno vincolante"
            },
            {
                "id": "CTA4",
                "check": "C'è UNA sola azione principale?",
                "dettaglio": "Non 5 CTA diverse. UNA azione chiara.",
                "red_flag": "'Iscriviti, commenta, condividi, scarica, prenota' tutto insieme"
            }
        ]
    },
    "generale": {
        "nome": "GENERALE",
        "peso": 3,
        "items": [
            {
                "id": "G1",
                "check": "Il tono è conversazionale (non da articolo)?",
                "dettaglio": "Si legge come si PARLA, non come si scrive.",
                "red_flag": "Frasi lunghe e formali da blog post"
            },
            {
                "id": "G2",
                "check": "Le frasi sono brevi (max 15-20 parole)?",
                "dettaglio": "Frasi corte. Punti. Ritmo.",
                "red_flag": "Periodi complessi con subordinate multiple"
            },
            {
                "id": "G3",
                "check": "C'è varietà di energia (non monotono)?",
                "dettaglio": "Alternanza: calmo → energico → riflessivo → diretto.",
                "red_flag": "Stesso tono per 10 minuti"
            },
            {
                "id": "G4",
                "check": "Il video potrebbe essere più corto senza perdere valore?",
                "dettaglio": "Se sì → taglia. Ogni sezione si guadagna il suo posto.",
                "red_flag": "Ripetizioni, divagazioni, filler"
            },
            {
                "id": "G5",
                "check": "Se togli una sezione, manca qualcosa?",
                "dettaglio": "Se no → toglila. Se sì → necessaria ✅.",
                "red_flag": "Sezioni che non aggiungono nulla"
            },
            {
                "id": "G6",
                "check": "Lo spettatore TARGET direbbe 'questo è per me' in 15 secondi?",
                "dettaglio": "Il video è per il TUO ICP, non per 'tutti'.",
                "red_flag": "Troppo generico, potrebbe essere per chiunque"
            }
        ]
    },
    "titolo": {
        "nome": "TITOLO",
        "peso": 5,
        "items": [
            {
                "id": "T1",
                "check": "< 60 caratteri?",
                "dettaglio": "Visibile per intero su mobile.",
                "red_flag": "Titolo tagliato su mobile"
            },
            {
                "id": "T2",
                "check": "Contiene keyword (se Anchor)?",
                "dettaglio": "Keyword nei primi 40 caratteri.",
                "red_flag": "Keyword assente o alla fine del titolo"
            },
            {
                "id": "T3",
                "check": "Crea curiosità?",
                "dettaglio": "Il titolo fa venire voglia di cliccare.",
                "red_flag": "Titolo descrittivo senza curiosità"
            },
            {
                "id": "T4",
                "check": "Ho scritto 5 varianti?",
                "dettaglio": "5 titoli diversi provati.",
                "red_flag": "Primo titolo = titolo usato"
            }
        ]
    },
    "thumbnail": {
        "nome": "THUMBNAIL",
        "peso": 5,
        "items": [
            {
                "id": "TH1",
                "check": "Leggibile su mobile?",
                "dettaglio": "Test: riduci a 150×84px.",
                "red_flag": "Testo troppo piccolo o troppi dettagli"
            },
            {
                "id": "TH2",
                "check": "Max 4-5 parole di testo?",
                "dettaglio": "Meno = meglio.",
                "red_flag": "Più di 5 parole nella thumbnail"
            },
            {
                "id": "TH3",
                "check": "Espressione facciale chiara?",
                "dettaglio": "Emozione riconoscibile.",
                "red_flag": "Faccia neutra o assente"
            },
            {
                "id": "TH4",
                "check": "Complementa il titolo (non lo ripete)?",
                "dettaglio": "Titolo e thumbnail dicono cose DIVERSE.",
                "red_flag": "Stesse parole nel titolo e nella thumbnail"
            }
        ]
    },
    "description": {
        "nome": "DESCRIPTION",
        "peso": 2,
        "items": [
            {
                "id": "D1",
                "check": "Link CTA nelle prime 2 righe?",
                "dettaglio": "Visibili SENZA cliccare 'mostra altro'.",
                "red_flag": "Link sepolti dopo il testo"
            },
            {
                "id": "D2",
                "check": "Timestamps presenti?",
                "dettaglio": "Ogni sezione/punto con timestamp.",
                "red_flag": "Nessun timestamp"
            },
            {
                "id": "D3",
                "check": "Keyword nella prima frase?",
                "dettaglio": "SEO: keyword principale nella prima frase del testo.",
                "red_flag": "Keyword assente dalla description"
            }
        ]
    },
    "pinned_comment": {
        "nome": "PINNED COMMENT",
        "peso": 1,
        "items": [
            {
                "id": "PC1",
                "check": "Scritto e pronto da pubblicare?",
                "dettaglio": "Testo preparato PRIMA della pubblicazione.",
                "red_flag": "Nessun pinned comment preparato"
            },
            {
                "id": "PC2",
                "check": "Include link CTA + timestamps?",
                "dettaglio": "Duplica link e timestamps dalla description.",
                "red_flag": "Pinned comment senza link o timestamps"
            }
        ]
    }
}


# ═══════════════════════════════════════════════════
# ERRORI TOP 10
# ═══════════════════════════════════════════════════

TOP_ERRORI = [
    {
        "rank": 1,
        "errore": "'Ciao ragazzi benvenuti' come hook",
        "impatto": "Abbandono immediato",
        "fix": "Parti col problema/risultato",
        "check_collegato": "H4"
    },
    {
        "rank": 2,
        "errore": "Nessun numero specifico nel hook",
        "impatto": "Hook generico, non cattura",
        "fix": "Aggiungi dato/metrica",
        "check_collegato": "H3"
    },
    {
        "rank": 3,
        "errore": "Setup vago o troppo lungo",
        "impatto": "Spettatore non sa cosa aspettarsi",
        "fix": "Max 30 sec, 3 punti specifici",
        "check_collegato": "S1"
    },
    {
        "rank": 4,
        "errore": "Credibilità = curriculum",
        "impatto": "Noioso, non convince",
        "fix": "Mostra risultati concreti",
        "check_collegato": "CR2"
    },
    {
        "rank": 5,
        "errore": "Contenuto senza esempi",
        "impatto": "Teorico, non applicabile",
        "fix": "1 esempio per ogni punto",
        "check_collegato": "CO3"
    },
    {
        "rank": 6,
        "errore": "Zero retention hooks",
        "impatto": "Watch time basso",
        "fix": "1 hook ogni 2-3 min",
        "check_collegato": "CO5"
    },
    {
        "rank": 7,
        "errore": "CTA generica 'link in descrizione'",
        "impatto": "Non motiva all'azione",
        "fix": "Specifica + beneficio + de-risking",
        "check_collegato": "CTA2"
    },
    {
        "rank": 8,
        "errore": "Titolo > 60 caratteri",
        "impatto": "Tagliato su mobile",
        "fix": "Riscrivi più corto",
        "check_collegato": "T1"
    },
    {
        "rank": 9,
        "errore": "Thumbnail illeggibile su mobile",
        "impatto": "CTR basso",
        "fix": "Test a 150×84px",
        "check_collegato": "TH1"
    },
    {
        "rank": 10,
        "errore": "Nessun takeaway nel ricap",
        "impatto": "Spettatore non ricorda nulla",
        "fix": "1 frase memorabile",
        "check_collegato": "R2"
    }
]


def valuta_script(
    titolo: str,
    risposte: dict,
    note: str = ""
) -> dict:
    """
    Valuta uno script con la checklist completa.

    Args:
        titolo: Titolo del video/script
        risposte: Dict {item_id: True/False} per ogni check
                  Es: {"H1": True, "H2": False, "H3": True, ...}
        note: Note aggiuntive opzionali

    Returns:
        Report completo con score, verdetto, punti deboli, priorità fix
    """

    report = {
        "titolo": titolo,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "sezioni": {},
        "score_totale": 0,
        "max_totale": 0,
        "punti_deboli": [],
        "top_fix": [],
        "note": note
    }

    totale_check = 0
    totale_ok = 0

    for sez_key, sezione in CHECKLIST.items():
        n_items = len(sezione["items"])
        n_ok = 0

        items_dettaglio = []
        for item in sezione["items"]:
            risposta = risposte.get(item["id"], False)
            if risposta:
                n_ok += 1
            items_dettaglio.append({
                "id": item["id"],
                "check": item["check"],
                "risultato": "✅" if risposta else "❌",
                "red_flag": item["red_flag"] if not risposta else None
            })

        pct = round((n_ok / n_items) * 100) if n_items > 0 else 0

        report["sezioni"][sez_key] = {
            "nome": sezione["nome"],
            "peso": sezione["peso"],
            "score": n_ok,
            "max": n_items,
            "percentuale": pct,
            "items": items_dettaglio
        }

        totale_check += n_items
        totale_ok += n_ok

        # Identifica punti deboli (sezioni sotto 75%)
        if pct < 75:
            failed_items = [i for i in items_dettaglio if i["risultato"] == "❌"]
            report["punti_deboli"].append({
                "sezione": sezione["nome"],
                "percentuale": pct,
                "peso": sezione["peso"],
                "items_falliti": failed_items
            })

    report["score_totale"] = totale_ok
    report["max_totale"] = totale_check
    report["percentuale_totale"] = round((totale_ok / totale_check) * 100) if totale_check > 0 else 0

    # Verdetto
    if totale_ok >= 40:
        report["verdetto"] = "✅ ECCELLENTE — Registra immediatamente"
        report["verdetto_emoji"] = "✅"
    elif totale_ok >= 35:
        report["verdetto"] = "🟡 BUONO — Migliora 2-3 punti deboli"
        report["verdetto_emoji"] = "🟡"
    elif totale_ok >= 28:
        report["verdetto"] = "🟠 MEDIOCRE — Revisione seria necessaria"
        report["verdetto_emoji"] = "🟠"
    else:
        report["verdetto"] = "🔴 DEBOLE — Riscrivi lo script"
        report["verdetto_emoji"] = "🔴"

    # Top fix — ordina punti deboli per peso sezione (priorità a sezioni critiche)
    report["punti_deboli"].sort(key=lambda x: x["peso"], reverse=True)
    fix_counter = 0
    for pd in report["punti_deboli"]:
        for item in pd["items_falliti"]:
            if fix_counter < 5:
                # Cerca errore collegato nei TOP_ERRORI
                errore_collegato = next(
                    (e for e in TOP_ERRORI if e["check_collegato"] == item["id"]), None
                )
                report["top_fix"].append({
                    "priorita": fix_counter + 1,
                    "id": item["id"],
                    "check": item["check"],
                    "sezione": pd["sezione"],
                    "red_flag": item["red_flag"],
                    "fix_suggerito": errore_collegato["fix"] if errore_collegato else "Rivedi questo punto",
                    "impatto": errore_collegato["impatto"] if errore_collegato else "Da valutare"
                })
                fix_counter += 1

    return report


def stampa_report(report: dict) -> str:
    """Formatta il report in testo leggibile."""

    lines = []

    lines.append("═" * 60)
    lines.append(f"  📋 QUALITY CHECK — \"{report['titolo']}\"")
    lines.append("═" * 60)
    lines.append(f"  Data: {report['data']}")
    lines.append("")
    lines.append(f"  SCORE: {report['score_totale']} / {report['max_totale']} ({report['percentuale_totale']}%)")
    lines.append(f"  VERDETTO: {report['verdetto']}")
    lines.append("")
    lines.append("─" * 60)
    lines.append("  PER SEZIONE:")
    lines.append("")

    for sez_key, sez in report["sezioni"].items():
        # Barra progresso
        filled = int((sez["percentuale"] / 100) * 10)
        bar = "█" * filled + "░" * (10 - filled)

        # Indicatore
        if sez["percentuale"] >= 75:
            indicator = "✅"
        elif sez["percentuale"] >= 50:
            indicator = "🟡"
        else:
            indicator = "🔴"

        stars = "⭐" * sez["peso"]
        lines.append(f"  {indicator} {sez['nome']:<20} [{sez['score']}/{sez['max']}] [{bar}] {sez['percentuale']}%  {stars}")

    # Punti deboli
    if report["punti_deboli"]:
        lines.append("")
        lines.append("─" * 60)
        lines.append("  PUNTI DEBOLI (sezioni sotto 75%):")
        lines.append("")

        for pd in report["punti_deboli"]:
            lines.append(f"  ❌ {pd['sezione']} ({pd['percentuale']}%)")
            for item in pd["items_falliti"]:
                lines.append(f"     → {item['id']}: {item['check']}")
                if item["red_flag"]:
                    lines.append(f"       🚩 {item['red_flag']}")
            lines.append("")

    # Top fix
    if report["top_fix"]:
        lines.append("─" * 60)
        lines.append("  PRIORITÀ DI FIX (dal più urgente):")
        lines.append("")

        for fix in report["top_fix"]:
            lines.append(f"  {fix['priorita']}. [{fix['id']}] {fix['check']}")
            lines.append(f"     Sezione: {fix['sezione']}")
            lines.append(f"     Fix: {fix['fix_suggerito']}")
            lines.append(f"     Impatto: {fix['impatto']}")
            lines.append("")

    # Dettaglio completo
    lines.append("─" * 60)
    lines.append("  DETTAGLIO COMPLETO:")
    lines.append("")

    for sez_key, sez in report["sezioni"].items():
        lines.append(f"  {sez['nome']}:")
        for item in sez["items"]:
            lines.append(f"    {item['risultato']} [{item['id']}] {item['check']}")
        lines.append("")

    if report["note"]:
        lines.append(f"  📝 Note: {report['note']}")

    lines.append("═" * 60)

    return "\n".join(lines)


def checklist_interattiva(titolo: str) -> dict:
    """
    Esegue la checklist in modo interattivo da terminale.
    Chiede all'utente di rispondere sì/no per ogni check.
    """

    print("═" * 60)
    print(f"  📋 QUALITY CHECK INTERATTIVO")
    print(f"  Script: \"{titolo}\"")
    print("═" * 60)
    print("  Rispondi s/n per ogni check.\n")

    risposte = {}

    for sez_key, sezione in CHECKLIST.items():
        print(f"\n{'─' * 40}")
        print(f"  {sezione['nome']} ({'⭐' * sezione['peso']})")
        print(f"{'─' * 40}")

        for item in sezione["items"]:
            while True:
                ans = input(f"  [{item['id']}] {item['check']} (s/n): ").strip().lower()
                if ans in ("s", "n", "si", "no", "y"):
                    risposte[item["id"]] = ans in ("s", "si", "y")
                    break
                print("    → Rispondi 's' o 'n'")

    note = input("\n  📝 Note aggiuntive (opzionale): ").strip()

    report = valuta_script(titolo, risposte, note)
    return report


def valuta_da_script_json(script_json: dict) -> dict:
    """
    Esegue una valutazione AUTOMATICA parziale basata sullo script JSON
    generato da genera_script.py. Verifica i punti che si possono
    controllare programmaticamente.
    """

    risposte = {}
    meta = script_json.get("meta", {})
    componenti = script_json.get("componenti", [])
    retention = script_json.get("retention_hooks", [])
    post_video = script_json.get("post_video", {})

    # ─── HOOK ───
    hook_comp = next((c for c in componenti if c.get("nome") == "HOOK"), None)
    if hook_comp:
        hook_text = hook_comp.get("testo", "")
        risposte["H1"] = len(hook_text) > 10  # Ha un hook
        risposte["H2"] = any(kw in hook_text.lower() for kw in
                             ["problema", "stai", "perché", "errore", "come", "quanto"])
        # Controlla numeri
        risposte["H3"] = any(c.isdigit() for c in hook_text) or any(
            w in hook_text for w in ["%", "€", "mille", "cento"])
        risposte["H4"] = not any(saluto in hook_text.lower() for saluto in
                                  ["ciao ragazzi", "benvenuti", "ciao a tutti", "buongiorno a tutti"])
        risposte["H5"] = True  # Assumo sì se usa genera_hooks (genera 3)

    # ─── SETUP ───
    setup_comp = next((c for c in componenti if c.get("nome") == "SETUP"), None)
    if setup_comp:
        setup_text = setup_comp.get("testo", "")
        risposte["S1"] = any(kw in setup_text.lower() for kw in ["ti mostro", "vedrai", "imparerai"])
        # Conta punti elencati
        risposte["S2"] = setup_text.count(";") >= 2 or setup_text.count(",") >= 2
        risposte["S3"] = setup_comp.get("cta_level", "") != ""
        risposte["S4"] = True  # Assumo ok se generato dal sistema

    # ─── CREDIBILITÀ ───
    cred_comp = next((c for c in componenti if c.get("nome") == "CREDIBILITÀ"), None)
    if cred_comp:
        cred_text = cred_comp.get("testo", "")
        risposte["CR1"] = len(cred_text) > 20
        risposte["CR2"] = any(kw in cred_text.lower() for kw in
                               ["lavorato con", "ho analizzato", "ho ottimizzato", "risultato", "pattern"])
        risposte["CR3"] = True  # Assumo ok se usa il sistema

    # ─── CONTENUTO ───
    contenuto_comp = next((c for c in componenti if c.get("nome") == "CONTENUTO CORE"), None)
    if contenuto_comp:
        sottosezioni = contenuto_comp.get("sottosezioni", [])
        risposte["CO1"] = True  # 1 idea se usa il sistema
        risposte["CO2"] = len(sottosezioni) >= 2
        # Controlla struttura punti
        has_structure = all("AFFERMAZIONE" in s.get("testo", "") or "ATTO" in s.get("sottosezione", "")
                           for s in sottosezioni)
        risposte["CO3"] = has_structure
        has_screencast = any("[SCREENCAST]" in s.get("testo", "") for s in sottosezioni)
        risposte["CO4"] = has_screencast
        risposte["CO5"] = len(retention) >= 3
        has_open_loop = any("open_loop" in rh.get("pattern", "") for rh in retention)
        risposte["CO6"] = has_open_loop
        has_transitions = any("TRANSIZIONE" in s.get("testo", "") or "transizione" in s.get("testo", "").lower()
                              for s in sottosezioni)
        risposte["CO7"] = has_transitions
        risposte["CO8"] = True  # Non verificabile automaticamente → assume ok

    # ─── RICAP ───
    ricap_comp = next((c for c in componenti if c.get("nome") == "RICAP"), None)
    if ricap_comp:
        ricap_text = ricap_comp.get("testo", "")
        risposte["R1"] = len(ricap_text) > 20
        risposte["R2"] = "takeaway" in ricap_text.lower() or "principale" in ricap_text.lower()

    # ─── CTA ───
    cta_comp = next((c for c in componenti if c.get("nome") == "CTA FINALE"), None)
    if cta_comp:
        # Conta menzioni CTA totali
        cta_mentions = sum(1 for c in componenti if c.get("cta_level"))
        risposte["CTA1"] = cta_mentions >= 2
        cta_text = cta_comp.get("testo", "")
        risposte["CTA2"] = any(kw in cta_text.lower() for kw in ["scarica", "prenota", "per applicare"])
        risposte["CTA3"] = any(kw in cta_text.lower() for kw in ["gratis", "gratuito", "senza impegno", "zero"])
        risposte["CTA4"] = True  # Assume ok se usa il sistema

    # ─── GENERALE ───
    all_text = " ".join(c.get("testo", "") for c in componenti)
    risposte["G1"] = True  # Non verificabile precisamente
    avg_sentence_len = len(all_text.split()) / max(all_text.count("."), 1)
    risposte["G2"] = avg_sentence_len < 25
    risposte["G3"] = "(TONO:" in all_text or "TONO:" in all_text.upper()
    risposte["G4"] = True  # Assumo ok
    risposte["G5"] = True  # Assumo ok
    risposte["G6"] = True  # Non verificabile automaticamente

    # ─── TITOLO ───
    titolo = meta.get("titolo", "")
    risposte["T1"] = len(titolo) <= 60
    keyword = meta.get("keyword", "")
    risposte["T2"] = keyword.lower() in titolo.lower() if keyword else True
    risposte["T3"] = any(c.isdigit() for c in titolo) or "?" in titolo or "come" in titolo.lower()
    risposte["T4"] = True  # Assume ok se usa genera_titoli

    # ─── THUMBNAIL ───
    thumb_concepts = post_video.get("thumbnail_concepts", [])
    risposte["TH1"] = True  # Non verificabile
    risposte["TH2"] = all(len(tc.get("testo_thumbnail", "").split()) <= 5 for tc in thumb_concepts) if thumb_concepts else False
    risposte["TH3"] = all(tc.get("espressione") for tc in thumb_concepts) if thumb_concepts else False
    risposte["TH4"] = True  # Assume ok se usa il sistema

    # ─── DESCRIPTION ───
    desc = post_video.get("description", "")
    risposte["D1"] = "LINK" in desc[:100] or "link" in desc[:100]
    risposte["D2"] = "TIMESTAMPS" in desc.upper() or "0:00" in desc
    risposte["D3"] = keyword.lower() in desc[:200].lower() if keyword else True

    # ─── PINNED COMMENT ───
    pinned = post_video.get("pinned_comment", "")
    risposte["PC1"] = len(pinned) > 20
    risposte["PC2"] = "LINK" in pinned or "0:00" in pinned

    report = valuta_script(meta.get("titolo", "Script"), risposte, "Valutazione automatica da JSON")
    return report


# ═══════════════════════════════════════════════════
# ESEMPIO DI UTILIZZO
# ═══════════════════════════════════════════════════

if __name__ == "__main__":

    # OPZIONE 1: Valutazione manuale con risposte predefinite
    print("\n" + "=" * 60)
    print("  DEMO: Valutazione manuale")
    print("=" * 60)

    risposte_esempio = {
        # Hook
        "H1": True, "H2": True, "H3": True, "H4": True, "H5": True,
        # Setup
        "S1": True, "S2": True, "S3": True, "S4": True,
        # Credibilità
        "CR1": True, "CR2": True, "CR3": True,
        # Contenuto
        "CO1": True, "CO2": True, "CO3": True, "CO4": True,
        "CO5": False, "CO6": False, "CO7": True, "CO8": True,
        # Ricap
        "R1": True, "R2": True,
        # CTA
        "CTA1": False, "CTA2": True, "CTA3": True, "CTA4": True,
        # Generale
        "G1": True, "G2": True, "G3": False, "G4": True, "G5": True, "G6": True,
        # Titolo
        "T1": True, "T2": True, "T3": True, "T4": True,
        # Thumbnail
        "TH1": True, "TH2": True, "TH3": True, "TH4": True,
        # Description
        "D1": True, "D2": True, "D3": True,
        # Pinned
        "PC1": True, "PC2": True,
    }

    report = valuta_script(
        "3 errori che uccidono le tue conversioni",
        risposte_esempio,
        "Demo script — alcuni retention hooks mancanti"
    )

    print(stampa_report(report))

    # OPZIONE 2: Valutazione automatica da JSON
    print("\n\n" + "=" * 60)
    print("  DEMO: Valutazione automatica da JSON")
    print("=" * 60)

    # Simula script JSON (struttura da genera_script.py)
    script_mock = {
        "meta": {
            "titolo": "3 errori che uccidono le tue conversioni",
            "tipo": "anchor",
            "keyword": "errori landing page",
            "pilastro": 2
        },
        "componenti": [
            {
                "nome": "HOOK",
                "testo": "Stai spendendo in ads senza risultati? Il 90% delle landing page ha questo errore. Il problema non è dove pensi."
            },
            {
                "nome": "SETUP",
                "testo": "In questo video ti mostro 3 errori critici;\nprimo, la headline;\nsecondo, la CTA;\nterzo, la social proof.",
                "cta_level": "PREVIEW"
            },
            {
                "nome": "CREDIBILITÀ",
                "testo": "Ho lavorato con 20+ aziende sulla conversione. Il pattern che vedo è sempre lo stesso."
            },
            {
                "nome": "CONTENUTO CORE",
                "sottosezioni": [
                    {
                        "sottosezione": "PUNTO 1",
                        "testo": "[FACCIA]\nAFFERMAZIONE: La headline non parla al cliente.\n[SCREENCAST]\nESEMPIO: Vi faccio vedere...\nTRANSIZIONE: Ma c'è di peggio."
                    },
                    {
                        "sottosezione": "PUNTO 2",
                        "testo": "[FACCIA]\nAFFERMAZIONE: La CTA è troppo vaga.\n[SCREENCAST]\nESEMPIO: Guardate questa pagina...\nTRANSIZIONE: E arriviamo al punto più grave."
                    },
                    {
                        "sottosezione": "PUNTO 3",
                        "testo": "[FACCIA]\nAFFERMAZIONE: Nessuna social proof.\n[SCREENCAST]\nESEMPIO: (TONO: energia alta) Questo è il punto cruciale.\nTRANSIZIONE: Ricapitoliamo."
                    }
                ]
            },
            {
                "nome": "RICAP",
                "testo": "Ricapitoliamo. Il takeaway principale è: il copy batte il design."
            },
            {
                "nome": "CTA FINALE",
                "testo": "Se vuoi applicare tutto, scarica la Checklist CRO Gratuita. È gratis. Link in descrizione.",
                "cta_level": "FINALE"
            }
        ],
        "retention_hooks": [
            {"timestamp": "0:30", "pattern": "open_loop"},
            {"timestamp": "3:00", "pattern": "teaser"},
            {"timestamp": "5:00", "pattern": "bonus"},
            {"timestamp": "6:00", "pattern": "cta_reminder"},
            {"timestamp": "7:00", "pattern": "prova_visiva"}
        ],
        "post_video": {
            "description": "📋 Checklist CRO GRATUITA: [LINK]\n📞 Prenota call: [LINK]\n\nIn questo video errori landing page...\n\n⏰ TIMESTAMPS:\n0:00 Intro",
            "pinned_comment": "📋 Checklist CRO: [LINK]\n0:00 Intro\n💬 Scrivimi nei commenti!",
            "thumbnail_concepts": [
                {"testo_thumbnail": "3 ERRORI", "espressione": "shock"},
                {"testo_thumbnail": "PRIMA DOPO", "espressione": "determinazione"},
                {"testo_thumbnail": "+200% CR", "espressione": "soddisfazione"}
            ]
        }
    }

    report_auto = valuta_da_script_json(script_mock)
    print(stampa_report(report_auto))

    # Salva report
    with open("quality_report.json", "w") as f:
        json.dump(report_auto, f, indent=2, ensure_ascii=False)
    print("\n✅ Report salvato in quality_report.json")
