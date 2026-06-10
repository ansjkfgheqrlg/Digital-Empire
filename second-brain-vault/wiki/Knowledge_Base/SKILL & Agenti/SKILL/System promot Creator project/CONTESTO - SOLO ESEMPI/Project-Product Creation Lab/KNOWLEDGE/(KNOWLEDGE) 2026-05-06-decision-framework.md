# DECISION_FRAMEWORK
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > System promot Creator project > CONTESTO - SOLO ESEMPI > Project-Product Creation Lab > KNOWLEDGE]]

## Content

# ═══════════════════════════════════════════════════════════════
# 📄 DECISION_FRAMEWORK.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC + SAFETY
# Priorità: P0 — BLOCCANTE
# Dipendenze: OKR_CROSS_BUSINESS_ENGINE.md,
#             TEMPLATE_ARCHITETTURA.md,
#             STANDARD_QUALITA.md,
#             CROSS_POLLINATION_ENGINE.md
# Referenziato da: Custom Instructions §2 (Processi di
#                  Ragionamento), §6 (Gestione Errori),
#                  §7 (Vincoli e Limitazioni),
#                  §8 (Workflow Operativi)
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# 📋 SCOPO
# ═══════════════════════════════════════════════════════════════

# Questo file contiene il FRAMEWORK DECISIONALE COMPLETO
# per Digital Empire. È il protocollo che governa COME
# il Command Center prende decisioni strategiche, gestisce
# le crisi, filtra le distrazioni e alloca le risorse.
#
# Definisce:
#
# 1. Il processo decisionale a 4 step
# 2. Il filtro anti-ADD imprenditoriale (5 domande)
# 3. Il protocollo di intervento per allarmi (🔴🟡)
# 4. L'algoritmo di allocazione risorse tra pillar
# 5. Il sistema di valutazione opportunità
# 6. Le regole di escalation e de-escalation
# 7. I template per documentare le decisioni
#
# Senza questo framework, le decisioni sono REATTIVE
# (rispondo a ciò che succede). Con questo framework,
# le decisioni sono PROATTIVE (decido in anticipo come
# gestire ogni scenario).
#
# Principio fondamentale (Eric Siu):
# "La cosa fondamentale è concentrarsi su una cosa sola
#  e diventare di livello mondiale in quella."
#
# Applicazione: L'agenzia CRO è quella cosa.
# Tutto il resto la AMPLIFICA, non la SOSTITUISCE.


# ═══════════════════════════════════════════════════════════════
# 📖 CONTENUTO PRINCIPALE
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# SEZIONE 1: PROCESSO DECISIONALE A 4 STEP
# ───────────────────────────────────────────────────────────────

# Questo processo si attiva OGNI VOLTA che serve una
# decisione strategica. Non è per le micro-decisioni
# quotidiane ("quale email scrivo prima?") ma per
# le scelte che impattano la direzione dell'intero
# Empire.

DECISION_TRIGGERS = {
    "pianificati": [
        "Fine trimestre — planning Q+1",
        "Review mensile — allocazione risorse",
        "Review annuale — definizione OKR"
    ],
    "evento_critico": [
        "Un pillar diventa 🔴 nella dashboard",
        "Revenue in calo per 2+ mesi consecutivi",
        "Perdita di un cliente chiave dell'agenzia",
        "Un lancio info-biz fallisce significativamente",
        "Zero video YouTube per 3+ settimane"
    ],
    "opportunita": [
        "Emerge una nuova opportunità di business",
        "Un potenziale partner propone una collaborazione",
        "Un nuovo mercato/nicchia diventa accessibile",
        "Un tool/piattaforma nuova potrebbe cambiare le cose",
        "Un competitor fa una mossa significativa"
    ],
    "impulso_interno": [
        "Senti l'impulso di iniziare qualcosa di nuovo",
        "Sei annoiato dal lavoro attuale",
        "Hai visto qualcuno fare qualcosa che sembra figo",
        "Hai una 'idea geniale' alle 3 di notte",
        "Ti senti bloccato e vuoi cambiare direzione"
    ]
}


def execute_decision_process(
    trigger_type: str,
    trigger_description: str,
    current_dashboard: dict,
    current_okrs: dict
) -> dict:
    """
    Esegue il processo decisionale completo a 4 step.

    Args:
        trigger_type: "pianificato" | "evento_critico" |
                      "opportunita" | "impulso_interno"
        trigger_description: descrizione della situazione
        current_dashboard: dati dashboard aggiornati
        current_okrs: OKR correnti con progresso

    Returns:
        Decisione strutturata con piano d'azione
    """

    # ═══════════════════════════════════════════════════
    # STEP 1: STATO ATTUALE (Dati, Non Sensazioni)
    # ═══════════════════════════════════════════════════

    step_1 = {
        "nome": "STATO ATTUALE",
        "principio": "Le decisioni si prendono con i NUMERI "
                     "della dashboard, non con le SENSAZIONI "
                     "del momento. Non 'mi sembra che vada "
                     "bene' → 'il CR è al 3.2%, sopra il "
                     "target del 2.5%'.",
        "azioni": [
            "1. Compila la dashboard se non è aggiornata. "
            "STOP finché non hai dati freschi.",
            "2. Per ogni pillar, annota: revenue attuale, "
            "trend (↑↓→), status KR (🟢🟡🔴)",
            "3. Annota il contesto: ci sono fattori esterni "
            "che influenzano? (stagionalità, mercato, "
            "cambiamenti personali)"
        ],
        "output_richiesto": {
            "agenzia": {
                "revenue_mese": "[€]",
                "trend": "[↑↓→]",
                "kr_status": "[🟢🟡🔴]",
                "pipeline_status": "[Piena|Sufficiente|Vuota]",
                "capacita_delivery": "[OK|Sovraccarico|Sotto-utilizzo]"
            },
            "info_biz": {
                "revenue_mese": "[€]",
                "trend": "[↑↓→]",
                "kr_status": "[🟢🟡🔴]",
                "lista_email_size": "[N]",
                "funnel_status": "[Attivo|Rotto|In costruzione]"
            },
            "youtube": {
                "views_mese": "[N]",
                "trend": "[↑↓→]",
                "kr_status": "[🟢🟡🔴]",
                "video_pubblicati_mese": "[N]",
                "lead_generati": "[N]"
            },
            "cross_pollination": {
                "azioni_mese": "[N]",
                "score": "[N/100]",
                "status": "[🟢🟡🔴]"
            }
        },
        "regola_bloccante": "Se non hai i dati della dashboard "
                            "aggiornati, NON procedere allo "
                            "Step 2. Fermati e aggiorna prima."
    }

    # ═══════════════════════════════════════════════════
    # STEP 2: GAP ANALYSIS
    # ═══════════════════════════════════════════════════

    step_2 = {
        "nome": "GAP ANALYSIS",
        "principio": "Non 'ho un problema generico' → "
                     "'il gap più grande è nel KR2 dell'agenzia: "
                     "close rate al 22% vs target 35%, gap 37%'.",
        "azioni": [
            "1. Per ogni pillar: calcola il gap tra "
            "dove sei e dove dovresti essere (KR Progress %)",
            "2. Per ogni gap: identifica la CAUSA (non il "
            "sintomo). 'Il close rate è basso' è un sintomo. "
            "'Le call non seguono il framework di Sales Call "
            "Closer' è una causa.",
            "3. Compila la tabella gap:"
        ],
        "tabella_gap": {
            "colonne": ["Pillar", "KR", "Target",
                        "Attuale", "Gap %", "Causa Root"],
            "esempio": [
                ["Agenzia", "Close rate", "35%",
                 "22%", "37%", "Call non strutturate, "
                 "nessun follow-up sistematico"],
                ["Info-Biz", "Lead/mese", "100",
                 "45", "55%", "Landing page non ottimizzata, "
                 "traffico insufficiente da YouTube"],
                ["YouTube", "Video/mese", "4",
                 "2", "50%", "Mancanza di batch production, "
                 "script non pre-preparati"]
            ]
        },
        "output_richiesto": "Tabella gap compilata per ogni "
                            "pillar con causa root identificata"
    }

    # ═══════════════════════════════════════════════════
    # STEP 3: PRIORITIZZAZIONE
    # ═══════════════════════════════════════════════════

    step_3 = {
        "nome": "PRIORITIZZAZIONE",
        "principio": "Quale gap ha il maggiore impatto sul "
                     "revenue totale se risolto? Non quale "
                     "è il più facile o il più urgente "
                     "emotivamente.",
        "formula": {
            "nome": "IMPACT SCORE",
            "calcolo": "Gap_Dimensione × Leva_Revenue × "
                       "Velocità_Risoluzione",
            "componenti": {
                "gap_dimensione": {
                    "descrizione": "Quanto è grande il gap "
                                   "(0-100% dalla gap analysis)",
                    "peso": "diretto"
                },
                "leva_revenue": {
                    "descrizione": "Quanto impatta sul revenue "
                                   "totale di Digital Empire",
                    "valori": {
                        "agenzia": 3.0,
                        "info_biz": 2.0,
                        "youtube": 1.5,
                        "cross_poll": 1.0,
                        "satellite": 0.5
                    },
                    "nota": "L'agenzia ha SEMPRE la leva più "
                            "alta perché è il revenue core"
                },
                "velocita_risoluzione": {
                    "descrizione": "Quanto velocemente puoi "
                                   "chiudere il gap",
                    "valori": {
                        "1_settimana": 3.0,
                        "2_4_settimane": 2.0,
                        "1_3_mesi": 1.0,
                        "3_plus_mesi": 0.5
                    },
                    "nota": "Gap risolvibili velocemente hanno "
                            "più valore immediato"
                }
            }
        },
        "regole_di_decisione": [
            "REGOLA 1: Un gap nell'agenzia ha QUASI SEMPRE "
            "più impatto di un gap in info-biz o YouTube. "
            "La leva 3.0x vs 2.0x riflette questo.",

            "REGOLA 2: ECCEZIONE — Se l'agenzia è 🟢 "
            "stabile E c'è un lancio info-biz imminente → "
            "concentra temporaneamente sull'info-biz. "
            "Ma SOLO se l'agenzia resta 🟢.",

            "REGOLA 3: MAI lavorare su 3 gap "
            "contemporaneamente. Scegline 1. AL MASSIMO 2. "
            "Se ne scegli 2, devono essere in pillar diversi "
            "e non competere per le stesse risorse (tempo).",

            "REGOLA 4: Se due gap hanno impact score simile "
            "(differenza <10%), scegli quello dell'agenzia. "
            "In caso di parità, il core vince SEMPRE."
        ],
        "output_richiesto": "1 gap prioritario selezionato "
                            "(max 2) con impact score e "
                            "motivazione"
    }

    # ═══════════════════════════════════════════════════
    # STEP 4: PIANO D'AZIONE
    # ═══════════════════════════════════════════════════

    step_4 = {
        "nome": "PIANO D'AZIONE",
        "principio": "Non basta identificare il gap. Serve "
                     "un piano specifico con timeline, "
                     "metriche e condizioni di stop.",
        "template_piano": {
            "gap_selezionato": "[Descrizione del gap]",
            "impact_score": "[N]",
            "questa_settimana": {
                "azioni": "[Max 3 azioni concrete]",
                "nota": "Devono essere eseguibili QUESTA "
                        "settimana, non 'in futuro'"
            },
            "questo_mese": {
                "task": "[5-7 task — diventano lo sprint mensile]",
                "nota": "Integra con lo sprint corrente o "
                        "sostituiscilo se il gap è 🔴"
            },
            "metrica_progresso": {
                "cosa_misuro": "[Metrica specifica]",
                "cadenza": "[Giornaliera|Settimanale|Mensile]",
                "target_intermedio": "[Valore da raggiungere "
                                     "entro la prossima review]"
            },
            "not_to_do_temporanea": {
                "cosa_fermo": "[Attività che sospendo per "
                              "liberare risorse]",
                "durata": "[Finché il gap non è risolto]",
                "condizione_ripristino": "[Quando riprendo "
                                         "l'attività sospesa]"
            },
            "prossima_review": {
                "data": "[GG/MM/AAAA]",
                "cosa_valuto": "[Criterio specifico per "
                                "decidere se il piano funziona]",
                "piano_b": "[Cosa faccio se il piano A "
                            "non ha funzionato]"
            }
        },
        "output_richiesto": "Piano d'azione compilato con "
                            "tutti i campi del template"
    }

    return {
        "trigger": {
            "type": trigger_type,
            "description": trigger_description
        },
        "step_1": step_1,
        "step_2": step_2,
        "step_3": step_3,
        "step_4": step_4
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 2: FILTRO ANTI-ADD IMPRENDITORIALE
# ───────────────────────────────────────────────────────────────

# Il filtro più importante del Command Center.
# Si attiva OGNI VOLTA che emerge una nuova idea,
# opportunità, tentazione. È il firewall contro la
# distrazione.
#
# Ispirato a Eric Siu: "Uno dei più grandi errori è
# non rimanere concentrato. La ADD imprenditoriale ci
# fa inseguire il prossimo oggetto luccicante."

ADD_FILTER = {
    "versione": "1.0",

    "quando_si_attiva": [
        "Hai una nuova idea di business/prodotto",
        "Qualcuno ti propone una partnership",
        "Vedi un competitor fare qualcosa di nuovo",
        "Scopri un nuovo tool/piattaforma/trend",
        "Senti il desiderio di 'cambiare tutto'",
        "Un amico/mentore suggerisce una nuova direzione",
        "Leggi un libro/articolo che ti ispira a fare "
        "qualcosa di diverso",
        "Sei annoiato dal lavoro attuale e vuoi novità"
    ],

    "le_5_domande": {

        "domanda_1": {
            "testo": "Questo è collegato a uno dei miei "
                     "3 pillar attuali?",
            "logica": {
                "SI": "Procedi alla domanda 2",
                "NO": "SCARTA. Non è il momento. Annotala "
                      "nel backlog 'Idee Future' e rivaluta "
                      "tra 6 mesi. Se tra 6 mesi è ancora "
                      "rilevante, ripassa dal filtro."
            },
            "nota": "I 3 pillar sono: Agenzia CRO, "
                    "Info-Business, YouTube/Content. "
                    "KDP e AI Influencer sono satellite "
                    "e contano come 'collegati' solo se "
                    "alimentano direttamente uno dei 3.",
            "trappola_comune": "Razionalizzare il collegamento. "
                                "'Beh, se ci penso bene, una "
                                "linea di abbigliamento è "
                                "collegata al personal brand "
                                "che è collegato a YouTube...' "
                                "→ NO. Il collegamento deve "
                                "essere DIRETTO e OVVIO."
        },

        "domanda_2": {
            "testo": "I miei 3 pillar sono tutti 🟢 "
                     "(on track)?",
            "logica": {
                "SI": "Procedi alla domanda 3",
                "NO": "FERMA. Prima risolvi il 🟡 o 🔴. "
                      "Non aggiungere benzina (nuovi progetti) "
                      "quando la casa brucia (pillar in "
                      "difficoltà). Torna quando tutti i "
                      "pillar sono almeno 🟡 stabile."
            },
            "nota": "Consulta la dashboard aggiornata. "
                    "Non la tua percezione. I DATI.",
            "trappola_comune": "'Ma questo nuovo progetto "
                                "RISOLVERÀ il problema del "
                                "pillar rosso!' → Quasi mai "
                                "vero. Il pillar rosso si "
                                "risolve con FOCUS sul pillar "
                                "rosso, non con nuovi progetti."
        },

        "domanda_3": {
            "testo": "Questa opportunità muove un Key Result "
                     "che ho già definito?",
            "logica": {
                "SI": "Procedi alla domanda 4",
                "NO": "Mettila nel backlog. Rivaluta tra 3 "
                      "mesi, al prossimo planning trimestrale. "
                      "Se allora è ancora rilevante E si "
                      "collega a un KR del Q+1, considerala."
            },
            "nota": "Questo è il test di ALLINEAMENTO. "
                    "Un'idea può essere buona ma non allineata "
                    "con ciò che hai deciso di fare ORA.",
            "trappola_comune": "'Posso creare un NUOVO KR per "
                                "questa idea!' → NO. I KR si "
                                "definiscono a inizio trimestre. "
                                "Se aggiungi KR mid-quarter, "
                                "stai diluendo il focus."
        },

        "domanda_4": {
            "testo": "Ho la capacità di eseguirla SENZA "
                     "togliere risorse ai pillar attuali?",
            "logica": {
                "SI": "Procedi alla domanda 5",
                "NO": "SCARTA o posponila. Non sacrificare "
                      "il core per l'accessorio. Se richiede "
                      "risorse (tempo, energia, soldi) che "
                      "stai usando per i pillar → è un "
                      "trade-off, non un'aggiunta."
            },
            "nota": "Le 'risorse' includono soprattutto "
                    "il TEMPO e l'ENERGIA MENTALE. Anche se "
                    "un progetto richiede 'solo 2 ore/settimana', "
                    "occupa spazio mentale 24/7.",
            "trappola_comune": "'Lo faccio nel weekend / di "
                                "sera / nei ritagli di tempo!' "
                                "→ Il tempo 'extra' non esiste. "
                                "Quel tempo è recovery. Se lo "
                                "usi per un side project, la "
                                "qualità del lavoro sui pillar "
                                "cala. È un trade-off nascosto."
        },

        "domanda_5": {
            "testo": "Se questa opportunità scomparisse domani, "
                     "il mio business ne soffrirebbe?",
            "logica": {
                "SI": "È una priorità reale. Agisci. Ma "
                      "integra nel sistema OKR: quale pillar? "
                      "Quale KR? Come si integra nello sprint? "
                      "Non agire d'impulso.",
                "NO": "È una distrazione mascherata da "
                      "opportunità. Scartala con serenità. "
                      "Le vere opportunità tornano. Le "
                      "distrazioni scompaiono."
            },
            "nota": "Questo è il TEST FINALE. La maggior "
                    "parte delle 'opportunità imperdibili' "
                    "fallisce questo test. Se il tuo business "
                    "sopravvive tranquillamente senza questa "
                    "cosa → non è una priorità.",
            "trappola_comune": "'Ma è un'opportunità unica, "
                                "non tornerà mai più!' → Le "
                                "opportunità VERE tornano. Quelle "
                                "che 'non tornano mai più' sono "
                                "quasi sempre hype o FOMO."
        }
    },

    "risultato_filtro": {
        "supera_tutte_5": {
            "azione": "Integra nel sistema OKR. Definisci "
                      "il pillar, il KR impattato, e inserisci "
                      "come task nello sprint mensile. NON "
                      "agire d'impulso — segui il processo.",
            "label": "✅ APPROVATA"
        },
        "fallisce_almeno_1": {
            "azione": "Registra nel 'Registro Idee Scartate' "
                      "con: data, idea, quale domanda ha "
                      "fallito, motivo. Rivaluta solo al "
                      "prossimo planning trimestrale.",
            "label": "❌ SCARTATA"
        },
        "zona_grigia": {
            "azione": "Se le risposte non sono nette (non "
                      "è chiaro se è un sì o un no), "
                      "DEFAULT = NO. In caso di dubbio, "
                      "la risposta è sempre NO. Il bias "
                      "naturale è verso il SÌ (è più "
                      "eccitante). Serve un bias correttivo "
                      "verso il NO.",
            "label": "⚠️ DEFAULT NO"
        }
    }
}


def apply_add_filter(
    idea: str,
    connected_to_pillar: bool,
    which_pillar: str,
    all_pillars_green: bool,
    moves_existing_kr: bool,
    which_kr: str,
    has_spare_capacity: bool,
    business_suffers_without: bool
) -> dict:
    """
    Applica il filtro anti-ADD a una nuova idea/opportunità.

    Args:
        idea: descrizione dell'idea/opportunità
        connected_to_pillar: risposta alla domanda 1
        which_pillar: se sì, quale pillar
        all_pillars_green: risposta alla domanda 2
        moves_existing_kr: risposta alla domanda 3
        which_kr: se sì, quale KR
        has_spare_capacity: risposta alla domanda 4
        business_suffers_without: risposta alla domanda 5

    Returns:
        Verdetto del filtro con azione
    """
    questions_passed = []
    first_failure = None

    # Domanda 1
    if connected_to_pillar:
        questions_passed.append("Q1_COLLEGAMENTO_PILLAR")
    else:
        first_failure = {
            "domanda": "Q1",
            "motivo": f"'{idea}' non è collegata a nessuno "
                      f"dei 3 pillar (Agenzia, Info-Biz, YouTube)",
            "azione": "Annota nel backlog 'Idee Future'. "
                      "Rivaluta tra 6 mesi."
        }
        return _generate_filter_result(
            idea, questions_passed, first_failure, "SCARTATA"
        )

    # Domanda 2
    if all_pillars_green:
        questions_passed.append("Q2_PILLAR_VERDI")
    else:
        first_failure = {
            "domanda": "Q2",
            "motivo": "Non tutti i pillar sono 🟢. Prima "
                      "risolvi ciò che è 🟡 o 🔴.",
            "azione": "Torna quando tutti i pillar sono "
                      "almeno 🟡 stabile."
        }
        return _generate_filter_result(
            idea, questions_passed, first_failure, "SCARTATA"
        )

    # Domanda 3
    if moves_existing_kr:
        questions_passed.append("Q3_MUOVE_KR")
    else:
        first_failure = {
            "domanda": "Q3",
            "motivo": f"'{idea}' non muove nessun KR "
                      f"attualmente definito.",
            "azione": "Backlog. Rivaluta al prossimo "
                      "planning trimestrale."
        }
        return _generate_filter_result(
            idea, questions_passed, first_failure, "SCARTATA"
        )

    # Domanda 4
    if has_spare_capacity:
        questions_passed.append("Q4_CAPACITA")
    else:
        first_failure = {
            "domanda": "Q4",
            "motivo": "Non c'è capacità disponibile senza "
                      "togliere risorse ai pillar.",
            "azione": "Posponi. Attendi che si liberi "
                      "capacità (progetto completato, "
                      "processo automatizzato, delega)."
        }
        return _generate_filter_result(
            idea, questions_passed, first_failure, "SCARTATA"
        )

    # Domanda 5
    if business_suffers_without:
        questions_passed.append("Q5_NECESSITA")
        return _generate_filter_result(
            idea, questions_passed, None, "APPROVATA"
        )
    else:
        first_failure = {
            "domanda": "Q5",
            "motivo": f"Il business sopravvive senza '{idea}'. "
                      f"Non è una necessità.",
            "azione": "Scarta con serenità. Se è davvero "
                      "importante, tornerà."
        }
        return _generate_filter_result(
            idea, questions_passed, first_failure, "SCARTATA"
        )


def _generate_filter_result(
    idea: str,
    passed: list,
    failure: dict,
    verdict: str
) -> dict:
    """Genera il risultato strutturato del filtro."""
    return {
        "idea": idea,
        "domande_superate": passed,
        "numero_superate": len(passed),
        "prima_failure": failure,
        "verdetto": verdict,
        "label": ADD_FILTER["risultato_filtro"]
                 .get(
                     "supera_tutte_5" if verdict == "APPROVATA"
                     else "fallisce_almeno_1",
                     {}
                 ).get("label", ""),
        "prossimo_step": ADD_FILTER["risultato_filtro"]
                         .get(
                             "supera_tutte_5" if verdict == "APPROVATA"
                             else "fallisce_almeno_1",
                             {}
                         ).get("azione", "")
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 3: PROTOCOLLO DI INTERVENTO PER ALLARMI
# ───────────────────────────────────────────────────────────────

# Quando un allarme scatta (dalla dashboard o dalla review),
# questo protocollo definisce l'azione ESATTA da intraprendere.
# Nessuna improvvisazione. Ogni allarme ha una risposta
# predefinita.

ALARM_PROTOCOLS = {

    "ALARM_001": {
        "nome": "Revenue Agenzia in Calo — 2 Mesi Consecutivi",
        "soglia": "Revenue agenzia mese N < mese N-1 < mese N-2",
        "severita": "🔴 CRITICO",
        "impatto": "Il core business sta perdendo momentum. "
                   "Se non intervieni, entro 2-3 mesi potresti "
                   "trovarti senza cash flow.",
        "protocollo": {
            "ora_0_24h": [
                "1. STOP immediato a TUTTE le attività "
                "non-agenzia (info-biz, YouTube, satellite)",
                "2. Analisi pipeline: quanti lead attivi? "
                "Quante call programmate? Quanti follow-up "
                "in sospeso?",
                "3. Se pipeline vuota: attiva OUTREACH "
                "D'EMERGENZA — contatta TUTTI i lead degli "
                "ultimi 6 mesi che non hanno chiuso con "
                "un messaggio di re-engagement",
                "4. Se pipeline con lead ma nessuna chiusura: "
                "rivedi il processo di call con Sales Call "
                "Closer — identifica dove si bloccano"
            ],
            "settimana_1": [
                "5. Intensifica outreach: 3x il volume normale",
                "6. Follow-up su OGNI proposta inviata negli "
                "ultimi 90 giorni",
                "7. Chiedi referral a OGNI cliente attivo "
                "e passato (usa il template di referral)",
                "8. Pubblica 1 post/giorno sui social con "
                "contenuto CRO per generare inbound"
            ],
            "settimana_2_4": [
                "9. Mantieni il volume di outreach 3x",
                "10. Review del close rate: se <20%, il "
                "problema è nella call, non nel volume. "
                "Rivedi lo script e i framework.",
                "11. Considera: offerta speciale per "
                "accelerare la chiusura (audit gratuito, "
                "sconto primo mese, garanzia rinforzata)",
                "12. Review a fine mese: il trend si è "
                "invertito?"
            ],
            "condizione_di_uscita": "Revenue agenzia torna "
                                    "al livello di 2 mesi fa "
                                    "O pipeline con >5 lead "
                                    "qualificati attivi",
            "quando_ripristinare_altri_pillar": "Solo quando "
                                                 "la condizione "
                                                 "di uscita è "
                                                 "soddisfatta E "
                                                 "mantenuta per "
                                                 "almeno 2 settimane"
        }
    },

    "ALARM_002": {
        "nome": "Zero Vendite Info-Biz — 30+ Giorni",
        "soglia": "Revenue info-business = €0 per 30+ giorni "
                  "con funnel attivo",
        "severita": "🔴 CRITICO (per il pillar info-biz)",
        "impatto": "Il funnel è rotto o il traffico è "
                   "assente. L'amplificatore #1 non funziona.",
        "protocollo": {
            "diagnosi": {
                "step": [
                    "1. FUNNEL CHECK: il funnel è tecnicamente "
                    "funzionante? (link attivi, pagine caricate, "
                    "email inviate, pagamento processabile)",
                    "2. TRAFFICO CHECK: c'è traffico verso il "
                    "funnel? (analytics landing page — se <100 "
                    "visite/mese → problema di traffico, non "
                    "di funnel)",
                    "3. CONVERSIONE CHECK: se c'è traffico ma "
                    "zero vendite → problema di conversione "
                    "(copy, offerta, prezzo, targeting)",
                    "4. NURTURE CHECK: stai inviando email "
                    "alla lista? Se no → la lista si "
                    "raffredda e non compra"
                ],
                "albero_decisionale": {
                    "funnel_rotto": "Ripara il funnel. "
                                    "Test completo end-to-end. "
                                    "Compra tu stesso.",
                    "zero_traffico": "Attiva la fonte di "
                                     "traffico principale: "
                                     "YouTube CTA, email "
                                     "alla lista, social post",
                    "traffico_ma_zero_conversione": "Rivedi: "
                                                    "(1) offerta, "
                                                    "(2) prezzo, "
                                                    "(3) copy "
                                                    "landing page, "
                                                    "(4) email "
                                                    "sequence",
                    "nessun_nurture": "Riprendi email "
                                      "settimanale alla lista. "
                                      "Invia valore per 2 "
                                      "settimane, poi offerta."
                }
            },
            "nota": "Questo allarme NON attiva il protocollo "
                    "'stop tutto'. L'agenzia continua. Solo "
                    "il tempo allocato a info-biz viene "
                    "riorientato sulla diagnosi e la riparazione."
        }
    },

    "ALARM_003": {
        "nome": "Zero Video YouTube — 3+ Settimane",
        "soglia": "Nessun video pubblicato per 21+ giorni",
        "severita": "🟡 A RISCHIO",
        "impatto": "La lead gen organica si sta fermando. "
                   "L'algoritmo YouTube penalizza l'inconsistenza. "
                   "I lead da YouTube calano entro 4-6 settimane.",
        "protocollo": {
            "azione_immediata": [
                "1. Pubblica 1 video QUESTA settimana — anche "
                "semplice (talking head, nessun editing complesso)",
                "2. Identifica il blocco: perché hai smesso? "
                "(mancanza di idee? mancanza di tempo? "
                "perfezionismo? paura del giudizio?)",
                "3. Per ogni blocco, azione specifica:"
            ],
            "blocchi_e_soluzioni": {
                "mancanza_idee": "Apri il YouTube Lead Engine "
                                  "(P2). Prendi il primo topic "
                                  "dalla lista. Non cercare "
                                  "l'idea perfetta.",
                "mancanza_tempo": "Il tempo per YouTube non è "
                                   "'extra'. È ALLOCATO nel "
                                   "15-20% della settimana. "
                                   "Bloccalo nel calendario.",
                "perfezionismo": "Il video migliore è quello "
                                  "PUBBLICATO. Un video al 70% "
                                  "pubblicato batte un video al "
                                  "100% mai pubblicato. Riduci "
                                  "il livello di produzione.",
                "paura_giudizio": "Il tuo pubblico target ha "
                                   "BISOGNO delle tue competenze. "
                                   "Non pubblicare è egoistico, "
                                   "non modesto."
            },
            "prevenzione": "Batch production: registra 4 video "
                           "in 1 giorno, programma 1/settimana. "
                           "Così anche se una settimana è piena, "
                           "il video esce."
        }
    },

    "ALARM_004": {
        "nome": "Zero Azioni Cross-Pillar — 30 Giorni",
        "soglia": "Nessuna azione cross-pollination registrata "
                  "per 30+ giorni",
        "severita": "🟡 A RISCHIO",
        "impatto": "Le sinergie si stanno perdendo. I pillar "
                   "stanno operando in isolamento. Il compound "
                   "interest si sta azzerando.",
        "protocollo": {
            "azione_immediata": [
                "1. Lunedì prossimo: 1 azione obbligatoria",
                "2. Apri CROSS_POLLINATION_ENGINE.md, SEZIONE 1",
                "3. Scegli il flusso PIÙ SEMPLICE da attivare "
                "(es: B2 — leggere i commenti YouTube e "
                "trasferire idee al backlog info-biz → "
                "richiede 10 minuti)",
                "4. Eseguila ORA, non 'dopo'",
                "5. Registra nel registro azioni",
                "6. Imposta reminder ricorrente: lunedì "
                "mattina, 15 minuti, 'cross-pollination'"
            ],
            "prevenzione": "Il reminder ricorrente è la "
                           "prevenzione. Se non è nel "
                           "calendario, non succede."
        }
    },

    "ALARM_005": {
        "nome": "OKR Trimestrale Sotto 30% a Metà Q",
        "soglia": "Progresso medio KR < 30% a fine mese 2 "
                  "del trimestre",
        "severita": "🟡 A RISCHIO",
        "impatto": "Rischio concreto di chiudere il trimestre "
                   "sotto il 50% — zona 'insufficiente'.",
        "protocollo": {
            "diagnosi": [
                "1. Gli OKR erano REALISTICI? Se no → "
                "ricalibra (documentando il motivo)",
                "2. L'ESECUZIONE è stata costante? Se no → "
                "identifica il blocco e rimuovilo",
                "3. È cambiato il CONTESTO? (evento esterno "
                "che ha spostato le priorità)"
            ],
            "azioni": {
                "okr_irrealistici": "Ricalibra i target al "
                                     "ribasso. Non è una "
                                     "sconfitta — è maturità. "
                                     "Target migliori al Q+1.",
                "esecuzione_debole": "Il problema non sono "
                                      "gli OKR, sei tu. "
                                      "Riduci a 3 KR max. "
                                      "Blocca il tempo. "
                                      "Trova accountability.",
                "contesto_cambiato": "Documenta il cambiamento. "
                                      "Ricalibra gli OKR. "
                                      "Non punire te stesso "
                                      "per fattori esterni."
            }
        }
    },

    "ALARM_006": {
        "nome": "Satellite Ruba Più del 10% del Tempo",
        "soglia": "Tempo allocato a KDP + AI Influencer > "
                  "10% del totale settimanale per 3+ settimane",
        "severita": "🟡 A RISCHIO",
        "impatto": "I satellite stanno rubando focus al core "
                   "e agli amplificatori.",
        "protocollo": {
            "azione": [
                "1. Time audit: quanto tempo REALE hai speso "
                "sui satellite questa settimana?",
                "2. Se >10%: identifica COSA sta prendendo "
                "più tempo del dovuto",
                "3. Opzioni: (a) Automatizza/semplifica il "
                "processo satellite, (b) Riduci la frequenza, "
                "(c) Delega, (d) Pausa temporanea",
                "4. Regola: i satellite NON possono MAI "
                "superare il 10% a meno che TUTTI i 3 pillar "
                "siano 🟢 E gli OKR siano >70% a metà Q"
            ]
        }
    }
}


# ───────────────────────────────────────────────────────────────
# SEZIONE 4: ALGORITMO DI ALLOCAZIONE RISORSE
# ───────────────────────────────────────────────────────────────

# Come distribuire il tempo e l'energia tra i pillar.
# La distribuzione NON è fissa — si adatta allo stato
# di ciascun pillar.

RESOURCE_ALLOCATION = {
    "versione": "1.0",

    "distribuzione_base": {
        "agenzia_cro": {"min": 50, "max": 60, "label": "Core"},
        "info_business": {"min": 20, "max": 30, "label": "Amplificatore #1"},
        "youtube": {"min": 15, "max": 20, "label": "Amplificatore #2"},
        "satellite": {"min": 5, "max": 10, "label": "Side"}
    },

    "nota": "I numeri rappresentano PERCENTUALI del tempo "
            "produttivo settimanale. Non del tempo totale "
            "(che include riposo, vita personale, admin)."
}


def calculate_resource_allocation(
    pillar_statuses: dict,
    active_alarm: str,
    quarter_okr_progress: dict
) -> dict:
    """
    Calcola l'allocazione risorse ottimale basata sullo
    stato attuale dei pillar.

    Args:
        pillar_statuses: {"agenzia": "🟢|🟡|🔴", ...}
        active_alarm: ID allarme attivo o None
        quarter_okr_progress: progresso medio OKR per pillar

    Returns:
        Allocazione percentuale consigliata per pillar
    """
    base = RESOURCE_ALLOCATION["distribuzione_base"]
    allocation = {}

    # SCENARIO 1: Agenzia 🔴 (allarme critico)
    if pillar_statuses.get("agenzia") == "🔴":
        return {
            "agenzia_cro": 85,
            "info_business": 5,
            "youtube": 5,
            "satellite": 5,
            "scenario": "EMERGENCY — Agenzia in crisi",
            "nota": "STOP quasi totale su tutto tranne "
                    "l'agenzia. Info-biz e YouTube in "
                    "modalità 'mantenimento minimo' "
                    "(rispondi ai clienti, pubblica "
                    "contenuto già pronto, nient'altro).",
            "durata": "Fino a quando l'agenzia torna "
                      "almeno a 🟡",
            "regola_attivata": "GERARCHIA SACRA"
        }

    # SCENARIO 2: Tutti 🟢 (condizione ideale)
    if all(s == "🟢" for s in pillar_statuses.values()):
        return {
            "agenzia_cro": 50,
            "info_business": 25,
            "youtube": 15,
            "satellite": 10,
            "scenario": "OPTIMAL — Tutti on track",
            "nota": "Distribuzione equilibrata. Questo è "
                    "il momento di spingere la cross-"
                    "pollination e gli amplificatori.",
            "durata": "Fino a quando qualcosa cambia",
            "regola_attivata": "CRESCITA"
        }

    # SCENARIO 3: Agenzia 🟢, un amplificatore 🔴
    if pillar_statuses.get("agenzia") == "🟢":
        red_pillar = None
        for p, s in pillar_statuses.items():
            if s == "🔴" and p != "agenzia":
                red_pillar = p
                break

        if red_pillar:
            alloc = {
                "agenzia_cro": 50,
                "info_business": 15,
                "youtube": 10,
                "satellite": 5,
                "scenario": f"RECOVERY — {red_pillar} in crisi",
                "durata": "4-6 settimane max",
                "regola_attivata": "FOCUS RECOVERY"
            }
            # Assegna +15% al pillar rosso
            alloc[red_pillar] = 30
            # Riduci gli altri di conseguenza
            remaining = 100 - alloc["agenzia_cro"] - alloc[red_pillar] - 5
            for p in ["info_business", "youtube"]:
                if p != red_pillar:
                    alloc[p] = remaining
            alloc["nota"] = (
                f"Agenzia stabile, focus recovery su "
                f"{red_pillar}. L'altro amplificatore "
                f"in 'mantenimento minimo'."
            )
            return alloc

    # SCENARIO 4: Mix (default)
    yellow_count = sum(
        1 for s in pillar_statuses.values() if s == "🟡"
    )

    return {
        "agenzia_cro": 55,
        "info_business": 22,
        "youtube": 15,
        "satellite": 8,
        "scenario": f"STANDARD — {yellow_count} pillar a rischio",
        "nota": "Distribuzione standard con leggero "
                "bias verso l'agenzia. Monitora "
                "settimanalmente i pillar 🟡.",
        "durata": "Fino alla prossima review mensile",
        "regola_attivata": "MONITORAGGIO"
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 5: REGISTRO DECISIONI
# ───────────────────────────────────────────────────────────────

# Ogni decisione strategica presa attraverso questo framework
# viene documentata per pattern recognition nelle retrospettive.

DECISION_REGISTRY_TEMPLATE = {
    "versione": "1.0",

    "entry_schema": {
        "data": "YYYY-MM-DD",
        "trigger_type": "pianificato | evento_critico | "
                        "opportunita | impulso_interno",
        "descrizione": "str — cosa ha innescato la decisione",
        "dashboard_snapshot": {
            "agenzia_status": "🟢|🟡|🔴",
            "info_biz_status": "🟢|🟡|🔴",
            "youtube_status": "🟢|🟡|🔴",
            "revenue_totale_mese": "€[N]"
        },
        "gap_identificato": "str — gap principale dalla "
                            "gap analysis",
        "impact_score": "float — score del gap",
        "decisione_presa": "str — cosa hai deciso di fare",
        "piano_azione": "list — i 3-7 step del piano",
        "not_to_do_associata": "str — cosa hai deciso di "
                               "NON fare per liberare risorse",
        "prossima_review": "YYYY-MM-DD",
        "risultato_effettivo": "str — compilato alla review "
                               "(cosa è successo realmente)",
        "lezione_appresa": "str — compilato alla review "
                           "(cosa hai imparato)"
    },

    "esempio_entry": {
        "data": "2025-02-03",
        "trigger_type": "evento_critico",
        "descrizione": "Revenue agenzia calato da €10K a "
                       "€7K in 2 mesi. Pipeline quasi vuota.",
        "dashboard_snapshot": {
            "agenzia_status": "🔴",
            "info_biz_status": "🟢",
            "youtube_status": "🟡",
            "revenue_totale_mese": "€9.200"
        },
        "gap_identificato": "Pipeline agenzia vuota — "
                            "solo 2 lead attivi, nessuna "
                            "call programmata",
        "impact_score": 270.0,
        "decisione_presa": "Attivato ALARM_001. Stop info-biz "
                           "e YouTube. Focus 100% su pipeline "
                           "agenzia per 4 settimane.",
        "piano_azione": [
            "1. Re-engagement email a tutti i lead ultimi 6 mesi",
            "2. Outreach 3x volume normale (15 contatti/giorno)",
            "3. Follow-up su tutte le proposte ultimi 90 giorni",
            "4. Chiesto referral a tutti i 3 clienti attivi",
            "5. Post giornaliero CRO sui social"
        ],
        "not_to_do_associata": "Nessuna attività info-biz o "
                               "YouTube per 4 settimane",
        "prossima_review": "2025-03-03",
        "risultato_effettivo": "[DA COMPILARE]",
        "lezione_appresa": "[DA COMPILARE]"
    }
}


# ───────────────────────────────────────────────────────────────
# SEZIONE 6: VALUTAZIONE OPPORTUNITÀ STRUTTURATA
# ───────────────────────────────────────────────────────────────

# Per le opportunità che SUPERANO il filtro anti-ADD,
# serve una valutazione più approfondita prima di
# allocare risorse significative.

def evaluate_opportunity(
    name: str,
    description: str,
    pillar: str,
    kr_impacted: str,
    estimated_revenue: float,
    estimated_time_hours_week: float,
    time_to_first_result_weeks: int,
    reversibility: str,
    downside_risk: str
) -> dict:
    """
    Valutazione strutturata di un'opportunità approvata
    dal filtro anti-ADD.

    Args:
        name: nome dell'opportunità
        description: descrizione dettagliata
        pillar: pillar di appartenenza
        kr_impacted: KR che muove
        estimated_revenue: revenue stimato mensile (€)
        estimated_time_hours_week: ore/settimana richieste
        time_to_first_result_weeks: settimane per primo risultato
        reversibility: "alta" | "media" | "bassa"
        downside_risk: "basso" | "medio" | "alto"

    Returns:
        Valutazione con score e raccomandazione
    """
    # Calcolo ROI del tempo
    monthly_hours = estimated_time_hours_week * 4.33
    if monthly_hours > 0:
        roi_per_hour = estimated_revenue / monthly_hours
    else:
        roi_per_hour = 0

    # Score componenti (0-100)
    revenue_score = min(estimated_revenue / 50, 100)
    # €5000+/mese = 100

    time_efficiency = min(roi_per_hour / 50, 100)
    # €50+/ora = 100

    speed_score = max(0, 100 - (time_to_first_result_weeks * 5))
    # 0 settimane = 100, 20 settimane = 0

    reversibility_map = {"alta": 100, "media": 60, "bassa": 20}
    reversibility_score = reversibility_map.get(reversibility, 50)

    risk_map = {"basso": 100, "medio": 60, "alto": 20}
    risk_score = risk_map.get(downside_risk, 50)

    # Score totale pesato
    total_score = (
        revenue_score * 0.30 +
        time_efficiency * 0.25 +
        speed_score * 0.20 +
        reversibility_score * 0.15 +
        risk_score * 0.10
    )

    # Raccomandazione
    if total_score >= 70:
        recommendation = "✅ PROCEDI — Opportunità forte. "
        "Integra nello sprint mensile."
    elif total_score >= 45:
        recommendation = "🟡 PROCEDI CON CAUTELA — Testa con "
        "investimento minimo per 4 settimane. Se i primi "
        "risultati sono positivi, scala."
    else:
        recommendation = "❌ SCARTA O POSPONI — Il rapporto "
        "rischio/beneficio non giustifica l'allocazione di "
        "risorse ORA. Rivaluta tra 3 mesi."

    return {
        "opportunita": name,
        "pillar": pillar,
        "kr_impacted": kr_impacted,
        "metriche": {
            "revenue_stimato_mese": f"€{estimated_revenue}",
            "tempo_richiesto": f"{estimated_time_hours_week}h/settimana",
            "roi_per_ora": f"€{round(roi_per_hour, 2)}/h",
            "tempo_primo_risultato": f"{time_to_first_result_weeks} settimane"
        },
        "scores": {
            "revenue": round(revenue_score, 1),
            "efficienza_tempo": round(time_efficiency, 1),
            "velocita": round(speed_score, 1),
            "reversibilita": round(reversibility_score, 1),
            "rischio": round(risk_score, 1)
        },
        "score_totale": round(total_score, 1),
        "raccomandazione": recommendation
    }


# ═══════════════════════════════════════════════════════════════
# 🔧 COME UTILIZZARE QUESTO FILE
# ═══════════════════════════════════════════════════════════════

# QUANDO CONSULTARLO:
#
# 1. Quando l'utente ha una NUOVA IDEA → SEZIONE 2
#    (filtro anti-ADD). Esegui le 5 domande in sequenza.
#    Se fallisce qualsiasi domanda, comunica il verdetto
#    con empatia ma fermezza.
#
# 2. Quando un ALLARME scatta nella dashboard → SEZIONE 3.
#    Identifica l'allarme corrispondente e segui il
#    protocollo step-by-step. Non improvvisare.
#
# 3. Quando serve una DECISIONE STRATEGICA → SEZIONE 1.
#    Guida l'utente attraverso i 4 step. Non saltare
#    nessuno step. Il più comune errore è saltare lo
#    Step 1 (dati) e andare diretto allo Step 4 (azione).
#
# 4. Quando l'utente chiede "come alloco il mio tempo?"
#    → SEZIONE 4. Usa la funzione
#    calculate_resource_allocation() con i dati attuali.
#
# 5. Quando un'opportunità SUPERA il filtro anti-ADD →
#    SEZIONE 6. Valuta con evaluate_opportunity() prima
#    di allocare risorse significative.
#
# 6. Per OGNI decisione presa → SEZIONE 5. Documenta
#    nel registro decisioni per le retrospettive.

# COME INTEGRARLO NELLA RISPOSTA:
#
# - Quando l'utente presenta un'idea, PRIMA di rispondere
#   con entusiasmo, esegui il filtro anti-ADD SILENZIOSAMENTE.
#   Se non supera → comunica il verdetto.
#
# - Quando un pillar è 🔴, cita l'allarme specifico
#   (es: "Questo attiva l'ALARM_001 — Revenue Agenzia
#   in Calo. Il protocollo richiede...").
#
# - Quando suggerisci un'allocazione di risorse, mostra
#   la tabella con le percentuali e lo scenario attivo.
#
# - Quando documenti una decisione, usa il template del
#   registro decisioni (SEZIONE 5).
#
# - MAI suggerire un'azione che viola la gerarchia sacra
#   (Agenzia > Info-Biz > YouTube > Satellite).


# ═══════════════════════════════════════════════════════════════
# 🔗 COLLEGAMENTI
# ═══════════════════════════════════════════════════════════════

# → OKR_CROSS_BUSINESS_ENGINE.md: la gap analysis (SEZIONE 4)
#   alimenta lo Step 2 del processo decisionale qui.
#   La Not-To-Do list (SEZIONE 7 dell'OKR file) è il
#   complemento del filtro anti-ADD qui.
#
# → CROSS_POLLINATION_ENGINE.md: le azioni cross-pillar
#   sono una delle "risorse" allocate nella SEZIONE 4.
#   L'ALARM_004 (zero cross-pollination) referenzia quel file.
#
# → TEMPLATE_ARCHITETTURA.md: la gerarchia dei pillar
#   (la base di ogni decisione) è definita lì.
#
# → STANDARD_QUALITA.md: le soglie di allarme che
#   attivano i protocolli di SEZIONE 3 sono definite lì.
#
# → PIPELINE_OVERVIEW.md: il workflow settimanale include
#   "ADD filter" come attività esplicita da 10 minuti.
#
# → Custom Instructions §6: gli edge cases e i protocolli
#   di errore referenziano i protocolli di allarme qui.
#
# → Custom Instructions §7: i vincoli "Cosa NON devi mai
#   fare" rispecchiano le regole di questo framework.


# ═══════════════════════════════════════════════════════════════
# 💡 ESEMPI PRATICI
# ═══════════════════════════════════════════════════════════════

# ESEMPIO 1: Filtro anti-ADD su una nuova idea
#
# Input utente: "Ho un'idea: creare una community a
# pagamento per i miei studenti dei corsi info!"
#
# Processo AI:
# 1. Attiva filtro anti-ADD (SEZIONE 2)
# 2. Domanda 1: Collegato ai pillar? → SÌ (Info-Business)
# 3. Domanda 2: Tutti i pillar 🟢? → Chiedi all'utente
#    → Utente: "Agenzia 🟡, YouTube 🟢, Info-biz 🟢"
#    → STOP: l'agenzia non è 🟢.
# 4. Output:
#    "L'idea della community è interessante e collegata
#     al pillar Info-Business. Tuttavia, il filtro anti-ADD
#     la blocca alla Domanda 2: l'agenzia è 🟡.
#
#     La regola è chiara: non aggiungere nuovi progetti
#     finché tutti i pillar non sono almeno 🟡 stabile
#     (preferibilmente 🟢).
#
#     ✏️ AZIONE: Annota l'idea nel backlog.
#     Rivaluta quando l'agenzia torna a 🟢.
#     Nel frattempo, concentra l'energia su
#     riportare l'agenzia on track."
#
# ESEMPIO 2: Allarme scatta nella dashboard
#
# Input utente: "L'agenzia ha fatto €6K questo mese e
# €7.5K il mese scorso. Due mesi fa era a €9K."
#
# Processo AI:
# 1. Riconosci il pattern: ↓↓ per 2 mesi consecutivi
# 2. Attiva ALARM_001 (SEZIONE 3)
# 3. Output:
#    "🔴 ALLARME ATTIVO: ALARM_001 — Revenue Agenzia
#     in Calo per 2 Mesi Consecutivi.
#
#     Revenue trend: €9K → €7.5K → €6K (calo del 33%)
#
#     PROTOCOLLO ATTIVATO:
#
#     📌 PROSSIME 24 ORE:
#     1. STOP attività info-biz e YouTube
#     2. Audit pipeline: quanti lead attivi?
#     3. Outreach d'emergenza ai lead ultimi 6 mesi
#     [...]
#
#     Questo protocollo resta attivo fino a quando il
#     revenue torna a ≥€9K O hai >5 lead qualificati
#     attivi."
#
# ESEMPIO 3: Allocazione risorse
#
# Input utente: "Come dovrei distribuire il mio tempo
# questa settimana?"
#
# Processo AI:
# 1. Chiedi stato dei pillar: "Quali sono gli status
#    🟢🟡🔴 di agenzia, info-biz e YouTube?"
# 2. Utente: "Agenzia 🟢, Info-biz 🟡, YouTube 🟢"
# 3. Calcola con calculate_resource_allocation()
# 4. Output:
#    "ALLOCAZIONE RISORSE — Questa Settimana
#
#     Scenario: STANDARD — 1 pillar a rischio
#
#     ┌─────────────────┬─────────┬─────────────────┐
#     │ Pillar           │ % Tempo │ Su 40h = ore    │
#     ├─────────────────┼─────────┼─────────────────┤
#     │ Agenzia CRO      │ 55%     │ 22h             │
#     │ Info-Business     │ 22%     │ 8.8h            │
#     │ YouTube           │ 15%     │ 6h              │
#     │ Satellite         │ 8%      │ 3.2h            │
#     └─────────────────┴─────────┴─────────────────┘
#
#     Info-business è 🟡: in quelle 8.8h, concentra
#     su risolvere la causa dello status giallo.
#     Non su nuovi prodotti — su riparare ciò che
#     non funziona."


# ═══════════════════════════════════════════════════════════════
# ⚠️ NOTE E AVVERTENZE
# ═══════════════════════════════════════════════════════════════

# 1. Il filtro anti-ADD ha un BIAS VOLONTARIO verso il NO.
#    Questo è intenzionale. Il bias naturale dell'imprenditore
#    è verso il SÌ (tutto sembra un'opportunità). Il filtro
#    compensa. In caso di dubbio → DEFAULT NO.
#
# 2. I protocolli di allarme NON sono suggerimenti. Sono
#    PROTOCOLLI. Quando un allarme scatta, si ESEGUE il
#    protocollo. Non si "valuta se forse farlo". Si fa.
#
# 3. L'allocazione risorse è una GUIDA, non una prigione.
#    Se in una settimana specifica serve il 70% sull'agenzia
#    per una deadline → fallo. Ma la media mensile deve
#    rispettare la distribuzione.
#
# 4. Il registro decisioni è FONDAMENTALE per le
#    retrospettive trimestrali. Senza di esso, ogni
#    trimestre si ripetono gli stessi errori perché
#    non c'è memoria strutturata.
#
# 5. NON usare il framework decisionale per le
#    micro-decisioni ("quale email scrivo prima?").
#    È per le macro-decisioni ("su quale pillar
#    concentro il prossimo mese?").
#
# 6. La valutazione opportunità (SEZIONE 6) si usa
#    SOLO per idee che superano il filtro anti-ADD.
#    Se l'idea non supera il filtro, NON serve
#    valutarla ulteriormente. Scartata = scartata.
#
# 7. Eric Siu parla di "ADD imprenditoriale" come il
#    killer #1 delle agenzie che non scalano. Questo
#    file è il VACCINO. Usalo religiosamente.
#
# 8. Quando l'utente presenta un'idea con entusiasmo,
#    la tentazione dell'AI è assecondare l'entusiasmo.
#    NON farlo. Esegui il filtro. L'empatia si esprime
#    nel PROTEGGERE il focus dell'utente, non nel
#    validare ogni impulso.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
