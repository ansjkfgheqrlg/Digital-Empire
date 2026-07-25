# ═══════════════════════════════════════════════════════════════
# 📄 DASHBOARD_ENGINE.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC + DATA_HANDLING
# Priorità: P0 — BLOCCANTE
# Dipendenze: TEMPLATE_PRODUZIONE.md, STANDARD_QUALITA.md,
#             OKR_CROSS_BUSINESS_ENGINE.md,
#             CROSS_POLLINATION_ENGINE.md,
#             DECISION_FRAMEWORK.md
# Referenziato da: Custom Instructions §2 (Processi di
#                  Ragionamento), §3 (Gestione Input),
#                  §4 (Generazione Output), §8 (Workflow)
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# 📋 SCOPO
# ═══════════════════════════════════════════════════════════════

# Questo file contiene il MOTORE DI COMPILAZIONE, ANALISI
# E INTERPRETAZIONE della Dashboard Empire Unificata.
# È il file che trasforma DATI GREZZI in INSIGHT AZIONABILI.
#
# Definisce:
#
# 1. Il protocollo di raccolta dati per ogni pillar
# 2. L'algoritmo di compilazione dashboard
# 3. Il sistema di analisi trend (MoM, QoQ, YoY)
# 4. Il motore di rilevamento anomalie automatico
# 5. Il generatore di insight e raccomandazioni
# 6. I protocolli per cadenze diverse (rapida vs completa)
# 7. Il collegamento dashboard → OKR → azioni
#
# La dashboard NON è un documento passivo che si legge.
# È uno STRUMENTO ATTIVO che genera decisioni.
#
# Principio fondamentale:
# "Se non lo misuri, non lo gestisci. Se non lo analizzi,
#  lo misuri per niente."


# ═══════════════════════════════════════════════════════════════
# 📖 CONTENUTO PRINCIPALE
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# SEZIONE 1: PROTOCOLLO DI RACCOLTA DATI
# ───────────────────────────────────────────────────────────────

# Per ogni metrica della dashboard, definisce:
# - DOVE trovare il dato
# - COME calcolarlo se è derivato
# - QUANDO raccoglierlo
# - CHI è responsabile (in un team di 1 = tu)

DATA_COLLECTION_PROTOCOL = {
    "versione": "1.0",

    "pillar_1_agenzia": {
        "metriche_acquisizione": {
            "lead_qualificati_mese": {
                "definizione": "Numero di persone/aziende che "
                               "hanno espresso interesse concreto "
                               "per i servizi dell'agenzia E "
                               "soddisfano i criteri di qualifica "
                               "(hanno traffico, budget, decisore)",
                "fonte": "CRM / Foglio tracking lead / Email",
                "calcolo": "Conteggio manuale dei nuovi lead "
                           "che soddisfano TUTTI i criteri: "
                           "(1) hanno un sito con traffico, "
                           "(2) hanno budget per il servizio, "
                           "(3) il contatto è il decisore",
                "frequenza_raccolta": "Continuo → compilazione "
                                      "mensile",
                "nota": "Un lead NON qualificato non va contato. "
                        "Meglio 5 lead qualificati che 50 curiosi."
            },
            "call_strategiche_mese": {
                "definizione": "Numero di sales call effettuate "
                               "(non programmate — effettuate)",
                "fonte": "Calendario + CRM",
                "calcolo": "Conteggio call avvenute con durata "
                           "≥15 minuti e prospect qualificato",
                "frequenza_raccolta": "Post-call → compilazione "
                                      "mensile"
            },
            "proposte_inviate_mese": {
                "definizione": "Numero di proposte/preventivi "
                               "formali inviati dopo la call",
                "fonte": "Email inviate / Cartella proposte",
                "calcolo": "Conteggio documenti di proposta "
                           "inviati (non bozze — inviati)",
                "frequenza_raccolta": "Post-invio → compilazione "
                                      "mensile"
            },
            "clienti_chiusi_mese": {
                "definizione": "Numero di prospect che hanno "
                               "accettato la proposta e pagato "
                               "(o firmato contratto)",
                "fonte": "Pagamenti ricevuti / Contratti firmati",
                "calcolo": "Conteggio clienti che hanno "
                           "effettuato il primo pagamento",
                "frequenza_raccolta": "Post-chiusura → "
                                      "compilazione mensile"
            },
            "close_rate": {
                "definizione": "Percentuale di call che si "
                               "trasformano in clienti chiusi",
                "fonte": "Derivato",
                "calcolo": "clienti_chiusi_mese / "
                           "call_strategiche_mese × 100",
                "frequenza_raccolta": "Calcolato a fine mese",
                "benchmark": "Target ≥30%. Sotto 20% = problema "
                             "nel processo di call."
            },
            "revenue_agenzia": {
                "definizione": "Revenue totale incassato "
                               "dall'agenzia nel mese",
                "fonte": "Conto bancario / Stripe / PayPal / "
                         "Fatture emesse",
                "calcolo": "Somma di tutti i pagamenti ricevuti "
                           "per servizi agenzia (fissi + "
                           "success fee)",
                "frequenza_raccolta": "Fine mese",
                "nota": "Conta l'INCASSATO, non il fatturato. "
                        "Se hai fatturato ma non incassato, "
                        "non conta."
            },
            "valore_medio_progetto": {
                "definizione": "Revenue medio per progetto "
                               "nel mese",
                "fonte": "Derivato",
                "calcolo": "revenue_agenzia / clienti_chiusi_mese "
                           "(o progetti attivi se nessun nuovo "
                           "cliente nel mese)",
                "frequenza_raccolta": "Calcolato a fine mese"
            }
        },

        "metriche_delivery": {
            "progetti_attivi": {
                "definizione": "Progetti in corso con deliverable "
                               "ancora da consegnare",
                "fonte": "Foglio tracking progetti",
                "calcolo": "Conteggio progetti non completati",
                "frequenza_raccolta": "Continuo"
            },
            "progetti_completati_mese": {
                "definizione": "Progetti chiusi e consegnati "
                               "con successo nel mese",
                "fonte": "Foglio tracking progetti",
                "calcolo": "Conteggio progetti con status "
                           "'completato' e data nel mese",
                "frequenza_raccolta": "Fine mese"
            },
            "nps_clienti": {
                "definizione": "Net Promoter Score medio dei "
                               "clienti (0-10)",
                "fonte": "Survey fine progetto / feedback diretto",
                "calcolo": "Media dei punteggi NPS ricevuti. "
                           "Domanda: 'Da 0 a 10, quanto "
                           "consiglieresti il mio servizio?'",
                "frequenza_raccolta": "Post-progetto",
                "benchmark": "Target >8. Sotto 7 = problema "
                             "di delivery."
            },
            "uplift_medio": {
                "definizione": "Miglioramento medio del conversion "
                               "rate ottenuto nei progetti",
                "fonte": "Report progetto / Analytics",
                "calcolo": "(CR_dopo - CR_prima) / CR_prima × 100 "
                           "mediato su tutti i progetti completati",
                "frequenza_raccolta": "Post-progetto"
            },
            "referral_ricevuti": {
                "definizione": "Nuovi lead arrivati tramite "
                               "referral da clienti esistenti",
                "fonte": "Chiedere al lead come ti ha trovato",
                "calcolo": "Conteggio lead con fonte = referral",
                "frequenza_raccolta": "Continuo"
            }
        },

        "health_check": {
            "domande": [
                {
                    "domanda": "Pipeline piena per i prossimi "
                               "30 giorni?",
                    "definizione_piena": "≥3 call strategiche "
                                         "programmate O ≥5 lead "
                                         "qualificati attivi",
                    "se_no": "Attiva outreach d'urgenza. Vedi "
                             "ALARM_001 in DECISION_FRAMEWORK.md"
                },
                {
                    "domanda": "Capacità di delivery sufficiente?",
                    "definizione": "Puoi prendere 1+ nuovo "
                                   "cliente senza compromettere "
                                   "la qualità dei progetti attivi",
                    "se_no": "Non fare outreach aggressivo. "
                             "Completa prima i progetti in corso."
                },
                {
                    "domanda": "Clienti esistenti soddisfatti?",
                    "definizione": "Nessun cliente con lamentele "
                                   "aperte o deliverable in ritardo",
                    "se_no": "Priorità massima: risolvi i problemi "
                             "aperti prima di cercare nuovi clienti."
                },
                {
                    "domanda": "Outreach attivo e costante?",
                    "definizione": "≥5 nuovi contatti outreach "
                                   "a settimana, costante",
                    "se_no": "Rimetti l'outreach in calendario. "
                             "Non è opzionale."
                }
            ]
        }
    },

    "pillar_2_info_biz": {
        "metriche_lista": {
            "dimensione_lista_email": {
                "definizione": "Numero totale di iscritti attivi "
                               "nella lista email (esclusi "
                               "disiscritti e bounce)",
                "fonte": "Email marketing tool (ConvertKit / "
                         "Mailchimp / ActiveCampaign)",
                "calcolo": "Totale iscritti - disiscritti - bounce",
                "frequenza_raccolta": "Fine mese"
            },
            "nuovi_lead_mese": {
                "definizione": "Nuovi iscritti alla lista nel mese",
                "fonte": "Email marketing tool → report nuovi "
                         "iscritti",
                "calcolo": "Conteggio nuove iscrizioni con "
                           "data nel mese",
                "frequenza_raccolta": "Fine mese",
                "segmentazione_consigliata": {
                    "per_fonte": "YouTube / Social / KDP / "
                                 "Paid / Referral / Altro",
                    "come": "Usa UTM diversi per ogni fonte. "
                            "Segmenta automaticamente nel tool "
                            "email con tag per fonte."
                }
            },
            "open_rate": {
                "definizione": "% di email aperte sul totale "
                               "inviate (media del mese)",
                "fonte": "Email marketing tool → report campagne",
                "calcolo": "Media open rate di tutte le email "
                           "inviate nel mese",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target >25%. Sotto 15% = problema "
                             "di deliverability o subject line."
            },
            "click_rate": {
                "definizione": "% di click sui link nelle email "
                               "sul totale inviate",
                "fonte": "Email marketing tool",
                "calcolo": "Media click rate di tutte le email",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target >3%. Sotto 1% = contenuto "
                             "non rilevante o CTA debole."
            },
            "unsubscribe_rate": {
                "definizione": "% di disiscrizioni sul totale "
                               "inviate",
                "fonte": "Email marketing tool",
                "calcolo": "Media unsubscribe rate del mese",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target <1%. Sopra 2% = invii "
                             "troppo frequenti o contenuto "
                             "non allineato."
            }
        },

        "metriche_prodotti": {
            "prodotti_attivi_catalogo": {
                "definizione": "Numero di prodotti info "
                               "attualmente in vendita",
                "fonte": "Conteggio manuale / Piattaforma corsi",
                "calcolo": "Tutti i prodotti con pagina di "
                           "vendita attiva e checkout funzionante",
                "frequenza_raccolta": "Fine mese"
            },
            "revenue_info_biz_mese": {
                "definizione": "Revenue totale da vendita "
                               "prodotti info nel mese",
                "fonte": "Stripe / PayPal / Piattaforma corsi",
                "calcolo": "Somma pagamenti per prodotti info "
                           "(esclusi refund)",
                "frequenza_raccolta": "Fine mese"
            },
            "vendite_per_tier": {
                "definizione": "Numero vendite per livello "
                               "della scala prodotti",
                "fonte": "Piattaforma corsi / Checkout",
                "calcolo": "Conteggio per: mini-corsi, corsi, "
                           "percorsi premium",
                "frequenza_raccolta": "Fine mese"
            },
            "refund_rate": {
                "definizione": "% di rimborsi sul totale vendite",
                "fonte": "Stripe / PayPal → refund report",
                "calcolo": "refund_count / vendite_totali × 100",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target <10%. Sopra 15% = "
                             "problema di qualità prodotto "
                             "o aspettative disallineate."
            },
            "nps_studenti": {
                "definizione": "Net Promoter Score medio degli "
                               "studenti dei corsi",
                "fonte": "Survey fine corso",
                "calcolo": "Media punteggi NPS studenti",
                "frequenza_raccolta": "Post-corso",
                "benchmark": "Target >7."
            }
        },

        "metriche_funnel": {
            "opt_in_rate_landing": {
                "definizione": "% di visitatori landing page "
                               "che si iscrivono (opt-in)",
                "fonte": "Analytics landing page + Email tool",
                "calcolo": "nuovi_iscritti / visitatori_landing × 100",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target >30%. Sotto 15% = landing "
                             "page da ottimizzare."
            },
            "conversion_rate_funnel": {
                "definizione": "% di lead che acquistano un "
                               "prodotto (qualsiasi livello)",
                "fonte": "Derivato",
                "calcolo": "acquirenti_mese / nuovi_lead_mese × 100",
                "frequenza_raccolta": "Fine mese"
            }
        },

        "health_check": {
            "domande": [
                {
                    "domanda": "Almeno 2 idee con score >60 "
                               "nel backlog?",
                    "se_no": "Attiva raccolta idee: commenti "
                             "YouTube, domande clienti agenzia, "
                             "ricerca competitor."
                },
                {
                    "domanda": "Funnel evergreen attivo e "
                               "funzionante?",
                    "se_no": "Test end-to-end del funnel. "
                             "Compra tu stesso."
                },
                {
                    "domanda": "Nurture settimanale inviato "
                               "regolarmente?",
                    "se_no": "Riprendi email settimanale. "
                             "La lista si raffredda."
                },
                {
                    "domanda": "Cross-pollination attiva con "
                               "agenzia e YouTube?",
                    "se_no": "Consulta CROSS_POLLINATION_ENGINE.md "
                             "e attiva 1 flusso."
                }
            ]
        }
    },

    "pillar_3_youtube": {
        "metriche_canale": {
            "iscritti_totali": {
                "definizione": "Numero totale di iscritti al canale",
                "fonte": "YouTube Studio → Dashboard",
                "calcolo": "Lettura diretta",
                "frequenza_raccolta": "Fine mese"
            },
            "nuovi_iscritti_mese": {
                "definizione": "Nuovi iscritti acquisiti nel mese",
                "fonte": "YouTube Studio → Analytics → Iscritti",
                "calcolo": "Iscritti guadagnati - iscritti persi",
                "frequenza_raccolta": "Fine mese"
            },
            "views_totali_mese": {
                "definizione": "Visualizzazioni totali nel mese",
                "fonte": "YouTube Studio → Analytics → Overview",
                "calcolo": "Lettura diretta",
                "frequenza_raccolta": "Fine mese"
            },
            "watch_time_medio": {
                "definizione": "Durata media di visualizzazione "
                               "per video (minuti)",
                "fonte": "YouTube Studio → Analytics → Engagement",
                "calcolo": "Media watch time su tutti i video "
                           "pubblicati nel mese",
                "frequenza_raccolta": "Fine mese"
            },
            "video_pubblicati_mese": {
                "definizione": "Numero di video pubblicati nel mese",
                "fonte": "YouTube Studio → Content",
                "calcolo": "Conteggio video con data pubblicazione "
                           "nel mese",
                "frequenza_raccolta": "Fine mese"
            },
            "ctr_medio": {
                "definizione": "Click-Through Rate medio delle "
                               "thumbnail (Impressions → Click)",
                "fonte": "YouTube Studio → Analytics → Reach",
                "calcolo": "Media CTR su video pubblicati nel mese",
                "frequenza_raccolta": "Fine mese",
                "benchmark": "Target >5%. Sotto 3% = thumbnail "
                             "o titoli da migliorare."
            }
        },

        "metriche_lead_gen": {
            "click_link_descrizione": {
                "definizione": "Click totali sui link nella "
                               "descrizione dei video",
                "fonte": "Bitly / UTM tracking / Analytics landing",
                "calcolo": "Somma click su tutti i link tracciati "
                           "nei video del mese",
                "frequenza_raccolta": "Fine mese"
            },
            "lead_da_youtube_mese": {
                "definizione": "Nuovi lead nella lista email "
                               "con fonte = YouTube",
                "fonte": "Email tool → segmento fonte YouTube",
                "calcolo": "Conteggio iscritti con tag "
                           "'fonte:youtube' nel mese",
                "frequenza_raccolta": "Fine mese"
            }
        },

        "content_mix": {
            "definizione": "Distribuzione dei video per tipo "
                           "(dal YouTube Lead Engine P2)",
            "target": {
                "anchor_70": "Video educativi, how-to, tutorial "
                             "(70% della produzione)",
                "shift_20": "Video opinione, trend, posizionamento "
                            "(20% della produzione)",
                "conversion_10": "Video con CTA diretta verso "
                                 "servizio/prodotto (10%)"
            },
            "calcolo": "Conteggio video per tipo / totale × 100",
            "frequenza_raccolta": "Fine mese"
        },

        "health_check": {
            "domande": [
                {
                    "domanda": "Pubblicazione costante "
                               "(min 1 video/settimana)?",
                    "se_no": "Vedi ALARM_003 in "
                             "DECISION_FRAMEWORK.md."
                },
                {
                    "domanda": "CTA verso PDF/funnel info-biz "
                               "in ogni video?",
                    "se_no": "Aggiungi CTA a tutti i video "
                             "futuri. Aggiorna descrizione "
                             "dei video recenti."
                },
                {
                    "domanda": "Content mix rispetta 70/20/10?",
                    "se_no": "Ribilancia la produzione per "
                             "il mese prossimo."
                },
                {
                    "domanda": "Video alimentano i topic dei "
                               "prodotti info?",
                    "se_no": "Allinea il piano editoriale con "
                             "il catalogo prodotti info-biz."
                }
            ]
        }
    },

    "satellite": {
        "kdp": {
            "libri_pubblicati_totali": {
                "fonte": "KDP Dashboard",
                "frequenza_raccolta": "Fine mese"
            },
            "revenue_kdp_mese": {
                "fonte": "KDP Dashboard → Reports",
                "frequenza_raccolta": "Fine mese"
            },
            "nuovi_libri_mese": {
                "fonte": "KDP Dashboard",
                "frequenza_raccolta": "Fine mese"
            }
        },
        "ai_influencer": {
            "personaggi_attivi": {
                "fonte": "Tracking interno",
                "frequenza_raccolta": "Fine mese"
            },
            "follower_totali": {
                "fonte": "Social analytics",
                "frequenza_raccolta": "Fine mese"
            },
            "revenue_ai_influencer_mese": {
                "fonte": "Pagamenti ricevuti",
                "frequenza_raccolta": "Fine mese"
            }
        }
    }
}


# ───────────────────────────────────────────────────────────────
# SEZIONE 2: ALGORITMO DI COMPILAZIONE DASHBOARD
# ───────────────────────────────────────────────────────────────

# Due modalità: RAPIDA (settimanale) e COMPLETA (mensile).

def compile_dashboard_rapid(
    raw_data: dict
) -> dict:
    """
    Compilazione rapida settimanale.
    Raccoglie solo le metriche critiche per un health check.

    Args:
        raw_data: dati grezzi della settimana

    Returns:
        Dashboard rapida con health status per pillar

    Metriche raccolte (solo queste):
    - Agenzia: lead in entrata, call fatte, revenue
    - Info-biz: nuovi lead lista, vendite, email inviate
    - YouTube: video pubblicati, views, lead generati
    - Cross-poll: azione settimanale fatta sì/no
    """
    rapid = {
        "tipo": "RAPIDA",
        "tempo_compilazione": "15 minuti",
        "cadenza": "Settimanale (lunedì)",

        "agenzia": {
            "lead_questa_settimana": raw_data.get(
                "agenzia_lead_settimana", 0
            ),
            "call_questa_settimana": raw_data.get(
                "agenzia_call_settimana", 0
            ),
            "revenue_progressivo_mese": raw_data.get(
                "agenzia_revenue_mtd", 0
            ),
            "quick_status": None  # calcolato sotto
        },

        "info_biz": {
            "nuovi_lead_settimana": raw_data.get(
                "info_lead_settimana", 0
            ),
            "vendite_settimana": raw_data.get(
                "info_vendite_settimana", 0
            ),
            "email_inviate": raw_data.get(
                "info_email_inviate", "Sì/No"
            ),
            "quick_status": None
        },

        "youtube": {
            "video_pubblicati_settimana": raw_data.get(
                "yt_video_settimana", 0
            ),
            "views_settimana": raw_data.get(
                "yt_views_settimana", 0
            ),
            "quick_status": None
        },

        "cross_poll": {
            "azione_fatta": raw_data.get(
                "cross_poll_action", False
            ),
            "quale_azione": raw_data.get(
                "cross_poll_action_desc", ""
            )
        }
    }

    # Quick status per pillar
    rapid["agenzia"]["quick_status"] = _quick_health(
        "agenzia", rapid["agenzia"]
    )
    rapid["info_biz"]["quick_status"] = _quick_health(
        "info_biz", rapid["info_biz"]
    )
    rapid["youtube"]["quick_status"] = _quick_health(
        "youtube", rapid["youtube"]
    )

    return rapid


def compile_dashboard_full(
    all_data: dict,
    previous_month: dict,
    targets: dict
) -> dict:
    """
    Compilazione completa mensile.
    Raccoglie TUTTE le metriche, calcola trend,
    genera status, e produce insight.

    Args:
        all_data: tutti i dati del mese corrente
        previous_month: dashboard del mese precedente
        targets: target per ogni metrica

    Returns:
        Dashboard completa con analisi e insight
    """
    dashboard = {
        "tipo": "COMPLETA",
        "tempo_compilazione": "45 minuti",
        "cadenza": "Mensile (primo lunedì)",
        "mese": all_data.get("mese", ""),
        "anno": all_data.get("anno", ""),

        # OVERVIEW
        "overview": _compile_overview(all_data, previous_month),

        # PILLAR 1
        "agenzia": _compile_pillar_agenzia(
            all_data.get("agenzia", {}),
            previous_month.get("agenzia", {}),
            targets.get("agenzia", {})
        ),

        # PILLAR 2
        "info_biz": _compile_pillar_info_biz(
            all_data.get("info_biz", {}),
            previous_month.get("info_biz", {}),
            targets.get("info_biz", {})
        ),

        # PILLAR 3
        "youtube": _compile_pillar_youtube(
            all_data.get("youtube", {}),
            previous_month.get("youtube", {}),
            targets.get("youtube", {})
        ),

        # SATELLITE
        "satellite": _compile_satellite(
            all_data.get("satellite", {})
        ),

        # CROSS-POLLINATION
        "cross_pollination": _compile_cross_poll(
            all_data.get("cross_poll", {})
        ),

        # INSIGHT (generati dopo la compilazione)
        "insights": [],
        "allarmi_attivi": [],
        "azioni_suggerite": []
    }

    # Genera insight automatici
    dashboard["insights"] = _generate_insights(dashboard)
    dashboard["allarmi_attivi"] = _check_alarms(dashboard)
    dashboard["azioni_suggerite"] = _suggest_actions(
        dashboard, targets
    )

    return dashboard


def _compile_overview(
    current: dict, previous: dict
) -> dict:
    """Compila la sezione overview con revenue totale."""
    revenue_components = {
        "agenzia": current.get("agenzia", {}).get(
            "revenue", 0
        ),
        "info_biz": current.get("info_biz", {}).get(
            "revenue", 0
        ),
        "youtube": current.get("youtube", {}).get(
            "revenue", 0
        ),
        "kdp": current.get("satellite", {}).get(
            "kdp_revenue", 0
        ),
        "ai_influencer": current.get("satellite", {}).get(
            "ai_revenue", 0
        )
    }

    revenue_totale = sum(revenue_components.values())
    revenue_prev = previous.get("overview", {}).get(
        "revenue_totale", 0
    )

    if revenue_prev > 0:
        trend_pct = ((revenue_totale - revenue_prev) /
                     revenue_prev) * 100
        trend_dir = "↑" if trend_pct > 0 else (
            "↓" if trend_pct < 0 else "→"
        )
    else:
        trend_pct = 0
        trend_dir = "→"

    # Distribuzione percentuale
    distribuzione = {}
    for key, val in revenue_components.items():
        if revenue_totale > 0:
            distribuzione[key] = round(
                val / revenue_totale * 100, 1
            )
        else:
            distribuzione[key] = 0

    return {
        "revenue_totale": revenue_totale,
        "revenue_per_pillar": revenue_components,
        "distribuzione_pct": distribuzione,
        "trend_vs_mese_precedente": {
            "direzione": trend_dir,
            "percentuale": round(trend_pct, 1)
        },
        "revenue_mese_precedente": revenue_prev
    }


def _quick_health(pillar: str, data: dict) -> str:
    """Health check rapido per la dashboard settimanale."""
    if pillar == "agenzia":
        if data.get("lead_questa_settimana", 0) == 0 and \
           data.get("call_questa_settimana", 0) == 0:
            return "🔴 — Nessun lead e nessuna call. Pipeline ferma."
        elif data.get("lead_questa_settimana", 0) == 0 or \
             data.get("call_questa_settimana", 0) == 0:
            return "🟡 — Attività parziale. Verifica pipeline."
        else:
            return "🟢 — Attività in corso."

    elif pillar == "info_biz":
        if data.get("email_inviate") == "No":
            return "🟡 — Nessuna email inviata. Lista si raffredda."
        elif data.get("nuovi_lead_settimana", 0) == 0:
            return "🟡 — Zero nuovi lead. Verifica traffico."
        else:
            return "🟢 — Flusso attivo."

    elif pillar == "youtube":
        if data.get("video_pubblicati_settimana", 0) == 0:
            return "🟡 — Nessun video questa settimana."
        else:
            return "🟢 — Produzione attiva."

    return "⚪ — Dati insufficienti."


# ───────────────────────────────────────────────────────────────
# SEZIONE 3: SISTEMA DI ANALISI TREND
# ───────────────────────────────────────────────────────────────

def analyze_trend(
    metric_name: str,
    current_value: float,
    previous_values: list,
    target: float
) -> dict:
    """
    Analizza il trend di una metrica nel tempo.

    Args:
        metric_name: nome della metrica
        current_value: valore attuale
        previous_values: lista valori precedenti
                         [mese-1, mese-2, mese-3, ...]
                         ordinati dal più recente
        target: valore target

    Returns:
        Analisi trend con direzione, velocità e proiezione
    """
    if not previous_values:
        return {
            "metrica": metric_name,
            "trend": "INSUFFICIENTE",
            "nota": "Serve almeno 1 mese di storico "
                    "per calcolare il trend"
        }

    # Month-over-Month
    mom = current_value - previous_values[0]
    if previous_values[0] != 0:
        mom_pct = (mom / abs(previous_values[0])) * 100
    else:
        mom_pct = 100 if current_value > 0 else 0

    # Direzione trend (basata sugli ultimi 3 mesi)
    values = [current_value] + previous_values[:2]
    if len(values) >= 3:
        if values[0] > values[1] > values[2]:
            direction = "↑↑ CRESCITA FORTE"
        elif values[0] > values[1]:
            direction = "↑ CRESCITA"
        elif values[0] == values[1]:
            direction = "→ STABILE"
        elif values[0] < values[1] and values[0] > values[2]:
            direction = "↕ OSCILLANTE"
        elif values[0] < values[1]:
            direction = "↓ CALO"
            if len(values) >= 3 and values[0] < values[2]:
                direction = "↓↓ CALO FORTE"
    else:
        if mom > 0:
            direction = "↑ CRESCITA"
        elif mom < 0:
            direction = "↓ CALO"
        else:
            direction = "→ STABILE"

    # Gap dal target
    if target > 0:
        gap_from_target = target - current_value
        gap_pct = (gap_from_target / target) * 100
        on_target = current_value >= target
    else:
        gap_from_target = 0
        gap_pct = 0
        on_target = True

    # Proiezione (se il trend continua)
    if len(previous_values) >= 2:
        avg_change = mom  # semplificazione: usa ultimo MoM
        projected_3m = current_value + (avg_change * 3)
        months_to_target = None
        if avg_change > 0 and gap_from_target > 0:
            months_to_target = round(
                gap_from_target / avg_change, 1
            )
    else:
        projected_3m = None
        months_to_target = None

    return {
        "metrica": metric_name,
        "valore_attuale": current_value,
        "target": target,
        "mom_assoluto": round(mom, 2),
        "mom_pct": round(mom_pct, 1),
        "direction": direction,
        "on_target": on_target,
        "gap_from_target": round(gap_from_target, 2),
        "gap_pct": round(gap_pct, 1),
        "proiezione_3_mesi": (round(projected_3m, 2)
                              if projected_3m else None),
        "mesi_al_target": months_to_target,
        "storico": {
            "attuale": current_value,
            "mese_precedente": previous_values[0]
            if previous_values else None,
            "2_mesi_fa": previous_values[1]
            if len(previous_values) > 1 else None
        }
    }


# ───────────────────────────────────────────────────────────────
# SEZIONE 4: MOTORE DI RILEVAMENTO ANOMALIE
# ───────────────────────────────────────────────────────────────

ANOMALY_RULES = {
    "versione": "1.0",

    "regole": {
        "calo_significativo": {
            "condizione": "Calo MoM > 20% su qualsiasi "
                          "metrica di revenue",
            "severita": "ALTA",
            "azione": "Indaga la causa. Compila la sezione "
                      "root cause della gap analysis."
        },
        "crescita_anomala": {
            "condizione": "Crescita MoM > 100% su qualsiasi "
                          "metrica",
            "severita": "INFO",
            "azione": "Verifica: è reale o è un errore di "
                      "misurazione? Se reale, identifica la "
                      "causa per replicarla."
        },
        "stagnazione": {
            "condizione": "Variazione MoM < 2% per 3+ mesi "
                          "consecutivi su una metrica non "
                          "ancora a target",
            "severita": "MEDIA",
            "azione": "La strategia attuale non sta funzionando. "
                      "Serve un cambiamento di approccio, "
                      "non più dello stesso."
        },
        "distribuzione_sbilanciata": {
            "condizione": "Un pillar genera >80% del revenue "
                          "totale",
            "severita": "MEDIA",
            "azione": "Dipendenza eccessiva da un solo pillar. "
                      "Accelera la diversificazione (ma senza "
                      "violare la gerarchia)."
        },
        "cross_poll_zero": {
            "condizione": "Zero bridge metrics per 30+ giorni",
            "severita": "MEDIA",
            "azione": "Le sinergie sono ferme. Attiva ALARM_004 "
                      "in DECISION_FRAMEWORK.md."
        },
        "calo_doppio": {
            "condizione": "Revenue in calo per 2+ mesi "
                          "consecutivi su qualsiasi pillar",
            "severita": "ALTA",
            "azione": "Se è l'agenzia → ALARM_001. "
                      "Se è info-biz → ALARM_002. "
                      "Se è YouTube → ALARM_003."
        }
    }
}


def detect_anomalies(
    current_dashboard: dict,
    historical_data: list
) -> list:
    """
    Scansiona la dashboard alla ricerca di anomalie.

    Args:
        current_dashboard: dashboard compilata del mese
        historical_data: lista di dashboard dei mesi
                         precedenti (più recente prima)

    Returns:
        Lista di anomalie rilevate con severità e azione
    """
    anomalies = []

    if not historical_data:
        return [{
            "tipo": "DATI_INSUFFICIENTI",
            "messaggio": "Primo mese di tracking. Nessuna "
                         "anomalia rilevabile. Continua a "
                         "raccogliere dati.",
            "severita": "INFO"
        }]

    prev = historical_data[0]

    # Check: calo significativo revenue per pillar
    for pillar in ["agenzia", "info_biz", "youtube"]:
        curr_rev = current_dashboard.get(pillar, {}).get(
            "revenue", 0
        )
        prev_rev = prev.get(pillar, {}).get("revenue", 0)

        if prev_rev > 0:
            change_pct = ((curr_rev - prev_rev) /
                          prev_rev) * 100
            if change_pct < -20:
                anomalies.append({
                    "tipo": "CALO_SIGNIFICATIVO",
                    "pillar": pillar,
                    "valore_attuale": curr_rev,
                    "valore_precedente": prev_rev,
                    "variazione_pct": round(change_pct, 1),
                    "severita": "ALTA",
                    "azione": ANOMALY_RULES["regole"][
                        "calo_significativo"
                    ]["azione"]
                })

    # Check: calo doppio (2 mesi consecutivi)
    if len(historical_data) >= 2:
        for pillar in ["agenzia", "info_biz", "youtube"]:
            curr = current_dashboard.get(pillar, {}).get(
                "revenue", 0
            )
            m1 = historical_data[0].get(pillar, {}).get(
                "revenue", 0
            )
            m2 = historical_data[1].get(pillar, {}).get(
                "revenue", 0
            )
            if curr < m1 < m2:
                anomalies.append({
                    "tipo": "CALO_DOPPIO",
                    "pillar": pillar,
                    "trend": f"€{m2} → €{m1} → €{curr}",
                    "severita": "ALTA",
                    "azione": ANOMALY_RULES["regole"][
                        "calo_doppio"
                    ]["azione"]
                })

    # Check: stagnazione (3 mesi)
    if len(historical_data) >= 3:
        for pillar in ["agenzia", "info_biz", "youtube"]:
            values = [
                current_dashboard.get(pillar, {}).get(
                    "revenue", 0
                )
            ] + [
                h.get(pillar, {}).get("revenue", 0)
                for h in historical_data[:2]
            ]
            if all(v > 0 for v in values):
                max_var = max(values) - min(values)
                avg_val = sum(values) / len(values)
                if avg_val > 0 and (max_var / avg_val) < 0.05:
                    anomalies.append({
                        "tipo": "STAGNAZIONE",
                        "pillar": pillar,
                        "valori_3_mesi": values,
                        "severita": "MEDIA",
                        "azione": ANOMALY_RULES["regole"][
                            "stagnazione"
                        ]["azione"]
                    })

    # Check: distribuzione sbilanciata
    overview = current_dashboard.get("overview", {})
    dist = overview.get("distribuzione_pct", {})
    for pillar, pct in dist.items():
        if pct > 80:
            anomalies.append({
                "tipo": "DISTRIBUZIONE_SBILANCIATA",
                "pillar": pillar,
                "percentuale": pct,
                "severita": "MEDIA",
                "azione": ANOMALY_RULES["regole"][
                    "distribuzione_sbilanciata"
                ]["azione"]
            })

    return anomalies


# ───────────────────────────────────────────────────────────────
# SEZIONE 5: GENERATORE DI INSIGHT E RACCOMANDAZIONI
# ───────────────────────────────────────────────────────────────

def _generate_insights(dashboard: dict) -> list:
    """
    Genera insight automatici dalla dashboard compilata.
    Ogni insight è un'osservazione azionabile, non un
    dato grezzo.

    Formato insight:
    "OSSERVAZIONE + IMPLICAZIONE + AZIONE SUGGERITA"
    """
    insights = []

    # Insight 1: Revenue mix
    overview = dashboard.get("overview", {})
    dist = overview.get("distribuzione_pct", {})
    agenzia_pct = dist.get("agenzia", 0)

    if agenzia_pct > 90:
        insights.append({
            "tipo": "CONCENTRAZIONE",
            "osservazione": f"Il {agenzia_pct}% del revenue "
                           f"viene dall'agenzia.",
            "implicazione": "Dipendenza quasi totale dal "
                            "core business. Se perdi 1 "
                            "cliente, l'impatto è enorme.",
            "azione": "Accelera il pillar Info-Business. "
                      "Lancia il prossimo prodotto nel "
                      "backlog per creare un secondo "
                      "flusso di revenue.",
            "priorita": "MEDIA"
        })
    elif agenzia_pct < 40:
        insights.append({
            "tipo": "GERARCHIA_INVERTITA",
            "osservazione": f"L'agenzia genera solo il "
                           f"{agenzia_pct}% del revenue.",
            "implicazione": "La gerarchia sacra è invertita. "
                            "Il core business non è più il "
                            "core. Rischio di dispersione.",
            "azione": "Verifica: l'agenzia è in difficoltà "
                      "o gli altri pillar sono cresciuti? "
                      "Se l'agenzia è debole → ALARM_001.",
            "priorita": "ALTA"
        })

    # Insight 2: Trend revenue totale
    trend = overview.get("trend_vs_mese_precedente", {})
    trend_pct = trend.get("percentuale", 0)

    if trend_pct > 20:
        insights.append({
            "tipo": "CRESCITA_FORTE",
            "osservazione": f"Revenue totale in crescita "
                           f"del {trend_pct}% MoM.",
            "implicazione": "Momentum positivo. Importante "
                            "capire COSA ha causato la "
                            "crescita per replicarla.",
            "azione": "Identifica la fonte della crescita. "
                      "È un nuovo cliente? Un lancio? "
                      "Traffico organico? Replica.",
            "priorita": "BASSA"
        })
    elif trend_pct < -10:
        insights.append({
            "tipo": "CALO",
            "osservazione": f"Revenue totale in calo del "
                           f"{abs(trend_pct)}% MoM.",
            "implicazione": "Se il trend continua, il "
                            "trimestre è a rischio.",
            "azione": "Attiva il processo decisionale "
                      "a 4 step (DECISION_FRAMEWORK.md) "
                      "con priorità ALTA.",
            "priorita": "ALTA"
        })

    # Insight 3: Cross-pollination health
    cross = dashboard.get("cross_pollination", {})
    azioni_mese = cross.get("azioni_mese", 0)

    if azioni_mese == 0:
        insights.append({
            "tipo": "CROSS_POLL_FERMA",
            "osservazione": "Zero azioni cross-pillar "
                           "questo mese.",
            "implicazione": "I pillar stanno operando in "
                            "isolamento. Il compound "
                            "interest si sta azzerando.",
            "azione": "Lunedì prossimo: 1 azione obbligatoria. "
                      "Consulta CROSS_POLLINATION_ENGINE.md.",
            "priorita": "MEDIA"
        })
    elif azioni_mese >= 4:
        insights.append({
            "tipo": "CROSS_POLL_ATTIVA",
            "osservazione": f"{azioni_mese} azioni cross-pillar "
                           f"questo mese. Obiettivo raggiunto.",
            "implicazione": "Le sinergie sono attive. Il "
                            "compound interest sta lavorando.",
            "azione": "Mantieni la cadenza. Verifica i "
                      "bridge metrics per misurare l'impatto.",
            "priorita": "BASSA"
        })

    return insights


def _check_alarms(dashboard: dict) -> list:
    """
    Verifica se qualche soglia di allarme è stata
    superata. Referenzia DECISION_FRAMEWORK.md
    per i protocolli.
    """
    alarms = []

    # ALARM_001 check
    overview = dashboard.get("overview", {})
    trend = overview.get("trend_vs_mese_precedente", {})
    agenzia_rev = dashboard.get("agenzia", {}).get("revenue", 0)

    if trend.get("percentuale", 0) < -10 and \
       dashboard.get("_prev_trend_also_negative", False):
        alarms.append({
            "alarm_id": "ALARM_001",
            "nome": "Revenue Agenzia in Calo — 2 Mesi",
            "severita": "🔴 CRITICO",
            "azione": "Consulta DECISION_FRAMEWORK.md → "
                      "ALARM_001 per il protocollo completo"
        })

    # ALARM_003 check
    yt_videos = dashboard.get("youtube", {}).get(
        "video_pubblicati_mese", 0
    )
    if yt_videos == 0:
        alarms.append({
            "alarm_id": "ALARM_003",
            "nome": "Zero Video YouTube Questo Mese",
            "severita": "🟡 A RISCHIO",
            "azione": "Consulta DECISION_FRAMEWORK.md → "
                      "ALARM_003"
        })

    # ALARM_004 check
    cross_actions = dashboard.get(
        "cross_pollination", {}
    ).get("azioni_mese", 0)
    if cross_actions == 0:
        alarms.append({
            "alarm_id": "ALARM_004",
            "nome": "Zero Cross-Pollination Questo Mese",
            "severita": "🟡 A RISCHIO",
            "azione": "Consulta DECISION_FRAMEWORK.md → "
                      "ALARM_004"
        })

    return alarms


def _suggest_actions(
    dashboard: dict, targets: dict
) -> list:
    """
    Genera 3-5 azioni suggerite basate sulla dashboard.
    Ordinate per impatto decrescente.
    """
    actions = []

    # Suggerimento basato su health checks
    for pillar in ["agenzia", "info_biz", "youtube"]:
        health = dashboard.get(pillar, {}).get(
            "health_check", {}
        )
        failed_checks = [
            q for q in health.get("domande", [])
            if q.get("risposta") == "No"
        ]
        for check in failed_checks[:2]:
            actions.append({
                "pillar": pillar,
                "azione": check.get("se_no", ""),
                "urgenza": "MEDIA",
                "tipo": "HEALTH_CHECK_FAILED"
            })

    # Suggerimento basato su anomalie
    anomalies = detect_anomalies(
        dashboard,
        dashboard.get("_historical", [])
    )
    for anomaly in anomalies[:2]:
        actions.append({
            "pillar": anomaly.get("pillar", "empire"),
            "azione": anomaly.get("azione", ""),
            "urgenza": anomaly.get("severita", "MEDIA"),
            "tipo": "ANOMALY_DETECTED"
        })

    # Ordina per urgenza
    urgency_order = {"ALTA": 0, "MEDIA": 1, "BASSA": 2,
                     "INFO": 3}
    actions.sort(
        key=lambda a: urgency_order.get(a["urgenza"], 2)
    )

    return actions[:5]


# ═══════════════════════════════════════════════════════════════
# 🔧 COME UTILIZZARE QUESTO FILE
# ═══════════════════════════════════════════════════════════════

# QUANDO CONSULTARLO:
#
# 1. Ogni LUNEDÌ → usa compile_dashboard_rapid() per il
#    health check settimanale. 15 minuti max.
#    Chiedi all'utente solo le metriche rapide.
#
# 2. Ogni PRIMO LUNEDÌ DEL MESE → usa compile_dashboard_full()
#    per la dashboard completa. 45 minuti.
#    Guida l'utente nella raccolta di TUTTI i dati seguendo
#    il protocollo di SEZIONE 1.
#
# 3. Quando l'utente dice "come sto?" o "come va il business?"
#    → verifica quando è stata compilata l'ultima dashboard.
#    Se >7 giorni fa → chiedi un update rapido.
#    Se >30 giorni fa → serve la dashboard completa.
#
# 4. Quando l'utente fornisce dati → usa analyze_trend()
#    per contestualizzare. Non mostrare solo numeri,
#    mostra TREND + GAP + AZIONE.
#
# 5. Dopo ogni compilazione completa → esegui
#    detect_anomalies() e mostra i risultati.
#
# 6. Le azioni suggerite (_suggest_actions) vengono incluse
#    alla fine della dashboard come "PROSSIMI STEP".

# COME INTEGRARLO NELLA RISPOSTA:
#
# - Quando mostri dati, usa SEMPRE il formato tabella
#   con Target / Reale / Status (🟢🟡🔴)
# - Quando mostri un trend, includi: direzione (↑↓→),
#   percentuale MoM, proiezione 3 mesi
# - Quando rilevi un'anomalia, cita l'ALARM specifico
#   e il protocollo di risposta
# - Gli insight devono essere nel formato:
#   OSSERVAZIONE + IMPLICAZIONE + AZIONE (non solo numeri)
# - Non aspettare che l'utente chieda "e quindi?". Genera
#   SEMPRE almeno 3 azioni suggerite dopo una dashboard


# ═══════════════════════════════════════════════════════════════
# 🔗 COLLEGAMENTI
# ═══════════════════════════════════════════════════════════════

# → TEMPLATE_PRODUZIONE.md: il template VISIVO della dashboard
#   che l'utente vede. Questo file è il MOTORE che lo popola
#   e lo interpreta.
#
# → STANDARD_QUALITA.md: i benchmark e i target per ogni
#   metrica sono definiti lì. Questo file li usa per
#   calcolare gli status 🟢🟡🔴.
#
# → OKR_CROSS_BUSINESS_ENGINE.md: dopo la dashboard,
#   il passo successivo è aggiornare i KR con i nuovi dati.
#   La dashboard alimenta la gap analysis.
#
# → CROSS_POLLINATION_ENGINE.md: la sezione "Cross-Pollination
#   Report" della dashboard usa i dati del registro azioni
#   e i bridge metrics definiti lì.
#
# → DECISION_FRAMEWORK.md: gli allarmi rilevati dal motore
#   anomalie triggerano i protocolli di allarme definiti lì.
#   Lo Step 1 del processo decisionale ("Stato Attuale")
#   richiede la dashboard compilata.
#
# → PIPELINE_OVERVIEW.md: le cadenze settimanale e mensile
#   includono la compilazione dashboard come primo step.
#
# → Custom Instructions §3: la validazione dell'input
#   dati dall'utente segue il protocollo di SEZIONE 1.
#
# → Custom Instructions §4: il formato output delle
#   dashboard segue le regole di SEZIONE 2 e 5.


# ═══════════════════════════════════════════════════════════════
# 💡 ESEMPI PRATICI
# ═══════════════════════════════════════════════════════════════

# ESEMPIO 1: Dashboard Rapida Settimanale
#
# Input utente: "Quick check — come sto questa settimana?"
#
# Processo AI:
# 1. Chiedi solo le metriche rapide:
#    "Dammi un update veloce:
#     - Agenzia: lead in entrata? Call fatte? Revenue MTD?
#     - Info-biz: nuovi lead lista? Vendite? Email inviata?
#     - YouTube: video pubblicati? Views?
#     - Cross-poll: hai fatto 1 azione questa settimana?"
#
# 2. Utente: "2 lead, 1 call, €3K MTD. 15 lead lista,
#    0 vendite, sì email. 1 video, 500 views. No cross-poll."
#
# 3. Compila dashboard rapida:
#    "📊 QUICK CHECK — Settimana [N]
#
#     AGENZIA: 🟢 — 2 lead, 1 call, €3K MTD
#     → Pipeline attiva. Programma 1-2 call per la
#       prossima settimana.
#
#     INFO-BIZ: 🟡 — 15 lead, 0 vendite, email ✅
#     → Lead arrivano ma non convertono. Verifica il
#       funnel: la sequenza email porta all'offerta?
#
#     YOUTUBE: 🟢 — 1 video, 500 views
#     → Produzione attiva. Bene.
#
#     CROSS-POLL: ❌ — Nessuna azione
#     → Scegline 1 per la prossima settimana.
#
#     FOCUS QUESTA SETTIMANA:
#     Diagnostica funnel info-biz (0 vendite con lead in
#     entrata = il funnel ha un problema)."
#
# ESEMPIO 2: Dashboard Completa Mensile
#
# Input utente: "Facciamo la dashboard di gennaio"
#
# Processo AI:
# 1. Guida l'utente nella raccolta di TUTTE le metriche
#    seguendo il protocollo di SEZIONE 1
# 2. Compila il template di TEMPLATE_PRODUZIONE.md
# 3. Esegui analyze_trend() su metriche chiave
# 4. Esegui detect_anomalies()
# 5. Genera insight con _generate_insights()
# 6. Output finale:
#    - Dashboard completa con tabelle
#    - Sezione TREND con grafici testuali
#    - Sezione ANOMALIE (se rilevate)
#    - Sezione INSIGHT (3-5 osservazioni azionabili)
#    - Sezione PROSSIMI STEP (3-5 azioni suggerite)
#    - Collegamento agli OKR: "Questo impatta il KR [X]
#      che è attualmente al [Y]%"
#
# ESEMPIO 3: Rilevamento Anomalia
#
# Utente: "Revenue agenzia: €6K (mese scorso: €8K,
# 2 mesi fa: €9.5K)"
#
# Processo AI:
# 1. detect_anomalies(): CALO_DOPPIO su agenzia
#    (€9.5K → €8K → €6K)
# 2. Output:
#    "⚠️ ANOMALIA RILEVATA: CALO_DOPPIO
#     Il revenue agenzia è in calo per 2 mesi consecutivi.
#     Trend: €9.5K → €8K → €6K (-37% in 2 mesi)
#
#     Questo attiva l'ALARM_001 (Revenue Agenzia in Calo).
#     Protocollo: [riferimento a DECISION_FRAMEWORK.md]
#
#     ❗ AZIONE IMMEDIATA RICHIESTA:
#     Il protocollo richiede STOP su info-biz e YouTube
#     e focus 100% sulla pipeline agenzia.
#     Confermi di voler attivare il protocollo?"


# ═══════════════════════════════════════════════════════════════
# ⚠️ NOTE E AVVERTENZE
# ═══════════════════════════════════════════════════════════════

# 1. La dashboard è INUTILE se non è compilata con dati
#    REALI. Non inventare numeri. Non arrotondare troppo.
#    Non usare "circa". Usa il numero esatto.
#
# 2. Se l'utente non ha ancora un sistema di tracking per
#    una metrica, NON ignorare la metrica. Suggerisci:
#    "Primo step: impostare il tracking per [metrica].
#    Non puoi gestire ciò che non misuri."
#
# 3. La dashboard RAPIDA non sostituisce la COMPLETA.
#    La rapida è un health check. La completa è una
#    diagnosi. Servono entrambe.
#
# 4. Gli insight generati automaticamente sono un PUNTO
#    DI PARTENZA, non la risposta finale. L'AI deve
#    contestualizzare con il contesto specifico dell'utente.
#
# 5. Quando l'utente dice "non ho i dati", non arrenderti.
#    Guida verso una stima ragionevole: "Non hai il numero
#    esatto? Sai almeno se è più di X o meno di Y?"
#    Una stima informata è meglio di zero dati.
#
# 6. Il collegamento dashboard → OKR → azioni è la
#    catena più importante. Dopo OGNI dashboard, chiedi:
#    "Come impattano questi numeri sui tuoi KR?"
#    Non lasciare la dashboard come un documento isolato.
#
# 7. Le anomalie NON sono sempre negative. Una crescita
#    anomala (+100% MoM) merita attenzione quanto un calo.
#    Se non capisci PERCHÉ qualcosa è cresciuto, non puoi
#    replicarla.