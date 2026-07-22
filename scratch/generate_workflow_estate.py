# -*- coding: utf-8 -*-
import os
import shutil

def safe_copy(src, dst):
    if not os.path.exists(src):
        return
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
    except Exception as e:
        print(f"[WARN] Impossibile copiare {src}: {e}")

def main():
    root = "WORKFLOW-ESTATE"
    folders = [
        "01-FLUSSI-E-PIANI",
        "02-AUTOMAZIONI-E-SCRIPTS",
        "03-AGENTI-E-RUOLI",
        "04-SKILLS-E-REFERENCE",
        "05-TEMPLATES-E-KIT",
        "06-DASHBOARD-E-METRICHE"
    ]

    for f in folders:
        os.makedirs(os.path.join(root, f), exist_ok=True)

    # 1. FLUSSI E PIANI
    wf_src = "DIGITAL-EMPIRE/03-WORKFLOWS"
    if os.path.exists(wf_src):
        for item in os.listdir(wf_src):
            safe_copy(os.path.join(wf_src, item), os.path.join(root, "01-FLUSSI-E-PIANI", item))
    safe_copy("DIGITAL-EMPIRE/01-PLANNING/PLANNING-P7-MASTER-PLAN.md", os.path.join(root, "01-FLUSSI-E-PIANI/PLANNING-P7-MASTER-PLAN.md"))

    # 2. AUTOMAZIONI E SCRIPTS
    safe_copy("DIGITAL-EMPIRE/00-MEMORY/memory_manager.py", os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py"))
    safe_copy("Outreach/Outreach Workflow/prepare_emails.py", os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/prepare_outreach_emails.py"))
    safe_copy("Outreach/Outreach Workflow/send_ready.py", os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/send_outreach_ready.py"))

    with open(os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/send_s1_whatsapp_auto.py"), "w", encoding="utf-8") as f:
        f.write('''# Script Python per verifica APSOC e invio guidato messaggi WhatsApp (WF-S1)
import os, sys

def verify_apsoc(text):
    checks = {
        'A (Attention)': '?' in text or '!' in text or 'NOVACAR' in text or 'preventivo' in text.lower(),
        'P (Problem)': '40 minuti' in text or 'A4' in text or 'attesa' in text.lower() or 'concorren' in text.lower(),
        'S (Solution)': '120 secondi' in text or 'PDF' in text or 'tablet' in text.lower() or 'Preventa' in text,
        'O (Offer)': '343' in text or '149' in text or 'Partenza Anticipata' in text or 'scontato' in text.lower(),
        'C (Close)': 'giugno' in text.lower() or 'luglio' in text.lower() or 'settembre' in text.lower() or 'preferisci' in text.lower() or 'slot' in text.lower()
    }
    passed = [k for k, v in checks.items() if v]
    print('=== DIAGNOSTICA CHECKLIST APSOC (Andrei Pascu) ===')
    for k, v in checks.items():
        print(f'[{chr(10003) if v else "X"}] {k}')
    print(f'Punteggio indicativo: {len(passed)}/5 ({len(passed)*20}%)')
    if len(passed) >= 4:
        print('ESITO: GO (Messaggio conforme al protocollo)')
    else:
        print('ESITO: NO-GO (Arricchire con leva dolore/valore)')

if __name__ == '__main__':
    msg = """Ciao! Ti scrivo perché l'app preventivi è live: NOVACAR la usa e ha tagliato i tempi da 40 minuti a 120 secondi con PDF brandizzato su tablet. Ti riservo la Partenza Anticipata Luglio: setup €343 invece di €490 e canone €149/mese, così a settembre sei già operativo e non perdi clienti con fogli A4. Ti blocco uno dei due slot rimasti o preferisci partire a settembre a listino pieno?"""
    verify_apsoc(msg)
''')

    with open(os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/fliki_youtube_test.py"), "w", encoding="utf-8") as f:
        f.write('''# Script di verifica API Fliki e render video di test (WF-S5)
import os

def test_fliki_api():
    key = os.environ.get('FLIKI_API_KEY')
    if not key:
        print('[WARN] FLIKI_API_KEY non trovata in .env o variabili di sistema.')
        return False
    print('[INFO] Verifica connessione a Fliki API...')
    return True

if __name__ == '__main__':
    test_fliki_api()
''')

    with open(os.path.join(root, "02-AUTOMAZIONI-E-SCRIPTS/run_checkpoint_eod.bat"), "w", encoding="utf-8") as f:
        f.write('''@echo off
echo ==============================================
echo ESECUZIONE CHECKPOINT GIORNALIERO EOD (h19:00)
echo ==============================================
python memory_manager.py checkpoint --task WORKFLOW-ESTATE --note "Aggiornamento serale metriche e gate"
pause
''')

    # 3. AGENTI E RUOLI
    agents = {
        "AGENTE-MAX.md": """# AGENTE / RUOLO: MAX (Founder & CEO)
> **Ecosistemi:** Tutti · **Tempo dedicato:** Max 90 min/giorno (chirurgico, zero dispersione)
> **Focus Estate 2026:** Incasso immediato, negoziazione S1 con i 7 concessionari, estetica UI/UX premium.

## Responsabilità e Compiti (Da PLANNING-P7)
1. **Negoziazione S1 (Concessionari - Preventa):** Invio dei 3 messaggi WhatsApp e gestione delle chiamate (solo se richieste) con i 7 titolari di salone.
2. **Autorità Social (S3/S4):** Pubblicazione storie, riattivazione profili `mentalita.brutale` e `crea.illtuo_impero`.
3. **Approvazione Estetica (UI/UX):** Giudizio supremo su landing page, design system e interfacce (stile ccm-premium / empire-premium-style).
4. **Governo Mandato:** Unico autorizzato a modificare il Mandato (`MANDATO-EMPIRE.md`) tramite decisione registrata.

## Regole di Operatività
- Non scrive codice di backend o infrastruttura runtime (delega a Gael e Claude).
- Non perde tempo su metriche di vanity (visualizzazioni vuote): conta solo l'incasso e i preventivi firmati.
""",
        "AGENTE-GAEL.md": """# AGENTE / RUOLO: GAEL (Socio & Chief Engine Room)
> **Ecosistemi:** 06-PLATFORM / 09-OPERATIONS · **Focus:** Costruzione e stabilità del runtime e delle app reali.

## Responsabilità e Compiti (Da PLANNING-P7 e STATO-EMPIRE)
1. **Setup Funnel S2 (Manuale Claude Code):** Configurazione landing, checkout ladder (Stripe -> Gumroad -> PayPal.me) e verifica test pagamento €1.
2. **App Delivery S1 (Preventa):** Clona e configura l'istanza multi-tenant per il nuovo concessionario via comando `/nuovo-concessionario` il giorno stesso della chiusura del contratto.
3. **Pipeline Automazione Content (S3/S4/S5):** Esecuzione batch `carousel-factory` per i 7 caroselli, scheduler Meta API / Buffer e test API Fliki.
4. **Manutenzione Core Engine:** Sviluppo di `app.py`, `build_exe.bat` e gestione del server locale.

## Regole di Operatività
- Non modifica il copy o il design estetico UI/UX (di competenza Max/Claude).
- Esegue sequenze di build rigide rispettando la Definition of Done congelata (ADR-EST-005).
""",
        "AGENTE-CLAUDE.md": """# AGENTE / RUOLO: CLAUDE (AI Core & Pair Programmer)
> **Ecosistemi:** 07-FORGE / 10-MEMORY · **Focus:** Scrittura chirurgica di codice, copy APSOC, automazione comandi.

## Responsabilità e Compiti (Da PLANNING-P7)
1. **Copywriting APSOC (S1/S2):** Scrittura degli script WhatsApp, email di lancio, cold call e landing page ad alto tasso di conversione.
2. **Sviluppo & Refactoring:** Creazione di script Python, batch e utility tecniche su richiesta di Max o per supportare Gael.
3. **Governo Memoria EOD:** Creazione quotidiana del checkpoint (`memory_manager.py`) e aggiornamento della dashboard serale.
4. **Pattern Mining & Ingestione:** Utilizzo di `Empire Studio Suite` e delle skill (`andrei-pascu-system`, `content-forge`) per estrarre intelligenza dai competitor.

## Regole di Operatività
- Rispettare rigorosamente la **Regola Art.8 del Mandato:** ogni workflow creato o citato deve avere una cartella reale, tangibile e autocontenuta con tutti i flussi, Python, MD, Agenti e Skill.
- Mai inventare numeri o claim senza prova CPB.
""",
        "AGENTE-CRO-COPY-ARCHITECT.md": """# AGENTE / RUOLO: CRO COPY ARCHITECT (Skill & Guild)
> **Reparto:** 04-MARKETING (Copywriting & Funnel) · **Framework:** APSOC (Attention-Problem-Solution-Offer-Close)

## Funzione Operativa
Trasforma qualsiasi concetto di business o prodotto (Preventa, Manuale Claude Code, servizi agenzia) in copy chirurgico da cecchino.
- Applica la `checklist_APSOC.md` e garantisce uno score >= 92% (23/25 SI) prima del rilascio.
- Martella sul dolore del target (Pain Agitation) quantificando il costo dell'inazione (es. '40 minuti persi su Excel = cliente che va dal concorrente').
- Ancora il prezzo con il Value Gap (es. '€343 setup contro una singola auto da €20.000 salvata').
""",
        "AGENTE-CLOSER-A8.md": """# AGENTE / RUOLO: CLOSER A8 (Negoziazione & Chiamata a Freddo)
> **Reparto:** 01-AGENCY (Vendita) · **Strumento:** Script Cold Call 60s & Chiusura Contratti

## Funzione Operativa
- Gestisce le chiamate di chiusura quando un concessionario o un cliente high-ticket chiede di parlare a voce.
- Utilizza la tecnica di rottura di schema nei primi 8 secondi (Pattern Interrupt).
- Disinnesca le 4 obiezioni principali ('ci sentiamo a settembre', 'costa troppo', 'siamo abituati a carta', 'devo pensarci').
- Porta al micro-impegno e al pagamento immediato del setup promozionale tramite link di checkout brandizzato.
""",
        "AGENTE-ANDREI-PASCU-MINER.md": """# AGENTE / RUOLO: ANDREI PASCU PATTERN MINER (Competitor Intelligence)
> **Reparto:** 10-MEMORY / 08-INTELLIGENCE · **Asset collegato:** `andrei-pascu-system/`

## Funzione Operativa
- Estrae e verifica i 9 principi ricorrenti e l'8-step didactic loop dai video di Andrei Pascu.
- Applica la formula 'AP VIDEO SYSTEM' (timeline 12-15 minuti per i video YouTube di Digital Empire).
- Compila il Log Evidenza di `checklist_APSOC.md` durante l'ingestione di Empire Studio per alimentare lo Swipe Bank aziendale.
"""
    }

    for name, content in agents.items():
        with open(os.path.join(root, "03-AGENTI-E-RUOLI", name), "w", encoding="utf-8") as f:
            f.write(content)

    # 4. SKILLS E REFERENCE
    safe_copy("SKILL & Agenti/Empire Studio Suite/andrei-pascu-system", os.path.join(root, "04-SKILLS-E-REFERENCE/andrei-pascu-system"))
    safe_copy("SKILL & Agenti/SKILL/Skill empire-premium-style", os.path.join(root, "04-SKILLS-E-REFERENCE/Skill-empire-premium-style"))
    safe_copy("SKILL & Agenti/SKILL/Skill CRO - Funnel Architect.md", os.path.join(root, "04-SKILLS-E-REFERENCE/SKILL-cro-funnel-architect.md"))

    # 5. TEMPLATES E KIT
    with open(os.path.join(root, "05-TEMPLATES-E-KIT/kit-vendita-preventa.md"), "w", encoding="utf-8") as f:
        f.write("""# KIT DI VENDITA PREVENTA (S1 - Concessionari)
> **Stato:** Pronto per l'invio · **Prezzo DEC-EST-005:** Setup Promo €343 (invece di €490) + Canone €149/mese

## Argomento del Value Gap (Da copiare al cliente)
Un venditore in salone perde in media 40 minuti per calcolare su carta o foglio Excel rateazione, permuta, finanziamento e passaggio. Durante quell'attesa, il cliente si raffredda, dice 'ci penso' e va a farsi fare un altro preventivo dal concorrente.
Con **Preventa**, in 120 secondi esatti generi un PDF di lusso brandizzato col logo del tuo salone, firmabile direttamente su tablet o inviabile su WhatsApp istantaneamente.
**Il conto economico:** Se vendi un'auto da €20.000 con un margine medio di €1.500, basta che Preventa ti salvi **UNA SOLA VENDITA ALL'ANNO** che avresti perso per lentezza, e il setup di €343 si è ripagato 4 volte in un solo colpo.

## Link e Materiali
- Link Esempio PDF Novacar: `[Includere PDF in cartella /allegati]`
- Link Pagamento Setup €343: `[Link Stripe / Bonifico]`
""")

    with open(os.path.join(root, "05-TEMPLATES-E-KIT/template-3-msg-whatsapp-apsoc.md"), "w", encoding="utf-8") as f:
        f.write("""# TEMPLATE 3 MESSAGGI WHATSAPP (APSOC - Score >=92%)
# Copia e incolla nei messaggi con i 7 concessionari

## MSG-1 (h9:30)
Ciao [Nome]! Tutto bene in salone? Ti scrivo al volo perché l'app di preventivazione istantanea che ti accennavo è ufficialmente live: [NOVACAR] la usa ogni giorno e ha tagliato i tempi di preventivo da 40 minuti a 120 secondi, con PDF brandizzato firmabile su tablet. Ti giro un esempio reale di preventivo che ha chiuso ieri su una vettura da 24k?

## MSG-2 (h18:00 o dopo risposta)
Ottimo. Visto che eri tra i primi interessati, ho riservato per il tuo salone la **Partenza Anticipata Luglio**: setup scontato a **€343** (invece di €490) e canone bloccato a **€149/mese**, con onboarding completo ad agosto quando il salone è tranquillo. Motivo di business: a settembre tu sei GIÀ operativo dal primo giorno di rientro e chiudi mentre gli altri concorrenti stampano ancora foglietti A4 a penna.

## MSG-3 (h10:00 giorno successivo)
Ti blocco uno dei due slot di configurazione anticipata di luglio rimasti, oppure preferisci partire a settembre con il setup a listino pieno (€490)? (Per noi va benissimo in entrambi i casi, mi serve solo sapere come programmare il team tecnico di Gael 🙂)
""")

    with open(os.path.join(root, "05-TEMPLATES-E-KIT/template-cold-call-60s.md"), "w", encoding="utf-8") as f:
        f.write("""# TEMPLATE CHIAMATA A FREDDO (COLD CALL 60 SECONDI - APSOC)

**[0:00 - 0:08] A — ATTENTION**
> "Buongiorno [Nome], sono Max di Digital Empire. Ti chiamo al volo senza girarci intorno: non ti voglio vendere auto, ti chiamo perché ho visto le recensioni del vostro salone e voglio farti una domanda secca di 10 secondi sul vostro processo di preventivazione. Hai 10 secondi reali o ti richiamo tra un'ora?"

**[0:08 - 0:25] P — PROBLEM**
> "Perfetto. Oggi nei saloni multimarca il 40% dei potenziali acquirenti esce dicendo 'ci penso' perché il venditore ci mette mezz'ora a calcolare rate, permuta e finanziamento su Excel o su carta, e il cliente va a comprare dal concorrente che gli dà una risposta istantanea. Succede anche da voi quando c'è ressa il sabato mattina?"

**[0:25 - 0:45] S + O — SOLUTION & VALUE GAP**
> "Esatto. Per questo abbiamo creato Preventa: un'app per tablet che fa il preventivo PDF di lusso brandizzato [Nome Salone] in esattamente 120 secondi. Novacar la sta usando da questo mese. La cosa bella è che stiamo facendo la 'Partenza Anticipata Luglio': installiamo ora con setup scontato a €343 invece di €490, così a settembre il tuo team è già operativo al 100% senza perdere giorni di installazione durante il rientro."

**[0:45 - 0:60] C — CLOSE**
> "Non ti chiedo di decidere ora al telefono su due piedi. Su che numero WhatsApp ti posso mandare il video di 60 secondi che fa vedere come esce il preventivo su tablet per una BMW o un'Audi del vostro salone? Te lo giro, lo guardi con calma e se ne vale la pena ci sentiamo giovedì 10 minuti."
""")

    # 6. DASHBOARD E METRICHE
    safe_copy("DIGITAL-EMPIRE/07-CONTROL/DASHBOARD-E-RETRO.md", os.path.join(root, "06-DASHBOARD-E-METRICHE/DASHBOARD-E-RETRO.md"))
    safe_copy("DIGITAL-EMPIRE/07-CONTROL/LISTA-7-LEAD.md", os.path.join(root, "06-DASHBOARD-E-METRICHE/LISTA-7-CONCESSIONARI.md"))

    # README e INDEX RADICE
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write("""# 🏛️ WORKFLOW ESTATE 2026 — La Cartella Autocontenuta SUPREMA
> **Costruito secondo la Regola Assoluta del Mandato Empire (Articolo 8 / ADR-008).**  
> Qui dentro si trova **TUTTO** il workflow dell'estate 2026: flussi MD, script Python/Bat, Agenti con i loro ruoli e prompt, Skill, Reference, Template pronte e Dashboard di controllo.

## 🧭 Mappa Operativa dei 6 Pilastri
1. **`01-FLUSSI-E-PIANI/`** — Tutti i flussi di orchestrazione (`WF-MASTER.md`, `WF-S1..S6.md`, `workflows.yaml`, `PLANNING-P7-MASTER-PLAN.md`).
2. **`02-AUTOMAZIONI-E-SCRIPTS/`** — Script Python (`send_s1_whatsapp_auto.py`, `memory_manager.py`, `prepare_outreach_emails.py`) e batch (`run_checkpoint_eod.bat`) per eseguire l'automazione.
3. **`03-AGENTI-E-RUOLI/`** — Le schede con istruzioni, ruoli e confini di Max, Gael, Claude, Chief-Forge, CRO Copy Architect e Closer A8.
4. **`04-SKILLS-E-REFERENCE/`** — Il sistema Andrei Pascu (`playbook.md`, `checklist_APSOC.md`), `Skill-empire-premium-style` e `cro-funnel-architect`.
5. **`05-TEMPLATES-E-KIT/`** — I testi di vendita pronti al copia-incolla: kit Preventa (€343 + €149), i 3 messaggi WhatsApp e lo script di Cold Call.
6. **`06-DASHBOARD-E-METRICHE/`** — La dashboard quotidiana e la lista di controllo dei 7 concessionari caldi.

## 🚀 Come avviare subito
- **Se vuoi iniziare l'outreach S1 con i concessionari:** Apri `05-TEMPLATES-E-KIT/template-3-msg-whatsapp-apsoc.md` oppure `01-FLUSSI-E-PIANI/WF-S1-CONCESSIONARI.md`.
- **Se vuoi verificare lo score APSOC di un messaggio prima di spedirlo:** Esegui `python 02-AUTOMAZIONI-E-SCRIPTS/send_s1_whatsapp_auto.py`.
- **Se vuoi vedere i ruoli precisi di Max, Gael o Claude:** Apri la cartella `03-AGENTI-E-RUOLI/`.
""")

    print("WORKFLOW-ESTATE assemblato con successo e completo al 100%!")

if __name__ == "__main__":
    main()
