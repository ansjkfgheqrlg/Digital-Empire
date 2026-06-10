"""
Orchestratore Multi-Agente — Digital Empire Outreach
Architettura: 6 Team coordinati (pattern Anthropic multi-agent teams)

TEAM 1 — INTELLIGENCE:   Scraper + Extractor + Qualifier
TEAM 2 — COPY KNOWLEDGE: CopyKnowledgeAgent (briefing pack)
TEAM 3 — STRATEGY:       StrategistAgent (hook angle + brief)
TEAM 4 — COPY:           EmailWriter (NVIDIA Nemotron)
TEAM 5 — HUMAN VOICE QA: HumanizerAgent (3 check + revision loop)
TEAM 6 — DELIVERY:       SenderAgent + SQLite tracker

Costo: $0/giorno — tutto NVIDIA Nemotron via OpenRouter (gratuito)
"""

import sqlite3
from datetime import datetime
from pathlib import Path

from utils.printer import (
    scraping_header, scraping_query, scraping_risultato, scraping_done,
    email_header, email_generando, email_ok, email_scartata, sezione, warn, errore
)

from agents.scraper import FacebookScraperAgent
from agents.google_scraper import GooglePlacesScraper
from agents.outscraper_scraper import OutscraperScraper
from agents.apify_scraper import ApifyScraper
from agents.apify_leads_finder import ApifyLeadsFinder
from agents.maps_browser_scraper import MapsBrowserScraper, SESSION_DIR
from agents.extractor import EmailExtractorAgent
from agents.qualifier import QualifierAgent
from agents.research import ResearchAgent
from agents.copy_knowledge import CopyKnowledgeAgent
from agents.strategist import StrategistAgent
from agents.writer import EmailWriterAgent
from agents.humanizer import HumanizerAgent
from agents.bibbia_team import BibbiaTeam
from agents.sender import EmailSenderAgent


class OutreachOrchestrator:
    """
    Orchestratore centrale del sistema di outreach a 6 team.

    Coordina l'intero flusso dall'acquisizione dei lead fino all'invio,
    con revision loop qualità e report finale dettagliato.
    """

    def __init__(self, config: dict, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.db_path = self.output_dir / "leads.db"

        openrouter_key = config["OPENROUTER_API_KEY"]

        # Scraper: ApifyLeadsFinder > Apify Maps > Outscraper > Google Places > Facebook
        # Tutti gli scraper vengono istanziati se disponibili — fallback runtime automatico
        apify_token       = config.get("APIFY_API_TOKEN", "").strip()
        use_leads_finder  = config.get("APIFY_LEADS_FINDER", "").strip() == "1"
        outscraper_key    = config.get("OUTSCRAPER_API_KEY", "").strip()
        google_key        = config.get("GOOGLE_PLACES_API_KEY", "").strip()
        fb_token          = config.get("FB_ACCESS_TOKEN", "").strip()

        # Catena di fallback runtime (tentati in ordine finché uno funziona)
        self._scraper_chain = []
        # Maps Browser Scraper — priorità massima se sessione disponibile (zero costi, zero limiti)
        if SESSION_DIR.exists():
            self._scraper_chain.append(("Google Maps Browser", MapsBrowserScraper()))
        if apify_token and use_leads_finder:
            self._scraper_chain.append(("Apify Leads Finder", ApifyLeadsFinder(apify_token)))
        if apify_token:
            self._scraper_chain.append(("Apify Google Maps", ApifyScraper(apify_token)))
        if outscraper_key:
            self._scraper_chain.append(("Outscraper", OutscraperScraper(outscraper_key)))
        if google_key:
            self._scraper_chain.append(("Google Places API", GooglePlacesScraper(google_key)))
        if fb_token:
            self._scraper_chain.append(("Facebook Ads Library", FacebookScraperAgent(fb_token)))

        if not self._scraper_chain:
            raise RuntimeError(
                "Nessun scraper configurato. Aggiungi APIFY_API_TOKEN "
                "(consigliato, free tier) o GOOGLE_PLACES_API_KEY nel .env"
            )
        # scraper primario (per compatibilità con codice che usa self.scraper)
        self.scraper = self._scraper_chain[0][1]
        print(f"[ORCHESTRATOR] Scraper primario: {self._scraper_chain[0][0]}"
              f" | Fallback: {len(self._scraper_chain)-1}")
        self.extractor = EmailExtractorAgent()
        self.qualifier = QualifierAgent(openrouter_key)
        self.research = ResearchAgent()
        self.copy_knowledge = CopyKnowledgeAgent(openrouter_key)
        self.strategist = StrategistAgent(openrouter_key)
        self.writer = EmailWriterAgent(openrouter_key)
        self.humanizer = HumanizerAgent(openrouter_key)
        self.bibbia_team = BibbiaTeam(openrouter_key)
        self.sender = EmailSenderAgent(config["GMAIL_USER"], config["GMAIL_APP_PASSWORD"])

        self._init_db()

    # ────────────────────────────────────────────────────────────────────────
    # Database SQLite (deduplicazione + tracking)
    # ────────────────────────────────────────────────────────────────────────

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS leads_contattati (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    page_id     TEXT,
                    email       TEXT UNIQUE,
                    page_name   TEXT,
                    settore     TEXT,
                    citta       TEXT,
                    website     TEXT,
                    template    TEXT,
                    score       INTEGER,
                    oggetto     TEXT,
                    oggetto_b   TEXT,
                    oggetto_c   TEXT,
                    corpo       TEXT,
                    qa_score    REAL,
                    stato       TEXT,
                    data        TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Migrazione schema per DB esistenti (aggiunge colonne se mancano)
            for col, tipo in [
                ("oggetto_b", "TEXT"), ("oggetto_c", "TEXT"), ("corpo", "TEXT"),
                # Follow-up tracking
                ("f1_oggetto",          "TEXT"),
                ("f1_corpo",            "TEXT"),
                ("f1_inviata",          "TEXT"),   # ISO date
                ("f2_oggetto",          "TEXT"),
                ("f2_corpo",            "TEXT"),
                ("f2_inviata",          "TEXT"),   # ISO date
                # Reply tracking
                ("risposta_ricevuta",   "TEXT"),   # ISO date
                ("risposta_testo",      "TEXT"),
                ("risposta_oggetto",    "TEXT"),
                ("conversazione_stato", "TEXT"),   # attivo | risposto | in_conversazione | esaurito | chiamata_fissata
                # Settore calibrato (nicchia per follow-up writer)
                ("settore_calibrato",   "TEXT"),
            ]:
                try:
                    conn.execute(f"ALTER TABLE leads_contattati ADD COLUMN {col} {tipo}")
                except Exception:
                    pass  # Colonna già presente

    def _filtra_business_noti(self, businesses: list) -> list:
        """Rimuove business già nel DB per nome o website — PRIMA dell'estrazione email."""
        if not businesses:
            return []
        with sqlite3.connect(self.db_path) as conn:
            nomi_noti = {r[0].strip().lower() for r in
                         conn.execute("SELECT page_name FROM leads_contattati WHERE page_name IS NOT NULL").fetchall()}
            siti_noti = {r[0].strip().lower().rstrip('/') for r in
                         conn.execute("SELECT website FROM leads_contattati WHERE website IS NOT NULL AND website != ''").fetchall()}
        result = []
        for b in businesses:
            nome = (b.get("page_name") or "").strip().lower()
            sito = (b.get("website") or "").strip().lower().rstrip('/')
            if nome in nomi_noti or (sito and sito in siti_noti):
                continue
            result.append(b)
        return result

    def _filtra_nuovi(self, leads: list) -> list:
        if not leads:
            return []
        with sqlite3.connect(self.db_path) as conn:
            return [
                lead for lead in leads
                if lead.get("email") and not conn.execute(
                    "SELECT id FROM leads_contattati WHERE email = ?",
                    (lead["email"],)
                ).fetchone()
            ]

    def _registra_inviati(self, risultati: list):
        if not risultati:
            return
        with sqlite3.connect(self.db_path) as conn:
            for r in risultati:
                try:
                    conn.execute("""
                        INSERT OR IGNORE INTO leads_contattati
                        (page_id, email, page_name, settore, citta, website,
                         template, score, oggetto, oggetto_b, oggetto_c, corpo, qa_score, stato)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        r.get("page_id", ""),
                        r.get("email", ""),
                        r.get("page_name", ""),
                        r.get("settore", ""),
                        r.get("citta", ""),
                        r.get("website", ""),
                        r.get("template", ""),
                        r.get("score", 0),
                        r.get("oggetto", ""),
                        r.get("oggetto_b", ""),
                        r.get("oggetto_c", ""),
                        r.get("corpo", ""),
                        r.get("qa_score_media", 0.0),
                        r.get("stato", ""),
                    ))
                except sqlite3.IntegrityError:
                    pass

    def _salva_pronte_per_invio(self, approvate: list):
        """Salva le email approvate nel DB con stato='pronta' — verranno inviate dal run_invia."""
        if not approvate:
            return
        with sqlite3.connect(self.db_path) as conn:
            for r in approvate:
                try:
                    conn.execute("""
                        INSERT OR IGNORE INTO leads_contattati
                        (page_id, email, page_name, settore, citta, website,
                         template, score, oggetto, oggetto_b, oggetto_c, corpo, qa_score, stato)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pronta')
                    """, (
                        r.get("page_id", ""),
                        r.get("email", ""),
                        r.get("page_name", ""),
                        r.get("settore", ""),
                        r.get("citta", ""),
                        r.get("website", ""),
                        r.get("template", ""),
                        r.get("score", 0),
                        r.get("oggetto", ""),
                        r.get("oggetto_b", ""),
                        r.get("oggetto_c", ""),
                        r.get("corpo", ""),
                        r.get("qa_score_media", 0.0),
                    ))
                except sqlite3.IntegrityError:
                    pass
        print(f"[ORCHESTRATOR] {len(approvate)} email salvate nel DB come 'pronta'")

    def _carica_pronte_per_invio(self) -> list:
        """Carica dal DB le email pronte ma non ancora inviate."""
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute("""
                SELECT email, page_name, settore, citta, oggetto, oggetto_b, oggetto_c, corpo
                FROM leads_contattati
                WHERE stato = 'pronta'
                ORDER BY data ASC
            """).fetchall()
        return [
            {
                "email": r[0], "page_name": r[1], "settore": r[2],
                "citta": r[3], "oggetto": r[4], "oggetto_b": r[5],
                "oggetto_c": r[6], "corpo": r[7],
            }
            for r in rows
        ]

    def _marca_inviate(self, emails: list):
        """Aggiorna stato da 'pronta' a 'inviata' per le email spedite."""
        if not emails:
            return
        with sqlite3.connect(self.db_path) as conn:
            for r in emails:
                if r.get("stato") == "inviata":
                    conn.execute(
                        "UPDATE leads_contattati SET stato='inviata' WHERE email=?",
                        (r["email"],)
                    )

    def stats_database(self) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            totale = conn.execute("SELECT COUNT(*) FROM leads_contattati").fetchone()[0]
            inviati = conn.execute(
                "SELECT COUNT(*) FROM leads_contattati WHERE stato='inviata'"
            ).fetchone()[0]
        return {"totale_nel_db": totale, "email_inviate_storico": inviati}

    # ────────────────────────────────────────────────────────────────────────
    # Report qualità
    # ────────────────────────────────────────────────────────────────────────

    def _stampa_report_qualita(self, stats: dict):
        """Stampa il report di qualità del run."""
        print(f"\n{'─'*70}")
        print(f"  REPORT QUALITÀ")
        print(f"{'─'*70}")
        print(f"  Email scritte:              {stats.get('email_scritte', 0)}")
        print(f"  Passate al 1° tentativo:    {stats.get('qa_passed_first', 0)} "
              f"({stats.get('qa_pass_rate_first', 0):.0f}%)")
        print(f"  Revisionate e poi passate:  {stats.get('qa_passed_after_revision', 0)}")
        print(f"  Scartate (doppio fail QA):  {stats.get('qa_rejected', 0)}")
        print(f"  Bibbia score medio:         {stats.get('qa_score_medio', 0):.1f}/10  (soglia 7.0/10)")
        print(f"  Email in coda invio:        {stats.get('email_in_coda', 0)}")
        if stats.get("template_distribution"):
            td = stats["template_distribution"]
            print(f"  Prodotto-gancio:            Outreach={td.get('A',0)} Content={td.get('B',0)} SecondBrain={td.get('C',0)}")
        print(f"{'─'*70}")

    # ────────────────────────────────────────────────────────────────────────
    # Flusso principale
    # ────────────────────────────────────────────────────────────────────────

    def run(self, target: int = 300, anteprima: bool = False, solo_genera: bool = False, mock_leads: list = None) -> dict:
        """
        Esegue il flusso completo di outreach in 6 fasi coordinate.

        FASE 1 — TEAM 1 (Intelligence):  Scraping + Estrazione email + Qualificazione
        FASE 2 — TEAM 2 (Copy Knowledge): Briefing pack personalizzato per ogni lead
        FASE 3 — TEAM 3 (Strategy):      Strategy brief per ogni lead
        FASE 4 — TEAM 4 (Copy):          Scrittura email APSOC
        FASE 5 — TEAM 5 (QA):            3 check + revision loop
        FASE 6 — TEAM 6 (Delivery):      Invio Gmail SMTP

        Args:
            target:    numero di email da inviare (default 300)
            anteprima: se True, mostra le email senza inviarle
        """
        inizio = datetime.now()
        db_stats = self.stats_database()

        print(f"\n{'='*70}")
        print(f"  DIGITAL EMPIRE — OUTREACH AUTOMATICO v2.0")
        print(f"  {inizio.strftime('%Y-%m-%d %H:%M')} | Target: {target} email")
        print(f"  Lead già nel DB: {db_stats['totale_nel_db']} | "
              f"Storicamente inviati: {db_stats['email_inviate_storico']}")
        print(f"  Costo: $0 (tutto NVIDIA Nemotron via OpenRouter)")
        if anteprima:
            print(f"  MODALITÀ: ANTEPRIMA (nessuna email verrà inviata)")
        print(f"{'='*70}\n")

        qualita_stats = {
            "email_scritte": 0,
            "qa_passed_first": 0,
            "qa_passed_after_revision": 0,
            "qa_rejected": 0,
            "qa_score_medio": 0.0,
            "template_distribution": {"A": 0, "B": 0, "C": 0},
        }

        # ─── FASE 1: Intelligence ──────────────────────────────────────────
        print("╔══ FASE 1/6 — INTELLIGENCE ══════════════════════════════════╗")

        if mock_leads:
            businesses = []
            leads_con_email = mock_leads
            # Filtra lead già nel DB (già contattati o già pianificati) — stesso check del live scraping
            nuovi = self._filtra_nuovi(mock_leads)
            gia_presenti = len(mock_leads) - len(nuovi)
            if gia_presenti:
                print(f"║  MOCK MODE: {gia_presenti} lead già nel DB saltati (già contattati)")
            qualificati = nuovi
            da_processare = nuovi[:target]
            print(f"║  MOCK MODE: salto scraping, uso {len(da_processare)} lead nuovi (di {len(mock_leads)} nel CSV)")
            print(f"╚══ Lead mock pronti: {len(da_processare)}\n")
        else:
            # Scraping con catena di fallback automatica — include anche l'estrazione email.
            # Se uno scraper trova business ma 0 email (es. Maps Browser senza email dirette
            # e l'extractor fallisce), si passa automaticamente al prossimo scraper.
            # Conta lead già noti nel DB per calibrare il target scraping
            with sqlite3.connect(self.db_path) as _c:
                _noti = _c.execute("SELECT COUNT(*) FROM leads_contattati").fetchone()[0]
            # Più il DB cresce, più dobbiamo raschiare per trovare lead nuovi
            duplication_rate = max(3.0, 3.0 + _noti / 300)
            businesses    = []
            leads_con_email = []

            for scraper_nome, scraper_obj in self._scraper_chain:
                # Loop: continua a cercare finché non abbiamo abbastanza lead nuovi
                leads_nuovi_trovati = []
                tentativo = 0
                while len(leads_nuovi_trovati) < target:
                    tentativo += 1
                    mancanti = target - len(leads_nuovi_trovati)
                    target_questo_giro = int(mancanti * duplication_rate)
                    print(f"║  [{scraper_nome}] cerca {target_questo_giro} business (giro {tentativo}, mancano {mancanti} nuovi)...")
                    try:
                        raw = scraper_obj.run(target=target_questo_giro)
                    except RuntimeError as e:
                        err_str = str(e)
                        if "MONTHLY_LIMIT" in err_str:
                            warn(f"{scraper_nome}: limite mensile esaurito → fallback")
                        break
                    except Exception as e:
                        warn(f"{scraper_nome}: errore ({e}) → fallback")
                        break

                    if not raw:
                        warn(f"{scraper_nome}: 0 risultati → stop ricerca")
                        break

                    print(f"║  [{scraper_nome}] ✓ {len(raw)} business trovati")

                    # Filtro memoria PRIMA dell'estrazione email
                    raw_nuovi = self._filtra_business_noti(raw)
                    saltati = len(raw) - len(raw_nuovi)
                    print(f"║  Memoria: {saltati} già noti saltati → {len(raw_nuovi)} nuovi da estrarre")

                    if not raw_nuovi:
                        # Tutto già noto — se non riesce a trovare nuovi, esce
                        warn(f"{scraper_nome}: tutti i risultati già noti, stop")
                        break

                    leads_nuovi_trovati.extend(raw_nuovi)

                    # Se lo scraper ha restituito meno di quanto richiesto, non ha più risultati
                    if len(raw) < target_questo_giro * 0.5:
                        print(f"║  [{scraper_nome}] scraper esaurito (trovati {len(raw)} su {target_questo_giro} richiesti)")
                        break

                if not leads_nuovi_trovati:
                    continue  # Prova scraper successivo nella catena

                businesses = leads_nuovi_trovati
                raw = leads_nuovi_trovati

                # Estrazione email — bypass per scraper che forniscono email dirette
                con_email_diretta = [b for b in raw if b.get("email_diretta")]
                senza_email       = [b for b in raw if not b.get("email_diretta")]
                batch = []

                if con_email_diretta:
                    for lead in con_email_diretta:
                        lead["email"] = lead.pop("email_diretta")
                        batch.append(lead)
                    print(f"║  [{scraper_nome}] {len(con_email_diretta)} email dirette (no extraction)")

                if senza_email:
                    print(f"║  ExtractorAgent: estrae email da {len(senza_email)} siti...")
                    batch.extend(self.extractor.run(senza_email))

                if batch:
                    leads_con_email = batch
                    break  # Abbiamo email → usciamo dalla catena
                else:
                    warn(f"{scraper_nome}: 0 email trovate dopo estrazione → fallback al prossimo scraper")
                    continue

            if not leads_con_email:
                return self._report_errore(
                    "Nessuna email trovata da nessun scraper. "
                    "Maps Browser: email non visibili su Maps. "
                    "Apify: limite mensile o token non valido."
                )

            # Deduplicazione
            nuovi = self._filtra_nuovi(leads_con_email)
            print(f"║  Deduplicazione: {len(leads_con_email)} trovati → {len(nuovi)} nuovi")

            if not nuovi:
                print("║  Tutti i lead già contattati. Il sistema troverà nuovi lead domani.")
                return {"leads_trovati": len(businesses), "email_trovate": len(leads_con_email),
                        "lead_nuovi": 0, "email_inviate": 0}

            # Qualificazione
            print(f"║  QualifierAgent: scoring e template selection...")
            qualificati = self.qualifier.run(nuovi)

            if not qualificati:
                return self._report_errore("Nessun lead qualificato (score >= 40)")

            da_processare = qualificati[:target]
            scraping_done(len(businesses), len(leads_con_email), len(nuovi))
            print(f"╚══ Lead qualificati: {len(qualificati)} | Da processare: {len(da_processare)}\n")

            # ── CHECKPOINT: salva lead grezzi su CSV subito (prima di qualsiasi AI) ──
            import csv as _csv
            checkpoint_path = self.output_dir / "leads_checkpoint.csv"
            fields = ["page_name", "email", "settore", "citta", "website"]
            with open(checkpoint_path, "w", newline="", encoding="utf-8") as _f:
                _w = _csv.DictWriter(_f, fieldnames=fields, extrasaction="ignore")
                _w.writeheader()
                for _lead in qualificati:
                    _w.writerow({k: _lead.get(k, "") for k in fields})
            print(f"[CHECKPOINT] {len(qualificati)} lead salvati → {checkpoint_path.name} (backup sicuro)\n")

        # Distribuzione template
        for lead in da_processare:
            t = lead.get("template", "A")
            if t in qualita_stats["template_distribution"]:
                qualita_stats["template_distribution"][t] += 1

        import json as _json_bk

        def _email_set(lst):
            return {e.get("email", "").strip().lower() for e in lst if e.get("email")}

        def _load_phase_bk(path, cur_list, label):
            """Carica backup fase se esiste e le email corrispondono ai lead correnti."""
            if not path.exists():
                return None
            try:
                data = _json_bk.loads(path.read_text(encoding="utf-8"))
                if data and _email_set(data) == _email_set(cur_list):
                    print(f"║  [RECOVERY] {len(data)} lead caricati dal backup — {label} saltato!")
                    return data
            except Exception as _e:
                print(f"[RECOVERY] Backup {label} non leggibile ({_e}) — rigenero")
            return None

        _research_bk  = self.output_dir / "leads_post_research.json"
        _copykn_bk    = self.output_dir / "leads_post_copykn.json"
        _strategy_bk  = self.output_dir / "leads_post_strategy.json"

        # ─── FASE 1.5: RESEARCH SITO (no AI, puro scraping) ──────────────
        print("╔══ FASE 1.5 — RESEARCH SITO (no AI) ════════════════════════╗")
        _rec = _load_phase_bk(_research_bk, da_processare, "ResearchAgent")
        if _rec is not None:
            da_processare = _rec
        else:
            con_sito = sum(1 for l in da_processare if l.get("website"))
            print(f"║  ResearchAgent: visita siti di {con_sito}/{len(da_processare)} lead con website")
            da_processare = self.research.run(da_processare)
            _research_bk.write_text(_json_bk.dumps(da_processare, ensure_ascii=False), encoding="utf-8")
        n_ok = sum(1 for l in da_processare if l.get("website_intelligence", {}).get("available"))
        print(f"╚══ Siti analizzati: {n_ok} | Dati reali pronti per il Writer\n")

        # ─── FASE 2: Copy Knowledge ────────────────────────────────────────
        print("╔══ FASE 2/6 — COPY KNOWLEDGE ════════════════════════════════╗")
        _rec = _load_phase_bk(_copykn_bk, da_processare, "CopyKnowledgeAgent")
        if _rec is not None:
            leads_con_pack = _rec
        else:
            print(f"║  CopyKnowledgeAgent: preparo briefing pack per {len(da_processare)} lead...")
            leads_con_pack = self.copy_knowledge.run(da_processare)
            _copykn_bk.write_text(_json_bk.dumps(leads_con_pack, ensure_ascii=False), encoding="utf-8")
        print(f"╚══ Briefing pack pronti: {len(leads_con_pack)}\n")

        # ─── FASE 3: Strategy ──────────────────────────────────────────────
        print("╔══ FASE 3/6 — STRATEGY ══════════════════════════════════════╗")
        _rec = _load_phase_bk(_strategy_bk, leads_con_pack, "StrategistAgent")
        if _rec is not None:
            leads_con_brief = _rec
        else:
            print(f"║  StrategistAgent: genero hook brief per {len(leads_con_pack)} lead...")
            leads_con_brief = self.strategist.run(leads_con_pack)
            _strategy_bk.write_text(_json_bk.dumps(leads_con_brief, ensure_ascii=False), encoding="utf-8")
        print(f"╚══ Strategy brief pronti: {len(leads_con_brief)}\n")

        # ─── FASE 4: Copy ──────────────────────────────────────────────────
        _writer_bk = self.output_dir / "emails_post_writer.json"
        emails_scritte = None

        # Recovery crash: se esiste backup con le stesse email, salta Writer
        if _writer_bk.exists():
            try:
                _bk_data = _json_bk.loads(_writer_bk.read_text(encoding="utf-8"))
                _bk_set  = {e.get("email", "").strip().lower() for e in _bk_data}
                _cur_set = {l.get("email", "").strip().lower() for l in leads_con_brief}
                if _bk_set == _cur_set and len(_bk_data) > 0:
                    emails_scritte = _bk_data
                    print(f"\n╔══ FASE 4/6 — COPY (RECOVERY DA BACKUP) ════════════════════╗")
                    print(f"║  ✓ {len(emails_scritte)} email caricate dal backup — Writer saltato!")
                    print(f"╚══ Email scritte (da backup): {len(emails_scritte)}\n")
            except Exception as _e:
                print(f"[RECOVERY] Backup post-Writer non leggibile ({_e}) — riscrivo da zero")

        if emails_scritte is None:
            email_header(len(leads_con_brief))
            emails_scritte = self.writer.run(leads_con_brief)
            if emails_scritte:
                _writer_bk.write_text(
                    _json_bk.dumps(emails_scritte, ensure_ascii=False), encoding="utf-8"
                )
                print(f"[BACKUP] {len(emails_scritte)} email salvate → {_writer_bk.name} (crash recovery)\n")

        qualita_stats["email_scritte"] = len(emails_scritte) if emails_scritte else 0

        if not emails_scritte:
            return self._report_errore("Nessuna email generata — verifica OPENROUTER_API_KEY")

        print(f"╚══ Email scritte: {len(emails_scritte)}\n")

        # ─── FASE 5: BIBBIA TEAM QA ────────────────────────────────────────
        # 3 agenti AI in parallelo leggono la Bibbia Outreach e valutano ogni email.
        # Sostituisce il vecchio HumanizerAgent (punteggi hardcoded 8/10).
        print("╔══ FASE 5/6 — BIBBIA TEAM QA (3 checker AI paralleli) ═══════╗")

        _bibbia_bk = self.output_dir / "emails_post_bibbia.json"

        # Recovery crash: se esiste backup post-QA completo, salta BibbiaTeam + revision
        _bibbia_recovery = False
        approvate = []
        if _bibbia_bk.exists():
            try:
                _bib_data = _json_bk.loads(_bibbia_bk.read_text(encoding="utf-8"))
                if _bib_data:
                    approvate = _bib_data
                    _bibbia_recovery = True
                    print(f"║  [RECOVERY] {len(approvate)} email caricate dal backup — BibbiaTeam saltato!")
                    print(f"╚══ Email approvate QA (da backup): {len(approvate)}\n")
                    qualita_stats["qa_passed_first"] = len(approvate)
                    qualita_stats["email_in_coda"] = len(approvate)
            except Exception as _e:
                print(f"[RECOVERY] Backup BibbiaTeam non leggibile ({_e}) — rifaccio QA")

        if not _bibbia_recovery:
            # Checkpoint incrementale: salva dopo ogni email — ripresa esatta su restart
            _bibbia_cp   = self.output_dir / "bibbia_checkpoint.jsonl"
            _already_ok  = []   # approvate da checkpoint
            _already_rev = []   # da rivedere da checkpoint
            _skip_emails = set()

            if _bibbia_cp.exists():
                for _line in _bibbia_cp.read_text(encoding="utf-8").splitlines():
                    try:
                        _item = _json_bk.loads(_line)
                        _skip_emails.add(_item["email"].strip().lower())
                        if _item["passed"]:
                            _already_ok.append(_item["data"])
                        else:
                            _already_rev.append(_item["data"])
                    except Exception:
                        pass
                if _skip_emails:
                    print(f"║  [RECOVERY] Bibbia checkpoint: {len(_skip_emails)} email già valutate — riprendo da {len(_skip_emails)+1}/{len(emails_scritte)}")

            _rimanenti = [e for e in emails_scritte
                          if e.get("email", "").strip().lower() not in _skip_emails]

            # Primo check Bibbia — email per email con salvataggio checkpoint
            print(f"║  Check Bibbia su {len(_rimanenti)} email (Umano + Struttura + Conversione)...")
            _nuove_ok, _nuove_rev = [], []
            for _em in _rimanenti:
                _app_1, _rev_1 = self.bibbia_team.run([_em])
                _passed = bool(_app_1)
                _data   = _app_1[0] if _app_1 else (_rev_1[0] if _rev_1 else _em)
                if _passed:
                    _nuove_ok.append(_data)
                else:
                    _nuove_rev.append(_data)
                with open(_bibbia_cp, "a", encoding="utf-8") as _cpf:
                    _cpf.write(_json_bk.dumps(
                        {"email": _em.get("email", ""), "passed": _passed, "data": _data},
                        ensure_ascii=False
                    ) + "\n")

            approvate   = _already_ok  + _nuove_ok
            da_rivedere = _already_rev + _nuove_rev
            qualita_stats["qa_passed_first"] = len(approvate)

            # Revision loop (max 1 retry per email rifiutata)
            if da_rivedere:
                print(f"║  Revision loop: {len(da_rivedere)} email rifiutate → Writer riscrive con feedback Bibbia...")
                email_revisionate = []
                for lead_con_feedback in da_rivedere:
                    if not lead_con_feedback.get("bibbia_hard_block"):
                        rivista = self.writer.revise(lead_con_feedback)
                        if rivista:
                            email_revisionate.append(rivista)

                if email_revisionate:
                    print(f"║  Secondo check Bibbia su {len(email_revisionate)} email revisionate...")
                    approvate_rev, scartate = self.bibbia_team.run(email_revisionate)
                    approvate.extend(approvate_rev)
                    qualita_stats["qa_passed_after_revision"] = len(approvate_rev)
                    qualita_stats["qa_rejected"] = len(scartate) + sum(
                        1 for l in da_rivedere if l.get("bibbia_hard_block")
                    )
                    if scartate:
                        print(f"║  ⚠ Scartate dopo revisione: {len(scartate)} email")
                else:
                    qualita_stats["qa_rejected"] = len(da_rivedere)

            # Salva backup post-QA (recovery crash durante Delivery)
            if approvate:
                _bibbia_bk.write_text(
                    _json_bk.dumps(approvate, ensure_ascii=False), encoding="utf-8"
                )
                print(f"[BACKUP] {len(approvate)} email approvate → {_bibbia_bk.name} (crash recovery)\n")

        # Calcola score medio e pass rate (validi sia per live che per recovery)
        scores = [
            e.get("bibbia_score_media", e.get("qa_score_media", 0))
            for e in approvate
            if e.get("bibbia_score_media") or e.get("qa_score_media")
        ]
        qualita_stats["qa_score_medio"] = sum(scores) / len(scores) if scores else 0.0
        qualita_stats["email_in_coda"] = len(approvate)
        if qualita_stats["email_scritte"] > 0:
            qualita_stats["qa_pass_rate_first"] = (
                qualita_stats["qa_passed_first"] / qualita_stats["email_scritte"] * 100
            )

        # Stampa report qualità e check finale
        print(f"╚══ Email approvate QA: {len(approvate)} | Scartate: {qualita_stats['qa_rejected']}\n")
        self._stampa_report_qualita(qualita_stats)

        if not approvate:
            return self._report_errore("Nessuna email superato il QA — controlla la qualità del prompt")

        # ─── FASE 6: Delivery ──────────────────────────────────────────────
        print(f"\n╔══ FASE 6/6 — DELIVERY ══════════════════════════════════════╗")

        if solo_genera:
            # Modalità GENERA: salva nel DB, non inviare ora
            self._salva_pronte_per_invio(approvate)
            print(f"║  MODALITÀ GENERA: email salvate nel DB — usa 'run.py --mode invia'")
            print(f"║  per inviarle durante l'orario business (lun-ven, 9:00-18:00)")
            print(f"╚══ Email in coda: {len(approvate)}\n")
            inviati = 0
        elif anteprima:
            risultati = self.sender.run(approvate, anteprima=True, output_dir=str(self.output_dir))
            inviati = 0
            print(f"╚══ Anteprima completata\n")
        else:
            risultati = self.sender.run(approvate, anteprima=False, output_dir=str(self.output_dir))
            if risultati:
                self._registra_inviati(risultati)
            inviati = sum(1 for r in risultati if r.get("stato") == "inviata") if risultati else 0
            print(f"╚══ Email inviate: {inviati}\n")

        # ─── REPORT FINALE ─────────────────────────────────────────────────
        fine = datetime.now()
        durata = int((fine - inizio).total_seconds())

        stats = {
            "data": inizio.strftime("%Y-%m-%d %H:%M"),
            "durata_minuti": durata // 60,
            "leads_trovati": len(businesses),
            "email_trovate": len(leads_con_email),
            "lead_nuovi": len(nuovi),
            "lead_qualificati": len(qualificati),
            "email_scritte": qualita_stats["email_scritte"],
            "qa_passed_first": qualita_stats["qa_passed_first"],
            "qa_passed_after_revision": qualita_stats["qa_passed_after_revision"],
            "qa_rejected": qualita_stats["qa_rejected"],
            "qa_score_medio": qualita_stats["qa_score_medio"],
            "email_approvate_qa": len(approvate),
            "email_inviate": inviati,
            "costo_api": "$0.00 (NVIDIA Nemotron gratuito)",
            "template_distribution": qualita_stats["template_distribution"],
        }

        # Pulizia backup (run completato con successo)
        _bibbia_cp_cleanup = self.output_dir / "bibbia_checkpoint.jsonl"
        for _bk in [_research_bk, _copykn_bk, _strategy_bk, _writer_bk, _bibbia_bk, _bibbia_cp_cleanup]:
            try:
                if _bk.exists():
                    _bk.unlink()
            except Exception:
                pass

        print(f"\n{'='*70}")
        print(f"  COMPLETATO — {fine.strftime('%H:%M')} (durata: {durata // 60}min)")
        print(f"{'='*70}")
        print(f"  Business trovati:        {stats['leads_trovati']}")
        print(f"  Email estratte:          {stats['email_trovate']}")
        print(f"  Lead nuovi (dedup):      {stats['lead_nuovi']}")
        print(f"  Lead qualificati:        {stats['lead_qualificati']}")
        print(f"  Email scritte:           {stats['email_scritte']}")
        print(f"  QA pass (1° tentativo):  {stats['qa_passed_first']}")
        print(f"  QA pass (dopo revisione):{stats['qa_passed_after_revision']}")
        print(f"  Email scartate QA:       {stats['qa_rejected']}")
        print(f"  Bibbia score medio:      {stats['qa_score_medio']:.1f}/10  (soglia: 7.0 tutti i checker)")
        print(f"  Email inviate:           {stats['email_inviate']}")
        print(f"  Costo API:               {stats['costo_api']}")
        print(f"{'='*70}\n")

        return stats

    def run_invia(self) -> dict:
        """
        Modalità INVIA: legge le email 'pronte' dal DB e le invia durante l'orario business.
        Da chiamare con: python run.py --mode invia
        Orario consigliato: lun-ven ore 09:00 (Task Scheduler Windows)
        """
        from datetime import datetime as dt
        ora = dt.now()
        giorno = ora.weekday()  # 0=lun ... 6=dom
        ora_h = ora.hour

        print(f"\n{'='*70}")
        print(f"  DIGITAL EMPIRE — MODALITÀ INVIA")
        print(f"  {ora.strftime('%Y-%m-%d %H:%M')} ({['Lun','Mar','Mer','Gio','Ven','Sab','Dom'][giorno]})")
        print(f"{'='*70}\n")

        # Check orario business: lun-ven 8:00-19:00
        if giorno >= 5:
            print("[INVIA] Oggi è weekend — le cold email non si inviano nel weekend.")
            print("        Configura Task Scheduler solo per lun-ven.")
            return {"errore": "weekend", "email_inviate": 0}

        if not (8 <= ora_h < 19):
            print(f"[INVIA] Orario fuori business ({ora_h}:00). Orario consentito: 8:00-19:00 lun-ven.")
            print("        Configura Task Scheduler alle 09:00.")
            return {"errore": "fuori orario", "email_inviate": 0}

        pronte = self._carica_pronte_per_invio()
        if not pronte:
            print("[INVIA] Nessuna email in coda. Esegui prima: python run.py --mode genera")
            return {"email_pronte": 0, "email_inviate": 0}

        print(f"[INVIA] {len(pronte)} email in coda da inviare...")
        risultati = self.sender.run(pronte, anteprima=False, output_dir=str(self.output_dir))
        self._marca_inviate(risultati)

        inviati = sum(1 for r in risultati if r.get("stato") == "inviata") if risultati else 0
        print(f"\n[INVIA] Completato: {inviati}/{len(pronte)} email inviate.")
        return {"email_pronte": len(pronte), "email_inviate": inviati}

    def _report_errore(self, messaggio: str) -> dict:
        print(f"\n[ORCHESTRATOR] ERRORE: {messaggio}")
        return {"errore": messaggio, "email_inviate": 0}
