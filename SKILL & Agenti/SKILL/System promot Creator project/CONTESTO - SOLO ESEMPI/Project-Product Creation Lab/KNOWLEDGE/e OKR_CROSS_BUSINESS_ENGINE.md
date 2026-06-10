# ═══════════════════════════════════════════════════════════════
# 📄 OKR_CROSS_BUSINESS_ENGINE.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC
# Priorità: P0 — BLOCCANTE
# Dipendenze: TEMPLATE_PRODUZIONE.md, TEMPLATE_ARCHITETTURA.md,
#             STANDARD_QUALITA.md, CROSS_POLLINATION_ENGINE.md
# Referenziato da: Custom Instructions §2 (Processi di
#                  Ragionamento), §5 (Utilizzo Knowledge Base),
#                  §8 (Workflow Operativi)
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# 📋 SCOPO
# ═══════════════════════════════════════════════════════════════

# Questo file contiene il MOTORE COMPLETO del sistema OKR
# (Objectives and Key Results) per il multi-business Digital
# Empire. Definisce:
#
# 1. La logica di cascata Annuale → Trimestrale → Sprint Mensile
# 2. L'algoritmo di definizione OKR per ogni livello
# 3. Il sistema di scoring e progresso dei Key Results
# 4. I protocolli di review per ogni cadenza
# 5. La gap analysis automatizzata
# 6. Le regole di ricalibrazione mid-quarter
# 7. Il collegamento OKR ↔ Sprint Task ↔ Azioni quotidiane
# 8. Il meccanismo "Not-To-Do" integrato
#
# Senza OKR, Digital Empire opera per SENSAZIONE.
# Con OKR, opera per DATI E DIREZIONE.
#
# Principio fondamentale:
# "Se un task non è collegato a un Key Result,
#  NON È UNA PRIORITÀ. È una distrazione."


# ═══════════════════════════════════════════════════════════════
# 📖 CONTENUTO PRINCIPALE
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# SEZIONE 1: ARCHITETTURA DELLA CASCATA OKR
# ───────────────────────────────────────────────────────────────

# Il sistema OKR di Digital Empire opera su 3 livelli
# gerarchici. Ogni livello alimenta il successivo.
# La cascata garantisce che OGNI azione quotidiana sia
# collegata alla visione annuale.

OKR_CASCADE_ARCHITECTURE = {
    "versione": "1.0",

    "livelli": {
        "L1_ANNUALE": {
            "orizzonte": "12 mesi",
            "definito_quando": "Gennaio (o quando si inizia)",
            "review_cadenza": "Trimestrale",
            "struttura": {
                "vision_statement": "1 frase che definisce dove "
                                    "Digital Empire sarà a fine anno",
                "obiettivi_per_pillar": {
                    "pillar_1_agenzia": {
                        "objective": "1 — chiaro, ambizioso, "
                                     "ispirante",
                        "key_results": "3 — misurabili, "
                                       "con target numerico"
                    },
                    "pillar_2_info_biz": {
                        "objective": "1",
                        "key_results": "3"
                    },
                    "pillar_3_youtube": {
                        "objective": "1",
                        "key_results": "3"
                    },
                    "cross_pollination": {
                        "objective": "1",
                        "key_results": "3"
                    }
                },
                "totale_objectives": 4,
                "totale_key_results": 12
            }
        },

        "L2_TRIMESTRALE": {
            "orizzonte": "13 settimane",
            "definito_quando": "Primo lunedì del trimestre",
            "review_cadenza": "Mensile",
            "struttura": {
                "obiettivi_per_pillar": {
                    "per_ogni_pillar": {
                        "objectives": "1-2 — sotto-obiettivi "
                                      "che muovono i KR annuali",
                        "key_results": "2-3 per obiettivo"
                    }
                },
                "priorita_trimestre": "Max 3 — le cose PIÙ "
                                      "importanti del Q",
                "not_to_do": "3 — le cose che SCEGLI di "
                             "NON fare",
                "totale_objectives": "4-8",
                "totale_key_results": "8-24"
            }
        },

        "L3_SPRINT_MENSILE": {
            "orizzonte": "4-5 settimane",
            "definito_quando": "Primo lunedì del mese",
            "review_cadenza": "Settimanale",
            "struttura": {
                "focus_del_mese": "1 frase — il tema dominante",
                "task_prioritari": {
                    "numero": "5-7 — MAI più di 7",
                    "regola": "Ogni task DEVE essere collegato "
                              "a un Key Result trimestrale",
                    "formato": "Task specifico + Pillar + "
                               "KR linked + Status"
                },
                "regola_fondamentale": "Se un task non è "
                                       "collegabile a nessun KR → "
                                       "va nella Not-To-Do o "
                                       "viene posticipato"
            }
        }
    },

    "flusso_cascata": [
        "VISION ANNUALE → definisce la DIREZIONE",
        "OKR ANNUALI → definiscono il TRAGUARDO",
        "OKR TRIMESTRALI → definiscono il PERCORSO",
        "SPRINT MENSILE → definisce le AZIONI",
        "REVIEW SETTIMANALE → verifica l'ESECUZIONE"
    ]
}


# ───────────────────────────────────────────────────────────────
# SEZIONE 2: ALGORITMO DI DEFINIZIONE OKR
# ───────────────────────────────────────────────────────────────

# Processo sistematico per definire OKR di qualità.
# Un buon OKR rispetta criteri specifici. Un cattivo OKR
# è peggio di nessun OKR (crea falsa sicurezza).

def define_objective(
    pillar: str,
    livello: str,
    stato_attuale: dict,
    ambizione: str
) -> dict:
    """
    Genera un Objective di qualità per un pillar specifico.

    Args:
        pillar: "agenzia" | "info_biz" | "youtube" | "cross_poll"
        livello: "annuale" | "trimestrale"
        stato_attuale: metriche correnti del pillar
        ambizione: "conservativo" | "moderato" | "aggressivo"

    Returns:
        Objective validato con assessment di qualità
    """

    # REGOLE PER UN BUON OBJECTIVE:
    objective_rules = {
        "qualitativo": "L'Objective descrive UNA CONDIZIONE "
                       "da raggiungere, non un numero. "
                       "Es: 'Trasformare l'agenzia nel punto "
                       "di riferimento CRO in Italia' — NON "
                       "'Fare €50K/mese'",
        "ispirante": "Deve motivare. Leggendolo devi sentire "
                     "energia, non ansia.",
        "chiaro": "Chiunque lo legga deve capire COSA si "
                  "vuole ottenere. Zero ambiguità.",
        "raggiungibile_ma_sfidante": "Devi credere che sia "
                                      "possibile ma non facile. "
                                      "Se sei sicuro al 100% di "
                                      "raggiungerlo → è troppo "
                                      "basso. Se sei sicuro al "
                                      "100% di NON raggiungerlo "
                                      "→ è troppo alto.",
        "timeboxed": "Deve avere un orizzonte temporale "
                     "implicito (l'anno o il trimestre)."
    }

    # ANTI-PATTERN DA EVITARE:
    objective_antipatterns = [
        "Troppo vago: 'Crescere il business' → non misurabile",
        "Troppo specifico: 'Chiudere 12 clienti a €3K' → "
        "questo è un KR, non un Objective",
        "Troppo passivo: 'Mantenere le cose come sono' → "
        "non è un obiettivo, è inerzia",
        "Troppo disperso: 'Lanciare 3 corsi, scalare "
        "l'agenzia e fare 100K su YouTube' → sono 3 "
        "obiettivi, non 1",
        "Non controllabile: 'Diventare virale su YouTube' → "
        "non è sotto il tuo controllo diretto"
    ]

    return {
        "pillar": pillar,
        "livello": livello,
        "objective": "[DA COMPILARE]",
        "rules_checklist": objective_rules,
        "antipatterns_checklist": objective_antipatterns,
        "quality_score": None  # calcolato dopo compilazione
    }


def define_key_results(
    objective: str,
    pillar: str,
    livello: str,
    stato_attuale: dict,
    ambizione: str
) -> list:
    """
    Genera Key Results di qualità per un Objective.

    Args:
        objective: l'Objective di riferimento
        pillar: pillar di appartenenza
        livello: "annuale" | "trimestrale"
        stato_attuale: metriche correnti
        ambizione: livello di sfida dei target

    Returns:
        Lista di Key Results validati
    """

    # REGOLE PER UN BUON KEY RESULT:
    kr_rules = {
        "quantitativo": "Il KR DEVE avere un numero. "
                        "'Aumentare il close rate' NON è un KR. "
                        "'Portare il close rate dal 20% al 35%' "
                        "SÌ è un KR.",
        "misurabile_oggettivamente": "Due persone diverse che "
                                     "guardano gli stessi dati "
                                     "devono concordare se il KR "
                                     "è stato raggiunto o no.",
        "sotto_controllo": "Deve dipendere dalle TUE azioni, "
                           "non da fattori esterni. 'Ottenere "
                           "10 referral' è parzialmente fuori "
                           "controllo. 'Chiedere referral a "
                           "ogni cliente a fine progetto e "
                           "ottenerne almeno 5' è più sotto "
                           "controllo.",
        "collegato_all_objective": "Se raggiungi il KR, ti "
                                   "avvicini all'Objective. "
                                   "Se no, è il KR sbagliato.",
        "numero_giusto": "3 KR per Objective è il numero "
                         "ideale. 2 è accettabile. 4+ è "
                         "troppo (dispersione)."
    }

    # FORMULA PER SETTARE IL TARGET:
    target_formula = {
        "conservativo": {
            "descrizione": "Crescita del 10-20% sullo "
                           "stato attuale",
            "confidence": "80% di probabilità di raggiungerlo",
            "quando_usarlo": "Pillar nuovo o in difficoltà"
        },
        "moderato": {
            "descrizione": "Crescita del 30-50% sullo "
                           "stato attuale",
            "confidence": "50-60% di probabilità",
            "quando_usarlo": "Pillar stabile che vuoi far "
                             "crescere"
        },
        "aggressivo": {
            "descrizione": "Crescita del 70-100%+ sullo "
                           "stato attuale",
            "confidence": "20-30% di probabilità",
            "quando_usarlo": "Pillar con forte momentum o "
                             "quando vuoi un breakthrough"
        }
    }

    # CALIBRAZIONE RACCOMANDATA:
    calibrazione = {
        "annuale": "1 KR conservativo + 1 moderato + "
                   "1 aggressivo (moonshot)",
        "trimestrale": "2 KR moderati + 1 aggressivo "
                       "OPPURE 2 conservativi + 1 moderato "
                       "se il pillar è in difficoltà"
    }

    # ANTI-PATTERN KEY RESULTS:
    kr_antipatterns = [
        "KR di attività (non di risultato): 'Pubblicare 12 "
        "video' → è un task, non un KR. Il KR è 'Generare "
        "100 lead da YouTube'. I video sono il MEZZO.",
        "KR non misurabile: 'Migliorare la qualità dei "
        "contenuti' → come lo misuri? Riscrivi come "
        "'Aumentare il watch time medio da 4 a 7 minuti'.",
        "KR binario: 'Lanciare il corso X' → è un sì/no. "
        "Non misura il RISULTATO. Meglio: 'Lanciare il "
        "corso X e generare €5K nei primi 30 giorni'.",
        "KR disconnesso: un KR su YouTube sotto l'Objective "
        "dell'agenzia → indica confusione strutturale",
        "KR duplicato: lo stesso KR sotto due Objectives "
        "diversi → rimuovi da uno"
    ]

    return {
        "objective_ref": objective,
        "pillar": pillar,
        "livello": livello,
        "kr_template": [
            {
                "kr_id": f"{pillar}_KR1",
                "testo": "[DA COMPILARE — formato: verbo + "
                         "metrica + da X a Y + entro quando]",
                "metrica": "[Nome metrica]",
                "baseline": "[Valore attuale]",
                "target": "[Valore target]",
                "ambizione_tipo": "[conservativo|moderato|aggressivo]",
                "fonte_dato": "[Dove trovi questo numero]",
                "frequenza_misurazione": "[Settimanale|Mensile]"
            }
        ],
        "kr_rules": kr_rules,
        "target_formula": target_formula,
        "calibrazione": calibrazione,
        "antipatterns": kr_antipatterns
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 3: SISTEMA DI SCORING E PROGRESSO
# ───────────────────────────────────────────────────────────────

# Come misurare il progresso dei Key Results e determinare
# lo status (🟢🟡🔴) di ogni pillar.

SCORING_SYSTEM = {
    "versione": "1.0",

    "kr_progress_calculation": {
        "formula": "(valore_attuale - baseline) / "
                   "(target - baseline) × 100",
        "esempio": "Baseline: 20%, Target: 35%, "
                   "Attuale: 27.5% → Progresso: "
                   "(27.5 - 20) / (35 - 20) × 100 = 50%",
        "nota": "Se il valore attuale supera il target, "
                "il progresso è >100% (ottimo, ma non "
                "aggiustare il target retroattivamente)"
    },

    "status_thresholds": {
        "by_quarter_progress": {
            "fine_mese_1": {
                "on_track": ">= 25%",
                "at_risk": "15% — 24%",
                "off_track": "< 15%"
            },
            "fine_mese_2": {
                "on_track": ">= 55%",
                "at_risk": "35% — 54%",
                "off_track": "< 35%"
            },
            "fine_mese_3": {
                "on_track": ">= 70%",
                "at_risk": "50% — 69%",
                "off_track": "< 50%"
            }
        },
        "colori": {
            "on_track": "🟢",
            "at_risk": "🟡",
            "off_track": "🔴"
        }
    },

    "pillar_status_aggregation": {
        "regola": "Lo status del pillar = lo status del "
                  "KR con performance PEGGIORE",
        "logica": "Se hai 3 KR: 🟢 🟢 🔴 → il pillar è 🔴. "
                  "Il KR più debole determina lo status "
                  "perché indica dove serve attenzione.",
        "eccezione": "Se 2 su 3 KR sono 🟢 e 1 è 🟡 → "
                     "il pillar è 🟡 (non 🟢). La catena "
                     "è forte quanto l'anello più debole."
    },

    "empire_status_aggregation": {
        "regola": "Lo status di Digital Empire = lo status "
                  "dell'AGENZIA CRO",
        "logica": "L'agenzia è il core. Se l'agenzia è 🔴, "
                  "l'intero Empire è 🔴, anche se info-biz "
                  "e YouTube sono 🟢.",
        "eccezione": "Se l'agenzia è 🟢 ma gli altri 2 "
                     "pillar sono 🔴 → l'Empire è 🟡 "
                     "(il core è sano ma gli amplificatori "
                     "non stanno funzionando)"
    }
}


def calculate_kr_progress(
    baseline: float,
    target: float,
    current: float
) -> dict:
    """
    Calcola il progresso di un singolo Key Result.

    Args:
        baseline: valore di partenza
        target: valore obiettivo
        current: valore attuale

    Returns:
        Dizionario con progresso %, status, e gap
    """
    if target == baseline:
        progress = 100.0 if current >= target else 0.0
    else:
        progress = ((current - baseline) /
                    (target - baseline)) * 100

    progress = round(max(0, progress), 1)

    gap = target - current
    gap_pct = round(100 - progress, 1)

    return {
        "baseline": baseline,
        "target": target,
        "current": current,
        "progress_pct": progress,
        "gap_absolute": round(gap, 2),
        "gap_pct": gap_pct,
        "direction": "↑" if current > baseline else (
            "→" if current == baseline else "↓"
        )
    }


def determine_kr_status(
    progress_pct: float,
    month_in_quarter: int
) -> dict:
    """
    Determina lo status 🟢🟡🔴 di un KR basato sul
    progresso e sul punto del trimestre.

    Args:
        progress_pct: progresso percentuale del KR
        month_in_quarter: 1, 2, o 3

    Returns:
        Status con colore, label, e azione suggerita
    """
    thresholds = SCORING_SYSTEM["status_thresholds"][
        "by_quarter_progress"
    ]

    month_key = f"fine_mese_{month_in_quarter}"
    if month_key not in thresholds:
        month_key = "fine_mese_3"

    month_thresholds = thresholds[month_key]

    # Parse thresholds (valori esemplificativi)
    on_track_min = {
        "fine_mese_1": 25,
        "fine_mese_2": 55,
        "fine_mese_3": 70
    }
    at_risk_min = {
        "fine_mese_1": 15,
        "fine_mese_2": 35,
        "fine_mese_3": 50
    }

    ot_min = on_track_min.get(month_key, 70)
    ar_min = at_risk_min.get(month_key, 50)

    if progress_pct >= ot_min:
        return {
            "status": "🟢",
            "label": "ON TRACK",
            "azione": "Mantieni la cadenza. Nessuna "
                      "azione correttiva necessaria.",
            "urgenza": "BASSA"
        }
    elif progress_pct >= ar_min:
        return {
            "status": "🟡",
            "label": "A RISCHIO",
            "azione": "Analizza la causa del ritardo. "
                      "Serve una micro-correzione: più "
                      "tempo allocato, priorità diversa, "
                      "o approccio diverso.",
            "urgenza": "MEDIA"
        }
    else:
        return {
            "status": "🔴",
            "label": "OFF TRACK",
            "azione": "Intervento immediato necessario. "
                      "Opzioni: (1) Riallocare risorse da "
                      "un altro pillar, (2) Ricalibra il "
                      "target se era irrealistico, (3) "
                      "Cambia strategia di esecuzione.",
            "urgenza": "ALTA"
        }


def calculate_pillar_status(
    kr_statuses: list
) -> dict:
    """
    Calcola lo status aggregato di un pillar basato
    sui suoi Key Results.

    Args:
        kr_statuses: lista di status (🟢, 🟡, 🔴)
                     per ogni KR del pillar

    Returns:
        Status del pillar con analisi
    """
    status_priority = {"🔴": 0, "🟡": 1, "🟢": 2}

    worst_status = min(
        kr_statuses,
        key=lambda s: status_priority.get(s, 2)
    )

    count_green = kr_statuses.count("🟢")
    count_yellow = kr_statuses.count("🟡")
    count_red = kr_statuses.count("🔴")

    # Eccezione: 2 verdi + 1 giallo = giallo
    if count_green >= 2 and count_yellow == 1 and count_red == 0:
        aggregated = "🟡"
        note = "Prevalentemente on track ma 1 KR richiede attenzione"
    else:
        aggregated = worst_status
        if count_red > 0:
            note = f"{count_red} KR off track — intervento necessario"
        elif count_yellow > 0:
            note = f"{count_yellow} KR a rischio — monitorare"
        else:
            note = "Tutti i KR on track"

    return {
        "status": aggregated,
        "dettaglio": {
            "green": count_green,
            "yellow": count_yellow,
            "red": count_red
        },
        "note": note
    }


def calculate_empire_status(
    pillar_statuses: dict
) -> dict:
    """
    Calcola lo status complessivo di Digital Empire.

    Args:
        pillar_statuses: {
            "agenzia": "🟢"|"🟡"|"🔴",
            "info_biz": "🟢"|"🟡"|"🔴",
            "youtube": "🟢"|"🟡"|"🔴"
        }

    Returns:
        Status Empire con diagnosi e azione
    """
    agenzia = pillar_statuses.get("agenzia", "🟡")
    info_biz = pillar_statuses.get("info_biz", "🟡")
    youtube = pillar_statuses.get("youtube", "🟡")

    # Regola 1: L'agenzia determina lo status base
    if agenzia == "🔴":
        return {
            "empire_status": "🔴",
            "diagnosi": "Il CORE BUSINESS è in difficoltà. "
                        "Tutto il resto è irrilevante finché "
                        "l'agenzia non è almeno 🟡.",
            "azione_immediata": "STOP a info-biz e YouTube. "
                                 "100% focus su pipeline agenzia: "
                                 "outreach, follow-up, call.",
            "regola_attivata": "GERARCHIA SACRA — Agenzia = Ossigeno"
        }

    # Regola 2: Agenzia 🟢 ma altri 2 rossi
    if agenzia == "🟢" and info_biz == "🔴" and youtube == "🔴":
        return {
            "empire_status": "🟡",
            "diagnosi": "Core sano ma amplificatori fermi. "
                        "Stai operando come un business "
                        "singolo, non come un impero.",
            "azione_immediata": "Mantieni l'agenzia. Scegli "
                                 "1 solo amplificatore da "
                                 "riportare a 🟡. Non entrambi.",
            "regola_attivata": "FOCUS — Max 1 recovery alla volta"
        }

    # Regola 3: Tutto 🟢
    if agenzia == "🟢" and info_biz == "🟢" and youtube == "🟢":
        return {
            "empire_status": "🟢",
            "diagnosi": "Tutti i pillar on track. Rara "
                        "condizione ideale.",
            "azione_immediata": "Mantieni la cadenza. Questo "
                                 "è il momento di spingere la "
                                 "cross-pollination al massimo.",
            "regola_attivata": "CRESCITA — Attiva sinergie"
        }

    # Regola 4: Mix
    statuses = [agenzia, info_biz, youtube]
    if "🔴" in statuses:
        return {
            "empire_status": "🟡",
            "diagnosi": f"1+ pillar off track. Agenzia: "
                        f"{agenzia}, Info-Biz: {info_biz}, "
                        f"YouTube: {youtube}.",
            "azione_immediata": "Identifica il pillar 🔴 e "
                                 "alloca risorse extra dalla "
                                 "gap analysis. NON fermare "
                                 "l'agenzia per risolvere.",
            "regola_attivata": "GAP ANALYSIS — Prioritizza per impatto"
        }

    # Default: 🟡
    return {
        "empire_status": "🟡",
        "diagnosi": f"Situazione mista. Agenzia: {agenzia}, "
                    f"Info-Biz: {info_biz}, YouTube: {youtube}.",
        "azione_immediata": "Review mensile per identificare "
                             "quale KR muovere per primo.",
        "regola_attivata": "REVIEW — Analisi dati necessaria"
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 4: GAP ANALYSIS AUTOMATIZZATA
# ───────────────────────────────────────────────────────────────

# La gap analysis identifica DOVE intervenire basandosi sui
# dati, non sulle sensazioni. Si esegue mensilmente come
# parte del review OKR.

def execute_gap_analysis(
    okr_data: dict,
    month_in_quarter: int
) -> dict:
    """
    Esegue la gap analysis completa su tutti i KR
    di tutti i pillar.

    Args:
        okr_data: {
            "agenzia": [
                {"kr_id": "...", "baseline": N, "target": N,
                 "current": N, "label": "..."},
                ...
            ],
            "info_biz": [...],
            "youtube": [...],
            "cross_poll": [...]
        }
        month_in_quarter: 1, 2, o 3

    Returns:
        Gap analysis completa con prioritizzazione
    """
    all_gaps = []

    # STEP 1: Calcola progresso e status per ogni KR
    for pillar, krs in okr_data.items():
        for kr in krs:
            progress = calculate_kr_progress(
                kr["baseline"], kr["target"], kr["current"]
            )
            status = determine_kr_status(
                progress["progress_pct"], month_in_quarter
            )

            # STEP 2: Calcola impatto del gap
            impact = _calculate_gap_impact(
                pillar, kr, progress, status
            )

            all_gaps.append({
                "pillar": pillar,
                "kr_id": kr["kr_id"],
                "kr_label": kr["label"],
                "progress": progress,
                "status": status,
                "impact": impact
            })

    # STEP 3: Ordina per impatto (decrescente)
    all_gaps.sort(
        key=lambda g: g["impact"]["score"],
        reverse=True
    )

    # STEP 4: Identifica i top 3 gap su cui intervenire
    top_gaps = all_gaps[:3]

    # STEP 5: Genera raccomandazioni
    recommendations = []
    for i, gap in enumerate(top_gaps):
        recommendations.append({
            "priorita": i + 1,
            "pillar": gap["pillar"],
            "kr": gap["kr_label"],
            "gap": f"{gap['progress']['gap_pct']}% dal target",
            "status": gap["status"]["status"],
            "azione_suggerita": gap["status"]["azione"],
            "impatto_score": gap["impact"]["score"],
            "impatto_motivo": gap["impact"]["motivo"]
        })

    return {
        "data_analysis": f"Mese {month_in_quarter} del trimestre",
        "total_krs_analyzed": len(all_gaps),
        "krs_on_track": len([g for g in all_gaps
                             if g["status"]["status"] == "🟢"]),
        "krs_at_risk": len([g for g in all_gaps
                            if g["status"]["status"] == "🟡"]),
        "krs_off_track": len([g for g in all_gaps
                              if g["status"]["status"] == "🔴"]),
        "top_3_gaps": recommendations,
        "all_gaps": all_gaps
    }


def _calculate_gap_impact(
    pillar: str,
    kr: dict,
    progress: dict,
    status: dict
) -> dict:
    """
    Calcola l'impatto di un gap sul revenue totale.

    Formula: IMPATTO = Gap_Dimensione × Leva_Revenue ×
                       Velocità_Risoluzione

    La leva revenue riflette la gerarchia dei pillar:
    Agenzia ha leva massima, Satellite ha leva minima.
    """
    # Moltiplicatore per pillar (gerarchia)
    pillar_multiplier = {
        "agenzia": 3.0,       # Impatto massimo
        "info_biz": 2.0,      # Impatto alto
        "youtube": 1.5,       # Impatto medio
        "cross_poll": 1.0,    # Impatto indiretto
        "satellite": 0.5      # Impatto basso
    }

    # Dimensione del gap (0-100)
    gap_size = progress["gap_pct"]

    # Urgenza basata sullo status
    urgency_multiplier = {
        "🟢": 0.5,
        "🟡": 1.5,
        "🔴": 3.0
    }

    multiplier = pillar_multiplier.get(pillar, 1.0)
    urgency = urgency_multiplier.get(
        status["status"], 1.0
    )

    score = round(gap_size * multiplier * urgency, 1)

    # Motivo leggibile
    if pillar == "agenzia":
        motivo = ("Gap nell'agenzia = impatto diretto sul "
                  "revenue core. Priorità MASSIMA.")
    elif pillar == "info_biz":
        motivo = ("Gap nell'info-biz = amplificatore debole. "
                  "Risolvibile senza fermare il core.")
    elif pillar == "youtube":
        motivo = ("Gap in YouTube = lead generation rallentata. "
                  "Effetto nel medio termine.")
    elif pillar == "cross_poll":
        motivo = ("Gap nella cross-pollination = sinergie "
                  "non attive. Compound interest perso.")
    else:
        motivo = "Gap in area satellite."

    return {
        "score": score,
        "gap_size": gap_size,
        "pillar_multiplier": multiplier,
        "urgency_multiplier": urgency,
        "motivo": motivo
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 5: PROTOCOLLI DI REVIEW PER CADENZA
# ───────────────────────────────────────────────────────────────

REVIEW_PROTOCOLS = {

    "settimanale": {
        "nome": "Sprint Check (dentro la review settimanale)",
        "durata_minuti": 10,
        "domande_guida": [
            "Quanti dei 5-7 task dello sprint ho completato?",
            "Sono bloccato su qualcosa? Se sì, cosa?",
            "Sto lavorando su task collegati ai KR o su "
            "distrazioni?",
            "Devo riordinare le priorità per la prossima "
            "settimana?"
        ],
        "output": "Check rapido dei task, nessun aggiornamento KR",
        "azione_se_bloccato": "Identifica il blocco. Se è "
                               "risolvibile in <30 min → "
                               "risolvilo ORA. Se richiede "
                               "più tempo → ripianifica lo "
                               "sprint della settimana."
    },

    "mensile": {
        "nome": "OKR Progress Review",
        "durata_minuti": 30,
        "step": [
            "1. Per ogni KR trimestrale: aggiorna il valore "
            "attuale con i dati della dashboard",
            "2. Calcola il progresso % con la formula di "
            "SEZIONE 3",
            "3. Determina lo status 🟢🟡🔴 basato sul mese "
            "nel trimestre",
            "4. Esegui la gap analysis (SEZIONE 4)",
            "5. Identifica i top 3 gap",
            "6. Definisci il prossimo sprint mensile basato "
            "sui gap (i task devono COLMARE i gap, non "
            "fare cose nuove)"
        ],
        "output": "Status aggiornato per ogni KR + nuovo "
                  "sprint mensile",
        "ricalibrazione": {
            "quando": "Solo se un KR è stato raggiunto prima "
                      "del previsto (raro) o se le condizioni "
                      "di mercato sono cambiate radicalmente",
            "come": "Non abbassare mai un target perché sei "
                    "in ritardo. Il target resta. Cambia la "
                    "strategia di esecuzione, non il target.",
            "eccezione": "Se a metà trimestre il KR è sotto "
                         "il 15% E la causa è un evento "
                         "esterno imprevedibile → ricalibra "
                         "con documentazione del motivo"
        }
    },

    "trimestrale": {
        "nome": "OKR Close-Out e Planning Q+1",
        "durata_minuti": 105,
        "fase_1_closeout": {
            "durata": 45,
            "step": [
                "1. Per ogni KR: risultato finale vs target",
                "2. Score di completamento: "
                "risultato/target × 100",
                "3. Per ogni Objective: è stato raggiunto? "
                "(considerando tutti i KR insieme)",
                "4. Lezioni apprese: cosa ha funzionato? "
                "Cosa no? Perché?",
                "5. Quali KR erano mal definiti? (troppo "
                "vaghi, non misurabili, fuori controllo)",
                "6. Calcola OKR completion rate del trimestre: "
                "KR con progresso ≥70% / KR totali"
            ]
        },
        "fase_2_planning": {
            "durata": 60,
            "step": [
                "1. Rivedi gli OKR annuali: sono ancora "
                "rilevanti? Il contesto è cambiato?",
                "2. Per ogni pillar: definisci 1-2 Objectives "
                "per il Q+1 usando l'algoritmo di SEZIONE 2",
                "3. Per ogni Objective: definisci 2-3 KR "
                "usando le regole di SEZIONE 2",
                "4. Definisci le 3 PRIORITÀ del trimestre "
                "(le cose più importanti in assoluto)",
                "5. Definisci la NOT-TO-DO list del trimestre "
                "(le tentazioni da evitare)",
                "6. Verifica coerenza: i KR trimestrali "
                "muovono i KR annuali?"
            ]
        },
        "output": "Close-out Q corrente + OKR Q+1 + "
                  "Priorità + Not-To-Do",
        "okr_completion_rate_benchmark": {
            "eccellente": ">80% — Forse i target erano "
                          "troppo bassi. Alza l'ambizione.",
            "buono": "60-80% — Sweet spot. Target sfidanti "
                     "ma raggiungibili. Mantieni.",
            "sufficiente": "40-59% — Esecuzione debole o "
                           "target irrealistici. Analizza.",
            "insufficiente": "<40% — Problema sistemico: "
                              "troppi OKR, troppa dispersione, "
                              "o mancanza di focus."
        }
    },

    "annuale": {
        "nome": "OKR Annual Reset",
        "durata_minuti": 180,
        "step": [
            "1. Close-out tutti i 4 trimestri: risultati "
            "finali per ogni KR annuale",
            "2. Pattern analysis: quali trimestri sono "
            "andati meglio? Perché?",
            "3. Revenue analysis: revenue per pillar per "
            "trimestre. Trend.",
            "4. Scrivi la nuova VISION ANNUALE (1 frase)",
            "5. Definisci 4 Objectives annuali (1 per "
            "pillar + 1 cross-pollination)",
            "6. Definisci 12 Key Results annuali (3 per "
            "Objective)",
            "7. Definisci 1-2 'Strategic Bets' — scommesse "
            "per l'anno (cose nuove da testare con "
            "budget limitato)",
            "8. Definisci gli OKR del Q1 dell'anno nuovo "
            "(cascata immediata)"
        ],
        "output": "Vision + OKR Annuali + Q1 OKR + "
                  "Strategic Bets"
    }
}


# ───────────────────────────────────────────────────────────────
# SEZIONE 6: SPRINT MENSILE ENGINE
# ───────────────────────────────────────────────────────────────

# Il motore che trasforma i KR trimestrali in task concreti
# da eseguire questo mese.

def generate_monthly_sprint(
    quarterly_okrs: dict,
    gap_analysis: dict,
    previous_sprint_review: dict,
    available_capacity: str
) -> dict:
    """
    Genera lo sprint mensile basato sui KR trimestrali
    e sulla gap analysis.

    Args:
        quarterly_okrs: OKR del trimestre corrente
        gap_analysis: risultato della gap analysis
        previous_sprint_review: review dello sprint precedente
        available_capacity: "full" | "reduced" | "minimal"

    Returns:
        Sprint mensile con 5-7 task prioritizzati
    """

    # STEP 1: Identificazione focus
    # Il focus del mese = il gap più critico
    if gap_analysis["krs_off_track"] > 0:
        focus_source = "RECOVERY"
        focus = (f"Recuperare il KR off-track: "
                 f"{gap_analysis['top_3_gaps'][0]['kr']}")
    elif gap_analysis["krs_at_risk"] > 0:
        focus_source = "ACCELERATION"
        focus = (f"Accelerare il KR a rischio: "
                 f"{gap_analysis['top_3_gaps'][0]['kr']}")
    else:
        focus_source = "MOMENTUM"
        focus = "Mantenere il momentum su tutti i KR on track"

    # STEP 2: Determinazione numero task
    task_count = {
        "full": 7,
        "reduced": 5,
        "minimal": 3
    }
    max_tasks = task_count.get(available_capacity, 5)

    # STEP 3: Allocazione task per pillar
    # Segue la gerarchia: Agenzia prende più slot
    allocation = {
        "full": {
            "agenzia": 3,
            "info_biz": 2,
            "youtube": 1,
            "cross_poll": 1
        },
        "reduced": {
            "agenzia": 2,
            "info_biz": 1,
            "youtube": 1,
            "cross_poll": 1
        },
        "minimal": {
            "agenzia": 2,
            "info_biz": 1,
            "youtube": 0,
            "cross_poll": 0
        }
    }

    pillar_allocation = allocation.get(
        available_capacity,
        allocation["reduced"]
    )

    # STEP 4: Override per gap critici
    # Se un pillar ha un KR 🔴, ruba 1 slot dagli altri
    for gap in gap_analysis["top_3_gaps"]:
        if gap["status"] == "🔴":
            critical_pillar = gap["pillar"]
            # Aggiungi 1 slot al pillar critico
            pillar_allocation[critical_pillar] = \
                pillar_allocation.get(critical_pillar, 0) + 1
            # Rimuovi 1 slot dal pillar meno critico
            # (non dall'agenzia se non è lei il 🔴)
            for p in ["cross_poll", "youtube", "info_biz"]:
                if p != critical_pillar and \
                   pillar_allocation.get(p, 0) > 0:
                    pillar_allocation[p] -= 1
                    break

    # STEP 5: Template task
    sprint = {
        "mese": "[DA COMPILARE]",
        "focus": focus,
        "focus_source": focus_source,
        "capacity": available_capacity,
        "max_tasks": max_tasks,
        "allocation": pillar_allocation,
        "tasks": [],
        "not_to_do": []
    }

    # Genera template task per ogni slot allocato
    task_num = 1
    for pillar, count in pillar_allocation.items():
        for i in range(count):
            if task_num > max_tasks:
                break
            sprint["tasks"].append({
                "numero": task_num,
                "task": "[DA COMPILARE — azione specifica "
                        "e misurabile]",
                "pillar": pillar,
                "kr_linked": "[ID del KR che questo task muove]",
                "status": "□ Non iniziato",
                "deadline_settimana": "[W1/W2/W3/W4]",
                "definizione_di_done": "[Quando consideri "
                                       "questo task completato?]"
            })
            task_num += 1

    # STEP 6: Regola di validazione
    sprint["validation_rule"] = (
        "OGNI task nella lista DEVE avere un kr_linked "
        "compilato. Se non riesci a collegare un task "
        "a nessun KR → quel task NON appartiene allo "
        "sprint. Mettilo nella not_to_do o posticipalo."
    )

    return sprint


# ───────────────────────────────────────────────────────────────
# SEZIONE 7: NOT-TO-DO ENGINE
# ───────────────────────────────────────────────────────────────

# La Not-To-Do list è il contrappeso della To-Do.
# Senza di essa, la lista dei task cresce all'infinito
# e il focus si dissolve.

NOT_TO_DO_ENGINE = {
    "versione": "1.0",

    "principio": "Dire NO a cose buone per dire SÌ a "
                 "cose eccellenti. La Not-To-Do non contiene "
                 "cose inutili (quelle non serve scriverle). "
                 "Contiene cose ATTRAENTI che però distolgono "
                 "dal focus.",

    "categorie": {
        "nuovi_progetti": {
            "descrizione": "Nuovi business, nuovi prodotti, "
                           "nuove partnership che NON rientrano "
                           "nei 3 pillar definiti",
            "esempio": "'Non lancerò una community a pagamento "
                       "questo trimestre, anche se è un'idea "
                       "interessante. Prima stabilizzare i "
                       "3 pillar.'"
        },
        "ottimizzazioni_premature": {
            "descrizione": "Miglioramenti a sistemi che funzionano "
                           "'abbastanza bene' ma non sono la "
                           "priorità",
            "esempio": "'Non rifarò il sito web questo trimestre. "
                       "Funziona. Il tempo va nella pipeline.'"
        },
        "shiny_objects": {
            "descrizione": "Nuovi tool, nuove piattaforme, "
                           "nuovi trend che sembrano urgenti "
                           "ma non lo sono",
            "esempio": "'Non inizierò a usare [nuovo tool AI] "
                       "questo mese. Quello che ho funziona.'"
        },
        "favori_non_strategici": {
            "descrizione": "Richieste di aiuto, collaborazioni, "
                           "partnership che non muovono nessun KR",
            "esempio": "'Non farò consulenze gratuite a chi "
                       "me le chiede via DM. Il mio tempo "
                       "ha un valore.'"
        }
    },

    "processo_compilazione": [
        "1. A inizio trimestre: scrivi 3 'tentazioni' che "
        "sai che arriveranno",
        "2. Per ognuna: scrivi PERCHÉ la stai rifiutando "
        "(collegala al focus sui KR)",
        "3. Quando durante il trimestre emerge una nuova "
        "tentazione: aggiungila alla lista con motivazione",
        "4. Se una tentazione supera il filtro anti-ADD "
        "(tutte e 5 le domande) → rimuovila dalla "
        "Not-To-Do e valutala come task reale",
        "5. A fine trimestre: rivedi la lista. Le cose "
        "scartate erano davvero giuste da scartare? "
        "Qualcuna merita di entrare nei KR del Q+1?"
    ],

    "formato_entry": {
        "cosa": "str — descrizione della tentazione",
        "perche_no": "str — motivo per cui non la fai ORA",
        "kr_che_sacrificherebbe": "str — quale KR soffrirebbe",
        "rivaluta_quando": "str — data o condizione per rivalutare",
        "status": "SCARTATA | IN ATTESA | PROMOSSA_A_TASK"
    }
}


# ═══════════════════════════════════════════════════════════════
# 🔧 COME UTILIZZARE QUESTO FILE
# ═══════════════════════════════════════════════════════════════

# QUANDO CONSULTARLO:
#
# 1. INIZIO ANNO → SEZIONE 1 (architettura cascata) +
#    SEZIONE 2 (algoritmo definizione) per creare gli
#    OKR annuali
#
# 2. INIZIO TRIMESTRE → SEZIONE 2 (definizione) +
#    SEZIONE 5 (protocollo trimestrale) +
#    SEZIONE 7 (Not-To-Do) per pianificare il Q
#
# 3. INIZIO MESE → SEZIONE 3 (scoring) + SEZIONE 4
#    (gap analysis) + SEZIONE 6 (sprint engine) per
#    generare lo sprint mensile
#
# 4. OGNI SETTIMANA → SEZIONE 5 (protocollo settimanale)
#    per il check rapido
#
# 5. Quando l'utente chiede "come stanno i miei OKR?" →
#    usa SEZIONE 3 per calcolare progresso e status
#
# 6. Quando l'utente chiede "su cosa mi concentro?" →
#    usa SEZIONE 4 per gap analysis → SEZIONE 6 per
#    generare lo sprint
#
# 7. Quando l'utente propone una nuova idea → verifica
#    se è nella Not-To-Do (SEZIONE 7) e applica il
#    filtro anti-ADD (vedi DECISION_FRAMEWORK.md)

# COME INTEGRARLO NELLA RISPOSTA:
#
# - Quando compili la dashboard mensile, il blocco
#   "OKR Trimestrale Review" si popola con i calcoli
#   di SEZIONE 3
# - Quando generi uno sprint mensile, usa l'output di
#   SEZIONE 6 nel template di TEMPLATE_PRODUZIONE.md
# - Quando fai il planning trimestrale, segui il
#   protocollo di SEZIONE 5 fase_2_planning
# - Cita sempre lo STATUS (🟢🟡🔴) quando parli di
#   un KR o di un pillar
# - Quando suggerisci task, mostra SEMPRE il collegamento
#   al KR: "Task X → muove KR Y (attualmente al Z%)"


# ═══════════════════════════════════════════════════════════════
# 🔗 COLLEGAMENTI
# ═══════════════════════════════════════════════════════════════

# → TEMPLATE_PRODUZIONE.md: contiene i template compilabili
#   degli OKR (annuale, trimestrale, sprint) che vengono
#   popolati con la logica definita qui
#
# → TEMPLATE_ARCHITETTURA.md: definisce la gerarchia dei
#   pillar che questo file usa per il pillar_multiplier
#   nella gap analysis
#
# → STANDARD_QUALITA.md: contiene le soglie e i benchmark
#   che i KR devono rispettare
#
# → CROSS_POLLINATION_ENGINE.md: gli OKR cross-pollination
#   sono gestiti qui ma le azioni concrete sono nel
#   cross-pollination engine
#
# → PIPELINE_OVERVIEW.md: le cadenze operative includono
#   i protocolli di review definiti in SEZIONE 5
#
# → DECISION_FRAMEWORK.md (file futuro): il filtro
#   anti-ADD referenzia la Not-To-Do list di SEZIONE 7
#
# → Custom Instructions §2.1: il flusso di pensiero
#   principale include "Consulta OKR prima di rispondere"
#
# → Custom Instructions §8: tutti i workflow operativi
#   (settimanale, mensile, trimestrale, annuale) seguono
#   i protocolli definiti in SEZIONE 5


# ═══════════════════════════════════════════════════════════════
# 💡 ESEMPI PRATICI
# ═══════════════════════════════════════════════════════════════

# ESEMPIO 1: Definizione OKR Trimestrale per Agenzia CRO
#
# Input utente: "Devo definire gli OKR del Q2 per l'agenzia"
#
# Processo AI:
# 1. Chiedi: "Qual è lo stato attuale dell'agenzia?
#    Revenue mensile, close rate, clienti attivi,
#    pipeline status"
# 2. Utente: "Revenue €8K/mese, close rate 22%, 3 clienti
#    attivi, pipeline con 5 lead"
# 3. Chiedi: "Qual è il KR annuale dell'agenzia?"
# 4. Utente: "KR annuale: Raggiungere €15K/mese entro
#    dicembre"
# 5. Applica l'algoritmo di SEZIONE 2:
#    - Objective Q2: "Costruire una pipeline prevedibile
#      che porti l'agenzia a €12K/mese con close rate
#      superiore al 30%"
#    - KR1 (moderato): "Portare il close rate dal 22%
#      al 32% ottimizzando il processo di call"
#    - KR2 (moderato): "Chiudere almeno 3 nuovi clienti
#      nel trimestre con valore medio progetto >€3K"
#    - KR3 (aggressivo): "Ottenere 2 referral da clienti
#      esistenti"
# 6. Validazione: ogni KR è quantitativo? Misurabile?
#    Sotto controllo? Collegato all'Objective? ✅
#
# ESEMPIO 2: Gap Analysis a metà trimestre
#
# Input utente: "Siamo a metà Q2, come sto?"
#
# Processo AI:
# 1. Chiedi dati attuali per ogni KR
# 2. Utente fornisce:
#    - KR1 (close rate): attuale 25% (baseline 22%, target 32%)
#    - KR2 (clienti): 1 chiuso (target 3)
#    - KR3 (referral): 0 (target 2)
# 3. Calcola con SEZIONE 3:
#    - KR1: progresso 30% → mese 2 soglia 55% → 🔴 OFF TRACK
#    - KR2: progresso 33% → mese 2 soglia 55% → 🔴 OFF TRACK
#    - KR3: progresso 0% → mese 2 soglia 35% → 🔴 OFF TRACK
# 4. Gap analysis con SEZIONE 4:
#    - Pillar agenzia: 🔴 (tutti i KR off track)
#    - Empire status: 🔴 (agenzia è il core)
#    - Top gap: KR2 (clienti) ha impatto massimo
# 5. Output:
#    "🔴 ALLARME: L'agenzia è off track su tutti i KR.
#     Attivo il protocollo GERARCHIA SACRA:
#     - STOP attività info-biz e YouTube non essenziali
#     - Focus 100% sulla pipeline agenzia
#     - Gap critico: chiusura clienti (1/3, 33%)
#     - Azione immediata: intensifica outreach a 3x,
#       fai follow-up su tutti i lead in pipeline,
#       chiedi referral ai 3 clienti attivi ORA
#     - Review tra 2 settimane per valutare progresso"
#
# ESEMPIO 3: Generazione Sprint Mensile
#
# Input utente: "Genera lo sprint di marzo"
#
# Processo AI:
# 1. Consulta gap analysis del mese precedente
# 2. Identifica: KR agenzia 🟡, KR info-biz 🟢,
#    KR YouTube 🟡, KR cross-poll 🟢
# 3. Applica generate_monthly_sprint():
#    Focus: "Accelerare il KR agenzia a rischio:
#    close rate"
#    Capacity: "full" → 7 task
#    Allocation: agenzia 3, info-biz 2, youtube 1,
#    cross-poll 1
#    (nessun override perché niente è 🔴)
# 4. Output sprint con 7 task specifici, ognuno
#    collegato a un KR


# ═══════════════════════════════════════════════════════════════
# ⚠️ NOTE E AVVERTENZE
# ═══════════════════════════════════════════════════════════════

# 1. NON cambiare i target OKR a metà trimestre perché
#    sei in ritardo. Il target resta fisso. Cambia la
#    STRATEGIA di esecuzione. L'unica eccezione è un
#    evento esterno imprevedibile (documentalo).
#
# 2. Il completion rate ideale è 60-80%. Se raggiungi
#    il 100% di tutti i KR → i target erano troppo bassi.
#    Se raggiungi <40% → troppo alti o focus insufficiente.
#    Il sweet spot è: "sfidante ma raggiungibile con
#    impegno costante".
#
# 3. La gerarchia Agenzia > Info-Biz > YouTube si
#    applica ANCHE nella gap analysis: un gap dell'agenzia
#    ha SEMPRE più impatto di un gap uguale di YouTube.
#    Questo è codificato nel pillar_multiplier.
#
# 4. Lo sprint mensile ha un TETTO di 7 task. Se ne
#    servirebbero 10, significa che i task non sono
#    abbastanza specifici o che stai tentando di fare
#    troppe cose. Scomponi O taglia.
#
# 5. La Not-To-Do list è il documento più sottovalutato
#    del sistema. Compilarla FORZA la scelta e previene
#    la dispersione. Senza di essa, ogni nuova idea
#    sembra urgente.
#
# 6. Quando l'utente non ha dati per compilare la
#    dashboard (è all'inizio), usa stime conservative
#    come baseline e definisci come primo task "impostare
#    il tracking per [metrica X]". Non puoi gestire
#    ciò che non misuri.
#
# 7. Se l'utente ha solo 1 pillar attivo (es: solo
#    l'agenzia), semplifica: OKR solo per quel pillar +
#    OKR per l'attivazione del pillar successivo.
#    Non creare OKR per pillar che non esistono ancora.