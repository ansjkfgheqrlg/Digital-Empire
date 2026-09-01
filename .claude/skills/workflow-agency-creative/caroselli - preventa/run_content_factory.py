"""
Esegue ESATTAMENTE il flusso reale descritto da Max (CP-20260805-010), non il
motore Playwright grezzo di prima (3 slide, gradiente hardcoded - quello NON
e' il sistema "perfetto"):

1. Arena -> sidebar "Search"
2. Tab "Archived"
3. Apri la chat "# PROMPT INGEGNERIZZATI PER [ARENA.AI]"
4. Scrivi "/inizio-generazione"
5. Aspetta la risposta che chiede l'argomento del carosello
6. Scrivi SOLO l'argomento (Preventa)

Screenshot ad ogni step - non dare per riuscito un passaggio senza vederlo.
"""
import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
sys.path.insert(0, AGENCY_DIR)

from ArenaAI.arena_generator import wait_for_login, dismiss_blocking_dialogs, solve_arena_captcha  # noqa: E402
from Core.browser_manager import BrowserManager  # noqa: E402

DEBUG_DIR = os.path.join(PROJECT_DIR, "debug_screens_factory")
os.makedirs(DEBUG_DIR, exist_ok=True)

# Contesto ricco, non un one-liner: la chat Content Factory non conosce il
# prodotto Preventa, va dato tutto il contesto reale (posizionamento, pain
# point, leve psicologiche gia' validate nei 4 ganci di outreach in
# produzione) - segnalato da Max ("non ha idea di che prodotto sia").
# Override da riga di comando: python run_content_factory.py "<argomento>"
ARGOMENTO_DEFAULT = """Prodotto: Preventa.

Cosa fa: il titolare di un concessionario auto incolla il link di un annuncio
(anche di un sito estero, es. un portale tedesco) e in pochi secondi ottiene
un PDF preventivo professionale, brandizzato con il suo logo, in italiano,
con i prezzi che ha bloccato lui stesso in anticipo. Non e' un gestionale
nuovo da imparare: affianca quello che gia' usano.

Il problema reale che risolve: oggi un titolare perde 20-30 minuti a mano su
Excel o sul gestionale per fare un preventivo decente, mentre il cliente nel
frattempo ha gia' scritto ad altri 3 concessionari su WhatsApp e sceglie chi
risponde per primo con qualcosa di professionale. Chi importa auto dall'estero
ha un problema doppio: deve anche tradurre l'annuncio e ricalcolare a mano il
prezzo in euro/italiano - il doppio del lavoro.

Leve psicologiche/emotive da usare (gia' testate e validate su centinaia di
messaggi di outreach reali per questo prodotto):
- Perdita imminente: il cliente sta scrivendo AGLI ALTRI concessionari proprio
  ora, ogni minuto perso e' una vendita che rischia di andare a un competitor
  piu' veloce (urgenza/loss aversion, non scarsita' finta)
- Sollievo dal tempo perso: passare da 20-30 minuti di lavoro manuale
  frustrante a un'operazione da pochi secondi
- Immagine professionale vs vergogna del "brutto": un PDF brandizzato e
  curato contro un Excel disordinato mandato su WhatsApp - il titolare non
  vuole sembrare improvvisato davanti al cliente
- Per i concessionari import: liberazione specifica dal doppio lavoro di
  tradurre + ricalcolare un annuncio estero

Target: titolari di concessionari auto in Italia, focus primario su chi fa
import (Germania e altri mercati esteri).

Prezzo/posizionamento: 2.000 euro una tantum, pagamento unico, nessun canone
mensile - va menzionato come vantaggio concreto (investimento singolo, non un
ennesimo abbonamento software).

Tono: diretto, concreto, mai fuffa da "rivoluziona il tuo business" - parla di
tempo reale perso e clienti reali persi, con esempi specifici, non promesse
vaghe."""

ARGOMENTO_CAROSELLO = sys.argv[1] if len(sys.argv) > 1 else ARGOMENTO_DEFAULT

manager = BrowserManager('ArenaAI', headless=False)
try:
    context = manager.get_context()
    page = manager.new_page(context)

    # wait_until="load" non spara mai su arena.ai (SPA con polling/websocket di
    # sfondo che tiene la rete "occupata") - verificato con screenshot reale:
    # a 60s la pagina e' gia' completamente pronta, e' solo l'evento 'load' che
    # non arriva. "domcontentloaded" e' la condizione giusta qui.
    page.goto("https://arena.ai/", timeout=60000, wait_until="domcontentloaded")
    time.sleep(4)
    dismiss_blocking_dialogs(page)

    if not wait_for_login(page):
        print("[FACTORY] [X] Login non completato.")
        sys.exit(1)
    page.screenshot(path=os.path.join(DEBUG_DIR, "01_logged_in.png"))
    print("[FACTORY] Login OK.")

    # 1. Sidebar -> Search
    search_btn = page.locator("text=Search").first
    search_btn.wait_for(state="visible", timeout=10000)
    search_btn.click(force=True)
    time.sleep(2)
    page.screenshot(path=os.path.join(DEBUG_DIR, "02_search_open.png"))
    print("[FACTORY] Pannello Search aperto.")

    # 2. Tab "Archived"
    archived_tab = page.locator("button:has-text('Archived')").first
    archived_tab.wait_for(state="visible", timeout=10000)
    archived_tab.click(force=True)
    time.sleep(2)
    page.screenshot(path=os.path.join(DEBUG_DIR, "03_archived_tab.png"))
    print("[FACTORY] Tab Archived selezionato.")

    # 3. Apri la chat "# PROMPT INGEGNERIZZATI PER [ARENA.AI]"
    chat_item = page.locator("text=PROMPT INGEGNERIZZATI").first
    chat_item.wait_for(state="visible", timeout=10000)
    chat_item.click(force=True)
    time.sleep(4)
    dismiss_blocking_dialogs(page)
    page.screenshot(path=os.path.join(DEBUG_DIR, "04_chat_opened.png"))
    print("[FACTORY] Chat 'PROMPT INGEGNERIZZATI' aperta.")

    # Il composer e' chiaramente visibile nello screenshot ma ne' placeholder
    # ne' role="textbox" lo trovano - 2 tentativi di selettore falliti alla
    # cieca. Basta indovinare: interrogo il DOM vero per sapere cos'e'.
    els = page.evaluate("""
        () => {
          const boxes = [...document.querySelectorAll('textarea, [contenteditable], input[type=text], div[role]')];
          return boxes
            .filter(el => el.getBoundingClientRect().width > 100 && el.getBoundingClientRect().height > 10)
            .map(el => {
              const r = el.getBoundingClientRect();
              return {tag: el.tagName, contentEditable: el.contentEditable, role: el.getAttribute('role'),
                      cls: (el.className||'').toString().slice(0,60),
                      x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height),
                      visible: r.width>0 && r.height>0};
            });
        }
    """)
    print("[FACTORY] Elementi candidati trovati nel DOM:")
    for el in els:
        print(f"  {el}")

    # Clic diretto sulle coordinate reali del composer (dal DOM appena letto,
    # non indovinate) invece di un altro selettore alla cieca. Preferisce il
    # vero editor (contentEditable === "true", classe "ProseMirror"/"tiptap" -
    # confermato dal DOM reale) al wrapper "role=presentation" che lo contiene.
    editable = [e for e in els if e["visible"] and e["contentEditable"] == "true"]
    candidates = editable if editable else [e for e in els if e["visible"] and e["y"] > 400]
    if not candidates:
        print("[FACTORY] [X] Nessun composer candidato trovato nel DOM — controlla lo screenshot e i candidati sopra.")
        page.screenshot(path=os.path.join(DEBUG_DIR, "04b_no_composer_found.png"))
        sys.exit(1)
    target = candidates[0]
    click_x, click_y = target["x"] + target["w"] // 2, target["y"] + target["h"] // 2
    print(f"[FACTORY] Composer scelto: {target} — clic a ({click_x},{click_y})")
    page.mouse.click(click_x, click_y)
    time.sleep(1)
    page.screenshot(path=os.path.join(DEBUG_DIR, "04c_after_click.png"))

    def focus_and_type(text):
        page.mouse.click(click_x, click_y)
        time.sleep(0.5)
        # select-all + delete invece di .fill() (non disponibile senza Locator
        # su un contenteditable) - pulisce eventuale testo residuo prima di digitare.
        page.keyboard.press("Control+A")
        page.keyboard.press("Delete")
        # insert_text (non keyboard.type carattere per carattere): il testo
        # dell'argomento e' multi-riga con paragrafi (\n), e in questa chat
        # Enter = invia. keyboard.type() simulerebbe un vero tasto Enter per
        # ogni "\n" nel testo, spezzando/inviando il messaggio a meta' scrittura.
        # insert_text inserisce il contenuto senza sparare keydown per carattere.
        page.keyboard.insert_text(text)
        time.sleep(1)

    def submit():
        # Bottone submit preso in prestito dall'altra chat (Direct+Image) non
        # esiste qui - UI diversa. "Or hit Enter" e' il pattern gia' visto
        # altrove in Arena per inviare/confermare - usato qui come submit reale.
        page.keyboard.press("Enter")
        time.sleep(1)

    body_text_now = page.locator("body").inner_text()
    if "argomento del carosello" in body_text_now.lower():
        # La chat e' GIA' attivata da un run precedente (visto nello screenshot
        # 04: "Comando /inzio-generazione attivato" gia' presente in cronologia)
        # - rimandarlo di nuovo rischia di confondere lo stato. Si salta dritti
        # all'argomento.
        print("[FACTORY] Chat gia' attivata (trovato 'Argomento del carosello' in cronologia) — salto /inizio-generazione.")
    else:
        solve_arena_captcha(page)
        focus_and_type("/inizio-generazione")
        submit()
        time.sleep(2)
        if dismiss_blocking_dialogs(page, timeout_ms=2000):
            focus_and_type("/inizio-generazione")
            submit()
        print("[FACTORY] '/inizio-generazione' inviato. Aspetto la risposta...")
        time.sleep(15)

    page.screenshot(path=os.path.join(DEBUG_DIR, "05_before_argomento.png"))
    body_text = page.locator("body").inner_text()[-2000:]
    print("[FACTORY] --- ultimi 2000 char della pagina ---")
    print(body_text)

    # Invia l'argomento
    print("[FACTORY] Invio l'argomento Preventa.")
    focus_and_type(ARGOMENTO_CAROSELLO)
    submit()
    print("[FACTORY] Argomento inviato. Aspetto generazione (90s)...")
    time.sleep(90)
    page.screenshot(path=os.path.join(DEBUG_DIR, "06_after_argomento.png"))
    body_text2 = page.locator("body").inner_text()[-2500:]
    print("[FACTORY] --- ultimi 2500 char dopo argomento ---")
    print(body_text2)

finally:
    manager.close()
    print("[FACTORY] Fatto. Screenshot in:", DEBUG_DIR)
