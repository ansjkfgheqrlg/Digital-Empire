"""
Genera email 100% personalizzate per ogni lead — framework APSOC+V.
Input:  leads_nuove_nicchie.csv  (37 lead unici)
Output: emails_ready.json

Ogni email usa i mini-dettagli specifici del lead:
sito datato, trovato su Instagram, solo telefono, solo WhatsApp, trovato in PDF, ecc.
Questi dettagli entrano nell'apertura [A] e nell'oggetto — mai frasi generiche.

Run:
  python prepare_emails.py
  python prepare_emails.py --resume   # salta lead già pronti in emails_ready.json
"""
import csv
import json
import os
import re
import sys
import time
from pathlib import Path

# Carica .env senza dipendenza da python-dotenv
_env = Path(__file__).parent / ".env"
if _env.exists():
    for _line in _env.read_text(encoding="utf-8").splitlines():
        if "=" in _line and not _line.startswith("#") and not _line.startswith(" "):
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

from agents.writer import WRITER_SYSTEM_PROMPT, EmailWriterAgent
from agents.ai_client import build_rotation, call_ai

CSV_PATH    = "leads_nuove_nicchie.csv"
OUTPUT_PATH = "emails_ready.json"

_LINK_CTA = "https://agency-empire-landing.vercel.app"

def _aggiungi_cta(corpo: str) -> str:
    # DELIVERABILITY: link VIETATO nella prima email fredda (attiva filtri antispam).
    # Il link va SOLO nel follow-up #2 (giorno 7).
    # Questa funzione ora è un no-op per la prima email.
    # Lasciata per compatibilità con gli script che la chiamano.
    return corpo

# ─── CLI args (opzionali, per backward compatibility) ─────────────────────────
_argv = sys.argv[1:]
for _i in range(len(_argv)):
    if _argv[_i] == "--csv" and _i + 1 < len(_argv):
        CSV_PATH = _argv[_i + 1]
    elif _argv[_i] == "--output" and _i + 1 < len(_argv):
        OUTPUT_PATH = _argv[_i + 1]

# ─── Mappatura settore → parola clienti/pazienti ─────────────────────────────

_PAROLA = {
    "fisioterapista": "pazienti",
    "avvocato":       "clienti",
    "psicologo":      "pazienti",
    "commercialista": "clienti",
    "palestra":       "iscritti",
    "yoga":           "iscritti",
    "fitness":        "iscritti",
    "crossfit":       "iscritti",
    "estetica":       "clienti",
    "spa":            "clienti",
    "medico":         "pazienti",
    "dentista":       "pazienti",
    "chirurgia":      "pazienti",
    "clinica":        "pazienti",
}

_VALORE = {
    "fisioterapista": (
        "Il 65% delle prenotazioni fisioterapia avviene dopo le 19, quando gli studi sono "
        "chiusi. Un form di prenotazione online cattura quei pazienti automaticamente, "
        "senza dover rispondere al telefono fuori orario."
    ),
    "avvocato": (
        "Un intake form digitale riduce l'onboarding da 3 ore a 20 minuti per ogni nuovo "
        "cliente. Non serve software costoso: bastano un form online e un documento "
        "condiviso su Google Drive."
    ),
    "psicologo": (
        "Il 70% di chi cerca supporto psicologico lo fa la sera, tra le 21 e le 23. "
        "È il momento in cui si sentono finalmente pronti a chiedere aiuto. "
        "Un form di contatto attivo in quella finestra vale quanto tre mesi di passaparola."
    ),
    "commercialista": (
        "Eliminare lo scambio documenti via email riduce 10-15 ore di back-and-forth a "
        "settimana. Un portale clienti semplice — anche con strumenti gratuiti — "
        "risolve questo in modo definitivo."
    ),
    "palestra": (
        "L'80% degli abbonamenti persi avviene perché chi voleva iscriversi non è riuscito "
        "a prenotare una prova gratuita al primo tentativo. Se non trovano il form subito, "
        "raramente tornano."
    ),
    "yoga": (
        "L'80% degli abbonamenti persi avviene perché chi voleva iscriversi non è riuscito "
        "a prenotare una prova al primo tentativo. Se il form non c'è al primo accesso, "
        "raramente tornano."
    ),
    "crossfit": (
        "L'80% degli abbonamenti persi avviene perché chi voleva iscriversi non è riuscito "
        "a prenotare una prova gratuita al primo tentativo. Se il form non c'è, raramente tornano."
    ),
    "estetica": (
        "Le prenotazioni last-minute riempiono il 30% degli slot vuoti ogni settimana, "
        "ma solo se il sistema di prenotazione è attivo 24 ore. "
        "Una cliente che non trova disponibilità alle 23 prenota da qualcun altro la mattina dopo."
    ),
    "spa": (
        "Le prenotazioni last-minute riempiono il 30% degli slot vuoti ogni settimana, "
        "ma solo se il sistema è attivo 24 ore. "
        "Chi non trova il form alle 23 prenota altrove la mattina."
    ),
    "medico": (
        "Il 62% delle ricerche mediche avviene tra le 18 e le 22, quando gli studi sono chiusi. "
        "Senza prenotazione online in quel momento, quei pazienti finiscono dove trovano "
        "il pulsante 'prenota adesso'."
    ),
    "dentista": (
        "Il 62% delle ricerche odontoiatriche avviene fuori orario di studio. "
        "Senza prenotazione online visibile, quei pazienti finiscono allo studio "
        "che ha il form direttamente su Google."
    ),
    "chirurgia": (
        "Il 62% delle ricerche mediche avviene tra le 18 e le 22, quando gli studi sono chiusi. "
        "Senza form online, quei pazienti vanno dove trovano il pulsante 'prenota adesso'."
    ),
    "clinica": (
        "Il 62% delle ricerche mediche avviene tra le 18 e le 22, quando gli studi sono chiusi. "
        "Senza prenotazione online, quei pazienti finiscono dove trovano il pulsante 'prenota adesso'."
    ),
}

_DEFAULT_VALORE = (
    "Un sistema di contatto digitale cattura i lead che arrivano fuori orario — "
    "che sono spesso la maggioranza. Senza di esso, quegli utenti non tornano."
)


def _match(mapping: dict, nicchia: str, default: str) -> str:
    n = nicchia.lower()
    for k, v in mapping.items():
        if k in n:
            return v
    return default


# ─── Costruisce il mini-dettaglio specifico per il prompt ────────────────────

def _nota_contesto(lead: dict) -> str:
    note    = lead.get("note", "").lower()
    website = lead.get("website", "").lower()

    if "instagram" in note:
        return (
            "TROVATO SU INSTAGRAM: Il professionista non ha un sito web. "
            "Trovato su Instagram cercando nel settore. "
            "L'unico modo di contattarli è via DM o telefono."
        )
    if "facebook" in website and "sito" not in note:
        return (
            "SOLO PAGINA FACEBOOK: Nessun sito web proprietario. "
            "La presenza online è solo una pagina Facebook. "
            "Nessun form di contatto diretto."
        )
    if "social" in note:
        return (
            "SOLO CONTATTI SOCIAL: Nessun sito web. "
            "La presenza digitale è unicamente social. "
            "Per contattarli bisogna usare DM o telefono."
        )
    if any(y in note for y in ["2010", "2011", "2012", "2013", "2014", "2015"]):
        anno = next(y for y in ["2010","2011","2012","2013","2014","2015"] if y in note)
        return (
            f"SITO DATATO ({anno}): Il sito web è fermo al {anno}. "
            "Design obsoleto, probabilmente non ottimizzato per mobile, "
            "nessun form di contatto moderno."
        )
    if "pdf" in note:
        return (
            "TROVATO IN UN PDF: Questo professionista non ha una presenza web propria. "
            "Il nominativo è emerso da un documento PDF. "
            "Online è praticamente invisibile a chi cerca oggi."
        )
    if "nessun modulo" in note or "nessun form" in note:
        return (
            "SITO SENZA FORM: Il sito esiste ma non ha nessun modulo di contatto. "
            "Chi vuole fissare un appuntamento deve cercare il numero e chiamare."
        )
    if "solo telefono" in note or "solo email" in note:
        return (
            "CONTATTO SOLO ANALOGICO: L'unico canale è il telefono (o email). "
            "Nessun form, nessuna prenotazione online. "
            "Chi arriva fuori orario non ha alternativa."
        )
    if "whatsapp" in note:
        return (
            "PRENOTAZIONE VIA WHATSAPP: Per prenotare bisogna scrivere un messaggio WhatsApp. "
            "Funziona solo quando qualcuno è disponibile a rispondere in tempo reale."
        )
    if "nessuno" in website or not website.strip():
        return (
            "NESSUN SITO WEB: Questo professionista non ha un sito. "
            "Trovato tramite contatto diretto. Online è invisibile a chi cerca."
        )
    if "vetrina" in note:
        return (
            "SITO SOLO VETRINA: Il sito è puramente informativo. "
            "Nessun form, nessuna prenotazione. "
            "Chi vuole contattarli deve chiamare."
        )
    if "basic" in note or "base" in note:
        return (
            "SITO BASE: Esiste un sito ma è essenziale. "
            "Nessun sistema di prenotazione, probabilmente solo informazioni e telefono."
        )
    if "informativo" in note:
        return (
            "SITO INFORMATIVO: Il sito elenca i servizi ma non ha modo di "
            "contattarli o prenotare direttamente online."
        )
    return f"STATO DIGITALE: {lead.get('note', 'sito base, solo telefono')}."


# ─── User prompt per il Writer ────────────────────────────────────────────────

def build_prompt(lead: dict) -> str:
    nome    = lead["page_name"]
    nicchia = lead.get("nicchia", "professionista")
    citta   = lead.get("citta",   "Italia")
    website = lead.get("website", "nessuno")
    parola  = _match(_PAROLA, nicchia, "clienti")
    valore  = _match(_VALORE, nicchia, _DEFAULT_VALORE)
    dettaglio = _nota_contesto(lead)

    return f"""Scrivi la cold email per questo lead:

Business: {nome}
Settore: {nicchia}
Parola corretta per i loro clienti/pazienti: "{parola}"
Città: {citta}
Sito web: {website}
Booking online: NO

MINI-DETTAGLIO DA USARE NELL'APERTURA E NELL'OGGETTO:
{dettaglio}

INSIGHT SETTORE per la sezione [V] VALORE CONCRETO:
{valore}

ISTRUZIONI SPECIFICHE:
1. [A] ATTENZIONE — prima frase: usa il mini-dettaglio sopra. Come sono stati trovati o lo stato preciso del loro sito. Non iniziare con "Ho cercato {nicchia}" genericamente — entra nel dettaglio specifico di {nome}.
2. OGGETTO — deve riflettere il caso specifico di {nome}. Non generico. Usa il mini-dettaglio.
3. Usa "{parola}" ogni volta che parli dei loro clienti/utenti/pazienti.
4. Adatta il pain point al settore {nicchia} a {citta}.
5. [V] adatta l'insight settore al loro caso specifico (non incollarlo identico).
6. MAI riferimenti a dentisti, studi dentistici, odontoiatria — questo è un {nicchia}.
7. MAI trattini come separatori. MAI "noi/vogliamo/offriamo". Solo "io/ho/mi".

Restituisci SOLO il JSON con oggetto, oggetto_b, oggetto_c e corpo."""


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _parse_json(raw: str) -> dict | None:
    start = raw.find("{")
    if start < 0:
        return None
    try:
        result, _ = json.JSONDecoder().raw_decode(raw[start:])
        return result
    except json.JSONDecodeError:
        pass
    # Fallback regex
    def _rx(text, key):
        m = re.search(rf'"{key}"\s*:\s*"((?:[^"\\]|\\.)*)"', text, re.DOTALL)
        return m.group(1).replace("\\n", "\n").replace('\\"', '"') if m else ""
    r = {k: _rx(raw, k) for k in ("oggetto", "oggetto_b", "oggetto_c", "corpo")}
    return r if r.get("oggetto") and r.get("corpo") else None


def load_existing() -> tuple:
    """Returns (all_items_dict, ready_only_dict). Preserves sent/error statuses."""
    if not os.path.exists(OUTPUT_PATH):
        return {}, {}
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        all_items = json.load(f)
    all_dict   = {r["email"].lower(): r for r in all_items}
    ready_dict = {k: v for k, v in all_dict.items() if v.get("status") == "ready"}
    return all_dict, ready_dict

def load_ready() -> dict:
    _, ready = load_existing()
    return ready


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    resume = "--resume" in sys.argv

    # Costruisce rotation e writer (per _sanitize_corpo)
    writer   = EmailWriterAgent(os.getenv("OPENROUTER_API_KEY", ""))
    rotation = writer.rotation
    if not rotation:
        print("ERRORE: nessun client AI. Controlla .env (GROQ_API_KEY / OPENROUTER_API_KEY)")
        sys.exit(1)

    # Legge CSV — deduplicazione per email
    leads, seen = [], set()
    with open(CSV_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            em = row.get("email", "").strip().lower()
            if em and "@" in em and em not in seen:
                seen.add(em)
                leads.append(row)

    existing_all, existing_ready = load_existing()
    existing  = existing_ready if resume else {}
    # Always preserve sent/failed items; skip leads already done
    skip_set  = {e for e, r in existing_all.items() if r.get("status") in ("sent", "send_failed")}
    da_fare   = [l for l in leads if l["email"].strip().lower() not in existing
                 and l["email"].strip().lower() not in skip_set]

    print(f"\nLead totali   : {len(leads)}")
    print(f"Già pronti    : {len(existing)}")
    print(f"Già inviati   : {len(skip_set)}")
    print(f"Da generare   : {len(da_fare)}")
    print(f"Modello       : {rotation[0][1]}\n")

    # Preserve ALL existing statuses (sent, ready, error) to avoid overwrites
    results = list(existing_all.values())
    errors  = 0

    for i, lead in enumerate(da_fare, 1):
        email_dest = lead["email"].strip()
        nome       = lead["page_name"]

        print(f"[{i:02d}/{len(da_fare)}] {nome[:50]}")
        print(f"         {email_dest}")

        messages = [
            {"role": "system", "content": WRITER_SYSTEM_PROMPT},
            {"role": "user",   "content": build_prompt(lead)},
        ]
        raw = call_ai(rotation, messages, max_tokens=1600, temperature=0.65,
                      label=f"E{i:02d}")

        if not raw:
            print(f"         ERRORE: nessuna risposta AI")
            errors += 1
            results.append({
                "email": email_dest, "page_name": nome,
                "nicchia": lead.get("nicchia", ""), "oggetto": "",
                "corpo": "", "status": "error_no_response",
            })
            _flush(results)
            continue

        parsed = _parse_json(raw)
        if not parsed:
            print(f"         ERRORE: JSON non parsabile")
            errors += 1
            results.append({
                "email": email_dest, "page_name": nome,
                "nicchia": lead.get("nicchia", ""), "oggetto": "",
                "corpo": "", "status": "error_parse",
            })
            _flush(results)
            continue

        corpo   = writer._sanitize_corpo(parsed.get("corpo", ""))
        corpo   = _aggiungi_cta(corpo)
        oggetto = parsed.get("oggetto", "")
        parole  = len(corpo.split()) if corpo else 0

        if oggetto and corpo and parole >= 150:
            print(f"         OK [{parole}p] {oggetto[:60]}")
            results.append({
                "email":     email_dest,
                "page_name": nome,
                "nicchia":   lead.get("nicchia", ""),
                "citta":     lead.get("citta", ""),
                "oggetto":   oggetto,
                "oggetto_b": parsed.get("oggetto_b", ""),
                "oggetto_c": parsed.get("oggetto_c", ""),
                "corpo":     corpo,
                "status":    "ready",
            })
        else:
            print(f"         WARN: troppo corta ({parole}p) o oggetto mancante")
            errors += 1
            results.append({
                "email": email_dest, "page_name": nome,
                "nicchia": lead.get("nicchia", ""),
                "oggetto": oggetto, "corpo": corpo,
                "status": f"error_short_{parole}p",
            })

        _flush(results)
        time.sleep(1.2)

    pronte = sum(1 for r in results if r["status"] == "ready")
    print(f"\n{'='*55}")
    print(f"RISULTATO: {pronte}/{len(leads)} email pronte | {errors} errori")
    print(f"Salvato  : {OUTPUT_PATH}")
    print(f"{'='*55}")
    if pronte > 0:
        print(f"\nReviedi   : python review_emails.py")
        print(f"Poi invia : python send_ready.py")


def _flush(results: list):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
