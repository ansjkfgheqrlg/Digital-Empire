#!/usr/bin/env python3
"""
SKILL 5 — YouTube Script Factory PRO
Generatore Script Completo con tutti i 7 componenti.
"""

import json
from datetime import datetime
from typing import Optional


# ═══════════════════════════════════════════════════
# DATABASE HOOK FORMULAS
# ═══════════════════════════════════════════════════

HOOK_FORMULAS = {
    "A": {
        "nome": "PROBLEMA RICONOSCIBILE",
        "formule": {
            "A1": {
                "nome": "Sintomo Diretto",
                "template": "Stai {sintomo}? Il problema non è dove pensi.",
                "quando": "video Anchor su conversioni basse"
            },
            "A2": {
                "nome": "Frustrazione Quotidiana",
                "template": "Se ogni mattina {azione_quotidiana} e pensi '{pensiero_frustrante}' — questo video è per te.",
                "quando": "video che parla di CPA/ROI"
            },
            "A3": {
                "nome": "Confronto Doloroso",
                "template": "Il tuo competitor {fa_cosa_meglio}. Ha un prodotto peggiore. Eppure {risultato}. Ecco perché.",
                "quando": "video su differenziazione/CRO"
            },
            "A4": {
                "nome": "Domanda Diretta",
                "template": "Quanto ti costa ogni giorno avere {problema}?",
                "quando": "video su costo opportunità"
            },
            "A5": {
                "nome": "Errore Universale",
                "template": "C'è un errore che fanno il {percentuale}% {di_chi}. E probabilmente anche {tu_tuo}.",
                "quando": "video su errori comuni"
            }
        }
    },
    "B": {
        "nome": "RISULTATO/PROVA",
        "formule": {
            "B1": {
                "nome": "Numero Concreto",
                "template": "Abbiamo portato {metrica} da {prima} a {dopo} in {tempo}. Ti mostro esattamente come.",
                "quando": "video Conversion (case study)"
            },
            "B2": {
                "nome": "Prima/Dopo",
                "template": "{soggetto} faceva {prima}. Dopo {N} modifiche, fa {dopo}. Le {N} modifiche sono in questo video.",
                "quando": "video tutorial con risultati"
            },
            "B3": {
                "nome": "Analisi Live",
                "template": "Ho appena aperto il sito di {chi} e ho trovato {N} problemi in {tempo}.",
                "quando": "video audit/analisi"
            },
            "B4": {
                "nome": "Calcolo Scioccante",
                "template": "Facciamo un calcolo veloce. Se {situazione}, stai perdendo {calcolo} AL GIORNO. Ecco come recuperarle.",
                "quando": "video su ROI del CRO"
            },
            "B5": {
                "nome": "Lista con Promessa",
                "template": "{N} cose che puoi cambiare OGGI {su_cosa} per {risultato} DOMANI.",
                "quando": "video lista pratica"
            }
        }
    },
    "C": {
        "nome": "PROVOCAZIONE/CONTROINTUITIVO",
        "formule": {
            "C1": {
                "nome": "Credenza Sbagliata",
                "template": "Tutti ti dicono di {consiglio_comune}. Ecco perché è il consiglio peggiore che puoi seguire.",
                "quando": "video Shift"
            },
            "C2": {
                "nome": "Controintuitivo",
                "template": "Più {azione}, MENO {risultato_atteso}. Sembra assurdo, ma ti mostro la matematica.",
                "quando": "video Shift su traffico vs conversione"
            },
            "C3": {
                "nome": "Mito Smontato",
                "template": "'{mito_comune}.' Ho analizzato {N} {cosa}. Il {percentuale}% {risultato_negativo}. Ecco perché.",
                "quando": "video Shift su design vs conversione"
            },
            "C4": {
                "nome": "Rivelazione",
                "template": "C'è {una_cosa} che il {percentuale}% {di_chi} non {fa}. Ed è quella che determina se {conseguenza}.",
                "quando": "video su metriche CRO"
            },
            "C5": {
                "nome": "Affermazione Audace",
                "template": "{soggetto} sta perdendo il {percentuale}% {di_cosa} nei primi {tempo}. Ti dimostro come.",
                "quando": "video su above-the-fold"
            }
        }
    },
    "D": {
        "nome": "STORYTELLING",
        "formule": {
            "D1": {
                "nome": "Caso Reale",
                "template": "Un {chi} mi ha contattato {quando}. {situazione_problema}. In {tempo} abbiamo ribaltato la situazione.",
                "quando": "video Conversion"
            },
            "D2": {
                "nome": "Esperienza Personale",
                "template": "{quando} ho fatto un errore enorme con un cliente. Un errore che ci è costato {conseguenza}. Ti racconto cos'è successo e come non farlo.",
                "quando": "video lezioni apprese"
            },
            "D3": {
                "nome": "Analogia",
                "template": "Immagina di avere {analogia_setup}. {dettagli_analogia}. Quanti {risultato_analogia}? Ecco: {collegamento_realtà}.",
                "quando": "video che spiega il CRO ai neofiti"
            },
            "D4": {
                "nome": "Dietro le Quinte",
                "template": "Ti faccio vedere il processo ESATTO che uso quando {situazione}. {da_dove} a {dove}.",
                "quando": "video sul processo Digital Empire"
            },
            "D5": {
                "nome": "Sfida",
                "template": "Mi sono dato una sfida: {sfida}. {vincolo}. Ecco cosa è successo.",
                "quando": "video challenge/esperimento"
            }
        }
    }
}

# Matrice tipo video → categorie hook consigliate
HOOK_MATRIX = {
    "anchor": ["A", "B"],
    "shift": ["C", "A"],
    "conversion": ["B", "D"],
    "audit": ["B", "A"],
    "behind_the_scenes": ["D", "D"]
}


# ═══════════════════════════════════════════════════
# DATABASE TITLE FORMULAS
# ═══════════════════════════════════════════════════

TITLE_FORMULAS = {
    "numero_risultato": {
        "template": "{N} {cose} che {conseguenza}",
        "esempio": "3 errori che uccidono le tue conversioni"
    },
    "come_risultato": {
        "template": "Come {ottenere_risultato} ({condizione})",
        "esempio": "Come migliorare la landing page in 30 minuti"
    },
    "provocazione": {
        "template": "Perché {cosa_comune} non funziona",
        "esempio": "Perché spendere di più in ads è inutile"
    },
    "prova": {
        "template": "Da {prima} a {dopo}: {come}",
        "esempio": "Da 0.8% a 3.2% di conversioni: il processo"
    },
    "domanda": {
        "template": "{domanda_target}?",
        "esempio": "Perché nessuno compra dal mio sito?"
    },
    "audit": {
        "template": "Ho analizzato {cosa} — ecco cosa ho trovato",
        "esempio": "Ho analizzato 50 landing page italiane"
    }
}


# ═══════════════════════════════════════════════════
# DATABASE RETENTION HOOKS
# ═══════════════════════════════════════════════════

RETENTION_PATTERNS = {
    "open_loop": {
        "nome": "Open Loop",
        "template": "Tra poco ti mostro {cosa_futura}, che è {superlativo} — ma prima devi capire questo.",
        "potenza": 10,
        "posizione": "prima di ogni nuovo punto"
    },
    "contrasto": {
        "nome": "Contrasto Energia",
        "template": "(TONO: alza voce) E qui è dove la maggior parte SBAGLIA.",
        "potenza": 7,
        "posizione": "dopo spiegazione calma"
    },
    "prova_visiva": {
        "nome": "Prova Visiva",
        "template": "[SCREENCAST] Guardate questo... vedete? {cosa_mostrare}.",
        "potenza": 8,
        "posizione": "quando hai dati/screenshot da mostrare"
    },
    "domanda_retorica": {
        "nome": "Domanda Retorica",
        "template": "Ma aspetta — perché succede questo? Ci hai mai pensato?",
        "potenza": 6,
        "posizione": "dopo aver presentato un problema"
    },
    "teaser": {
        "nome": "Teaser",
        "template": "Quello che sto per mostrarti ha cambiato completamente il modo in cui guardo {cosa}.",
        "potenza": 7,
        "posizione": "prima di un punto chiave"
    },
    "aneddoto": {
        "nome": "Aneddoto Veloce",
        "template": "A proposito di questo, {quando} mi è successa una cosa... {micro_storia_15_sec}",
        "potenza": 8,
        "posizione": "seconda metà del video"
    },
    "disclaimer": {
        "nome": "Disclaimer Onesto",
        "template": "Ok, questo punto potrebbe sembrarti banale. Ma resta con me perché è il più importante.",
        "potenza": 6,
        "posizione": "prima di un punto che sembra ovvio"
    },
    "preview_interna": {
        "nome": "Preview Interna",
        "template": "Il prossimo punto è quello dove la maggior parte dei miei clienti ha l'AHA moment.",
        "potenza": 7,
        "posizione": "tra un punto e l'altro"
    },
    "interazione": {
        "nome": "Interazione",
        "template": "Fammi sapere nei commenti se anche tu {hai_questo_problema}.",
        "potenza": 5,
        "posizione": "dopo aver descritto un problema comune"
    },
    "bonus": {
        "nome": "Bonus Inaspettato",
        "template": "Ok, visto che sei arrivato fin qui, ti dò un bonus che non era previsto...",
        "potenza": 9,
        "posizione": "a metà video"
    }
}


# ═══════════════════════════════════════════════════
# DATABASE CREDIBILITY FORMULAS
# ═══════════════════════════════════════════════════

CREDIBILITY_FORMULAS = {
    "risultato": "Negli ultimi {tempo} ho lavorato con {N} aziende sulla conversione dei loro funnel. Il pattern che vedo più spesso è {pattern}.",
    "esperienza": "Questo è esattamente il tipo di problema che risolvo ogni giorno nella mia agenzia. E dopo averlo visto in {N} business diversi, posso dirti che la causa è quasi sempre la stessa.",
    "errore": "So di cosa parlo perché ho fatto esattamente questo errore all'inizio. Ed è costato a un mio cliente {conseguenza}. Da allora ho sviluppato un sistema per evitarlo.",
    "dato": "Ho analizzato {N} landing page nel settore {settore}. Il {percentuale}% aveva questo esatto problema.",
    "minimalista": "Se mi segui già, sai che mi occupo di CRO — ottimizzare le conversioni per aziende che hanno già traffico."
}


def genera_hooks(
    tipo_video: str,
    topic: str,
    keyword: str = "",
    credenza_da_smontare: str = "",
    risultato_case_study: str = "",
    numeri: dict = None
) -> list:
    """
    Genera 3+ hook personalizzati per il video.
    """
    if numeri is None:
        numeri = {}

    categorie_consigliate = HOOK_MATRIX.get(tipo_video.lower(), ["A", "B"])
    hooks = []

    # Hook 1 — dalla prima categoria consigliata
    cat1 = categorie_consigliate[0]
    formule_cat1 = HOOK_FORMULAS[cat1]["formule"]
    # Scegli la formula più adatta in base ai dati disponibili
    for cod, formula in formule_cat1.items():
        hook_text = _personalizza_hook(formula, topic, keyword, credenza_da_smontare, risultato_case_study, numeri)
        if hook_text:
            hooks.append({
                "codice": cod,
                "categoria": HOOK_FORMULAS[cat1]["nome"],
                "formula": formula["nome"],
                "testo": hook_text,
                "quando_usare": formula["quando"]
            })
            break

    # Hook 2 — dalla seconda categoria consigliata
    if len(categorie_consigliate) > 1:
        cat2 = categorie_consigliate[1]
        formule_cat2 = HOOK_FORMULAS[cat2]["formule"]
        for cod, formula in formule_cat2.items():
            hook_text = _personalizza_hook(formula, topic, keyword, credenza_da_smontare, risultato_case_study, numeri)
            if hook_text:
                hooks.append({
                    "codice": cod,
                    "categoria": HOOK_FORMULAS[cat2]["nome"],
                    "formula": formula["nome"],
                    "testo": hook_text,
                    "quando_usare": formula["quando"]
                })
                break

    # Hook 3 — custom basato sul topic
    hook_custom = _genera_hook_custom(tipo_video, topic, numeri, credenza_da_smontare, risultato_case_study)
    hooks.append({
        "codice": "CUSTOM",
        "categoria": "PERSONALIZZATO",
        "formula": "Custom per questo video",
        "testo": hook_custom,
        "quando_usare": "specifico per questo video"
    })

    return hooks


def _personalizza_hook(formula: dict, topic: str, keyword: str,
                       credenza: str, risultato: str, numeri: dict) -> str:
    """Personalizza un template hook con i dati disponibili."""
    template = formula["template"]

    # Sostituzioni basate su dati disponibili
    replacements = {
        "{sintomo}": f"spendendo in {topic} senza risultati" if topic else "spendendo senza risultati",
        "{azione_quotidiana}": "apri il tuo dashboard",
        "{pensiero_frustrante}": "dove stanno andando i miei soldi?",
        "{fa_cosa_meglio}": "vende più di te",
        "{risultato}": risultato if risultato else "converte il triplo",
        "{problema}": topic if topic else "un funnel che non converte",
        "{percentuale}": str(numeri.get("percentuale", 90)),
        "{di_chi}": "delle landing page italiane",
        "{tu_tuo}": "la tua",
        "{metrica}": numeri.get("metrica", "il conversion rate"),
        "{prima}": numeri.get("prima", "0.8%"),
        "{dopo}": numeri.get("dopo", "3.2%"),
        "{tempo}": numeri.get("tempo", "14 giorni"),
        "{soggetto}": "Questa landing page",
        "{N}": str(numeri.get("n_punti", 3)),
        "{chi}": "un'azienda che spende €50.000/mese in ads",
        "{situazione}": topic if topic else "il tuo sito",
        "{calcolo}": numeri.get("calcolo", "20 vendite"),
        "{su_cosa}": f"sulla tua {topic}" if topic else "sulla tua landing page",
        "{consiglio_comune}": credenza if credenza else "migliorare le ads",
        "{azione}": "spendi in traffico",
        "{risultato_atteso}": "guadagni",
        "{mito_comune}": credenza if credenza else "Fai un sito bello e i clienti arriveranno",
        "{cosa}": topic if topic else "siti",
        "{risultato_negativo}": "non converte",
        "{una_cosa}": "una metrica",
        "{fa}": "guarda",
        "{conseguenza}": "fai soldi o li butti",
        "{di_cosa}": "dei clienti",
        "{quando}": "la settimana scorsa",
        "{situazione_problema}": risultato if risultato else "Spendeva €3.000/mese senza risultati",
        "{analogia_setup}": "un negozio in centro",
        "{dettagli_analogia}": "100 persone entrano ogni giorno, ma la cassa è nascosta",
        "{risultato_analogia}": "comprerebbero?",
        "{collegamento_realtà}": "il tuo sito funziona esattamente così",
        "{da_dove}": "dall'audit",
        "{dove}": "alla prima vendita",
        "{sfida}": f"prendere una landing page e {topic}" if topic else "raddoppiare un conversion rate",
        "{vincolo}": "Usando solo copy, nessun redesign"
    }

    result = template
    for key, value in replacements.items():
        result = result.replace(key, value)

    # Se restano placeholder non sostituiti, non restituire
    if "{" in result:
        return ""
    return result


def _genera_hook_custom(tipo: str, topic: str, numeri: dict,
                        credenza: str, risultato: str) -> str:
    """Genera un hook completamente custom."""
    if tipo == "anchor" and topic:
        return (
            f"Se stai cercando di capire perché {topic} non funziona, "
            f"in questo video ti mostro esattamente il problema — "
            f"e la soluzione è più semplice di quello che pensi."
        )
    elif tipo == "shift" and credenza:
        return (
            f"'{credenza}' — lo dicono tutti. "
            f"Ma ho i numeri che dimostrano il contrario. "
            f"Ecco cosa succede DAVVERO."
        )
    elif tipo == "conversion" and risultato:
        return (
            f"Ecco un caso reale: {risultato}. "
            f"Ti mostro ogni singolo step."
        )
    else:
        return (
            f"In questo video ti svelo qualcosa "
            f"che il 90% degli imprenditori non sa su {topic if topic else 'le conversioni'}."
        )


def genera_titoli(
    topic: str,
    tipo_video: str,
    keyword: str = "",
    numeri: dict = None,
    credenza: str = ""
) -> list:
    """Genera 5 varianti di titolo per il video."""

    if numeri is None:
        numeri = {}

    titoli = []

    n = numeri.get("n_punti", 3)
    prima = numeri.get("prima", "")
    dopo = numeri.get("dopo", "")

    # Formula 1 — Numero + Risultato
    titoli.append({
        "formula": "numero_risultato",
        "testo": f"{n} errori che uccidono le tue conversioni",
        "caratteri": 0
    })

    # Formula 2 — Come + Risultato
    if keyword:
        titoli.append({
            "formula": "come_risultato",
            "testo": f"Come {keyword} (guida pratica)",
            "caratteri": 0
        })
    else:
        titoli.append({
            "formula": "come_risultato",
            "testo": f"Come migliorare {topic} in modo misurabile",
            "caratteri": 0
        })

    # Formula 3 — Provocazione
    if credenza:
        titoli.append({
            "formula": "provocazione",
            "testo": f"Perché '{credenza}' è sbagliato",
            "caratteri": 0
        })
    else:
        titoli.append({
            "formula": "provocazione",
            "testo": f"Perché {topic} non funziona come pensi",
            "caratteri": 0
        })

    # Formula 4 — Prova
    if prima and dopo:
        titoli.append({
            "formula": "prova",
            "testo": f"Da {prima} a {dopo}: il processo completo",
            "caratteri": 0
        })
    else:
        titoli.append({
            "formula": "prova",
            "testo": f"Ho risolto {topic} — ecco come",
            "caratteri": 0
        })

    # Formula 5 — Domanda
    titoli.append({
        "formula": "domanda",
        "testo": f"Perché {topic} non porta risultati?",
        "caratteri": 0
    })

    # Calcola caratteri e flag
    for t in titoli:
        t["caratteri"] = len(t["testo"])
        t["ok_lunghezza"] = t["caratteri"] <= 60
        t["ha_keyword"] = keyword.lower() in t["testo"].lower() if keyword else True

    return titoli


def genera_script_completo(
    # Info video
    titolo_scelto: str,
    tipo_video: str,            # "anchor" | "shift" | "conversion" | "audit"
    pilastro: int,              # 1-5
    topic: str,
    keyword: str = "",
    durata_target_minuti: int = 10,
    # Contenuto specifico
    punti_principali: list = None,      # per Anchor: lista di punti
    credenza_da_smontare: str = "",     # per Shift
    caso_studio: dict = None,           # per Conversion
    # CTA
    nome_lead_magnet: str = "",
    cta_tipo: str = "lead_magnet",      # "lead_magnet" | "call" | "doppia"
    # Hook scelto
    hook_scelto: str = "",
    # Credibilità
    credibilita_tipo: str = "risultato",  # chiave da CREDIBILITY_FORMULAS
    credibilita_dati: dict = None,
    # Takeaway
    takeaway: str = ""
) -> dict:
    """
    Genera lo script completo con tutti i 7 componenti,
    timestamps, note regia, e retention hooks posizionati.
    """

    if punti_principali is None:
        punti_principali = []
    if credibilita_dati is None:
        credibilita_dati = {}
    if caso_studio is None:
        caso_studio = {}

    script = {
        "meta": {
            "titolo": titolo_scelto,
            "tipo": tipo_video,
            "pilastro": pilastro,
            "topic": topic,
            "keyword": keyword,
            "durata_target": f"{durata_target_minuti} minuti",
            "cta_tipo": cta_tipo,
            "generato_il": datetime.now().strftime("%d/%m/%Y %H:%M")
        },
        "componenti": []
    }

    # ─── TIMESTAMP CALCULATOR ───
    durata_sec = durata_target_minuti * 60
    timestamps = _calcola_timestamps(durata_sec, tipo_video, len(punti_principali))

    # ─── 1. HOOK ───
    if not hook_scelto:
        hook_scelto = f"[INSERISCI HOOK SCELTO — usa genera_hooks() per generarne 3]"

    script["componenti"].append({
        "numero": 1,
        "nome": "HOOK",
        "timestamp": timestamps["hook"],
        "durata": "0-15 secondi",
        "regia": "[FACCIA — primo piano, energia alta, guarda in camera]",
        "testo": hook_scelto,
        "note": "Deve catturare in <5 secondi. Zero intro generiche."
    })

    # ─── 2. SETUP ───
    punti_setup = ""
    if punti_principali:
        for i, p in enumerate(punti_principali, 1):
            ordine = ["primo", "secondo", "terzo", "quarto", "quinto"][i-1] if i <= 5 else f"{i}"
            punti_setup += f"{ordine}, {p};\n"

    setup_testo = (
        f"In questo video ti mostro {topic}"
        f"{' — nello specifico:' if punti_principali else '.'}\n"
    )
    if punti_setup:
        setup_testo += punti_setup

    # CTA Preview
    if nome_lead_magnet:
        setup_testo += (
            f"\nA proposito — ho preparato {nome_lead_magnet} gratuito "
            f"che trovi in descrizione. Ma prima vediamo questi punti."
        )

    script["componenti"].append({
        "numero": 2,
        "nome": "SETUP",
        "timestamp": timestamps["setup"],
        "durata": "15-45 secondi",
        "regia": "[FACCIA — tono sicuro, roadmap del video]",
        "testo": setup_testo,
        "cta_level": "PREVIEW (menzione 1/3)",
        "note": "Max 30 sec. Ogni punto citato = loop aperto."
    })

    # ─── 3. CREDIBILITÀ ───
    cred_template = CREDIBILITY_FORMULAS.get(credibilita_tipo, CREDIBILITY_FORMULAS["minimalista"])
    cred_testo = cred_template
    for key, val in credibilita_dati.items():
        cred_testo = cred_testo.replace(f"{{{key}}}", str(val))

    script["componenti"].append({
        "numero": 3,
        "nome": "CREDIBILITÀ",
        "timestamp": timestamps["credibilita"],
        "durata": "30-60 secondi",
        "regia": "[FACCIA — tono autorevole ma umile]",
        "testo": cred_testo,
        "note": "Max 60 sec. MOSTRA, non DIRE. Risultati > curriculum."
    })

    # ─── 4. CONTENUTO CORE ───
    contenuto_componenti = []

    if tipo_video == "anchor":
        contenuto_componenti = _genera_contenuto_anchor(
            punti_principali, timestamps, nome_lead_magnet
        )
    elif tipo_video == "shift":
        contenuto_componenti = _genera_contenuto_shift(
            credenza_da_smontare, punti_principali, timestamps
        )
    elif tipo_video == "conversion":
        contenuto_componenti = _genera_contenuto_conversion(
            caso_studio, timestamps
        )
    elif tipo_video == "audit":
        contenuto_componenti = _genera_contenuto_audit(timestamps)

    script["componenti"].append({
        "numero": 4,
        "nome": "CONTENUTO CORE",
        "timestamp": timestamps["contenuto_start"],
        "durata": f"~{int(durata_sec * 0.75 / 60)} minuti (70-80%)",
        "sottosezioni": contenuto_componenti,
        "note": "70-80% del video. Include retention hooks ogni 2-3 min."
    })

    # ─── 5. RICAP ───
    ricap_punti = ""
    if punti_principali:
        ordini = ["Primo", "Secondo", "Terzo", "Quarto", "Quinto"]
        for i, p in enumerate(punti_principali[:5], 0):
            ricap_punti += f"{ordini[i]}: {p}.\n"

    ricap_testo = f"Ricapitoliamo. Abbiamo visto {len(punti_principali)} cose:\n"
    ricap_testo += ricap_punti
    ricap_testo += f"\nIl takeaway principale è questo:\n{takeaway if takeaway else '[INSERISCI TAKEAWAY — 1 frase memorabile]'}"

    script["componenti"].append({
        "numero": 5,
        "nome": "RICAP",
        "timestamp": timestamps["ricap"],
        "durata": "30-60 secondi",
        "regia": "[FACCIA — tono conclusivo, riassuntivo]",
        "testo": ricap_testo,
        "note": "Max 60 sec. 1 frase per punto + 1 takeaway memorabile."
    })

    # ─── 6. CTA FINALE ───
    cta_testo = _genera_cta_finale(cta_tipo, nome_lead_magnet)

    script["componenti"].append({
        "numero": 6,
        "nome": "CTA FINALE",
        "timestamp": timestamps["cta"],
        "durata": "30-60 secondi",
        "regia": "[FACCIA — tono diretto, invitante, non aggressivo]",
        "testo": cta_testo,
        "cta_level": "FINALE (menzione 3/3)",
        "note": "Specifica + beneficio + de-risking. UNA azione principale."
    })

    # ─── 7. RETENTION HOOKS MAP ───
    retention_map = _posiziona_retention_hooks(durata_target_minuti, tipo_video)
    script["retention_hooks"] = retention_map

    # ─── POST-VIDEO ───
    script["post_video"] = {
        "pinned_comment": _genera_pinned_comment(nome_lead_magnet, punti_principali, timestamps),
        "description": _genera_description(topic, keyword, nome_lead_magnet, punti_principali, timestamps),
        "thumbnail_concepts": _genera_thumbnail_concepts(titolo_scelto, topic, tipo_video)
    }

    return script


def _calcola_timestamps(durata_sec: int, tipo: str, n_punti: int) -> dict:
    """Calcola timestamps automatici per ogni componente."""
    ts = {}
    ts["hook"] = "0:00"
    ts["setup"] = "0:15"
    ts["credibilita"] = "0:45"
    ts["contenuto_start"] = "1:15"

    # Contenuto finisce a ~80% del video
    contenuto_end_sec = int(durata_sec * 0.82)
    ts["ricap"] = _sec_to_ts(contenuto_end_sec)
    ts["cta"] = _sec_to_ts(contenuto_end_sec + 45)

    # Sottopunti del contenuto
    if n_punti > 0:
        contenuto_durata = contenuto_end_sec - 75  # dopo hook+setup+cred
        per_punto = contenuto_durata // n_punti
        ts["punti"] = []
        for i in range(n_punti):
            ts["punti"].append(_sec_to_ts(75 + (i * per_punto)))

    return ts


def _sec_to_ts(seconds: int) -> str:
    """Converte secondi in timestamp MM:SS."""
    m = seconds // 60
    s = seconds % 60
    return f"{m}:{s:02d}"


def _genera_contenuto_anchor(punti: list, timestamps: dict, lead_magnet: str) -> list:
    """Genera contenuto per video Anchor (tutorial)."""
    componenti = []
    ts_punti = timestamps.get("punti", [])

    for i, punto in enumerate(punti):
        ts = ts_punti[i] if i < len(ts_punti) else "X:XX"

        retention = ""
        if i == 0:
            retention = "\n\n{RETENTION HOOK — Open Loop}: \"Tra poco vedremo il punto più importante, ma prima devi capire questo.\""
        elif i == len(punti) // 2:
            retention = f"\n\n{{RETENTION HOOK — CTA Reminder}}: \"Quello che ti sto mostrando adesso è esattamente uno dei punti della {lead_magnet} in descrizione.\""
        else:
            retention = "\n\n{RETENTION HOOK — Teaser}: \"Il prossimo punto è quello dove la maggior parte dei miei clienti ha l'AHA moment.\""

        componenti.append({
            "sottosezione": f"PUNTO {i+1}",
            "titolo": punto,
            "timestamp": ts,
            "testo": (
                f"[FACCIA]\n"
                f"AFFERMAZIONE: [Cosa dici su '{punto}' — 1-2 frasi]\n\n"
                f"SPIEGAZIONE: [Perché è importante — 2-3 frasi]\n"
                f"\"Il motivo è che [spiegazione]. "
                f"Questo significa che [conseguenza per lui].\"\n\n"
                f"[SCREENCAST]\n"
                f"ESEMPIO: [Caso concreto o mostra su schermo — 3-5 frasi]\n"
                f"\"Ti faccio un esempio...\"\n\n"
                f"[FACCIA]\n"
                f"AZIONE: [Cosa deve fare lui — 1-2 frasi]\n"
                f"\"Quello che puoi fare è [azione specifica].\""
                f"{retention}\n\n"
                f"TRANSIZIONE: [Collegamento al punto successivo]"
            ),
            "durata_stimata": "1.5-3 minuti",
            "regia_note": "[Alterna FACCIA e SCREENCAST]"
        })

    return componenti


def _genera_contenuto_shift(credenza: str, punti: list, timestamps: dict) -> list:
    """Genera contenuto per video Shift (reframe in 4 atti)."""
    return [
        {
            "sottosezione": "ATTO 1 — LA CREDENZA COMUNE",
            "timestamp": timestamps["contenuto_start"],
            "durata_stimata": "2-3 minuti",
            "testo": (
                f"[FACCIA]\n"
                f"\"La maggior parte degli imprenditori crede che {credenza if credenza else '[credenza da smontare]'}.\"\n\n"
                f"\"Ed è comprensibile — [perché sembra logica].\n"
                f"Non è colpa tua pensarla così. Quasi tutti ti dicono la stessa cosa.\"\n\n"
                f"{{RETENTION HOOK — Teaser}}\n"
                f"\"Ma c'è un problema con questo ragionamento.\""
            )
        },
        {
            "sottosezione": "ATTO 2 — PERCHÉ È SBAGLIATA",
            "timestamp": "X:XX",
            "durata_stimata": "3-5 minuti",
            "testo": (
                f"[SCREENCAST — mostra dati/evidenze]\n"
                f"DATI: \"Guardate questi numeri...\"\n\n"
                f"[FACCIA]\n"
                f"LOGICA: \"Se ci pensi, la logica non regge perché...\"\n\n"
                f"[SCREENCAST]\n"
                f"ESEMPIO: \"Vi faccio vedere un caso reale...\"\n\n"
                f"{{RETENTION HOOK — Open Loop}}\n\n"
                f"[FACCIA — energia alta]\n"
                f"MOMENTO AHA: \"Il punto è che il problema non è [{credenza}]. "
                f"Il problema è [vera causa].\""
            )
        },
        {
            "sottosezione": "ATTO 3 — IL REFRAME",
            "timestamp": "X:XX",
            "durata_stimata": "3-4 minuti",
            "testo": (
                f"[FACCIA]\n"
                f"\"Ecco come dovresti pensarla:\"\n\n"
                f"[Presenta il TUO framework/approccio]\n"
                f"[Spiega perché funziona — dati, logica, risultati]\n"
                f"[Se hai un framework con nome — presentalo qui]\n\n"
                f"{{RETENTION HOOK — Bonus Inaspettato}}\n\n"
                f"[SCREENCAST — esempio dove il reframe ha prodotto risultati]"
            )
        },
        {
            "sottosezione": "ATTO 4 — COSA FARE ADESSO",
            "timestamp": "X:XX",
            "durata_stimata": "2-3 minuti",
            "testo": (
                f"[FACCIA]\n"
                f"\"Ok, in pratica cosa puoi fare?\"\n\n"
                f"\"Il primo passo è [azione semplice]. Puoi farlo oggi.\"\n"
                f"\"Il secondo passo è [azione più avanzata].\"\n"
                f"\"E se vuoi fare il terzo passo — che è il più impattante — "
                f"ti serve [risorsa/aiuto].\"\n\n"
                f"→ Transizione naturale alla CTA"
            )
        }
    ]


def _genera_contenuto_conversion(caso: dict, timestamps: dict) -> list:
    """Genera contenuto per video Conversion (caso studio in 4 atti)."""
    return [
        {
            "sottosezione": "ATTO 1 — IL CONTESTO",
            "timestamp": timestamps["contenuto_start"],
            "durata_stimata": "1-2 minuti",
            "testo": (
                f"[FACCIA]\n"
                f"\"Un'azienda nel settore {caso.get('settore', '[settore]')} ci ha contattato "
                f"con questo problema: {caso.get('problema', '[problema]')}.\"\n\n"
                f"Metriche iniziali:\n"
                f"  CR: {caso.get('cr_prima', '[X]')}%\n"
                f"  CPA: €{caso.get('cpa_prima', '[X]')}\n"
                f"  Budget: €{caso.get('budget', '[X]')}/mese\n\n"
                f"\"Erano frustrati perché {caso.get('frustrazione', '[emozione]')}.\""
            )
        },
        {
            "sottosezione": "ATTO 2 — LA DIAGNOSI",
            "timestamp": "X:XX",
            "durata_stimata": "2-4 minuti",
            "testo": (
                f"[SCREENCAST — mostra analisi]\n"
                f"\"La prima cosa che abbiamo fatto è analizzare il funnel.\"\n\n"
                f"[Mostra screenshot, heatmap, dati]\n"
                f"Per ogni problema: \"Problema [N]: [cosa] — questo causava [conseguenza].\"\n\n"
                f"{{RETENTION HOOK — Open Loop}}\n\n"
                f"\"Dei [N] problemi trovati, questi 3 erano i più impattanti.\""
            )
        },
        {
            "sottosezione": "ATTO 3 — L'IMPLEMENTAZIONE",
            "timestamp": "X:XX",
            "durata_stimata": "3-5 minuti",
            "testo": (
                f"[SCREENCAST — before/after]\n"
                f"Per ogni intervento:\n"
                f"  \"Intervento [N]: [cosa abbiamo fatto]\"\n"
                f"  \"Perché: [ragionamento]\"\n"
                f"  [MOSTRA: Prima → Dopo]\n\n"
                f"{{RETENTION HOOK — Bonus}}: \"E qui c'è una cosa che non ci aspettavamo...\"\n\n"
                f"\"Timeline: questo ci ha richiesto {caso.get('durata', '[tempo]')}.\""
            )
        },
        {
            "sottosezione": "ATTO 4 — I RISULTATI",
            "timestamp": "X:XX",
            "durata_stimata": "2-3 minuti",
            "testo": (
                f"[SCREENCAST — dashboard before/after]\n"
                f"\"I numeri:\"\n"
                f"  CR: da {caso.get('cr_prima', '[X]')}% a {caso.get('cr_dopo', '[Y]')}%\n"
                f"  CPA: da €{caso.get('cpa_prima', '[X]')} a €{caso.get('cpa_dopo', '[Y]')}\n"
                f"  Revenue: +€{caso.get('revenue_delta', '[Z]')}/mese\n\n"
                f"[FACCIA]\n"
                f"\"Per l'imprenditore, questo ha significato {caso.get('impatto_umano', '[impatto concreto]')}.\"\n\n"
                f"\"Se la tua situazione è simile — questi stessi interventi "
                f"probabilmente funzionerebbero anche per te.\""
            )
        }
    ]


def _genera_contenuto_audit(timestamps: dict) -> list:
    """Genera struttura per video Audit Live."""
    return [
        {
            "sottosezione": "AUDIT LIVE",
            "timestamp": timestamps["contenuto_start"],
            "durata_stimata": "8-15 minuti",
            "testo": (
                "[SCREENCAST — condividi schermo]\n\n"
                "\"Oggi analizzo dal vivo la landing page di [iscritto/azienda]. "
                "Non ho preparato niente — è la prima volta che la vedo.\"\n\n"
                "[Apri la pagina]\n"
                "PRIMA IMPRESSIONE (5 sec): \"Ok, la prima cosa che noto è...\"\n\n"
                "ABOVE THE FOLD: \"La headline dice [X]. Funziona? Vediamo...\"\n\n"
                "SCROLL DOWN (sezione per sezione):\n"
                "  \"Qui vedo [cosa]. Il problema è [analisi]. Io farei [suggerimento].\"\n\n"
                "{RETENTION HOOK — Domanda}: \"Avete notato anche voi questo?\"\n\n"
                "CTA: \"La CTA dice [X]. Come la migliorerei: [Y].\"\n\n"
                "SOCIAL PROOF: \"Hanno testimonial? Dove? Efficaci?\"\n\n"
                "MOBILE CHECK: \"Vediamo su mobile...\"\n\n"
                "{RETENTION HOOK — Bonus}: \"C'è un'altra cosa che nessuno nota mai...\"\n\n"
                "RICAPITOLO AUDIT:\n"
                "\"In totale ho trovato [N] punti. I 3 più impattanti: [1], [2], [3].\""
            ),
            "regia_note": "Tono: pensiero ad alta voce, spontaneo, genuino. Non troppo scriptato."
        }
    ]


def _genera_cta_finale(cta_tipo: str, lead_magnet: str) -> str:
    """Genera il testo della CTA finale."""

    if cta_tipo == "lead_magnet":
        return (
            f"[FACCIA — tono diretto, invitante]\n"
            f"\"Se vuoi applicare tutto quello che abbiamo visto oggi, "
            f"ho preparato {lead_magnet if lead_magnet else '[nome lead magnet]'} "
            f"— è gratuito e lo trovi nel primo link in descrizione.\n\n"
            f"Dentro c'è [cosa contiene — 1 riga].\n"
            f"Scaricalo, usalo sul tuo sito, "
            f"e dimmi nei commenti cosa hai trovato.\""
        )
    elif cta_tipo == "call":
        return (
            f"[FACCIA — tono diretto]\n"
            f"\"Se riconosci questa situazione nel tuo business "
            f"— traffico che arriva ma non converte — "
            f"e vuoi che lo analizziamo insieme, "
            f"prenota una call gratuita.\n\n"
            f"Non è una vendita mascherata. "
            f"Nella call facciamo esattamente quello che ho fatto in questo video "
            f"— ma sul TUO caso specifico.\n"
            f"Link in descrizione.\""
        )
    else:  # doppia
        return (
            f"[FACCIA — tono diretto]\n"
            f"\"Due cose per te:\n\n"
            f"PRIMA: scarica {lead_magnet if lead_magnet else '[lead magnet]'} "
            f"— è gratis, link in descrizione. "
            f"Ti serve per applicare tutto da solo.\n\n"
            f"SECONDA: se preferisci che qualcuno lo faccia per te "
            f"— il mio team si occupa esattamente di questo. "
            f"C'è il link per una call gratuita sempre in descrizione.\n\n"
            f"Scegli quella che preferisci.\""
        )


def _posiziona_retention_hooks(durata_min: int, tipo: str) -> list:
    """Posiziona i retention hooks lungo il video."""
    hooks = []

    # Open loop nel primo minuto
    hooks.append({
        "timestamp": "0:30-1:00",
        "pattern": "open_loop",
        "testo": "\"Tra poco ti mostro [punto più importante] — ma prima devi capire questo.\"",
        "nota": "Inserisci durante il setup o inizio contenuto"
    })

    # Ogni 2-3 minuti
    minuti = list(range(3, durata_min, 2))
    patterns_rotation = ["teaser", "prova_visiva", "domanda_retorica",
                         "contrasto", "preview_interna", "aneddoto"]

    for i, m in enumerate(minuti):
        pattern_key = patterns_rotation[i % len(patterns_rotation)]
        pattern = RETENTION_PATTERNS[pattern_key]
        hooks.append({
            "timestamp": f"{m}:00",
            "pattern": pattern_key,
            "testo": pattern["template"],
            "nota": pattern["posizione"]
        })

    # Bonus a metà video
    meta = durata_min // 2
    hooks.append({
        "timestamp": f"{meta}:00",
        "pattern": "bonus",
        "testo": RETENTION_PATTERNS["bonus"]["template"],
        "nota": "Premia chi è arrivato fin qui"
    })

    # CTA reminder a metà (menzione 2/3)
    hooks.append({
        "timestamp": f"{meta + 1}:00",
        "pattern": "cta_reminder",
        "testo": "\"Quello che ti sto mostrando è esattamente uno dei punti della [lead magnet] in descrizione.\"",
        "nota": "Menzione 2/3 della CTA — collegata al contenuto"
    })

    return sorted(hooks, key=lambda x: x["timestamp"])


def _genera_pinned_comment(lead_magnet: str, punti: list, timestamps: dict) -> str:
    """Genera il testo del pinned comment."""
    pc = ""
    if lead_magnet:
        pc += f"📋 {lead_magnet} GRATUITO: [LINK]\n"
    pc += "📞 Prenota call gratuita: [LINK]\n\n"
    pc += "⏰ Timestamps:\n"
    pc += f"0:00 Hook + Intro\n"

    ts_punti = timestamps.get("punti", [])
    for i, p in enumerate(punti):
        ts = ts_punti[i] if i < len(ts_punti) else "X:XX"
        pc += f"{ts} {p}\n"

    pc += f"{timestamps.get('ricap', 'X:XX')} Ricap + Risorse\n\n"
    pc += "💬 Scrivimi nei commenti: qual è il problema più grande del tuo funnel in questo momento?"

    return pc


def _genera_description(topic: str, keyword: str, lead_magnet: str,
                        punti: list, timestamps: dict) -> str:
    """Genera la description completa."""
    desc = ""

    # Prime 2 righe (visibili senza expand)
    if lead_magnet:
        desc += f"📋 {lead_magnet} GRATUITO: [LINK]\n"
    desc += "📞 Prenota call gratuita: [LINK]\n\n"

    # Riassunto con keyword
    desc += f"In questo video ti mostro {topic}.\n"
    if keyword:
        desc += f"{keyword} — guida pratica con esempi reali.\n"
    desc += "\n"

    # Timestamps
    desc += "⏰ TIMESTAMPS:\n"
    desc += "0:00 Intro\n"
    ts_punti = timestamps.get("punti", [])
    for i, p in enumerate(punti):
        ts = ts_punti[i] if i < len(ts_punti) else "X:XX"
        desc += f"{ts} {p}\n"
    desc += f"{timestamps.get('ricap', 'X:XX')} Ricap + Risorse\n\n"

    # Risorse
    desc += "🔗 RISORSE CITATE NEL VIDEO:\n"
    desc += "• [Risorsa 1]: [link]\n"
    desc += "• [Risorsa 2]: [link]\n\n"

    # Chi sono
    desc += "📌 CHI SONO:\n"
    desc += "Digital Empire — agenzia CRO che aiuta aziende con traffico a convertire meglio, senza spendere di più in ads.\n\n"

    # Tags
    desc += "🏷️ TAGS:\n"
    desc += "#CRO #ConversionRate #LandingPage #DigitalMarketing"
    if keyword:
        kw_tag = keyword.replace(" ", "").title()
        desc += f" #{kw_tag}"
    desc += "\n"

    return desc


def _genera_thumbnail_concepts(titolo: str, topic: str, tipo: str) -> list:
    """Genera 3 concetti thumbnail."""
    concepts = []

    # Concept 1 — Testo + Faccia
    concepts.append({
        "concept": "Testo Bold + Faccia Espressiva",
        "testo_thumbnail": topic[:25].upper() if topic else "ERRORE #1",
        "espressione": "sorpresa / shock",
        "sfondo": "Colore solido contrastante (rosso o giallo)",
        "elemento_extra": "Freccia rossa che indica il testo"
    })

    # Concept 2 — Before/After
    concepts.append({
        "concept": "Before/After Screenshot",
        "testo_thumbnail": "PRIMA → DOPO",
        "espressione": "determinazione / soddisfazione",
        "sfondo": "Split screen (rosso sx / verde dx)",
        "elemento_extra": "Screenshot annotati del prima e dopo"
    })

    # Concept 3 — Numero Bold
    concepts.append({
        "concept": "Numero Grande + Reazione",
        "testo_thumbnail": "+200% CR" if tipo == "conversion" else "3 ERRORI",
        "espressione": "curiosità intensa",
        "sfondo": "Gradiente scuro",
        "elemento_extra": "Grafico con freccia verso l'alto"
    })

    return concepts


def stampa_script(script: dict) -> str:
    """Formatta lo script completo in testo leggibile per reference."""

    output = []
    m = script["meta"]

    output.append("=" * 70)
    output.append(f"  🎬 SCRIPT: {m['titolo']}")
    output.append("=" * 70)
    output.append(f"  Tipo: {m['tipo'].upper()} | Pilastro: {m['pilastro']}")
    output.append(f"  Topic: {m['topic']}")
    if m['keyword']:
        output.append(f"  Keyword: {m['keyword']}")
    output.append(f"  Durata target: {m['durata_target']}")
    output.append(f"  CTA: {m['cta_tipo']}")
    output.append(f"  Generato: {m['generato_il']}")
    output.append("=" * 70)

    # Componenti principali
    for comp in script["componenti"]:
        output.append(f"\n{'─' * 70}")

        if "sottosezioni" in comp:
            # Contenuto Core con sottosezioni
            output.append(f"  [{comp['timestamp']}] 📹 {comp['nome']} ({comp['durata']})")
            output.append(f"{'─' * 70}")
            for sub in comp["sottosezioni"]:
                output.append(f"\n  ▸ {sub['sottosezione']}: {sub.get('titolo', '')}")
                output.append(f"    Timestamp: {sub.get('timestamp', 'X:XX')}")
                output.append(f"    Durata: {sub.get('durata_stimata', 'N/A')}")
                if sub.get('regia_note'):
                    output.append(f"    Regia: {sub['regia_note']}")
                output.append(f"\n{sub['testo']}")
        else:
            output.append(f"  [{comp['timestamp']}] 📹 {comp['nome']} ({comp['durata']})")
            output.append(f"{'─' * 70}")
            if comp.get('regia'):
                output.append(f"  Regia: {comp['regia']}")
            if comp.get('cta_level'):
                output.append(f"  CTA Level: {comp['cta_level']}")
            output.append(f"\n{comp['testo']}")
            if comp.get('note'):
                output.append(f"\n  📝 Note: {comp['note']}")

    # Retention Hooks Map
    output.append(f"\n{'═' * 70}")
    output.append("  🔄 MAPPA RETENTION HOOKS")
    output.append(f"{'═' * 70}")
    for rh in script.get("retention_hooks", []):
        output.append(f"  [{rh['timestamp']}] {rh['pattern'].upper()}")
        output.append(f"    {rh['testo']}")
        output.append(f"    → {rh['nota']}")

    # Post-video
    pv = script.get("post_video", {})
    if pv:
        output.append(f"\n{'═' * 70}")
        output.append("  📌 POST-VIDEO")
        output.append(f"{'═' * 70}")

        if pv.get("pinned_comment"):
            output.append(f"\n  PINNED COMMENT:")
            output.append(f"  {pv['pinned_comment']}")

        if pv.get("thumbnail_concepts"):
            output.append(f"\n  THUMBNAIL CONCEPTS:")
            for i, tc in enumerate(pv["thumbnail_concepts"], 1):
                output.append(f"  Concept {i}: {tc['concept']}")
                output.append(f"    Testo: {tc['testo_thumbnail']}")
                output.append(f"    Espressione: {tc['espressione']}")
                output.append(f"    Sfondo: {tc['sfondo']}")
                output.append(f"    Extra: {tc['elemento_extra']}")

    output.append(f"\n{'═' * 70}")
    return "\n".join(output)


# ═══════════════════════════════════════════════════
# ESEMPIO DI UTILIZZO COMPLETO
# ═══════════════════════════════════════════════════

if __name__ == "__main__":

    # 1. Genera hooks
    print("=" * 70)
    print("  STEP 1: GENERAZIONE HOOKS")
    print("=" * 70)

    hooks = genera_hooks(
        tipo_video="anchor",
        topic="la landing page che non converte",
        keyword="errori landing page",
        numeri={
            "percentuale": 90,
            "n_punti": 3,
            "prima": "0.8%",
            "dopo": "3.2%",
            "tempo": "14 giorni"
        }
    )

    for i, h in enumerate(hooks, 1):
        print(f"\n  HOOK {i} [{h['codice']}] — {h['categoria']}")
        print(f"  Formula: {h['formula']}")
        print(f"  >>> \"{h['testo']}\"")

    # 2. Genera titoli
    print(f"\n{'=' * 70}")
    print("  STEP 2: GENERAZIONE TITOLI")
    print("=" * 70)

    titoli = genera_titoli(
        topic="la landing page",
        tipo_video="anchor",
        keyword="errori landing page",
        numeri={"n_punti": 3, "prima": "0.8%", "dopo": "3.2%"}
    )

    for i, t in enumerate(titoli, 1):
        ok = "✅" if t["ok_lunghezza"] else "❌"
        kw = "🔑" if t["ha_keyword"] else "  "
        print(f"  {i}. {ok}{kw} [{t['caratteri']} car] \"{t['testo']}\"")

    # 3. Genera script completo
    print(f"\n{'=' * 70}")
    print("  STEP 3: SCRIPT COMPLETO")
    print("=" * 70)

    script = genera_script_completo(
        titolo_scelto="3 errori che uccidono le tue conversioni",
        tipo_video="anchor",
        pilastro=2,
        topic="errori landing page che uccidono le conversioni",
        keyword="errori landing page",
        durata_target_minuti=10,
        punti_principali=[
            "La headline non parla al cliente",
            "La CTA è troppo vaga",
            "Nessuna social proof above-the-fold"
        ],
        nome_lead_magnet="la Checklist CRO Gratuita",
        cta_tipo="doppia",
        hook_scelto=hooks[0]["testo"],
        credibilita_tipo="risultato",
        credibilita_dati={
            "tempo": "12 mesi",
            "N": "20+",
            "pattern": "avere una landing page che non converte il traffico che già hanno"
        },
        takeaway="Non serve un redesign del sito. Servono 3 modifiche chirurgiche nei punti giusti. Il copy batte il design."
    )

    print(stampa_script(script))

    # Salva
    with open("script_3_errori_landing.json", "w") as f:
        json.dump(script, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Script salvato in JSON")
