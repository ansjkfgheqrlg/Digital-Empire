"""
WhatsApp Outreach — Genera messaggi brevi e dashboard HTML con link wa.me

Genera messaggi WhatsApp personalizzati per ogni lead con telefono,
poi crea una dashboard HTML con link wa.me precompilati per l'invio manuale.

Uso:
    python implementation/whatsapp_outreach.py --batch --max 300
    python implementation/whatsapp_outreach.py --dashboard-only

Output:
    bozze_whatsapp/YYYY-MM-DD/[ID_LEAD]_wa.txt  → messaggi generati
    whatsapp_dashboard.html                      → dashboard cliccabile
"""

import os
import sys
import csv
import glob
import json
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
import anthropic

from implementation.utils.logger import get_logger

load_dotenv()

CARTELLA_OUTPUT = "output"
CARTELLA_BOZZE_WA = "bozze_whatsapp"
FILE_DASHBOARD = "whatsapp_dashboard.html"

BRAND_VOICE_WA = """
Sei un copywriter per Digital Empire Team — agenzia CRO e funnel freelance.
Scrivi messaggi WhatsApp di cold outreach per business locali senza sito web.

REGOLE FERREE:
- Massimo 100 parole, idealmente 70-90
- Tono: diretto, colloquiale, mai formale
- Prima riga: osservazione concreta sul business (nome + dato)
- NO hype, NO superlative, NO "garantito", "rivoluzionario"
- UN solo problema: visibilità online persa
- CTA finale: domanda semplice su una call breve
- Firma: solo "[Il tuo nome]" (senza titoli, senza link)
- Niente emoji
- Scrivi in italiano

STRUTTURA (4 paragrafi max):
1. Osservazione: "[Nome], ho visto il vostro [tipo] su Maps — [dato concreto]."
2. Problema in 1 frase: ricerche mensili che vanno ai competitor
3. Soluzione 1 frase: non serve molto, una pagina basta
4. CTA: "Vale 10 minuti di chiamata?"
"""


def formatta_numero_wame(telefono: str) -> str:
    """
    Converte numero italiano nel formato per wa.me (solo cifre, con prefisso).
    Es: "+39 02 1234 5678" → "390212345678"
    """
    # Rimuovi tutti i caratteri non numerici tranne il +
    numeri = "".join(c for c in telefono if c.isdigit() or c == "+")

    # Rimuovi il +
    numeri = numeri.replace("+", "")

    # Se non inizia con 39, aggiungilo
    if not numeri.startswith("39"):
        numeri = "39" + numeri

    return numeri


def genera_messaggio_wa(business: dict, client: anthropic.Anthropic, logger) -> str:
    """
    Genera un messaggio WhatsApp breve personalizzato con Claude.
    """
    nome = business.get("NOME_BUSINESS", "il vostro locale")
    categoria = business.get("CATEGORIA", "locale")
    citta = business.get("CITTÀ", "") or business.get("CITT\u00c0", "") or business.get("CITTA", "")
    n_recensioni = business.get("N_RECENSIONI", "")
    rating = business.get("RATING_GOOGLE", "")

    # Costruisci contesto
    dati = []
    if n_recensioni:
        dati.append(f"{n_recensioni} recensioni su Google Maps")
    if rating:
        dati.append(f"rating {rating}/5")
    dato_principale = dati[0] if dati else "ottima reputazione"

    prompt = f"""Scrivi un messaggio WhatsApp di cold outreach per questo business:

Nome: {nome}
Tipo di attività: {categoria}
Città: {citta}
Dato principale: {dato_principale}
Problema: Non ha sito web — perde traffico organico ogni mese

{BRAND_VOICE_WA}

Rispondi SOLO con il testo del messaggio WhatsApp, niente altro."""

    risposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )

    return risposta.content[0].text.strip()


def carica_lead_da_csv() -> list:
    """
    Carica tutti i lead con telefono e pronto outreach dai CSV.
    """
    lead = []
    file_csv = sorted(glob.glob(f"{CARTELLA_OUTPUT}/*.csv"))

    for filepath in file_csv:
        try:
            with open(filepath, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    telefono = row.get("TELEFONO", "").strip()
                    pronto = row.get("PRONTO_OUTREACH", "").strip()
                    if telefono and pronto in ("Sì", "Si", "S\u00ec"):
                        row["_source_file"] = filepath
                        lead.append(row)
        except Exception as e:
            continue

    return lead


def carica_messaggi_esistenti() -> set:
    """
    Restituisce set di ID lead già processati.
    """
    processati = set()
    cartella = Path(CARTELLA_BOZZE_WA)
    if cartella.exists():
        for f in cartella.glob("**/*_wa.txt"):
            # Estrai ID dal nome file: ID_wa.txt
            id_lead = f.stem.replace("_wa", "")
            processati.add(id_lead)
    return processati


def salva_messaggio(id_lead: str, messaggio: str, data_oggi: str):
    """
    Salva il messaggio WhatsApp in bozze_whatsapp/YYYY-MM-DD/
    """
    cartella = Path(CARTELLA_BOZZE_WA) / data_oggi
    cartella.mkdir(parents=True, exist_ok=True)
    filepath = cartella / f"{id_lead}_wa.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(messaggio)
    return str(filepath)


def aggiorna_stato_csv(source_file: str, id_lead: str, campo: str, valore: str):
    """
    Aggiorna un campo nel CSV sorgente per il lead specificato.
    """
    try:
        rows = []
        with open(source_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            intestazioni = reader.fieldnames
            for row in reader:
                if row.get("ID_LEAD") == id_lead:
                    row[campo] = valore
                rows.append(row)

        with open(source_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=intestazioni)
            writer.writeheader()
            writer.writerows(rows)
    except Exception:
        pass


def crea_dashboard_html(lead_con_messaggi: list, data_oggi: str):
    """
    Crea una dashboard HTML con link wa.me cliccabili per ogni lead.
    """
    # Prepara dati per la tabella
    righe_html = []
    for i, item in enumerate(lead_con_messaggi, 1):
        row = item["row"]
        messaggio = item["messaggio"]
        id_lead = row.get("ID_LEAD", "")
        nome = row.get("NOME_BUSINESS", "?")
        citta = row.get("CITTÀ", "") or row.get("CITT\u00c0", "") or row.get("CITTA", "")
        categoria = row.get("CATEGORIA", "")
        telefono = row.get("TELEFONO", "")
        rating = row.get("RATING_GOOGLE", "")
        recensioni = row.get("N_RECENSIONI", "")
        fascia = row.get("FASCIA", "")

        numero_wame = formatta_numero_wame(telefono)
        messaggio_encoded = quote(messaggio)
        link_wa = f"https://wa.me/{numero_wame}?text={messaggio_encoded}"

        # Badge fascia
        colore_fascia = {"A": "#22c55e", "B": "#3b82f6", "C": "#94a3b8"}.get(fascia, "#94a3b8")

        # Anteprima messaggio (troncata)
        preview = messaggio.replace("\n", " ")[:120] + ("..." if len(messaggio) > 120 else "")

        righe_html.append(f"""
        <tr id="row-{i}" data-fascia="{fascia}">
            <td class="num">{i}</td>
            <td>
                <strong>{nome}</strong><br>
                <small style="color:#64748b">{citta} · {categoria}</small>
            </td>
            <td>
                <span class="badge" style="background:{colore_fascia}">{'★' if fascia=='A' else ''} {fascia}</span>
                {f'<br><small>⭐ {rating} ({recensioni} rec.)</small>' if rating else f'<br><small>({recensioni} rec.)</small>' if recensioni else ''}
            </td>
            <td class="phone">{telefono}</td>
            <td class="preview">{preview}</td>
            <td>
                <a href="{link_wa}" target="_blank" class="btn-wa" onclick="segnaInviato({i})">
                    Apri WhatsApp
                </a>
                <div class="sent-badge" id="sent-{i}" style="display:none">✓ Inviato</div>
            </td>
        </tr>""")

    righe_str = "\n".join(righe_html)
    totale = len(lead_con_messaggi)

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WhatsApp Dashboard — Digital Empire ({data_oggi})</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; min-height: 100vh; }}
  header {{ background: #1e293b; padding: 20px 32px; border-bottom: 1px solid #334155; display: flex; align-items: center; justify-content: space-between; }}
  header h1 {{ font-size: 20px; font-weight: 700; color: #f1f5f9; }}
  header p {{ color: #94a3b8; font-size: 13px; margin-top: 2px; }}
  .stats {{ display: flex; gap: 24px; }}
  .stat {{ text-align: center; }}
  .stat .num {{ font-size: 24px; font-weight: 700; color: #22c55e; display: block; }}
  .stat .lbl {{ font-size: 11px; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }}
  .filters {{ padding: 16px 32px; background: #1e293b; border-bottom: 1px solid #1e293b; display: flex; gap: 8px; align-items: center; }}
  .filter-btn {{ padding: 6px 14px; border-radius: 20px; border: 1px solid #334155; background: transparent; color: #94a3b8; cursor: pointer; font-size: 13px; transition: all 0.15s; }}
  .filter-btn.active {{ background: #3b82f6; border-color: #3b82f6; color: white; }}
  .filter-btn:hover {{ border-color: #64748b; color: #e2e8f0; }}
  .search {{ margin-left: auto; padding: 6px 14px; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: #e2e8f0; font-size: 13px; width: 240px; }}
  .search:focus {{ outline: none; border-color: #3b82f6; }}
  .progress-bar {{ height: 3px; background: #1e293b; }}
  .progress-fill {{ height: 100%; background: #22c55e; width: 0%; transition: width 0.3s; }}
  .container {{ padding: 24px 32px; }}
  table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 12px; overflow: hidden; }}
  th {{ padding: 12px 16px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #64748b; background: #0f172a; border-bottom: 1px solid #334155; }}
  td {{ padding: 12px 16px; border-bottom: 1px solid #1e3a5f22; font-size: 13px; vertical-align: top; }}
  tr:hover td {{ background: #ffffff08; }}
  tr.sent td {{ opacity: 0.4; }}
  td.num {{ color: #475569; width: 40px; }}
  td.phone {{ font-family: monospace; color: #94a3b8; white-space: nowrap; }}
  td.preview {{ color: #94a3b8; font-size: 12px; max-width: 280px; line-height: 1.5; }}
  .badge {{ display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 700; color: white; }}
  .btn-wa {{ display: inline-block; padding: 7px 14px; background: #25D366; color: white; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: 600; transition: background 0.15s; white-space: nowrap; }}
  .btn-wa:hover {{ background: #1ebe57; }}
  .sent-badge {{ display: inline-block; padding: 7px 14px; background: #334155; color: #22c55e; border-radius: 8px; font-size: 13px; font-weight: 600; }}
  .counter {{ position: fixed; bottom: 24px; right: 24px; background: #1e293b; border: 1px solid #334155; padding: 14px 20px; border-radius: 12px; font-size: 13px; color: #e2e8f0; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }}
  .counter span {{ font-size: 22px; font-weight: 700; color: #22c55e; display: block; }}
</style>
</head>
<body>

<header>
  <div>
    <h1>WhatsApp Outreach Dashboard</h1>
    <p>Digital Empire Team · Generato il {data_oggi} · {totale} lead con telefono</p>
  </div>
  <div class="stats">
    <div class="stat">
      <span class="num" id="stat-totale">{totale}</span>
      <span class="lbl">Lead totali</span>
    </div>
    <div class="stat">
      <span class="num" id="stat-inviati">0</span>
      <span class="lbl">Inviati</span>
    </div>
    <div class="stat">
      <span class="num" id="stat-rimanenti">{totale}</span>
      <span class="lbl">Rimanenti</span>
    </div>
  </div>
</header>

<div class="progress-bar">
  <div class="progress-fill" id="progress"></div>
</div>

<div class="filters">
  <button class="filter-btn active" onclick="filtra('tutti')">Tutti ({totale})</button>
  <button class="filter-btn" onclick="filtra('A')">Fascia A</button>
  <button class="filter-btn" onclick="filtra('B')">Fascia B</button>
  <button class="filter-btn" onclick="filtra('C')">Fascia C</button>
  <input type="text" class="search" id="search" placeholder="Cerca nome o città..." oninput="cercaTesto()">
</div>

<div class="container">
  <table id="lead-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Business</th>
        <th>Fascia</th>
        <th>Telefono</th>
        <th>Anteprima messaggio</th>
        <th>Azione</th>
      </tr>
    </thead>
    <tbody>
      {righe_str}
    </tbody>
  </table>
</div>

<div class="counter">
  <span id="counter-inviati">0</span>
  messaggi inviati
</div>

<script>
const TOTALE = {totale};
let inviati = JSON.parse(localStorage.getItem('wa_inviati') || '[]');

function segnaInviato(i) {{
  if (!inviati.includes(i)) {{
    inviati.push(i);
    localStorage.setItem('wa_inviati', JSON.stringify(inviati));
  }}
  setTimeout(() => aggiornaUI(i), 500);
}}

function aggiornaUI(i) {{
  const row = document.getElementById('row-' + i);
  const btn = row ? row.querySelector('.btn-wa') : null;
  const sentBadge = document.getElementById('sent-' + i);
  if (btn) btn.style.display = 'none';
  if (sentBadge) sentBadge.style.display = 'inline-block';
  if (row) row.classList.add('sent');

  const count = inviati.length;
  document.getElementById('counter-inviati').textContent = count;
  document.getElementById('stat-inviati').textContent = count;
  document.getElementById('stat-rimanenti').textContent = TOTALE - count;
  document.getElementById('progress').style.width = (count / TOTALE * 100) + '%';
}}

function filtra(fascia) {{
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('#lead-table tbody tr').forEach(row => {{
    if (fascia === 'tutti' || row.dataset.fascia === fascia) {{
      row.style.display = '';
    }} else {{
      row.style.display = 'none';
    }}
  }});
}}

function cercaTesto() {{
  const q = document.getElementById('search').value.toLowerCase();
  document.querySelectorAll('#lead-table tbody tr').forEach(row => {{
    const testo = row.textContent.toLowerCase();
    row.style.display = testo.includes(q) ? '' : 'none';
  }});
}}

// Ripristina stato da localStorage
window.addEventListener('load', () => {{
  inviati.forEach(i => aggiornaUI(i));
}});
</script>
</body>
</html>"""

    with open(FILE_DASHBOARD, "w", encoding="utf-8") as f:
        f.write(html)

    return FILE_DASHBOARD


def main():
    parser = argparse.ArgumentParser(description="WhatsApp outreach — genera messaggi e dashboard")
    parser.add_argument("--batch", action="store_true", help="Genera messaggi per tutti i lead")
    parser.add_argument("--max", type=int, default=300, help="Numero massimo di lead da processare")
    parser.add_argument("--dashboard-only", action="store_true", help="Rigenera solo la dashboard HTML")
    args = parser.parse_args()

    data_oggi = datetime.now().strftime("%Y-%m-%d")
    logger = get_logger("WF-WA", f"whatsapp_{data_oggi}")

    # Carica lead
    tutti_lead = carica_lead_da_csv()
    logger.info(f"Lead con telefono trovati: {len(tutti_lead)}")

    if not tutti_lead:
        logger.error("Nessun lead con telefono trovato nei CSV")
        sys.exit(1)

    # Filtra già processati
    gia_processati = carica_messaggi_esistenti()
    lead_da_fare = [r for r in tutti_lead if r.get("ID_LEAD") not in gia_processati]
    logger.info(f"Già processati: {len(gia_processati)} | Da processare: {len(lead_da_fare)}")

    # Limita al max
    lead_da_fare = lead_da_fare[:args.max]

    lead_con_messaggi = []

    if not args.dashboard_only and lead_da_fare:
        # Inizializza Claude
        api_key = os.getenv("ANTHROPIC_API_KEY", "").strip()
        if not api_key:
            logger.error("ANTHROPIC_API_KEY non configurata")
            sys.exit(1)

        client = anthropic.Anthropic(api_key=api_key)
        logger.info(f"START — Generando {len(lead_da_fare)} messaggi WhatsApp")

        ok = 0
        errori = 0

        for i, row in enumerate(lead_da_fare, 1):
            id_lead = row.get("ID_LEAD", "")
            nome = row.get("NOME_BUSINESS", "?")
            logger.info(f"[{i}/{len(lead_da_fare)}] {nome} ({id_lead})")

            try:
                messaggio = genera_messaggio_wa(row, client, logger)
                percorso = salva_messaggio(id_lead, messaggio, data_oggi)
                aggiorna_stato_csv(row["_source_file"], id_lead, "NOTE", f"WA_generato:{data_oggi}")
                lead_con_messaggi.append({"row": row, "messaggio": messaggio})
                ok += 1
                logger.info(f"OK: {nome} → {percorso}")

            except Exception as e:
                logger.error(f"ERRORE {nome}: {e}")
                errori += 1
                continue

        logger.info(f"Messaggi generati: {ok} | Errori: {errori}")

    # Aggiungi anche i lead già processati per la dashboard completa
    gia_processati_rows = [r for r in tutti_lead if r.get("ID_LEAD") in gia_processati]
    for row in gia_processati_rows:
        id_lead = row.get("ID_LEAD", "")
        # Cerca il messaggio salvato
        cartella = Path(CARTELLA_BOZZE_WA)
        file_wa = list(cartella.glob(f"**/{id_lead}_wa.txt"))
        if file_wa:
            with open(file_wa[0], encoding="utf-8") as f:
                messaggio = f.read().strip()
            lead_con_messaggi.append({"row": row, "messaggio": messaggio})
        else:
            # Usa messaggio placeholder
            nome = row.get("NOME_BUSINESS", "?")
            lead_con_messaggi.append({"row": row, "messaggio": f"Ciao {nome}, ho visto il vostro locale su Google Maps."})

    # Crea dashboard HTML
    logger.info(f"Creando dashboard HTML con {len(lead_con_messaggi)} lead...")
    percorso_dashboard = crea_dashboard_html(lead_con_messaggi, data_oggi)
    logger.info(f"Dashboard creata: {percorso_dashboard}")
    logger.info(f"END — Apri {percorso_dashboard} nel browser per iniziare l'outreach")

    print(f"\n{'='*60}")
    print(f"Dashboard pronta: {percorso_dashboard}")
    print(f"Lead totali con messaggio: {len(lead_con_messaggi)}")
    print(f"Apri il file HTML nel browser e clicca 'Apri WhatsApp' per ogni lead.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
