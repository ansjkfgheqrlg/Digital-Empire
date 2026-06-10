"""
WF-D — Generazione Bozze Email di Outreach

Legge i lead qualificati dai CSV locali in output/, genera email personalizzate
usando Claude AI e salva le bozze in bozze_email/ per revisione umana.
NON invia mai email automaticamente.

Uso:
    python implementation/draft_emails.py --batch
    python implementation/draft_emails.py --id NS-MI-20250115143022
    python implementation/draft_emails.py --batch --max 10

Input:
    --id: ID specifico del lead da processare
    --batch: Processa tutti i lead PRONTO_OUTREACH=Sì senza bozza ancora generata
    --max: Max email da generare in batch (default: 20)

Output:
    File .txt in bozze_email/YYYY-MM-DD/[ID_LEAD]_bozza.txt
    CSV aggiornato: colonne BOZZA_GENERATA, DATA_BOZZA, STATO_OUTREACH
"""

import os
import sys
import csv
import argparse
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger

load_dotenv()

try:
    import anthropic
    CLAUDE_DISPONIBILE = True
except ImportError:
    CLAUDE_DISPONIBILE = False


FIRMA_DEFAULT = """
[Il tuo nome]
Digital Empire
[Il tuo sito / LinkedIn]
"""

CARTELLA_BOZZE = "bozze_email"
CARTELLA_OUTPUT = "output"

# ---------------------------------------------------------------------------
# Brand Voice Guide — Digital Empire (v2.0)
# Integrato nei prompt per garantire coerenza di tono in ogni email generata.
# ---------------------------------------------------------------------------

BRAND_VOICE = """
IDENTITÀ BRAND: Digital Empire — CRO/Conversion Performance Agency
USP (one-liner da usare nel closing): "Lavoriamo a sprint: implementiamo e testiamo,
e la parte variabile la paghi solo sull'uplift misurato."

TONO: consulente performance-first. Diretto, specifico, misurabile. Empatico sul pain,
chirurgico sulla soluzione. Mai venditore, mai supplice.
Stile: "ho osservato X → impatta Y → ecco cosa farei io"
Rapporto: peer-to-peer, da professionista a professionista.

STRUTTURA APSOC (rispetta sempre questa sequenza):
1. ATTENZIONE: insight specifico e osservabile (non generico)
2. PROBLEMA: impatto economico concreto (spreco budget / clienti persi / conversioni mancate)
3. SOLUZIONE: 1-2 test o fix concreti con ipotesi misurabile
4. OBIEZIONI: anticipare "forse avete già provato" / "non vogliamo rifare tutto"
5. CTA: micro-step (call 15 min O invio di 3 idee scritte)

OPENING — USA SOLO questi pattern:
✅ "Ho cercato [categoria] a [città] e ho notato che..."
✅ "Ho visto i vostri annunci su Facebook e c'è un punto in cui state perdendo conversioni: ..."
✅ "Stavo confrontando voi con altri [settore] a [città] e ho notato una differenza misurabile: ..."
✅ "Una cosa mi ha colpito: avete [traffico/ads/recensioni], ma [problema specifico] ..."
❌ MAI iniziare con: "Mi chiamo...", "Spero che...", "So che sei impegnato..."

CLOSING — USA SOLO questi pattern:
✅ "Ha senso una call di 15 minuti per stimare uplift e priorità?"
✅ "Vuoi che ti mandi 3 test rapidi specifici per la vostra pagina?"
✅ "Hai 10 minuti questa settimana o preferisci un audit sintetico via email?"
❌ MAI: "Rimango in attesa...", "Non esitare...", "Cordiali saluti"

VOCABOLARIO APPROVATO: opportunità, attrito, drop-off, baseline, uplift, ipotesi,
test A/B, priorità, impatto, evidenza, percorso cliente, tracciamento, sprint, conversione.
VOCABOLARIO VIETATO: garantito, segreto, magico, rivoluzionario, esclusivo,
"posti limitati", "raddoppio garantito".

PAIN POINTS B2B AMMESSI (scegli il più pertinente):
- "State pagando traffico che non monetizzate"
- "Avete domanda, ma la pagina non la cattura"
- "Avete click, ma non avete fiducia"
- "Ogni ricerca online senza risultato = cliente che va dal competitor"

REGOLE ASSOLUTE:
- Max 150 parole nel corpo email
- Questo è il PRIMO contatto (problem aware): ZERO offerta diretta, ZERO pricing
- 1 sola CTA finale, non più di una
- Non deve sembrare automatizzata: deve sembrare scritta da una persona specifica
- Proponi 3 varianti di oggetto, poi scrivi il corpo
"""


# ---------------------------------------------------------------------------
# Lettura / aggiornamento CSV
# ---------------------------------------------------------------------------

def _carica_tutti_i_lead() -> list:
    """
    Carica tutti i lead dai CSV in output/.

    Returns:
        Lista di dict con chiave aggiuntiva _csv_path e _intestazioni
    """
    lead = []
    output_dir = Path(CARTELLA_OUTPUT)
    if not output_dir.exists():
        return lead

    for csv_file in sorted(output_dir.glob("*.csv")):
        try:
            with open(csv_file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                intestazioni = reader.fieldnames or []
                for row in reader:
                    row["_csv_path"] = str(csv_file)
                    row["_intestazioni"] = intestazioni
                    lead.append(row)
        except Exception:
            pass

    return lead


def _aggiorna_riga_csv(csv_path: str, id_lead: str, aggiornamenti: dict) -> None:
    """
    Aggiorna una riga nel CSV cercando per ID_LEAD.

    Args:
        csv_path: Path del file CSV
        id_lead: ID del lead da aggiornare
        aggiornamenti: Dict con le colonne da aggiornare
    """
    path = Path(csv_path)
    if not path.exists():
        return

    righe = []
    intestazioni = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        intestazioni = reader.fieldnames or []
        for row in reader:
            if row.get("ID_LEAD") == id_lead:
                row.update(aggiornamenti)
            righe.append(row)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=intestazioni)
        writer.writeheader()
        writer.writerows(righe)


# ---------------------------------------------------------------------------
# Costruzione prompt Claude
# ---------------------------------------------------------------------------

def costruisci_prompt_no_sito(riga: dict, firma: str) -> str:
    """
    Prompt APSOC per lead senza sito web.
    Questo è il PRIMO contatto (problem aware): osservazione specifica + impatto,
    zero offerta diretta.
    """
    nome = riga.get("NOME_BUSINESS", "questa attività")
    categoria = riga.get("CATEGORIA", "attività")
    citta = riga.get("CITTÀ", "")
    n_recensioni = riga.get("N_RECENSIONI", "")
    rating = riga.get("RATING_GOOGLE", "")
    note = riga.get("NOTE", "")

    info_business = f"""
- Nome: {nome}
- Categoria: {categoria}
- Città: {citta}
- Recensioni Google: {n_recensioni} (rating {rating}/5)
- Note: {note}
""".strip()

    return f"""Sei il copywriter di Digital Empire, una CRO/Conversion Performance Agency.

{BRAND_VOICE}

---

CONTESTO SPECIFICO — LEAD SENZA SITO WEB:
Questo business locale non ha un sito web, ma è presente su Google Maps con recensioni.
Il pain core: ogni persona che cerca "{categoria} a {citta}" online non trova nulla di loro.
Ogni ricerca senza risultato = potenziale cliente che va dal competitor che ha un sito.

DATI DEL BUSINESS:
{info_business}

ISTRUZIONI SPECIFICHE PER QUESTO TIPO DI LEAD:
- Apertura: evidenzia che li hai cercati online e non hai trovato niente (o quasi)
- Problema: quantifica l'opportunità persa in termini di ricerche locali mensili
  (es. "ogni mese ci sono centinaia di ricerche 'dentista Milano' — senza sito non captate nulla")
- Soluzione (max 1-2 frasi): landing page minima ottimizzata, non un sito enorme
- NON menzionare la nostra agenzia per nome nel corpo — solo nella firma
- Usare le loro recensioni positive come segnale che hanno già un'ottima reputazione
  da digitalizzare

FIRMA DA USARE:
{firma}

FORMATO OUTPUT (rispetta esattamente questo formato, nient'altro):
OGGETTO 1: [oggetto breve e specifico, max 8 parole]
OGGETTO 2: [variante curiosità/domanda]
OGGETTO 3: [variante benefit-focused]
---
CORPO EMAIL:
[testo, inizia direttamente con l'opening — niente "Gentile", niente "Mi chiamo"]
"""


def costruisci_prompt_funnel_scarso(riga: dict, firma: str) -> str:
    """
    Prompt APSOC per lead con funnel scarso (ads attivi, landing debole).
    Questo è il PRIMO contatto: osservazione sugli ads + landing, zero offerta.
    """
    nome = riga.get("NOME_PAGINA", "questa attività")
    settore = riga.get("SETTORE", "settore")
    citta = riga.get("CITTÀ", "")
    score_funnel = riga.get("SCORE_FUNNEL", "basso")
    problemi = riga.get("DETTAGLIO_SCORE", "")
    n_ads = riga.get("N_ADS_ATTIVI", "")

    # Converti problemi tecnici in linguaggio business leggibile
    mappa_problemi_human = {
        "manca headline chiaro": "la headline non comunica il valore in modo immediato",
        "nessun form di contatto": "non c'è un modo diretto per il visitatore di contattarvi o lasciare i dati",
        "nessuna call-to-action": "manca una CTA chiara — il visitatore non sa cosa fare dopo",
        "nessuna testimonianza": "manca social proof (recensioni/testimonianze) che riduca il rischio percepito",
        "nessun telefono visibile": "il numero di telefono non è visibile sopra la piega",
        "nessuna garanzia/policy": "manca un elemento che riduca il rischio percepito dell'acquisto",
        "nessun Pixel Facebook": "non state tracciando le conversioni degli ads — stimate il ROI al buio",
        "nessun Analytics": "non c'è tracciamento — non sapete dove i visitatori abbandonano",
    }

    problemi_lista = []
    for p in problemi.split(","):
        p = p.strip()
        problemi_lista.append(mappa_problemi_human.get(p, p))

    problemi_leggibili = "\n  - ".join(problemi_lista) if problemi_lista else "struttura del funnel migliorabile"

    info_business = f"""
- Nome: {nome}
- Settore: {settore}
- Città: {citta}
- Ads attivi su Facebook/Instagram: {n_ads}
- Score funnel (0=pessimo, 100=ottimo): {score_funnel}/100
- Attriti rilevati sulla landing page:
  - {problemi_leggibili}
""".strip()

    return f"""Sei il copywriter di Digital Empire, una CRO/Conversion Performance Agency.

{BRAND_VOICE}

---

CONTESTO SPECIFICO — LEAD CON ADS ATTIVI E FUNNEL SCARSO:
Questo business sta già spendendo in advertising su Facebook/Instagram,
ma la loro landing page ha attriti che abbassano il tasso di conversione.
Il pain core: stanno pagando per traffico che non monetizzano.
Ogni euro di ads che finisce su una pagina con attriti = budget sprecato.

DATI DEL BUSINESS:
{info_business}

ISTRUZIONI SPECIFICHE PER QUESTO TIPO DI LEAD:
- Apertura: mostra di aver visto i loro ads E la landing page (interesse genuino, non spam)
- Non elencare tutti gli attriti come una critica — scegli MAX 1-2 e trattali come "opportunità"
- Il frame giusto: "state già investendo bene in ads, c'è un'opportunità facile da recuperare"
- Sottolinea che non serve rifare tutto: bastano interventi chirurgici ad alto impatto
- Zero offerta diretta — closing con call 15 min o "ti mando 3 test specifici"

FIRMA DA USARE:
{firma}

FORMATO OUTPUT (rispetta esattamente questo formato, nient'altro):
OGGETTO 1: [oggetto breve e specifico, max 8 parole]
OGGETTO 2: [variante curiosità/domanda]
OGGETTO 3: [variante benefit-focused]
---
CORPO EMAIL:
[testo, inizia direttamente con l'opening — niente "Gentile", niente "Mi chiamo"]
"""


# ---------------------------------------------------------------------------
# Generazione email con Claude
# ---------------------------------------------------------------------------

def genera_email_con_claude(prompt: str, api_key: str, logger) -> str:
    """
    Genera l'email usando Claude API con retry automatico.

    Returns:
        Testo generato da Claude o stringa vuota in caso di errore
    """
    if not CLAUDE_DISPONIBILE:
        logger.error("anthropic non installato. Esegui: pip install anthropic")
        return ""

    client = anthropic.Anthropic(api_key=api_key)

    for tentativo in range(3):
        try:
            messaggio = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            return messaggio.content[0].text

        except anthropic.RateLimitError:
            attesa = 2 ** tentativo * 15  # 15, 30, 60 secondi
            logger.warning(f"Claude rate limit. Attendo {attesa}s (tentativo {tentativo + 1}/3)")
            time.sleep(attesa)

        except Exception as e:
            logger.error(f"Errore Claude API (tentativo {tentativo + 1}/3): {e}")
            if tentativo < 2:
                time.sleep(5)

    return ""


# ---------------------------------------------------------------------------
# Salvataggio bozza
# ---------------------------------------------------------------------------

def salva_bozza(id_lead: str, riga: dict, testo_generato: str, logger) -> str:
    """
    Salva la bozza email in un file .txt.

    Returns:
        Path del file salvato
    """
    oggi = datetime.now().strftime("%Y-%m-%d")
    cartella = Path(CARTELLA_BOZZE) / oggi
    cartella.mkdir(parents=True, exist_ok=True)

    # Gestisci versioni multiple (bozza, bozza_v2, ecc.)
    base_path = cartella / f"{id_lead}_bozza"
    percorso = Path(f"{base_path}.txt")
    versione = 1
    while percorso.exists():
        versione += 1
        percorso = Path(f"{base_path}_v{versione}.txt")

    nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA", "?")
    email_dest = riga.get("EMAIL", "")
    score = riga.get("SCORE_PRIORITÀ", "")

    intestazione = f"""# BOZZA EMAIL — {id_lead}
# Generata: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# Business: {nome}
# Città: {riga.get("CITTÀ", "")}
# Tipo lead: {"senza_sito" if id_lead.startswith("NS-") else "ads_funnel_scarso"}
# Score priorità: {score}
# Email destinatario: {email_dest}
# ============================================

"""

    istruzioni = """
# ============================================
# ISTRUZIONI PER L'OPERATORE:
# 1. Rivedi il testo sopra e personalizza dove necessario
# 2. Scegli uno dei tre oggetti proposti (o scrivine uno tuo)
# 3. Mostra anteprima:
#    python implementation/send_emails.py --id """ + id_lead + """ --anteprima
# 4. Invia (richiede conferma interattiva):
#    python implementation/send_emails.py --id """ + id_lead + """
# 5. Aggiorna lo stato:
#    python implementation/track_outreach.py --id """ + id_lead + """ --stato inviato
# ============================================
"""

    with open(percorso, "w", encoding="utf-8") as f:
        f.write(intestazione + testo_generato + istruzioni)

    logger.info(f"Bozza salvata: {percorso}")
    return str(percorso)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Genera bozze email personalizzate per i lead qualificati"
    )
    parser.add_argument("--id", help="ID specifico del lead da processare")
    parser.add_argument("--batch", action="store_true", help="Processa tutti i lead pronti")
    parser.add_argument("--max", type=int, default=20, help="Max email in batch (default: 20)")
    args = parser.parse_args()

    if not args.id and not args.batch:
        print("Errore: specifica --id [ID_LEAD] oppure --batch")
        print("Usa --help per maggiori informazioni")
        sys.exit(1)

    logger = get_logger("WF-D", "email_drafts")
    logger.info(f"START — Modalità: {'batch (max ' + str(args.max) + ')' if args.batch else 'singolo: ' + args.id}")

    # Credenziali
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key.startswith("LA_TUA"):
        logger.error("ERRORE: ANTHROPIC_API_KEY non configurata nel .env")
        sys.exit(1)

    firma = os.getenv("MITTENTE_FIRMA", FIRMA_DEFAULT)

    # Carica lead dai CSV
    tutti_lead = _carica_tutti_i_lead()

    if not tutti_lead:
        logger.error(f"Nessun CSV trovato in {CARTELLA_OUTPUT}/. Esegui prima WF-A o WF-B.")
        sys.exit(1)

    # Filtra lead da processare
    lead_da_processare = []

    for riga in tutti_lead:
        id_lead = riga.get("ID_LEAD", "")
        if not id_lead:
            continue

        if args.id:
            if id_lead == args.id:
                lead_da_processare.append(riga)
            continue

        if args.batch:
            if riga.get("PRONTO_OUTREACH") not in ("Sì", "Si"):
                continue
            if riga.get("BOZZA_GENERATA") in ("Sì", "Si"):
                continue
            lead_da_processare.append(riga)

    if not lead_da_processare:
        logger.info("Nessun lead da processare (tutti già con bozza o nessuno pronto)")
        sys.exit(0)

    # Limita batch
    if args.batch:
        lead_da_processare = lead_da_processare[:args.max]

    logger.info(f"Lead da processare: {len(lead_da_processare)}")

    # Genera email
    n_ok = 0
    n_errori = 0

    for riga in lead_da_processare:
        id_lead = riga["ID_LEAD"]
        nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA", "?")

        # Scegli template in base al tipo di lead
        if id_lead.startswith("NS-"):
            prompt = costruisci_prompt_no_sito(riga, firma)
        else:
            prompt = costruisci_prompt_funnel_scarso(riga, firma)

        # Genera con Claude
        logger.info(f"Generando email per: {nome} ({id_lead})")
        testo = genera_email_con_claude(prompt, api_key, logger)

        if not testo:
            logger.warning(f"Generazione fallita per {id_lead}: {nome}")
            n_errori += 1
            continue

        # Salva bozza
        percorso = salva_bozza(id_lead, riga, testo, logger)

        # Aggiorna CSV
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _aggiorna_riga_csv(
            riga["_csv_path"],
            id_lead,
            {
                "BOZZA_GENERATA": "Sì",
                "DATA_BOZZA": timestamp,
                "STATO_OUTREACH": "bozza_pronta",
            }
        )

        logger.info(f"OK: {nome} → {percorso}")
        n_ok += 1

        # Pausa tra richieste Claude
        if len(lead_da_processare) > 1:
            time.sleep(2)

    logger.info(f"END — Bozze generate: {n_ok} | Errori: {n_errori}")
    logger.info(f"Bozze salvate in: {CARTELLA_BOZZE}/{datetime.now().strftime('%Y-%m-%d')}/")


if __name__ == "__main__":
    main()
