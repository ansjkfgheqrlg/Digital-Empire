# Skill
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Skill CRO - Funnel Architect]]

## Content

---
name: launch-funnel-architect
description: Progetta architetture complete di funnel di lancio per vendere info-prodotti e servizi — dal primo touchpoint alla vendita e al nurture post-vendita. Usa questa skill ogni volta che devi progettare un funnel di vendita, scegliere il tipo di funnel giusto per un prodotto/prezzo, definire biforcazioni e percorsi per lead diversi, configurare tag system e automazioni email per un lancio, diagnosticare un funnel che non converte, adattare un funnel a un caso specifico, o convertire un funnel live in evergreen. Attiva questa skill anche quando l'utente menziona landing page per opt-in, pagine upsell, webinar funnel, VSL funnel, sequenze di vendita, lead magnet, conversion rate del funnel, show rate, follow-up post-webinar, tag system per email marketing, automazioni per lanci, o qualsiasi architettura commerciale per info-prodotti, corsi online, servizi di consulenza o coaching — anche se non usa esplicitamente la parola "funnel".
---

# Launch Funnel Architect

Sei un architetto di funnel specializzato in info-prodotti e servizi. Progetti la **struttura completa** di un sistema di vendita: pagine, biforcazioni, tag, automazioni, routing e tracking. Non scrivi copy (quello lo gestiscono altre skill dedicate) — tu progetti l'**architettura** che guida il prospect dal primo contatto alla vendita.

Hai a disposizione degli **script Python** nella cartella `scripts/` che producono output strutturati. Usali per generare mappe funnel, tag system, diagnostica e checklist — sono più precisi e coerenti di un output scritto a mano.

## Principi fondamentali

### Ogni step vende solo lo step successivo

Un funnel non è una sequenza di pagine — è un sistema di decisioni guidate. La landing page non vende il prodotto: vende il download del PDF. Il PDF non vende il prodotto: vende l'iscrizione al webinar. Il webinar non vende il prodotto: vende la decisione di comprare.

Se cerchi di vendere il prodotto finale in ogni step, non vendi niente in nessuno. Quando progetti una pagina, chiediti: "qual è l'UNICA azione che voglio che il prospect faccia qui?" Se la risposta contiene una virgola, stai sbagliando.

### Frizione strategica

Meno frizione = più lead, qualità più bassa. Più frizione = meno lead, qualità più alta.

- **High-volume / low-ticket** (ebook €19) → minima frizione, massimo volume
- **Low-volume / high-ticket** (percorso €997) → più frizione (telefono obbligatorio, call, form qualificanti)
- **Servizi** (agenzia/consulenza) → massima frizione (application form con routing automatico)

### Routing basato sul comportamento

Lead diversi meritano trattamenti diversi. Chi compra il mini-corso è più caldo di chi non compra. Chi apre tutte le email e risponde su WhatsApp è più caldo di chi sparisce. Il funnel deve differenziare il trattamento attraverso tag, scoring e biforcazioni esplicite.

Ogni biforcazione ha due rami definiti. Mai abbandonare un lead: chi non converte entra in un percorso alternativo (nurture), non nel nulla.


## Protocollo di intervista

Prima di progettare qualsiasi funnel, raccogli queste informazioni. Se il contesto della conversazione ne contiene già alcune, estraile e conferma.

### Informazioni essenziali

1. **Prodotto**: cosa vendi? (tipo, formato, contenuto principale)
2. **Prezzo**: quanto costa? (determina il tipo di funnel)
3. **Target**: a chi lo vendi? (ruolo, livello, situazione, problema)
4. **Lead magnet**: qual è l'entry point gratuito?
5. **Stato attuale**: funnel esistente o da zero?
6. **Piattaforme**: email tool, page builder, webinar tool, checkout
7. **Tipo di lancio**: live o evergreen?

### Se il funnel esiste già (diagnostica)

8. **Metriche per step**: numeri reali per ogni passaggio
9. **Volume e periodo**: da quanto è attivo e su quanto traffico
10. **Fonte traffico**: organico, ads, email list, mix

### Se ci sono più prodotti

11. **Posizione nella product ladder**: dove si colloca questo prodotto?
12. **Percorso ideale del cliente**: il viaggio completo


## Matrice decisionale

Il tipo di funnel dipende dal prezzo. Usa lo script `scripts/funnel_selector.py` per la selezione automatica, oppure questa tabella:

| Fascia di prezzo | Tipo di funnel | Architettura |
|---|---|---|
| €0–27 | Micro | Landing → Checkout diretto |
| €47–97 | Semplificato | Opt-in → VSL (15–25 min) → Sales page → Checkout |
| €97–297 | Funnel Unico Perfetto Standard | Opt-in → Upsell → VSL evento → Webinar (75–90 min) → Follow-up → Nurture |
| €497–997 | Funnel Unico Perfetto Completo | Come sopra + call obbligatorie + WhatsApp + follow-up 1:1 |
| Servizio/consulenza | Applicazione | Landing → VSL → Form con friction → Routing → Booking → Call |


## Come gestire le richieste

### "Devo creare un funnel da zero"

1. Conduci l'intervista (sezione Protocollo)
2. Esegui `scripts/funnel_selector.py` con prezzo e tipo prodotto
3. Presenta l'architettura ad alto livello
4. Dettaglia ogni step leggendo `references/blueprint-step-by-step.md` (e `references/varianti-funnel.md` se non è il Funnel Unico Perfetto)
5. Esegui `scripts/tag_generator.py` per generare il tag system
6. Esegui `scripts/automation_mapper.py` per la mappa automazioni
7. Esegui `scripts/checklist_generator.py` per la checklist pre-lancio
8. Produci i brief per le skill collegate

### "Il mio funnel non converte"

1. Raccogli le metriche per ogni step
2. Esegui `scripts/funnel_diagnostics.py` con i numeri dell'utente
3. Leggi `references/diagnostica.md` per approfondire le cause
4. Proponi intervento specifico, test concreto e metrica di successo

### "Voglio rendere il funnel evergreen"

1. Leggi `references/varianti-funnel.md`, sezione Evergreen
2. Mappa le differenze rispetto al funnel live
3. Configura automazioni triggered-by-registration

### "Quale funnel uso per il mio prodotto?"

1. Chiedi prezzo, tipo e target
2. Esegui `scripts/funnel_selector.py`
3. Spiega il perché della scelta


## Integrazione con altre skill

| Componente | Skill | Cosa includere nel brief |
|---|---|---|
| Copy landing/sales page | CRO Copy Architect | Posizione nel funnel, obiettivo, target, framework |
| Ricerca target/obiezioni | Client Research Engine | Prodotto, target → leve emotive e obiezioni |
| Sequenze email | Email Sequence Master | Trigger map: quali email, a quale step, con quale tag |
| Script webinar | Webinar Script Master | Contesto pre-webinar, livello consapevolezza, prodotto |
| Script VSL | VSL Script Builder | Per ogni VSL: posizione, durata, scopo, CTA |
| Prezzo/bonus/garanzia | Product Pricing Strategist | Tipo prodotto, target, posizione product ladder |


## Guida agli script

| Script | Quando usarlo | Input |
|---|---|---|
| `scripts/funnel_selector.py` | Per scegliere il tipo di funnel | Prezzo, tipo prodotto, tipo lancio |
| `scripts/tag_generator.py` | Per generare il tag system completo | Nome prodotto, nome lead magnet, tipo funnel |
| `scripts/funnel_diagnostics.py` | Per diagnosticare un funnel che non converte | Metriche per ogni step |
| `scripts/automation_mapper.py` | Per generare la mappa automazioni | Tipo funnel, piattaforme |
| `scripts/checklist_generator.py` | Per generare la checklist pre-lancio | Tipo funnel |
| `scripts/engagement_scorer.py` | Per calcolare lo scoring engagement | Comportamenti del lead |


## Guida ai file di riferimento

| File | Quando leggerlo |
|---|---|
| `references/blueprint-step-by-step.md` | Dettagli operativi di ogni step del Funnel Unico Perfetto |
| `references/varianti-funnel.md` | Prodotto NON nella fascia €97–997, o conversione live→evergreen, o funnel applicazione |
| `references/tag-system.md` | Configurare o verificare il tag system |
| `references/diagnostica.md` | Funnel esistente che non performa |
| `references/checklist-qualita.md` | Fine progettazione, prima del lancio |


## Formato output

Ogni progettazione produce:

1. **Mappa funnel** — Diagramma ASCII con pagine, biforcazioni, tag, automazioni
2. **Wireframe pagine** — Per ogni pagina: struttura, headline, CTA, regole
3. **Tag system** — Generato da `scripts/tag_generator.py`
4. **Automazioni** — Generate da `scripts/automation_mapper.py`
5. **Tracking** — Eventi pixel per ogni step
6. **Scoring engagement** — Se include webinar, generato da `scripts/engagement_scorer.py`
7. **Brief per skill collegate** — Per ogni componente che serve un'altra skill
8. **Checklist pre-lancio** — Generata da `scripts/checklist_generator.py`

Per la diagnostica:
1. **Gap analysis** — Generata da `scripts/funnel_diagnostics.py`
2. **Diagnosi** — Collo di bottiglia con evidenze
3. **Intervento** — Azione specifica, test, metrica di successo

scripts/funnel_selector.py
Python
#!/usr/bin/env python3
"""
Funnel Selector — Seleziona il tipo di funnel ottimale
in base al prezzo, tipo di prodotto e tipo di lancio.

Uso:
    python funnel_selector.py --prezzo 197 --tipo "corso" --lancio "live"
    python funnel_selector.py --prezzo 3000 --tipo "servizio" --lancio "live"
    python funnel_selector.py --interattivo
"""

import argparse
import json
import sys


FUNNEL_TYPES = {
    "micro": {
        "nome": "Funnel Micro",
        "fascia_prezzo": "€0–27",
        "architettura": "Landing page → Checkout diretto",
        "architettura_alternativa": "Capitolo/anteprima gratis → 2-3 email → Vendita prodotto completo",
        "step": [
            "Landing page / Sales page corta",
            "Checkout diretto",
            "Thank you + consegna prodotto",
            "1 email follow-up (se non compra)"
        ],
        "include": {
            "webinar": False,
            "vsl": False,
            "upsell": False,
            "whatsapp": False,
            "chiamate": False,
            "lead_magnet_separato": "opzionale"
        },
        "note": [
            "Acquisto d'impulso — il prezzo è così basso che non serve convincere a lungo",
            "Sales page corta: headline + bullet + prezzo + CTA",
            "NO VSL, NO webinar, NO call — il margine non copre il costo",
            "Se vuoi costruire una lista, usa la variante con lead magnet gratuito"
        ]
    },
    "semplificato": {
        "nome": "Funnel Semplificato",
        "fascia_prezzo": "€47–97",
        "architettura": "Opt-in PDF → VSL vendita diretta (15-25 min) → Sales page → Checkout → Nurture",
        "step": [
            "Landing page opt-in (lead magnet gratuito)",
            "VSL di vendita diretta (15-25 min)",
            "Sales page lunga (framework APP-SOC)",
            "Checkout",
            "Thank you + onboarding",
            "Email follow-up (3 email in 3 giorni)",
            "Nurture settimanale"
        ],
        "include": {
            "webinar": False,
            "vsl": True,
            "upsell": False,
            "whatsapp": False,
            "chiamate": False,
            "lead_magnet_separato": True
        },
        "note": [
            "NO webinar — il prezzo non giustifica 90 minuti di presentazione",
            "La VSL fa tutto il lavoro: hook + 1 segreto + 1 storia + pitch diretto",
            "Sales page con framework APP-SOC completo",
            "Email follow-up breve: 3 email in 3 giorni, poi nurture"
        ]
    },
    "unico_perfetto_standard": {
        "nome": "Funnel Unico Perfetto — Standard",
        "fascia_prezzo": "€97–297",
        "architettura": "Opt-in PDF → Upsell mini-corso (€15-47) → VSL evento → Webinar live (75-90 min) → Follow-up email → Nurture",
        "step": [
            "STEP 1: Landing page opt-in (PDF gratuito)",
            "STEP 2: Pagina upsell mini-corso (€15-47)",
            "STEP 3: Pagina VSL evento / webinar",
            "STEP 4: Form iscrizione webinar (nome + email + telefono)",
            "STEP 5: Sequenza pre-webinar (email + WhatsApp + chiamata)",
            "STEP 6: Webinar live (75-90 min)",
            "STEP 7: Follow-up post-webinar (5 email in 5 giorni)",
            "STEP 8: Nurture lungo termine (1 email/settimana)"
        ],
        "include": {
            "webinar": True,
            "vsl": True,
            "upsell": True,
            "whatsapp": "consigliato",
            "chiamate": "consigliate ma non obbligatorie",
            "lead_magnet_separato": True
        },
        "specifiche_webinar": {
            "durata": "75-90 minuti",
            "storie": "1-2",
            "follow_up": "email (no 1:1 DM salvo scalabili)",
            "urgenza": "prezzo temporaneo"
        },
        "note": [
            "Questo è il funnel 'default' per info-prodotti da €97 in su",
            "Chiamate consulente consigliate ma non obbligatorie",
            "Follow-up via email, non 1:1 DM (a meno che non sia scalabile)",
            "Il mini-corso upsell autofinanzia il traffico ads"
        ]
    },
    "unico_perfetto_completo": {
        "nome": "Funnel Unico Perfetto — Completo",
        "fascia_prezzo": "€497–997",
        "architettura": "Opt-in PDF → Upsell mini-corso → VSL evento → Webinar live (90-120 min) → Follow-up 1:1 → Call gratuita → Nurture",
        "step": [
            "STEP 1: Landing page opt-in (PDF gratuito)",
            "STEP 2: Pagina upsell mini-corso (€15-47)",
            "STEP 3: Pagina VSL evento / webinar",
            "STEP 4: Form iscrizione webinar (nome + email + telefono)",
            "STEP 5: Sequenza pre-webinar (email + WhatsApp + chiamate obbligatorie)",
            "STEP 6: Webinar live (90-120 min) con 3 storie",
            "STEP 7: Follow-up post-webinar 1:1 (email + DM + call gratuita)",
            "STEP 8: Nurture lungo termine"
        ],
        "include": {
            "webinar": True,
            "vsl": True,
            "upsell": True,
            "whatsapp": True,
            "chiamate": True,
            "call_gratuita": True,
            "lead_magnet_separato": True
        },
        "specifiche_webinar": {
            "durata": "90-120 minuti",
            "storie": "3 (più dettagliate)",
            "follow_up": "email + DM 1:1 personalizzati + call gratuita 15 min",
            "urgenza": "posti limitati (reale)"
        },
        "differenze_da_standard": [
            "Webinar più lungo (90-120 min vs 75-90 min)",
            "3 storie dettagliate nel webinar (vs 1-2)",
            "Chiamate consulente OBBLIGATORIE (vs consigliate)",
            "WhatsApp ATTIVO e gestito (vs consigliato)",
            "Follow-up 1:1 con DM personalizzati",
            "Call gratuita 15 min per lead caldi",
            "Urgenza basata su posti limitati reali (vs prezzo temporaneo)"
        ]
    },
    "applicazione": {
        "nome": "Funnel Applicazione",
        "fascia_prezzo": "Servizio/consulenza (€1.000+)",
        "architettura": "Landing page → VSL (5-10 min) → Form applicazione con friction → Routing per qualità → Booking page → Sequenza pre-call → Call strategica → Proposta → Follow-up",
        "step": [
            "Landing page con headline + social proof + portfolio",
            "VSL breve (5-10 min): posizionamento + caso studio",
            "Form applicazione con domande qualificanti",
            "Routing automatico per qualità lead",
            "Booking page (Calendly/Cal.com) — solo per qualificati",
            "Sequenza pre-call (2-3 email + WhatsApp)",
            "Call strategica (30-45 min)",
            "Proposta + follow-up"
        ],
        "include": {
            "webinar": False,
            "vsl": True,
            "upsell": False,
            "whatsapp": True,
            "chiamate": True,
            "form_qualificante": True,
            "routing": True,
            "lead_magnet_separato": False
        },
        "domande_form": [
            {"domanda": "Qual è il tuo fatturato mensile?", "routing": "<€10K → risorse gratuite, NO call"},
            {"domanda": "Hai traffico attivo (ads/organico)?", "routing": "No → redirect risorse traffico"},
            {"domanda": "Quanto spendi al mese in advertising?", "routing": "Contesto per la call"},
            {"domanda": "Qual è il tuo conversion rate attuale?", "routing": "Baseline per proposta"},
            {"domanda": "Quando vorresti iniziare?", "routing": "Subito → PRIORITÀ ALTA; Esplorando → BASSA"}
        ],
        "note": [
            "NO webinar di massa — servizio su misura richiede conversazione 1:1",
            "Il form con friction filtra i lead non qualificati PRIMA della call",
            "Il pixel si attiva SOLO quando un lead qualificato completa la prenotazione",
            "Senza routing, l'algoritmo ads manda i lead più economici (= meno qualificati)"
        ]
    }
}


def select_funnel(prezzo: float, tipo: str = "infoprodotto", lancio: str = "live") -> dict:
    """Seleziona il tipo di funnel ottimale."""

    tipo_lower = tipo.lower()

    # Servizio/agenzia/consulenza → sempre funnel applicazione
    service_keywords = ["servizio", "agenzia", "consulenza", "coaching", "done-for-you",
                        "service", "agency", "consulting"]
    if any(kw in tipo_lower for kw in service_keywords):
        funnel = FUNNEL_TYPES["applicazione"].copy()
        funnel["motivo_selezione"] = (
            f"Prezzo €{prezzo:,.0f} + tipo '{tipo}' = servizio/consulenza. "
            f"Il funnel applicazione filtra e qualifica i lead prima della call, "
            f"così il team vendita parla solo con prospect in target."
        )
        return funnel

    # Info-prodotti: selezione per fascia di prezzo
    if prezzo <= 27:
        key = "micro"
        motivo = (
            f"A €{prezzo:,.0f}, l'acquisto è d'impulso. Non serve un webinar o una VSL. "
            f"Servono una pagina chiara e un checkout veloce."
        )
    elif prezzo <= 97:
        key = "semplificato"
        motivo = (
            f"A €{prezzo:,.0f}, il prezzo giustifica una VSL di vendita ma non un webinar "
            f"di 90 minuti. La VSL fa tutto il lavoro di persuasione."
        )
    elif prezzo <= 297:
        key = "unico_perfetto_standard"
        motivo = (
            f"A €{prezzo:,.0f}, serve il Funnel Unico Perfetto Standard. Il webinar "
            f"è il momento di vendita, preceduto da lead magnet e upsell per scaldare il lead."
        )
    elif prezzo <= 997:
        key = "unico_perfetto_completo"
        motivo = (
            f"A €{prezzo:,.0f}, serve il Funnel Unico Perfetto Completo. Il prezzo alto "
            f"richiede più touchpoint umani: call obbligatorie, WhatsApp attivo, follow-up 1:1."
        )
    else:
        key = "applicazione"
        motivo = (
            f"A €{prezzo:,.0f}, il prodotto/servizio richiede un funnel applicazione. "
            f"A questo prezzo serve qualificazione e conversazione 1:1."
        )

    funnel = FUNNEL_TYPES[key].copy()
    funnel["motivo_selezione"] = motivo

    # Nota evergreen
    if lancio.lower() == "evergreen" and key in ("unico_perfetto_standard", "unico_perfetto_completo"):
        funnel["note_evergreen"] = [
            "Webinar → Masterclass on-demand (video registrato)",
            "Email pre-webinar → triggered al momento dell'iscrizione (non a date fisse)",
            "Urgenza → countdown personalizzato per lead (cookie-based): '48h dal momento in cui guardi'",
            "Chiamate consulente → solo per lead con score alto (non scalabile su tutti)",
            "WhatsApp → automatizzato o eliminato",
            "Tag aggiuntivo: evergreen-[nome-prodotto]",
            "L'evergreen converte meno del live ma funziona 24/7 — su un anno il volume compensa"
        ]

    return funnel


def print_funnel(funnel: dict) -> None:
    """Stampa il funnel in formato leggibile."""

    print("=" * 65)
    print(f"  FUNNEL SELEZIONATO: {funnel['nome']}")
    print(f"  Fascia prezzo: {funnel['fascia_prezzo']}")
    print("=" * 65)

    print(f"\n📋 MOTIVO: {funnel['motivo_selezione']}")

    print(f"\n🏗️  ARCHITETTURA:")
    print(f"   {funnel['architettura']}")
    if "architettura_alternativa" in funnel:
        print(f"   Alternativa: {funnel['architettura_alternativa']}")

    print(f"\n📌 STEP DEL FUNNEL:")
    for i, step in enumerate(funnel["step"], 1):
        print(f"   {i}. {step}")

    print(f"\n✅ INCLUDE:")
    for k, v in funnel["include"].items():
        label = k.replace("_", " ").title()
        if v is True:
            print(f"   ✅ {label}")
        elif v is False:
            print(f"   ❌ {label}")
        else:
            print(f"   ⚠️  {label}: {v}")

    if "specifiche_webinar" in funnel:
        print(f"\n🎤 SPECIFICHE WEBINAR:")
        for k, v in funnel["specifiche_webinar"].items():
            print(f"   • {k.replace('_', ' ').title()}: {v}")

    if "differenze_da_standard" in funnel:
        print(f"\n🔺 DIFFERENZE DAL FUNNEL STANDARD:")
        for diff in funnel["differenze_da_standard"]:
            print(f"   • {diff}")

    if "domande_form" in funnel:
        print(f"\n📝 DOMANDE FORM APPLICAZIONE:")
        for d in funnel["domande_form"]:
            print(f"   • {d['domanda']}")
            print(f"     Routing: {d['routing']}")

    if "note_evergreen" in funnel:
        print(f"\n🔄 NOTE EVERGREEN:")
        for nota in funnel["note_evergreen"]:
            print(f"   • {nota}")

    print(f"\n📝 NOTE:")
    for nota in funnel["note"]:
        print(f"   • {nota}")

    print()


def interactive_mode():
    """Modo interattivo — guida l'utente alla selezione."""

    print("\n" + "=" * 65)
    print("  FUNNEL SELECTOR — Selezione Interattiva")
    print("=" * 65)

    try:
        prezzo = float(input("\n💰 Prezzo del prodotto/servizio (€): "))
    except ValueError:
        print("❌ Inserisci un numero valido.")
        sys.exit(1)

    tipo = input("📦 Tipo (infoprodotto / servizio / consulenza / coaching): ").strip() or "infoprodotto"
    lancio = input("🚀 Tipo di lancio (live / evergreen): ").strip() or "live"

    funnel = select_funnel(prezzo, tipo, lancio)
    print_funnel(funnel)

    # Output JSON per uso programmatico
    json_path = "funnel_selection.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(funnel, f, ensure_ascii=False, indent=2)
    print(f"💾 Salvato in {json_path}")


def main():
    parser = argparse.ArgumentParser(description="Seleziona il tipo di funnel ottimale")
    parser.add_argument("--prezzo", type=float, help="Prezzo del prodotto (€)")
    parser.add_argument("--tipo", default="infoprodotto", help="Tipo: infoprodotto, servizio, consulenza, coaching")
    parser.add_argument("--lancio", default="live", help="Tipo di lancio: live o evergreen")
    parser.add_argument("--interattivo", action="store_true", help="Modo interattivo")
    parser.add_argument("--json", action="store_true", help="Output solo JSON")

    args = parser.parse_args()

    if args.interattivo:
        interactive_mode()
        return

    if args.prezzo is None:
        interactive_mode()
        return

    funnel = select_funnel(args.prezzo, args.tipo, args.lancio)

    if args.json:
        print(json.dumps(funnel, ensure_ascii=False, indent=2))
    else:
        print_funnel(funnel)


if __name__ == "__main__":
    main()

scripts/tag_generator.py
Python
#!/usr/bin/env python3
"""
Tag Generator — Genera il tag system completo per un funnel.

Uso:
    python tag_generator.py --prodotto "corso-email-marketing" --lead-magnet "5-template-bf" --tipo "unico_perfetto_standard"
    python tag_generator.py --prodotto "ebook-ricette" --lead-magnet "5-ricette" --tipo "micro"
    python tag_generator.py --prodotto "web-design" --tipo "applicazione"
    python tag_generator.py --interattivo
"""

import argparse
import json
import sys


def slugify(text: str) -> str:
    """Converte testo in slug per tag: minuscolo, trattini, no spazi."""
    return text.lower().strip().replace(" ", "-").replace("_", "-")


def generate_tags(prodotto: str, lead_magnet: str = "", tipo_funnel: str = "unico_perfetto_standard") -> dict:
    """Genera il tag system completo per un funnel."""

    prod = slugify(prodotto)
    lm = slugify(lead_magnet) if lead_magnet else f"lm-{prod}"

    result = {
        "convenzione_naming": "[categoria]-[specifico]-[dettaglio] — tutto minuscolo, trattini",
        "regole": [
            "I tag si ACCUMULANO — non si sovrascrivono",
            "Il tag 'buyer' è globale: si applica al primo acquisto di qualsiasi cosa, mai rimuovere",
            "I tag di acquisto (cliente-*) non si rimuovono mai — sono la storia del lead",
            "I tag di posizione (webinar-attesa, post-webinar-followup) si rimuovono quando il lead avanza",
            "Coerenza tra funnel: stessi nomi di tag in tutti i funnel"
        ],
        "tags_per_categoria": {},
        "mappa_funnel": [],
        "rimozioni": []
    }

    # === TAG FONTE INGRESSO ===
    result["tags_per_categoria"]["fonte_ingresso"] = [
        {
            "tag": f"pdf-{lm}",
            "quando": "Al download del lead magnet gratuito",
            "rimuovere": "Mai"
        }
    ]

    # === TAG ACQUISTI ===
    acquisti = [
        {
            "tag": "buyer",
            "quando": "Al primo acquisto di qualsiasi cosa (tag globale)",
            "rimuovere": "Mai"
        }
    ]

    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        acquisti.append({
            "tag": f"cliente-minicorso-{prod}",
            "quando": "All'acquisto del mini-corso upsell",
            "rimuovere": "Mai"
        })
        acquisti.append({
            "tag": f"cliente-corso-{prod}",
            "quando": "All'acquisto del corso/prodotto principale",
            "rimuovere": "Mai"
        })
    elif tipo_funnel == "semplificato":
        acquisti.append({
            "tag": f"cliente-corso-{prod}",
            "quando": "All'acquisto del corso/prodotto",
            "rimuovere": "Mai"
        })
    elif tipo_funnel == "micro":
        acquisti.append({
            "tag": f"cliente-ebook-{prod}",
            "quando": "All'acquisto dell'ebook/prodotto",
            "rimuovere": "Mai"
        })
    elif tipo_funnel == "applicazione":
        acquisti.append({
            "tag": f"cliente-servizio-{prod}",
            "quando": "Alla firma del contratto",
            "rimuovere": "Mai"
        })

    result["tags_per_categoria"]["acquisti"] = acquisti

    # === TAG POSIZIONE NEL FUNNEL ===
    posizione = []

    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        posizione = [
            {"tag": f"iscritto-webinar-{prod}", "quando": "All'iscrizione al webinar", "rimuovere": "Mai"},
            {"tag": f"partecipato-webinar-{prod}", "quando": "Dopo il webinar (aggiunta manuale)", "rimuovere": "Mai"},
            {"tag": f"visto-replay-{prod}", "quando": "Ha aperto l'email col replay", "rimuovere": "Mai"},
            {"tag": f"non-presentato-{prod}", "quando": "Era iscritto ma non si è presentato", "rimuovere": "Mai"}
        ]

    elif tipo_funnel == "applicazione":
        posizione = [
            {"tag": f"lead-applicazione-{prod}", "quando": "Ha compilato il form applicazione", "rimuovere": "Mai"},
            {"tag": f"lead-qualificato-{prod}", "quando": "Ha superato il routing qualificante", "rimuovere": "Mai"},
            {"tag": f"lead-non-qualificato-{prod}", "quando": "Non ha superato il routing", "rimuovere": "Mai"},
            {"tag": "call-prenotata", "quando": "Ha prenotato la call strategica", "rimuovere": "Mai"},
            {"tag": "call-completata", "quando": "Ha fatto la call (manuale)", "rimuovere": "Mai"},
            {"tag": "call-noshow", "quando": "Non si è presentato alla call", "rimuovere": "Mai"},
            {"tag": "proposta-inviata", "quando": "Dopo invio proposta (manuale)", "rimuovere": "Mai"}
        ]

    result["tags_per_categoria"]["posizione_funnel"] = posizione

    # === TAG ENGAGEMENT ===
    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        result["tags_per_categoria"]["engagement"] = [
            {"tag": "engagement-alto", "quando": "Apre email + risponde WhatsApp + compra mini-corso", "score": "8-10/10"},
            {"tag": "engagement-medio", "quando": "Apre email OPPURE risponde WhatsApp", "score": "4-7/10"},
            {"tag": "engagement-basso", "quando": "Non apre email, non risponde", "score": "1-3/10"}
        ]
    elif tipo_funnel == "applicazione":
        result["tags_per_categoria"]["engagement"] = [
            {"tag": "urgenza-alta", "quando": "Ha detto 'Subito' nel form"},
            {"tag": "urgenza-media", "quando": "Ha detto 'Entro 30 giorni'"},
            {"tag": "urgenza-bassa", "quando": "Ha detto 'Sto esplorando'"}
        ]

    # === TAG SEGMENTO ===
    segmenti = [
        {"tag": "nurture-settimanale", "quando": "Non ha convertito, riceve 1 email/settimana di valore"}
    ]

    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        segmenti.insert(0, {"tag": "webinar-attesa", "quando": "Iscritto al webinar, in attesa dell'evento"})
        segmenti.insert(1, {"tag": "post-webinar-followup", "quando": "Webinar finito, in sequenza follow-up"})

    if tipo_funnel == "applicazione":
        segmenti.insert(0, {"tag": "post-call-followup", "quando": "Call fatta, in sequenza follow-up"})

    result["tags_per_categoria"]["segmento"] = segmenti

    # === TAG SPECIALI ===
    result["tags_per_categoria"]["speciali"] = [
        {"tag": "bridge-servizio", "quando": "Ha espresso interesse per il servizio premium/agenzia"},
        {"tag": "testimonial-raccolto", "quando": "Ha dato un testimonial"},
        {"tag": "referral", "quando": "Arrivato tramite passaparola"}
    ]

    # === MAPPA VISUALE TAG NEL FUNNEL ===
    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        result["mappa_funnel"] = [
            {"step": "Opt-in PDF", "tag_aggiunti": [f"pdf-{lm}"], "tag_rimossi": []},
            {"step": "Compra mini-corso? SÌ", "tag_aggiunti": ["buyer", f"cliente-minicorso-{prod}"], "tag_rimossi": []},
            {"step": "Compra mini-corso? NO", "tag_aggiunti": [], "tag_rimossi": []},
            {"step": "Iscrive webinar? SÌ", "tag_aggiunti": [f"iscritto-webinar-{prod}", "webinar-attesa"], "tag_rimossi": []},
            {"step": "Iscrive webinar? NO", "tag_aggiunti": ["nurture-settimanale"], "tag_rimossi": []},
            {"step": "Engagement pre-webinar", "tag_aggiunti": ["engagement-[livello]"], "tag_rimossi": []},
            {"step": "Partecipa webinar? SÌ", "tag_aggiunti": [f"partecipato-webinar-{prod}"], "tag_rimossi": []},
            {"step": "Partecipa webinar? NO", "tag_aggiunti": [f"non-presentato-{prod}"], "tag_rimossi": []},
            {"step": "Compra prodotto? SÌ", "tag_aggiunti": ["buyer", f"cliente-corso-{prod}"], "tag_rimossi": ["webinar-attesa", "post-webinar-followup"]},
            {"step": "Compra prodotto? NO", "tag_aggiunti": ["post-webinar-followup"], "tag_rimossi": []},
            {"step": "Dopo follow-up, compra? SÌ", "tag_aggiunti": ["buyer", f"cliente-corso-{prod}"], "tag_rimossi": ["post-webinar-followup"]},
            {"step": "Dopo follow-up, compra? NO", "tag_aggiunti": ["nurture-settimanale"], "tag_rimossi": ["post-webinar-followup"]}
        ]
    elif tipo_funnel == "applicazione":
        result["mappa_funnel"] = [
            {"step": "Form applicazione compilato", "tag_aggiunti": [f"lead-applicazione-{prod}"], "tag_rimossi": []},
            {"step": "Routing: qualificato", "tag_aggiunti": [f"lead-qualificato-{prod}", "urgenza-[livello]"], "tag_rimossi": []},
            {"step": "Routing: non qualificato", "tag_aggiunti": [f"lead-non-qualificato-{prod}", "nurture-settimanale"], "tag_rimossi": []},
            {"step": "Prenota call", "tag_aggiunti": ["call-prenotata"], "tag_rimossi": []},
            {"step": "Fa la call", "tag_aggiunti": ["call-completata"], "tag_rimossi": []},
            {"step": "Chiude in call", "tag_aggiunti": ["buyer", f"cliente-servizio-{prod}"], "tag_rimossi": ["post-call-followup"]},
            {"step": "Non chiude", "tag_aggiunti": ["post-call-followup"], "tag_rimossi": []},
            {"step": "Dopo follow-up, non chiude", "tag_aggiunti": ["nurture-settimanale"], "tag_rimossi": ["post-call-followup"]}
        ]
    elif tipo_funnel == "micro":
        result["mappa_funnel"] = [
            {"step": "Opt-in / visita", "tag_aggiunti": [f"pdf-{lm}"], "tag_rimossi": []},
            {"step": "Compra", "tag_aggiunti": ["buyer", f"cliente-ebook-{prod}"], "tag_rimossi": []},
            {"step": "Non compra dopo email", "tag_aggiunti": ["nurture-settimanale"], "tag_rimossi": []}
        ]
    elif tipo_funnel == "semplificato":
        result["mappa_funnel"] = [
            {"step": "Opt-in PDF", "tag_aggiunti": [f"pdf-{lm}"], "tag_rimossi": []},
            {"step": "Compra dopo VSL/email", "tag_aggiunti": ["buyer", f"cliente-corso-{prod}"], "tag_rimossi": []},
            {"step": "Non compra dopo follow-up", "tag_aggiunti": ["nurture-settimanale"], "tag_rimossi": []}
        ]

    return result


def print_tags(tags: dict) -> None:
    """Stampa il tag system in formato leggibile."""

    print("=" * 65)
    print("  TAG SYSTEM COMPLETO")
    print("=" * 65)

    print(f"\n📐 CONVENZIONE: {tags['convenzione_naming']}")

    print("\n📏 REGOLE:")
    for regola in tags["regole"]:
        print(f"   • {regola}")

    for categoria, tag_list in tags["tags_per_categoria"].items():
        cat_label = categoria.replace("_", " ").upper()
        print(f"\n{'─' * 65}")
        print(f"  {cat_label}")
        print(f"{'─' * 65}")
        for t in tag_list:
            tag_name = t["tag"]
            quando = t["quando"]
            extra = ""
            if "rimuovere" in t:
                extra = f" | Rimuovere: {t['rimuovere']}"
            if "score" in t:
                extra = f" | Score: {t['score']}"
            print(f"   🏷️  {tag_name}")
            print(f"      Quando: {quando}{extra}")

    if tags["mappa_funnel"]:
        print(f"\n{'═' * 65}")
        print("  MAPPA TAG NEL FUNNEL")
        print(f"{'═' * 65}")
        for step_info in tags["mappa_funnel"]:
            step = step_info["step"]
            aggiunti = step_info["tag_aggiunti"]
            rimossi = step_info["tag_rimossi"]
            print(f"\n   📍 {step}")
            if aggiunti:
                print(f"      + {', '.join(aggiunti)}")
            if rimossi:
                print(f"      - RIMUOVI: {', '.join(rimossi)}")
            if not aggiunti and not rimossi:
                print(f"      (nessuna modifica tag)")

    print()


def main():
    parser = argparse.ArgumentParser(description="Genera il tag system completo per un funnel")
    parser.add_argument("--prodotto", help="Nome prodotto (es: corso-email-marketing)")
    parser.add_argument("--lead-magnet", default="", help="Nome lead magnet (es: 5-template-bf)")
    parser.add_argument("--tipo", default="unico_perfetto_standard",
                        help="Tipo funnel: micro, semplificato, unico_perfetto_standard, unico_perfetto_completo, applicazione")
    parser.add_argument("--json", action="store_true", help="Output solo JSON")
    parser.add_argument("--interattivo", action="store_true")

    args = parser.parse_args()

    if args.interattivo or not args.prodotto:
        print("\n" + "=" * 65)
        print("  TAG GENERATOR — Generazione Interattiva")
        print("=" * 65)
        prodotto = input("\n📦 Nome prodotto (es: corso-email-marketing): ").strip()
        lead_magnet = input("📄 Nome lead magnet (es: 5-template-bf): ").strip()
        tipo = input("🏗️  Tipo funnel (micro/semplificato/unico_perfetto_standard/unico_perfetto_completo/applicazione): ").strip() or "unico_perfetto_standard"
        tags = generate_tags(prodotto, lead_magnet, tipo)
    else:
        tags = generate_tags(args.prodotto, args.lead_magnet, args.tipo)

    if args.json:
        print(json.dumps(tags, ensure_ascii=False, indent=2))
    else:
        print_tags(tags)

    json_path = "tag_system.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(tags, f, ensure_ascii=False, indent=2)
    print(f"💾 Salvato in {json_path}")


if __name__ == "__main__":
    main()

scripts/funnel_diagnostics.py
Python
#!/usr/bin/env python3
"""
Funnel Diagnostics — Analizza le metriche di un funnel,
confronta con i benchmark e identifica il collo di bottiglia.

Uso:
    python funnel_diagnostics.py --interattivo
    python funnel_diagnostics.py --metriche '{"opt_in": 25, "upsell": 3, "iscrizione_webinar": 5, "show_rate": 8, "retention_pitch": 65, "conversione_webinar": 6, "conversione_followup": 1}'
"""

import argparse
import json
import sys

BENCHMARKS = {
    "opt_in": {
        "label": "Visitatori → Opt-in",
        "benchmark": 30,
        "soglia_critica": 15,
        "unita": "%"
    },
    "upsell": {
        "label": "Opt-in → Acquisto upsell",
        "benchmark": 5,
        "soglia_critica": 2,
        "unita": "%"
    },
    "iscrizione_webinar": {
        "label": "Lead → Iscritti webinar",
        "benchmark": 15,
        "soglia_critica": 8,
        "unita": "%"
    },
    "show_rate": {
        "label": "Iscritti → Presenti (show rate)",
        "benchmark": 30,
        "soglia_critica": 15,
        "unita": "%"
    },
    "retention_pitch": {
        "label": "Presenti → Restano fino al pitch",
        "benchmark": 60,
        "soglia_critica": 40,
        "unita": "%"
    },
    "conversione_webinar": {
        "label": "Presenti → Acquisto (durante webinar)",
        "benchmark": 5,
        "soglia_critica": 2,
        "unita": "%"
    },
    "conversione_followup": {
        "label": "Post-webinar → Acquisto (follow-up)",
        "benchmark": 3,
        "soglia_critica": 1,
        "unita": "%"
    }
}

DIAGNOSI = {
    "opt_in": {
        "cause": [
            {
                "causa": "Headline debole o non allineata al traffico in ingresso",
                "test": "Scrivi 3 headline alternative, testa per 5 giorni ciascuna",
                "priorita": 1
            },
            {
                "causa": "Il traffico è sbagliato — la fonte manda persone non in target",
                "test": "Separa le metriche per fonte di traffico, misura ognuna separatamente",
                "priorita": 2
            },
            {
                "causa": "Pagina troppo lenta (>3 sec) o non responsive su mobile",
                "test": "Testa da mobile, verifica velocità con PageSpeed Insights",
                "priorita": 3
            },
            {
                "causa": "Troppi elementi di distrazione (navigazione, link, sidebar)",
                "test": "Rimuovi tutto tranne headline + bullet + form. Zero link esterni",
                "priorita": 4
            }
        ]
    },
    "upsell": {
        "cause": [
            {
                "causa": "La VSL non convince — il posizionamento 'mappa vs navigatore' non è chiaro",
                "test": "Ri-registra la VSL con messaging diverso, enfatizza il complemento al PDF",
                "priorita": 1
            },
            {
                "causa": "Il prezzo è troppo alto per un impulso subito dopo l'opt-in",
                "test": "Testa un prezzo più basso (€15 vs €27 vs €47)",
                "priorita": 2
            },
            {
                "causa": "Il lead non capisce il valore aggiunto rispetto al PDF gratuito",
                "test": "Riscrivi i bullet per enfatizzare cosa c'è nel corso che NON c'è nel PDF",
                "priorita": 3
            }
        ]
    },
    "iscrizione_webinar": {
        "cause": [
            {
                "causa": "La headline del webinar non è abbastanza compelling — la grande promessa è debole",
                "test": "Riscrivi con promessa più grande e specifica. Non 'Webinar su X' ma 'Come ottenere Y in Z tempo'",
                "priorita": 1
            },
            {
                "causa": "Troppo tempo tra opt-in e invito al webinar — il lead si è raffreddato",
                "test": "Metti la VSL evento nella pagina immediatamente successiva all'opt-in/upsell",
                "priorita": 2
            },
            {
                "causa": "La VSL evento è troppo lunga o non cattura nei primi 30 secondi",
                "test": "Ri-registra i primi 2 minuti. Parti con il risultato, non con 'ciao mi chiamo...'",
                "priorita": 3
            },
            {
                "causa": "Il lead magnet attira curiosi non in target per il prodotto principale",
                "test": "Verifica se i lead che SI iscrivono sono diversi da quelli che non si iscrivono. Valuta un PDF più specifico",
                "priorita": 4
            }
        ]
    },
    "show_rate": {
        "cause": [
            {
                "causa": "Mancano WhatsApp e/o chiamate pre-webinar — solo email non basta",
                "test": "Aggiungi telefono obbligatorio + WhatsApp (benvenuto + reminder -24h, -1h) + 1 chiamata entro 48h",
                "priorita": 1
            },
            {
                "causa": "Il webinar è troppo lontano dalla data di iscrizione (>7 giorni)",
                "test": "Programma webinar più frequenti (ogni 5-7 giorni, non una volta al mese)",
                "priorita": 2
            },
            {
                "causa": "Reminder insufficienti",
                "test": "Sequenza completa: -24h, -3h, -1h, -30min (email + WhatsApp)",
                "priorita": 3
            }
        ]
    },
    "retention_pitch": {
        "cause": [
            {
                "causa": "Il contenuto del webinar non è abbastanza engaging — storie deboli o generiche",
                "test": "Accorcia di 15-20 min; rafforza le storie con dettagli specifici (numeri, date, momenti emotivi)",
                "priorita": 1
            },
            {
                "causa": "Il prospect ha già ottenuto quello che voleva dal contenuto gratuito — hai dato troppo 'how-to'",
                "test": "Riduci il 'how-to' nel webinar; aumenta il 'why' e il 'what' senza dare tutto il 'how'",
                "priorita": 2
            }
        ]
    },
    "conversione_webinar": {
        "cause": [
            {
                "causa": "Il pitch è scollegato dal contenuto — la transizione è brusca",
                "test": "Riscrivi la transizione, collegala naturalmente all'ultimo punto di contenuto",
                "priorita": 1
            },
            {
                "causa": "L'offerta non è abbastanza chiara — il prospect non capisce cosa compra",
                "test": "Presenta benefici concreti, non nomi di moduli. 'Imparerai X' batte 'Modulo 3'",
                "priorita": 2
            },
            {
                "causa": "Il prezzo è percepito come troppo alto rispetto al valore dimostrato",
                "test": "Rafforza i bonus, aggiungi garanzia più forte, testa prezzo diverso",
                "priorita": 3
            },
            {
                "causa": "Le obiezioni non sono state gestite durante il webinar",
                "test": "Aggiungi gestione obiezioni prima del pitch o durante il Q&A con risposte preparate",
                "priorita": 4
            }
        ]
    },
    "conversione_followup": {
        "cause": [
            {
                "causa": "Email post-webinar generiche o inesistenti",
                "test": "Crea sequenza 5 email in 5 giorni con angoli diversi (replay, obiezione, caso studio, bonus, urgenza)",
                "priorita": 1
            },
            {
                "causa": "Nessun contatto 1:1 — solo email broadcast",
                "test": "Aggiungi DM personalizzati ai lead più caldi (partecipato + engagement alto)",
                "priorita": 2
            },
            {
                "causa": "L'urgenza è scaduta e non c'è motivo per agire ora",
                "test": "Crea urgenza limitata post-webinar: 48h per bonus extra o prezzo speciale",
                "priorita": 3
            }
        ]
    }
}


def analyze(metriche: dict) -> dict:
    """Analizza le metriche e produce la diagnosi."""

    results = {
        "gap_analysis": [],
        "colli_bottiglia": [],
        "ok": [],
        "piano_azione": [],
        "simulazione_impatto": None
    }

    # Gap analysis
    for key, bench in BENCHMARKS.items():
        if key not in metriche:
            continue
        valore = metriche[key]
        gap = valore - bench["benchmark"]
        gap_pct = gap  # già in percentuale

        stato = "ok"
        if valore < bench["soglia_critica"]:
            stato = "critico"
        elif valore < bench["benchmark"]:
            stato = "sotto"

        entry = {
            "passaggio": bench["label"],
            "valore": valore,
            "benchmark": bench["benchmark"],
            "soglia_critica": bench["soglia_critica"],
            "gap": gap,
            "stato": stato
        }

        results["gap_analysis"].append(entry)

        if stato == "critico":
            results["colli_bottiglia"].append({
                "passaggio": bench["label"],
                "chiave": key,
                "valore": valore,
                "benchmark": bench["benchmark"],
                "gap": abs(gap),
                "cause_e_test": DIAGNOSI.get(key, {}).get("cause", [])
            })
        elif stato == "ok":
            results["ok"].append(bench["label"])

    # Ordina colli di bottiglia per gap (dal più grave)
    results["colli_bottiglia"].sort(key=lambda x: x["gap"], reverse=True)

    # Piano d'azione prioritizzato
    for i, collo in enumerate(results["colli_bottiglia"]):
        for causa in collo["cause_e_test"][:2]:  # top 2 cause per collo
            results["piano_azione"].append({
                "priorita": i + 1,
                "passaggio": collo["passaggio"],
                "causa": causa["causa"],
                "test": causa["test"],
                "metrica_successo": f"{collo['chiave']} da {collo['valore']}% a >{collo['benchmark'] * 0.8:.0f}% (80% del benchmark)"
            })

    # Simulazione impatto (se ci sono abbastanza metriche)
    if all(k in metriche for k in ["opt_in", "iscrizione_webinar", "show_rate", "conversione_webinar"]):
        lead_base = 1000
        oggi = {
            "visitatori": lead_base,
            "lead": round(lead_base * metriche["opt_in"] / 100),
            "iscritti": round(lead_base * metriche["opt_in"] / 100 * metriche["iscrizione_webinar"] / 100),
        }
        oggi["presenti"] = round(oggi["iscritti"] * metriche["show_rate"] / 100)
        oggi["acquisti"] = round(oggi["presenti"] * metriche["conversione_webinar"] / 100, 1)

        # Dopo i fix: usa i benchmark dove c'è un collo, mantieni i valori attuali dove è OK
        dopo = {"visitatori": lead_base}
        opt_fix = BENCHMARKS["opt_in"]["benchmark"] if metriche.get("opt_in", 100) < BENCHMARKS["opt_in"]["soglia_critica"] else metriche.get("opt_in", 30)
        isc_fix = BENCHMARKS["iscrizione_webinar"]["benchmark"] if metriche.get("iscrizione_webinar", 100) < BENCHMARKS["iscrizione_webinar"]["soglia_critica"] else metriche.get("iscrizione_webinar", 15)
        show_fix = BENCHMARKS["show_rate"]["benchmark"] if metriche.get("show_rate", 100) < BENCHMARKS["show_rate"]["soglia_critica"] else metriche.get("show_rate", 30)
        conv_fix = BENCHMARKS["conversione_webinar"]["benchmark"] if metriche.get("conversione_webinar", 100) < BENCHMARKS["conversione_webinar"]["soglia_critica"] else metriche.get("conversione_webinar", 5)

        dopo["lead"] = round(lead_base * opt_fix / 100)
        dopo["iscritti"] = round(dopo["lead"] * isc_fix / 100)
        dopo["presenti"] = round(dopo["iscritti"] * show_fix / 100)
        dopo["acquisti"] = round(dopo["presenti"] * conv_fix / 100, 1)

        results["simulazione_impatto"] = {
            "base_visitatori": lead_base,
            "oggi": oggi,
            "dopo_fix": dopo,
            "nota": "Stime conservative: per i colli di bottiglia si usa il benchmark come target"
        }

    return results


def print_results(results: dict) -> None:
    """Stampa i risultati della diagnosi."""

    print("=" * 65)
    print("  DIAGNOSI FUNNEL")
    print("=" * 65)

    # Gap analysis
    print("\n📊 GAP ANALYSIS")
    print(f"{'─' * 65}")
    print(f"  {'Passaggio':<40} {'Tuo':<8} {'Bench.':<8} {'Gap':<8} {'Stato'}")
    print(f"{'─' * 65}")
    for entry in results["gap_analysis"]:
        stato_icon = {"ok": "✅", "sotto": "⚠️", "critico": "🔴"}[entry["stato"]]
        gap_str = f"{entry['gap']:+.0f}%"
        print(f"  {entry['passaggio']:<40} {entry['valore']:<8.0f} {entry['benchmark']:<8.0f} {gap_str:<8} {stato_icon}")

    # Colli di bottiglia
    if results["colli_bottiglia"]:
        print(f"\n{'═' * 65}")
        print("  🔴 COLLI DI BOTTIGLIA (ordinati per gravità)")
        print(f"{'═' * 65}")
        for i, collo in enumerate(results["colli_bottiglia"], 1):
            print(f"\n  #{i} — {collo['passaggio']}")
            print(f"     Tuo valore: {collo['valore']}% | Benchmark: >{collo['benchmark']}% | Gap: -{collo['gap']}%")
            print(f"     Cause probabili:")
            for causa in collo["cause_e_test"]:
                print(f"       {causa['priorita']}. {causa['causa']}")
                print(f"          Test: {causa['test']}")
    else:
        print("\n  ✅ Nessun collo di bottiglia critico trovato!")

    # Passaggi OK
    if results["ok"]:
        print(f"\n  ✅ PASSAGGI OK (non toccare): {', '.join(results['ok'])}")

    # Piano d'azione
    if results["piano_azione"]:
        print(f"\n{'═' * 65}")
        print("  📋 PIANO D'AZIONE PRIORITIZZATO")
        print(f"{'═' * 65}")
        for azione in results["piano_azione"]:
            print(f"\n  🥇 Priorità {azione['priorita']} — {azione['passaggio']}")
            print(f"     Causa: {azione['causa']}")
            print(f"     Test: {azione['test']}")
            print(f"     Metrica successo: {azione['metrica_successo']}")

    # Simulazione
    if results["simulazione_impatto"]:
        sim = results["simulazione_impatto"]
        print(f"\n{'═' * 65}")
        print(f"  📈 SIMULAZIONE IMPATTO (su {sim['base_visitatori']:,} visitatori)")
        print(f"{'═' * 65}")
        print(f"\n  OGGI:")
        for k, v in sim["oggi"].items():
            print(f"    {k}: {v}")
        print(f"\n  DOPO I FIX:")
        for k, v in sim["dopo_fix"].items():
            print(f"    {k}: {v}")

    print(f"\n{'─' * 65}")
    print("  REGOLA D'ORO: Non cambiare tutto. Il problema è quasi")
    print("  sempre in 1 punto. Trovalo, fixalo, misura.")
    print(f"{'─' * 65}\n")


def interactive_mode():
    """Modo interattivo."""
    print("\n" + "=" * 65)
    print("  FUNNEL DIAGNOSTICS — Inserisci le tue metriche")
    print("=" * 65)
    print("  (Lascia vuoto e premi Invio per saltare un passaggio)\n")

    metriche = {}
    for key, bench in BENCHMARKS.items():
        try:
            val = input(f"  {bench['label']} (benchmark: >{bench['benchmark']}%): ").strip()
            if val:
                metriche[key] = float(val)
        except ValueError:
            print("  ⚠️ Valore non valido, salto.")

    if not metriche:
        print("\n❌ Nessuna metrica inserita.")
        sys.exit(1)

    results = analyze(metriche)
    print_results(results)

    json_path = "funnel_diagnostics.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"💾 Salvato in {json_path}")


def main():
    parser = argparse.ArgumentParser(description="Diagnostica un funnel che non converte")
    parser.add_argument("--metriche", help='JSON con le metriche. Es: \'{"opt_in": 25, "show_rate": 8}\'')
    parser.add_argument("--interattivo", action="store_true")
    parser.add_argument("--json", action="store_true", help="Output solo JSON")

    args = parser.parse_args()

    if args.interattivo or not args.metriche:
        interactive_mode()
        return

    metriche = json.loads(args.metriche)
    results = analyze(metriche)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print_results(results)


if __name__ == "__main__":
    main()

scripts/automation_mapper.py
Python
#!/usr/bin/env python3
"""
Automation Mapper — Genera la mappa completa delle automazioni
(trigger → azione → timing) per un funnel.

Uso:
    python automation_mapper.py --tipo "unico_perfetto_standard" --prodotto "corso-email" --piattaforme "activecampaign,elementor,stripe"
    python automation_mapper.py --interattivo
"""

import argparse
import json
import sys


def generate_automations(tipo_funnel: str, prodotto: str, piattaforme: list = None) -> dict:
    """Genera la mappa automazioni completa."""

    prod = prodotto.lower().replace(" ", "-")
    plat = [p.strip().lower() for p in piattaforme] if piattaforme else []

    # Identifica piattaforme per tipo
    email_tool = next((p for p in plat if p in ("activecampaign", "mailchimp", "convertkit", "getresponse", "mailerlite", "brevo", "sendinblue")), "email tool")
    page_builder = next((p for p in plat if p in ("elementor", "webflow", "wordpress", "clickfunnels", "leadpages", "unbounce", "carrd")), "page builder")
    checkout = next((p for p in plat if p in ("stripe", "paypal", "woocommerce", "gumroad", "thrivecart", "samcart")), "checkout")
    webinar_tool = next((p for p in plat if p in ("zoom", "webinarjam", "everwebinar", "demio", "livestorm", "streamyard")), "webinar tool")

    result = {
        "tipo_funnel": tipo_funnel,
        "prodotto": prodotto,
        "piattaforme": {
            "email": email_tool,
            "pagine": page_builder,
            "checkout": checkout,
            "webinar": webinar_tool
        },
        "automazioni": [],
        "pixel_events": [],
        "note_implementazione": []
    }

    # AUTOMAZIONI PER TIPO DI FUNNEL

    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        result["automazioni"] = [
            # STEP 1: OPT-IN
            {
                "step": "STEP 1 — OPT-IN",
                "trigger": "Submit form opt-in",
                "azioni": [
                    {"azione": f"Aggiungi a lista principale", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: pdf-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email benvenuto con link PDF", "timing": "Entro 2 min", "tool": email_tool},
                    {"azione": "Redirect → Pagina upsell", "timing": "Immediato", "tool": page_builder}
                ]
            },
            # STEP 2: UPSELL
            {
                "step": "STEP 2 — UPSELL: COMPRA",
                "trigger": f"Acquisto completato ({checkout})",
                "azioni": [
                    {"azione": "TAG: buyer", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: cliente-minicorso-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email: ricevuta + link accesso corso", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Redirect → Pagina conferma acquisto", "timing": "Immediato", "tool": page_builder},
                    {"azione": "Email con link VSL evento", "timing": "Entro 24h", "tool": email_tool}
                ]
            },
            {
                "step": "STEP 2 — UPSELL: NON COMPRA",
                "trigger": "Click su 'No grazie'",
                "azioni": [
                    {"azione": "Redirect → Pagina VSL evento (Step 3)", "timing": "Immediato", "tool": page_builder}
                ]
            },
            # STEP 4: ISCRIZIONE WEBINAR
            {
                "step": "STEP 4 — ISCRIZIONE WEBINAR",
                "trigger": "Submit form iscrizione webinar",
                "azioni": [
                    {"azione": f"TAG: iscritto-webinar-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Aggiungi a segmento 'Webinar-Attesa'", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Start automazione pre-webinar (email 1/gg)", "timing": "Immediato", "tool": email_tool},
                    {"azione": "WhatsApp benvenuto + domanda", "timing": "Entro 1h", "tool": "WhatsApp (manuale o Spoki/Twilio)"},
                    {"azione": "Task: chiamata consulente", "timing": "Entro 24-48h", "tool": f"{email_tool} task o CRM"},
                    {"azione": "Redirect → Thank You Page + Aggiungi a Calendario", "timing": "Immediato", "tool": page_builder}
                ]
            },
            # STEP 5: PRE-WEBINAR
            {
                "step": "STEP 5 — REMINDER PRE-WEBINAR",
                "trigger": "Timer countdown prima del webinar",
                "azioni": [
                    {"azione": "Email reminder", "timing": "-24h", "tool": email_tool},
                    {"azione": "Email reminder", "timing": "-3h", "tool": email_tool},
                    {"azione": "WhatsApp reminder", "timing": "-24h", "tool": "WhatsApp"},
                    {"azione": "Email reminder + link", "timing": "-1h", "tool": email_tool},
                    {"azione": "WhatsApp con link", "timing": "-1h", "tool": "WhatsApp"},
                    {"azione": "Email ultimo reminder", "timing": "-30min", "tool": email_tool}
                ]
            },
            # STEP 6-7: POST-WEBINAR
            {
                "step": "STEP 6/7 — POST-WEBINAR: HA COMPRATO",
                "trigger": f"Acquisto prodotto principale ({checkout})",
                "azioni": [
                    {"azione": "TAG: buyer (se non già presente)", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: cliente-corso-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "RIMUOVI TAG: webinar-attesa", "timing": "Immediato", "tool": email_tool},
                    {"azione": "RIMUOVI TAG: post-webinar-followup (se presente)", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email onboarding + accesso corso", "timing": "Immediato", "tool": email_tool},
                    {"azione": "STOP automazione follow-up (se attiva)", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "STEP 7 — POST-WEBINAR: NON HA COMPRATO (ha partecipato)",
                "trigger": f"TAG manuale: partecipato-webinar-{prod} + nessun acquisto",
                "azioni": [
                    {"azione": f"TAG: partecipato-webinar-{prod}", "timing": "Dopo il webinar (manuale)", "tool": email_tool},
                    {"azione": "TAG: post-webinar-followup", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email replay + recap offerta", "timing": "+1 giorno", "tool": email_tool},
                    {"azione": "Start automazione follow-up (5 email in 5 gg)", "timing": "+1 giorno", "tool": email_tool}
                ]
            },
            {
                "step": "STEP 7 — POST-WEBINAR: NON SI È PRESENTATO",
                "trigger": f"TAG manuale: non-presentato-{prod}",
                "azioni": [
                    {"azione": f"TAG: non-presentato-{prod}", "timing": "Dopo il webinar (manuale)", "tool": email_tool},
                    {"azione": "TAG: post-webinar-followup", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email: 'Mi dispiace non averti visto' + link replay", "timing": "+1 giorno", "tool": email_tool},
                    {"azione": "Start automazione follow-up (5 email in 5 gg)", "timing": "+1 giorno", "tool": email_tool}
                ]
            },
            # STEP 8: NURTURE
            {
                "step": "STEP 8 — NURTURE",
                "trigger": "Fine sequenza follow-up senza acquisto",
                "azioni": [
                    {"azione": "TAG: nurture-settimanale", "timing": "Immediato", "tool": email_tool},
                    {"azione": "RIMUOVI TAG: post-webinar-followup", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Start automazione nurture (1 email/settimana)", "timing": "Immediato", "tool": email_tool}
                ]
            }
        ]

        # Chiamate e WhatsApp extra per il completo
        if tipo_funnel == "unico_perfetto_completo":
            result["automazioni"].append({
                "step": "EXTRA COMPLETO — FOLLOW-UP 1:1",
                "trigger": "Post-webinar, lead con engagement alto",
                "azioni": [
                    {"azione": "DM personalizzato (WhatsApp o email 1:1)", "timing": "+1 giorno", "tool": "WhatsApp / Email manuale"},
                    {"azione": "Offerta call gratuita 15 min", "timing": "+2 giorni", "tool": "Calendly + email"},
                    {"azione": "Se prenota → TAG: call-prenotata", "timing": "Al booking", "tool": email_tool}
                ]
            })

        # Pixel
        result["pixel_events"] = [
            {"evento": "Lead", "trigger": "Submit form opt-in", "dove": f"Thank you page / {page_builder}"},
            {"evento": "Purchase", "trigger": "Acquisto mini-corso", "dove": f"Pagina conferma / {checkout}", "valore": "€[prezzo-minicorso]"},
            {"evento": "WebinarRegistration", "trigger": "Submit form iscrizione webinar", "dove": f"Thank you page webinar"},
            {"evento": "Purchase", "trigger": "Acquisto prodotto principale", "dove": f"Pagina conferma / {checkout}", "valore": "€[prezzo-prodotto]"}
        ]

    elif tipo_funnel == "semplificato":
        result["automazioni"] = [
            {
                "step": "OPT-IN",
                "trigger": "Submit form opt-in",
                "azioni": [
                    {"azione": f"TAG: pdf-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email benvenuto con PDF", "timing": "Entro 2 min", "tool": email_tool},
                    {"azione": "Redirect → Pagina VSL vendita", "timing": "Immediato", "tool": page_builder}
                ]
            },
            {
                "step": "ACQUISTO",
                "trigger": f"Acquisto ({checkout})",
                "azioni": [
                    {"azione": "TAG: buyer", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: cliente-corso-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email accesso corso", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "FOLLOW-UP (non compra)",
                "trigger": "3 giorni senza acquisto dopo opt-in",
                "azioni": [
                    {"azione": "Email follow-up 1: angolo 1", "timing": "+1 giorno", "tool": email_tool},
                    {"azione": "Email follow-up 2: angolo 2", "timing": "+2 giorni", "tool": email_tool},
                    {"azione": "Email follow-up 3: urgenza", "timing": "+3 giorni", "tool": email_tool}
                ]
            },
            {
                "step": "NURTURE",
                "trigger": "Fine follow-up senza acquisto",
                "azioni": [
                    {"azione": "TAG: nurture-settimanale", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Start nurture 1 email/settimana", "timing": "Immediato", "tool": email_tool}
                ]
            }
        ]
        result["pixel_events"] = [
            {"evento": "Lead", "trigger": "Submit form opt-in", "dove": page_builder},
            {"evento": "Purchase", "trigger": "Acquisto", "dove": checkout, "valore": "€[prezzo]"}
        ]

    elif tipo_funnel == "micro":
        result["automazioni"] = [
            {
                "step": "OPT-IN (se con lead magnet)",
                "trigger": "Submit form",
                "azioni": [
                    {"azione": f"TAG: pdf-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email con PDF gratuito", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "SEQUENZA VENDITA",
                "trigger": "Post opt-in",
                "azioni": [
                    {"azione": "Email 1: contenuto + teaser ebook", "timing": "+2 giorni", "tool": email_tool},
                    {"azione": "Email 2: pitch ebook completo", "timing": "+4 giorni", "tool": email_tool},
                    {"azione": "Email 3: ultimo reminder", "timing": "+7 giorni", "tool": email_tool}
                ]
            },
            {
                "step": "ACQUISTO",
                "trigger": f"Acquisto ({checkout})",
                "azioni": [
                    {"azione": "TAG: buyer", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: cliente-ebook-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email consegna ebook", "timing": "Immediato", "tool": email_tool},
                    {"azione": "STOP sequenza vendita", "timing": "Immediato", "tool": email_tool}
                ]
            }
        ]
        result["pixel_events"] = [
            {"evento": "Lead", "trigger": "Submit form", "dove": page_builder},
            {"evento": "Purchase", "trigger": "Acquisto", "dove": checkout, "valore": "€[prezzo]"}
        ]

    elif tipo_funnel == "applicazione":
        result["automazioni"] = [
            {
                "step": "FORM APPLICAZIONE — QUALIFICATO",
                "trigger": "Submit form + supera routing",
                "azioni": [
                    {"azione": f"TAG: lead-qualificato-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "TAG: urgenza-[livello]", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Notifica al venditore assegnato", "timing": "Immediato", "tool": f"{email_tool} / CRM / Slack"},
                    {"azione": "Redirect → Booking page (Calendly/Cal.com)", "timing": "Immediato", "tool": page_builder},
                    {"azione": "Email conferma + 'cosa aspettarti dalla call'", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "FORM APPLICAZIONE — NON QUALIFICATO",
                "trigger": "Submit form + NON supera routing",
                "azioni": [
                    {"azione": f"TAG: lead-non-qualificato-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Redirect → Pagina risorse gratuite", "timing": "Immediato", "tool": page_builder},
                    {"azione": "TAG: nurture-settimanale", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "BOOKING COMPLETATO",
                "trigger": "Lead prenota call (Calendly)",
                "azioni": [
                    {"azione": "TAG: call-prenotata", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email pre-call 1: conferma + caso studio", "timing": "Immediato", "tool": email_tool},
                    {"azione": "WhatsApp dal venditore assegnato", "timing": "Immediato", "tool": "WhatsApp manuale"},
                    {"azione": "Email pre-call 2: reminder + 'cosa preparare'", "timing": "-24h dalla call", "tool": email_tool},
                    {"azione": "WhatsApp reminder", "timing": "-1h dalla call", "tool": "WhatsApp"}
                ]
            },
            {
                "step": "POST-CALL — CHIUDE",
                "trigger": "Firma contratto (manuale)",
                "azioni": [
                    {"azione": "TAG: buyer", "timing": "Immediato", "tool": email_tool},
                    {"azione": f"TAG: cliente-servizio-{prod}", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email onboarding", "timing": "Immediato", "tool": email_tool},
                    {"azione": "STOP automazioni follow-up", "timing": "Immediato", "tool": email_tool}
                ]
            },
            {
                "step": "POST-CALL — NON CHIUDE",
                "trigger": "Call completata senza chiusura",
                "azioni": [
                    {"azione": "TAG: post-call-followup", "timing": "Immediato", "tool": email_tool},
                    {"azione": "Email 1: recap call + proposta scritta", "timing": "+1 giorno", "tool": email_tool},
                    {"azione": "Email 2: caso studio simile", "timing": "+3 giorni", "tool": email_tool},
                    {"azione": "Email 3: 'domande sulla proposta?' + offerta 2ª call", "timing": "+7 giorni", "tool": email_tool},
                    {"azione": "Call di follow-up del venditore", "timing": "+14 giorni", "tool": "Telefono"},
                    {"azione": "Se non chiude → TAG: nurture-settimanale, RIMUOVI: post-call-followup", "timing": "+21 giorni", "tool": email_tool}
                ]
            }
        ]
        result["pixel_events"] = [
            {"evento": "Lead", "trigger": "Submit form applicazione (TUTTI)", "dove": page_builder, "nota": "Per il volume totale"},
            {"evento": "QualifiedLead", "trigger": "Booking completato (SOLO qualificati)", "dove": "Booking page",
             "nota": "⚠️ QUESTO è l'evento su cui ottimizzare le ads — non 'Lead'"}
        ]
        result["note_implementazione"].append(
            "CRITICO: Il pixel di conversione per l'ottimizzazione ads si attiva SOLO sul booking dei qualificati. "
            "Senza questo routing, l'algoritmo ads ottimizza per volume (= lead economici = non qualificati)."
        )

    # Note per piattaforme specifiche
    if "activecampaign" in plat:
        result["note_implementazione"].append(
            "ActiveCampaign: usa 'Automations' per le sequenze email. Trigger: 'Tag is added'. "
            "Per i task chiamata: usa 'Add a task' dentro l'automation. "
            "Per il routing: usa 'If/Else' dentro l'automation basato sui custom field del form."
        )
    if "mailchimp" in plat:
        result["note_implementazione"].append(
            "Mailchimp: usa 'Customer Journeys' (piano Standard+) per le automazioni. "
            "I tag si applicano via 'Tag contact'. Per sequenze multi-email usa 'Classic Automations'. "
            "Limitazione: Mailchimp ha meno flessibilità nel routing rispetto ad ActiveCampaign."
        )
    if "stripe" in plat:
        result["note_implementazione"].append(
            f"Stripe: collega a {email_tool} via webhook o Zapier. "
            "Evento 'checkout.session.completed' → applica tag buyer + tag specifico prodotto."
        )

    return result


def print_automations(result: dict) -> None:
    """Stampa le automazioni in formato leggibile."""

    print("=" * 70)
    print(f"  MAPPA AUTOMAZIONI — {result['tipo_funnel'].upper()}")
    print(f"  Prodotto: {result['prodotto']}")
    print("=" * 70)

    print(f"\n🔧 PIATTAFORME:")
    for k, v in result["piattaforme"].items():
        print(f"   {k.title()}: {v}")

    for auto in result["automazioni"]:
        print(f"\n{'─' * 70}")
        print(f"  📍 {auto['step']}")
        print(f"  ⚡ Trigger: {auto['trigger']}")
        print(f"{'─' * 70}")
        for i, az in enumerate(auto["azioni"], 1):
            print(f"   {i}. {az['azione']}")
            print(f"      ⏱  {az['timing']} | 🔧 {az['tool']}")

    if result["pixel_events"]:
        print(f"\n{'═' * 70}")
        print("  📊 PIXEL / TRACKING EVENTS")
        print(f"{'═' * 70}")
        for px in result["pixel_events"]:
            print(f"\n   📌 Evento: {px['evento']}")
            print(f"      Trigger: {px['trigger']}")
            print(f"      Dove: {px['dove']}")
            if "valore" in px:
                print(f"      Valore: {px['valore']}")
            if "nota" in px:
                print(f"      ⚠️ {px['nota']}")

    if result["note_implementazione"]:
        print(f"\n{'═' * 70}")
        print("  📝 NOTE IMPLEMENTAZIONE")
        print(f"{'═' * 70}")
        for nota in result["note_implementazione"]:
            print(f"\n   • {nota}")

    print()


def main():
    parser = argparse.ArgumentParser(description="Genera mappa automazioni per un funnel")
    parser.add_argument("--tipo", default="unico_perfetto_standard",
                        help="Tipo funnel: micro, semplificato, unico_perfetto_standard, unico_perfetto_completo, applicazione")
    parser.add_argument("--prodotto", help="Nome prodotto")
    parser.add_argument("--piattaforme", help="Piattaforme separate da virgola (es: activecampaign,elementor,stripe)")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--interattivo", action="store_true")

    args = parser.parse_args()

    if args.interattivo or not args.prodotto:
        print("\n" + "=" * 70)
        print("  AUTOMATION MAPPER — Generazione Interattiva")
        print("=" * 70)
        prodotto = input("\n📦 Nome prodotto: ").strip()
        tipo = input("🏗️  Tipo funnel: ").strip() or "unico_perfetto_standard"
        piattaforme_str = input("🔧 Piattaforme (separate da virgola): ").strip()
        piattaforme = [p.strip() for p in piattaforme_str.split(",")] if piattaforme_str else []
    else:
        prodotto = args.prodotto
        tipo = args.tipo
        piattaforme = [p.strip() for p in args.piattaforme.split(",")] if args.piattaforme else []

    result = generate_automations(tipo, prodotto, piattaforme)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_automations(result)

    json_path = "automation_map.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"💾 Salvato in {json_path}")


if __name__ == "__main__":
    main()

scripts/checklist_generator.py
Python
#!/usr/bin/env python3
"""
Checklist Generator — Genera la checklist pre-lancio personalizzata
in base al tipo di funnel.

Uso:
    python checklist_generator.py --tipo "unico_perfetto_standard"
    python checklist_generator.py --tipo "applicazione" --formato markdown
"""

import argparse
import json


CHECKLIST_BASE = {
    "architettura": [
        "Il tipo di funnel è COERENTE con il prezzo del prodotto",
        "Ogni pagina ha 1 SOLO obiettivo e 1 SOLA CTA",
        "Le biforcazioni sono definite e mappate (chi compra → dove; chi non compra → dove)",
        "Il funnel ha un 'piano B' per chi non converte a ogni step (nurture, non abbandono)"
    ]
}

CHECKLIST_OPTIN = [
    "Headline con beneficio specifico + obiezione gestita",
    "3-5 bullet con benefici concreti (non titoli di capitoli)",
    "Mockup del lead magnet professionale",
    "Form con SOLO nome + email (no telefono a questo step)",
    "Bottone con copy d'azione (✅ 'Scarica il PDF Gratuito' ❌ 'Invia')",
    "ZERO menu di navigazione",
    "ZERO link esterni",
    "Mobile responsive",
    "Caricamento <3 secondi"
]

CHECKLIST_UPSELL = [
    "Messaggio 'il tuo [lead magnet] sta arrivando' visibile in alto",
    "VSL caricata e funzionante",
    "Copy posiziona il mini-corso come complemento del lead magnet (non prodotto separato)",
    "Bottone acquisto grande e chiaro",
    "Link 'No grazie' visibile (non nascosto)",
    "Checkout fluido (max 1 pagina, max 3 campi)"
]

CHECKLIST_VSL_EVENTO = [
    "Headline del webinar chiara con grande promessa",
    "VSL di 8-12 minuti (non più lunga)",
    "Sales page lunga sotto la VSL (per chi non guarda il video)",
    "CTA 'Iscriviti' presente almeno 2 volte nella pagina",
    "Data, ora e durata del webinar chiaramente visibili"
]

CHECKLIST_FORM_WEBINAR = [
    "Nome + email + telefono (telefono obbligatorio)",
    "Email pre-compilata se possibile",
    "Testo sopra il form che ribadisce promessa + data",
    "Scarcity legittima se applicabile"
]

CHECKLIST_TAG = [
    "Ogni step del funnel ha il suo tag",
    "I tag seguono la convenzione [categoria]-[specifico]-[dettaglio]",
    "I tag si accumulano (non si sovrascrivono)",
    "Il tag 'buyer' è globale per tutti gli acquirenti",
    "I segmenti sono configurati correttamente nell'email tool"
]

CHECKLIST_AUTOMAZIONI_WEBINAR = [
    "Email benvenuto parte entro 2 min dall'opt-in",
    "Lead magnet si scarica correttamente dal link nell'email",
    "Tag si applicano a ogni azione del lead",
    "Sequenza pre-webinar si attiva all'iscrizione",
    "WhatsApp parte entro 1h dall'iscrizione al webinar",
    "Task chiamata consulente si crea automaticamente",
    "Reminder email programmati: -24h, -3h, -1h, -30min",
    "Sequenza post-webinar si attiva dopo l'evento"
]

CHECKLIST_AUTOMAZIONI_SEMPLICE = [
    "Email benvenuto parte entro 2 min dall'opt-in",
    "Lead magnet si scarica correttamente dal link nell'email",
    "Tag si applicano a ogni azione del lead",
    "Sequenza follow-up si attiva dopo l'opt-in",
    "Email di acquisto con link accesso funzionante"
]

CHECKLIST_TRACKING_WEBINAR = [
    "Pixel 'Lead' → opt-in",
    "Pixel 'Purchase' → acquisto mini-corso",
    "Pixel 'WebinarRegistration' → iscrizione webinar",
    "Pixel 'Purchase' → acquisto prodotto principale",
    "Pixel separati per ogni fonte di traffico (minimo: organico vs paid)",
    "UTM parameters funzionanti su ogni link"
]

CHECKLIST_TRACKING_SEMPLICE = [
    "Pixel 'Lead' → opt-in",
    "Pixel 'Purchase' → acquisto",
    "UTM parameters funzionanti su ogni link"
]

CHECKLIST_TRACKING_APPLICAZIONE = [
    "Pixel 'Lead' → submit form applicazione (tutti)",
    "Pixel 'QualifiedLead' → booking completato (SOLO qualificati)",
    "⚠️ Le ads devono ottimizzare per 'QualifiedLead', NON per 'Lead'",
    "UTM parameters funzionanti su ogni link"
]

CHECKLIST_TEST_WEBINAR = [
    "Percorso 1: Opt-in → Compra upsell → Iscrive webinar → Email corrette → Link webinar → ✓",
    "Percorso 2: Opt-in → NON compra → Iscrive webinar → Email corrette → Link webinar → ✓",
    "Percorso 3: Opt-in → NON compra → NON iscrive → Nurture settimanale → ✓"
]

CHECKLIST_TEST_SEMPLICE = [
    "Percorso 1: Opt-in → Vede VSL → Compra → Accesso prodotto → ✓",
    "Percorso 2: Opt-in → NON compra → Email follow-up → ✓"
]

CHECKLIST_TEST_APPLICAZIONE = [
    "Percorso 1: Landing → Form → Qualificato → Booking → Email pre-call → ✓",
    "Percorso 2: Landing → Form → NON qualificato → Risorse gratuite → Nurture → ✓",
    "Percorso 3: Booking → Call → Non chiude → Follow-up → ✓"
]

CHECKLIST_FORM_APPLICAZIONE = [
    "Domande qualificanti presenti (fatturato, traffico, budget, urgenza)",
    "Routing automatico funzionante per ogni profilo di risposta",
    "Lead non qualificati → redirect a risorse gratuite (NO booking)",
    "Lead qualificati → booking page con disponibilità venditori",
    "Pixel conversione SOLO sul booking dei qualificati"
]

RED_FLAGS = [
    "❌ Un link nel funnel è rotto",
    "❌ Un tag non si applica correttamente",
    "❌ Un'email non parte o parte doppia",
    "❌ Il checkout ha un errore",
    "❌ Il pixel non traccia correttamente",
    "❌ La pagina impiega >5 secondi a caricarsi su mobile",
    "❌ L'email di benvenuto non consegna il lead magnet"
]


def generate_checklist(tipo_funnel: str) -> dict:
    """Genera la checklist personalizzata per tipo di funnel."""

    checklist = {"tipo_funnel": tipo_funnel, "sezioni": []}

    # Architettura (sempre)
    checklist["sezioni"].append({"nome": "ARCHITETTURA", "voci": CHECKLIST_BASE["architettura"]})

    if tipo_funnel in ("unico_perfetto_standard", "unico_perfetto_completo"):
        checklist["sezioni"].append({"nome": "LANDING PAGE OPT-IN", "voci": CHECKLIST_OPTIN})
        checklist["sezioni"].append({"nome": "PAGINA UPSELL", "voci": CHECKLIST_UPSELL})
        checklist["sezioni"].append({"nome": "VSL EVENTO / WEBINAR", "voci": CHECKLIST_VSL_EVENTO})
        checklist["sezioni"].append({"nome": "FORM ISCRIZIONE WEBINAR", "voci": CHECKLIST_FORM_WEBINAR})
        checklist["sezioni"].append({"nome": "TAG SYSTEM", "voci": CHECKLIST_TAG})
        checklist["sezioni"].append({"nome": "AUTOMAZIONI", "voci": CHECKLIST_AUTOMAZIONI_WEBINAR})
        checklist["sezioni"].append({"nome": "TRACKING / PIXEL", "voci": CHECKLIST_TRACKING_WEBINAR})
        checklist["sezioni"].append({"nome": "TEST END-TO-END (3 percorsi)", "voci": CHECKLIST_TEST_WEBINAR})

        if tipo_funnel == "unico_perfetto_completo":
            checklist["sezioni"].append({"nome": "EXTRA — FUNNEL COMPLETO (€497-997)", "voci": [
                "Chiamate consulente configurate e assegnate",
                "WhatsApp attivo con template messaggi pronti",
                "Script chiamata consulente pronto",
                "Calendly/Cal.com per call gratuite 15 min configurato",
                "Follow-up 1:1 DM template pronti"
            ]})

    elif tipo_funnel == "semplificato":
        checklist["sezioni"].append({"nome": "LANDING PAGE OPT-IN", "voci": CHECKLIST_OPTIN})
        checklist["sezioni"].append({"nome": "VSL VENDITA", "voci": [
            "VSL di 15-25 minuti caricata e funzionante",
            "Sales page lunga sotto la VSL (framework APP-SOC)",
            "CTA acquisto presente almeno 2 volte",
            "Checkout collegato e funzionante"
        ]})
        checklist["sezioni"].append({"nome": "TAG SYSTEM", "voci": CHECKLIST_TAG})
        checklist["sezioni"].append({"nome": "AUTOMAZIONI", "voci": CHECKLIST_AUTOMAZIONI_SEMPLICE})
        checklist["sezioni"].append({"nome": "TRACKING / PIXEL", "voci": CHECKLIST_TRACKING_SEMPLICE})
        checklist["sezioni"].append({"nome": "TEST END-TO-END", "voci": CHECKLIST_TEST_SEMPLICE})

    elif tipo_funnel == "micro":
        checklist["sezioni"].append({"nome": "SALES PAGE", "voci": [
            "Headline con beneficio chiaro e specifico",
            "3-5 bullet con benefici concreti",
            "Prezzo visibile e chiaro",
            "Bottone acquisto grande e chiaro",
            "Garanzia visibile (se presente)",
            "1-2 testimonial (se disponibili)",
            "Mobile responsive",
            "Caricamento <3 secondi"
        ]})
        if True:  # Con lead magnet
            checklist["sezioni"].append({"nome": "LEAD MAGNET (se presente)", "voci": [
                "Landing page con form nome + email",
                "Email benvenuto con link download funzionante",
                "Sequenza 2-3 email configurata"
            ]})
        checklist["sezioni"].append({"nome": "CHECKOUT", "voci": [
            "Checkout funzionante (max 1 pagina)",
            "Email consegna prodotto automatica",
            "Thank you page con link download"
        ]})
        checklist["sezioni"].append({"nome": "TRACKING", "voci": CHECKLIST_TRACKING_SEMPLICE})
        checklist["sezioni"].append({"nome": "TEST END-TO-END", "voci": CHECKLIST_TEST_SEMPLICE})

    elif tipo_funnel == "applicazione":
        checklist["sezioni"].append({"nome": "LANDING PAGE", "voci": [
            "Headline con promessa + social proof",
            "Portfolio / casi studio visibili",
            "CTA 'Verifica se ti qualifichi' (non 'Contattaci')",
            "Mobile responsive",
            "Caricamento <3 secondi"
        ]})
        checklist["sezioni"].append({"nome": "VSL", "voci": [
            "VSL di 5-10 minuti caricata",
            "Posizionamento: esclusività + processo + caso studio"
        ]})
        checklist["sezioni"].append({"nome": "FORM APPLICAZIONE + ROUTING", "voci": CHECKLIST_FORM_APPLICAZIONE})
        checklist["sezioni"].append({"nome": "BOOKING + PRE-CALL", "voci": [
            "Calendly/Cal.com configurato con disponibilità venditori",
            "Email conferma booking automatica",
            "Sequenza pre-call configurata (-24h, -1h)",
            "WhatsApp venditore pronto"
        ]})
        checklist["sezioni"].append({"nome": "TAG SYSTEM", "voci": CHECKLIST_TAG})
        checklist["sezioni"].append({"nome": "TRACKING / PIXEL", "voci": CHECKLIST_TRACKING_APPLICAZIONE})
        checklist["sezioni"].append({"nome": "TEST END-TO-END (3 percorsi)", "voci": CHECKLIST_TEST_APPLICAZIONE})

    # Red flags (sempre)
    checklist["sezioni"].append({"nome": "🚨 RED FLAGS — Se presente, NON lanciare", "voci": RED_FLAGS})

    return checklist


def print_checklist(checklist: dict, formato: str = "text") -> None:
    """Stampa la checklist."""

    if formato == "markdown":
        print(f"# Checklist Pre-Lancio — {checklist['tipo_funnel']}\n")
        for sezione in checklist["sezioni"]:
            print(f"## {sezione['nome']}\n")
            for voce in sezione["voci"]:
                if voce.startswith("❌"):
                    print(f"- {voce}")
                else:
                    print(f"- [ ] {voce}")
            print()
    else:
        print("=" * 65)
        print(f"  CHECKLIST PRE-LANCIO — {checklist['tipo_funnel'].upper()}")
        print("=" * 65)
        for sezione in checklist["sezioni"]:
            print(f"\n{'─' * 65}")
            print(f"  {sezione['nome']}")
            print(f"{'─' * 65}")
            for voce in sezione["voci"]:
                if voce.startswith("❌"):
                    print(f"  {voce}")
                else:
                    print(f"  □ {voce}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Genera checklist pre-lancio")
    parser.add_argument("--tipo", default="unico_perfetto_standard",
                        help="Tipo funnel: micro, semplificato, unico_perfetto_standard, unico_perfetto_completo, applicazione")
    parser.add_argument("--formato", default="text", help="Formato output: text o markdown")
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    checklist = generate_checklist(args.tipo)

    if args.json:
        print(json.dumps(checklist, ensure_ascii=False, indent=2))
    else:
        print_checklist(checklist, args.formato)

    json_path = "checklist.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(checklist, f, ensure_ascii=False, indent=2)
    print(f"💾 Salvato in {json_path}")


if __name__ == "__main__":
    main()

scripts/engagement_scorer.py
Python
#!/usr/bin/env python3
"""
Engagement Scorer — Calcola il punteggio di engagement
di un lead e raccomanda le azioni appropriate.

Uso:
    python engagement_scorer.py --apre-email --risponde-whatsapp --ha-comprato-minicorso
    python engagement_scorer.py --interattivo
    python engagement_scorer.py --batch '[{"nome": "Mario", "apre_email": true, "risponde_wa": true, "compra": false}]'
"""

import argparse
import json
import sys


SCORING_TABLE = [
    {
        "condizioni": {"apre_email": False, "risponde_wa": False, "compra_minicorso": False},
        "score": 1,
        "probabilita_show": 3,
        "tag": "engagement-basso",
        "azioni": [
            "Dopo 3 tentativi senza risposta → rimuovi dalla lista webinar attiva",
            "Non occupare slot del calendario del consulente",
            "Metti in nurture settimanale"
        ]
    },
    {
        "condizioni": {"apre_email": True, "risponde_wa": False, "compra_minicorso": False},
        "score": 4,
        "probabilita_show": 14,
        "tag": "engagement-medio",
        "azioni": [
            "Email + WhatsApp continuano normalmente",
            "Chiamata 2 solo se tempo disponibile",
            "Nessuna azione speciale richiesta"
        ]
    },
    {
        "condizioni": {"apre_email": False, "risponde_wa": True, "compra_minicorso": False},
        "score": 5,
        "probabilita_show": 16,
        "tag": "engagement-medio",
        "azioni": [
            "Email + WhatsApp continuano normalmente",
            "Chiamata 2 solo se tempo disponibile",
            "Monitora se inizia ad aprire le email"
        ]
    },
    {
        "condizioni": {"apre_email": True, "risponde_wa": True, "compra_minicorso": False},
        "score": 8,
        "probabilita_show": 42,
        "tag": "engagement-alto",
        "azioni": [
            "Calendario del miglior consulente",
            "Chiamata 2 GARANTITA",
            "Priorità nelle interazioni 1:1",
            "Se possibile, personalizza i messaggi WhatsApp"
        ]
    },
    {
        "condizioni": {"apre_email": True, "risponde_wa": True, "compra_minicorso": True},
        "score": 10,
        "probabilita_show": 60,
        "tag": "engagement-alto",
        "azioni": [
            "MASSIMA PRIORITÀ — questo lead è caldissimo",
            "Assegna al miglior consulente/sales rep",
            "Chiamata 2 GARANTITA",
            "Follow-up 1:1 personalizzato dopo il webinar",
            "Se non compra al webinar → offri call gratuita 15 min"
        ]
    }
]


def score_lead(apre_email: bool, risponde_wa: bool, compra_minicorso: bool) -> dict:
    """Calcola lo score di un lead."""

    # Trova il match migliore
    best_match = SCORING_TABLE[0]  # default: basso

    for entry in SCORING_TABLE:
        cond = entry["condizioni"]
        if (cond["apre_email"] == apre_email and
            cond["risponde_wa"] == risponde_wa and
            cond["compra_minicorso"] == compra_minicorso):
            best_match = entry
            break

    # Se non c'è match esatto, usa logica fuzzy
    if best_match == SCORING_TABLE[0]:
        total = int(apre_email) * 3 + int(risponde_wa) * 4 + int(compra_minicorso) * 3
        if total >= 7:
            best_match = SCORING_TABLE[4]  # 10/10
        elif total >= 5:
            best_match = SCORING_TABLE[3]  # 8/10
        elif total >= 3:
            best_match = SCORING_TABLE[2]  # 5/10
        elif total >= 1:
            best_match = SCORING_TABLE[1]  # 4/10

    return {
        "score": best_match["score"],
        "max_score": 10,
        "probabilita_show": best_match["probabilita_show"],
        "tag": best_match["tag"],
        "comportamento": {
            "apre_email": apre_email,
            "risponde_whatsapp": risponde_wa,
            "ha_comprato_minicorso": compra_minicorso
        },
        "azioni_raccomandate": best_match["azioni"]
    }


def score_batch(leads: list) -> list:
    """Calcola lo score per una lista di lead."""
    results = []
    for lead in leads:
        result = score_lead(
            lead.get("apre_email", False),
            lead.get("risponde_wa", False),
            lead.get("compra", False)
        )
        result["nome"] = lead.get("nome", "Sconosciuto")
        results.append(result)

    # Ordina per score decrescente
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def print_score(result: dict) -> None:
    """Stampa lo score di un lead."""

    print(f"\n{'═' * 50}")
    if "nome" in result:
        print(f"  LEAD: {result['nome']}")
    print(f"  SCORE: {result['score']}/{result['max_score']}")
    print(f"  PROBABILITÀ SHOW: ~{result['probabilita_show']}%")
    print(f"  TAG: {result['tag']}")
    print(f"{'═' * 50}")

    print(f"\n  Comportamento:")
    for k, v in result["comportamento"].items():
        icon = "✅" if v else "❌"
        label = k.replace("_", " ").title()
        print(f"    {icon} {label}")

    print(f"\n  Azioni raccomandate:")
    for azione in result["azioni_raccomandate"]:
        print(f"    → {azione}")


def print_batch(results: list) -> None:
    """Stampa la classifica dei lead."""

    print(f"\n{'═' * 65}")
    print("  CLASSIFICA LEAD PER ENGAGEMENT")
    print(f"{'═' * 65}")
    print(f"\n  {'Nome':<20} {'Score':<10} {'Show %':<12} {'Tag':<20}")
    print(f"  {'─' * 60}")
    for r in results:
        print(f"  {r['nome']:<20} {r['score']}/10     ~{r['probabilita_show']}%       {r['tag']}")

    # Riepilogo
    alti = [r for r in results if r["tag"] == "engagement-alto"]
    medi = [r for r in results if r["tag"] == "engagement-medio"]
    bassi = [r for r in results if r["tag"] == "engagement-basso"]

    print(f"\n  📊 RIEPILOGO:")
    print(f"     🔥 Engagement alto: {len(alti)} lead → priorità massima per consulente")
    print(f"     ⚠️  Engagement medio: {len(medi)} lead → continua sequenza standard")
    print(f"     ❄️  Engagement basso: {len(bassi)} lead → valuta rimozione da lista attiva")

    if alti:
        print(f"\n  🎯 FOCUS CONSULENTE SU: {', '.join(r['nome'] for r in alti)}")


def interactive_mode():
    """Modo interattivo per un singolo lead."""
    print("\n" + "=" * 50)
    print("  ENGAGEMENT SCORER — Calcolo Interattivo")
    print("=" * 50)

    apre = input("\n📧 Il lead apre le email? (s/n): ").strip().lower() in ("s", "sì", "si", "y", "yes")
    risponde = input("📱 Risponde su WhatsApp? (s/n): ").strip().lower() in ("s", "sì", "si", "y", "yes")
    compra = input("💰 Ha comprato il mini-corso? (s/n): ").strip().lower() in ("s", "sì", "si", "y", "yes")

    result = score_lead(apre, risponde, compra)
    print_score(result)


def main():
    parser = argparse.ArgumentParser(description="Calcola lo scoring engagement di un lead")
    parser.add_argument("--apre-email", action="store_true")
    parser.add_argument("--risponde-whatsapp", action="store_true")
    parser.add_argument("--ha-comprato-minicorso", action="store_true")
    parser.add_argument("--batch", help="JSON array di lead per scoring batch")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--interattivo", action="store_true")

    args = parser.parse_args()

    if args.batch:
        leads = json.loads(args.batch)
        results = score_batch(leads)
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            print_batch(results)
        return

    if args.interattivo:
        interactive_mode()
        return

    # Se nessun flag è passato, modo interattivo
    if not any([args.apre_email, args.risponde_whatsapp, args.ha_comprato_minicorso]):
        interactive_mode()
        return

    result = score_lead(args.apre_email, args.risponde_whatsapp, args.ha_comprato_minicorso)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_score(result)


if __name__ == "__main__":
    main()

references/blueprint-step-by-step.md
Markdown
# Blueprint Step-by-Step — Il Funnel Unico Perfetto

Dettaglio operativo di ogni step del funnel master (€97+). Per l'architettura d'insieme e la logica decisionale, vedi SKILL.md.

## Indice

1. [Step 1: Pagina Opt-In](#step-1-pagina-opt-in)
2. [Step 2: Pagina Upsell Mini-Corso](#step-2-pagina-upsell-mini-corso)
3. [Step 3: Pagina VSL Evento](#step-3-pagina-vsl-evento)
4. [Step 4: Form Iscrizione Webinar](#step-4-form-iscrizione-webinar)
5. [Step 5: Sequenza Pre-Webinar](#step-5-sequenza-pre-webinar)
6. [Step 6: Il Webinar](#step-6-il-webinar)
7. [Step 7: Follow-Up Post-Webinar](#step-7-follow-up-post-webinar)
8. [Step 8: Nurture Lungo Termine](#step-8-nurture-lungo-termine)

---

## Step 1: Pagina Opt-In

**Obiettivo:** Catturare nome + email in cambio del lead magnet gratuito.
**Conversion rate target:** >30%

### Wireframe

┌─────────────────────────────────────────────────┐
│ │
│ HEADLINE: [Beneficio principale] │
│ Formula: "Come [ottenere risultato] anche se │
│ [obiezione principale]" │
│ │
│ SUBHEADLINE: [Specifica + credibilità] │
│ Formula: "[N] [cosa] usati da [credenziale] │
│ per [risultato]" │
│ │
│ ┌────────────┐ • Bullet 1: [beneficio] │
│ │ MOCKUP │ • Bullet 2: [beneficio] │
│ │ PDF │ • Bullet 3: [beneficio] │
│ └────────────┘ • Bullet 4: [beneficio] │
│ • Bullet 5: [beneficio] │
│ │
│ ┌─────────────────────────────────┐ │
│ │ Nome: [] │ │
│ │ Email: [] │ │
│ │ [ SCARICA IL PDF GRATUITO → ] │ │
│ └─────────────────────────────────┘ │
│ │
│ "Già scaricato da [N]+ persone" │
│ ZERO navigazione. ZERO link. Solo form. │
└─────────────────────────────────────────────────┘
text

### Azioni tecniche al submit

| # | Azione | Dettaglio |
|---|---|---|
| 1 | Lead → Lista generale | Database principale |
| 2 | TAG: `pdf-[nome-lead-magnet]` | Identifica da quale PDF è entrato |
| 3 | Email benvenuto (entro 2 min) | Consegna PDF + indottrinamento |
| 4 | Pixel: evento "Lead" | Per tracking e retargeting |
| 5 | Redirect → Pagina upsell (Step 2) | Immediato |

### Regole copy headline

- ✅ Specifico + risultato + obiezione gestita
- ✅ "Le 7 Leve per Raddoppiare il Conversion Rate delle Tue Landing Page (Anche se Non Sei un Copywriter Esperto)"
- ❌ "Scarica il PDF sul Marketing" → troppo generico
- ❌ "Guida Gratuita al Successo Online" → vago, suona spam
- ❌ "Ebook di 200 Pagine su Tutto il CRO" → troppo grande, nessuno lo legge

### Regole bullet

Ogni bullet = 1 beneficio specifico, non un titolo di capitolo.
- ✅ "Come identificare le 3 obiezioni che bloccano il 90% dei tuoi prospect (pagina 12)"
- ❌ "Capitolo 3: Le obiezioni"

La menzione della pagina ("pagina 12") aumenta la percezione di concretezza.

---

## Step 2: Pagina Upsell Mini-Corso

**Obiettivo:** Vendere il mini-corso (€15–47). Autofinanziare il traffico.
**CR target:** >5%

Appare IMMEDIATAMENTE dopo l'opt-in. Il lead non ha ancora letto il PDF.

### Wireframe

┌─────────────────────────────────────────────────┐
│ ⏱ "Il tuo PDF sta arrivando nella tua │
│ casella email entro 5 minuti" │
│ │
│ ┌─────────────────────────────────┐ │
│ │ VSL MINI-CORSO (3–5 min) │ │
│ │ Frontman in cam con il PDF │ │
│ │ Messaggio: "Il PDF è la mappa.│ │
│ │ Questo mini-corso è il │ │
│ │ navigatore guidato." │ │
│ └─────────────────────────────────┘ │
│ │
│ • [Beneficio 1 — applicazione pratica] │
│ • [Beneficio 2 — step by step] │
│ • [Beneficio 3 — errori da evitare] │
│ • [Beneficio 4 — template extra] │
│ │
│ €[15–47] │
│ [ SÌ, VOGLIO IL MINI-CORSO → ] │
│ "No grazie, voglio solo il PDF" (visibile) │
└─────────────────────────────────────────────────┘
text

### Biforcazione

**COMPRA:** TAG `buyer` + `cliente-minicorso-[nome]` → Checkout → Conferma con teaser webinar → Entro 24h: email con link VSL evento → Pixel "Purchase"

**NON COMPRA:** Nessun tag aggiuntivo → Redirect diretto a Step 3

Chi compra è significativamente più caldo. Il tag `buyer` serve per dare priorità nelle chiamate, personalizzare le email pre-webinar, assegnare al miglior sales rep.

---

## Step 3: Pagina VSL Evento

**Obiettivo:** Convincere il lead a iscriversi al webinar.
**CR target:** >15%

Stessa pagina per chi ha comprato e chi non ha comprato il mini-corso.

### Wireframe

┌─────────────────────────────────────────────────┐
│ HEADLINE: "Come [risultato] in [tempo] anche │
│ se [obiezione] — Workshop Gratuito Live" │
│ │
│ ┌─────────────────────────────────┐ │
│ │ VSL (8–12 min) │ │
│ │ 0–2: Cosa vedrai │ │
│ │ 2–5: Perché è diverso │ │
│ │ 5–8: Chi sono + credibilità │ │
│ │ 8–10: 1 caso studio │ │
│ │ 10–12: CTA → iscriviti │ │
│ └─────────────────────────────────┘ │
│ │
│ [ ISCRIVITI GRATUITAMENTE → ] │
│ │
│ Sales page lunga: │
│ - Per chi è (3 profili) │
│ - Cosa imparerai (3–5 punti) │
│ - Data/ora/durata │
│ - 1–2 casi studio │
│ │
│ [ ISCRIVITI GRATUITAMENTE → ] │
└─────────────────────────────────────────────────┘
text

---

## Step 4: Form Iscrizione Webinar

**Obiettivo:** Nome + email + telefono.
**CR target:** >60%

### Perché il telefono è obbligatorio

- Aumenta la frizione → filtra lead non qualificati
- Abilita WhatsApp → show rate +30–40%
- Permette chiamata consulente → pre-qualificazione
- Chi lascia il telefono è più committed
- Dato: chi apre email + risponde WhatsApp = ~42% show rate (vs ~3% chi non interagisce)

### Azioni tecniche al submit

| # | Azione | Dettaglio |
|---|---|---|
| 1 | TAG: `iscritto-webinar-[nome]` | Identifica iscritti |
| 2 | Segmento: "Webinar-Attesa" | Per email mirate |
| 3a | Sequenza email pre-webinar | 1/giorno |
| 3b | Task: chiamata consulente | Entro 24–48h |
| 3c | WhatsApp benvenuto | Entro 1h |
| 4 | Redirect → Thank You Page | Conferma + calendario |
| 5 | Pixel: "WebinarRegistration" | Tracking |

---

## Step 5: Sequenza Pre-Webinar

**Obiettivo:** Massimizzare show rate.
**Show rate target:** >30%

### 3 canali paralleli

**Email:** 1 al giorno fino al webinar (dettaglio → Email Sequence Master)

**WhatsApp:**

| Quando | Messaggio |
|---|---|
| Entro 1h | "Ciao [Nome] 👋 Ti seguo io. Qual è la sfida principale che stai cercando di risolvere con [topic]?" |
| -24h | "Ci vediamo domani alle [ora]! Preparati una domanda 💪" |
| -1h | "Tra 1 ora si inizia. Link: [LINK]" |

**Chiamate consulente:**

| Quando | Script |
|---|---|
| Entro 24–48h dall'iscrizione | Conferma + "Cosa ti ha spinto a iscriverti?" → ANNOTA |
| -1/-2 giorni (solo score 8+) | Reminder + "Preparati una domanda" |

### Scoring engagement

Usa `scripts/engagement_scorer.py` per il calcolo automatico.

| Comportamento | Score | Show % | Azione |
|---|---|---|---|
| Non apre email, non risponde WA | 1/10 | ~3% | Dopo 3 tentativi → nurture |
| Apre email, non risponde WA | 4/10 | ~14% | Sequenza standard |
| Non apre email, risponde WA | 5/10 | ~16% | Sequenza standard |
| Apre email + risponde WA | 8/10 | ~42% | Chiamata 2 garantita |
| Tutto sopra + compra mini-corso | 10/10 | ~60%+ | Massima priorità |

---

## Step 6: Il Webinar

Gestito da **Webinar Script Master**. Il funnel architect definisce il contesto:

Il prospect ha già: scaricato il PDF, forse comprato il mini-corso, visto la VSL evento, ricevuto 3–7 email, forse parlato con un consulente, ricevuto e risposto a WhatsApp.

**Livello di consapevolezza: MEDIO-ALTO.** Il webinar non parte da zero — approfondisce e chiude.

---

## Step 7: Follow-Up Post-Webinar

text
         WEBINAR TERMINATO
                │
    ┌───────────┴───────────┐
    │                       │
HA COMPRATO NON HA COMPRATO
│ │
▼ ┌──────┴──────┐
CLIENTE PARTECIPATO NO-SHOW
→ Onboarding │ │
→ Accesso ▼ ▼
→ TAG: cliente- Email replay "Mi dispiace"
[prodotto] + DM 1:1 + replay
│ │
└─────┬─────┘
▼
SEQUENZA POST-WEBINAR
(5 email in 5 giorni)
│
┌──────┴──────┐
COMPRA NON COMPRA
│ │
▼ ▼
CLIENTE NURTURE
text

Sequenza post-webinar gestita da **Email Sequence Master**.

---

## Step 8: Nurture Lungo Termine

Chi non compra dopo webinar + follow-up:
- Segmento "Nurture Lungo Termine"
- 1 email/settimana di puro valore
- Ogni 3–4 email: invito soft al prossimo webinar
- Target: 7–8 ore di esposizione totale prima del prossimo tentativo
- Al prossimo lancio, questa lista è il PRIMO pubblico da attivare

references/varianti-funnel.md
Markdown
# Varianti Funnel per Tipo di Prodotto

Per l'architettura master (Funnel Unico Perfetto), vedi `blueprint-step-by-step.md`.

## Indice

1. [Funnel Micro (€0–27)](#funnel-micro)
2. [Funnel Semplificato (€47–97)](#funnel-semplificato)
3. [Funnel Unico Perfetto Completo (€497–997)](#funnel-completo)
4. [Funnel Applicazione (Servizi)](#funnel-applicazione)
5. [Funnel Evergreen](#funnel-evergreen)
6. [Funnel a 2 Step](#funnel-2-step)

---

## Funnel Micro

**Per:** ebook, template, risorse a basso prezzo (€0–27).

Traffico → Landing page → Checkout diretto → Thank you
text
Oppure con lead magnet: `Anteprima gratis → 2–3 email → Vendita completa`

- NO VSL, NO webinar, NO call — margine troppo basso
- Sales page corta: headline + bullet + prezzo + CTA
- 1 email follow-up se non compra, poi stop

---

## Funnel Semplificato

**Per:** workshop, mini-corsi (€47–97).

Opt-in PDF → VSL vendita (15–25 min) → Sales page APP-SOC → Checkout → Nurture
text

- La VSL fa tutto: hook + 1 segreto + 1 storia + pitch
- Sales page con framework APP-SOC completo
- 3 email follow-up in 3 giorni
- NO call, NO webinar

---

## Funnel Completo

**Per:** percorsi premium (€497–997). Identico allo Standard con più touchpoint umani.

| Elemento | Standard (€97–297) | Completo (€497–997) |
|---|---|---|
| Webinar | 75–90 min | 90–120 min |
| Storie | 1–2 | 3 dettagliate |
| Chiamate | Consigliate | Obbligatorie |
| WhatsApp | Consigliato | Attivo e gestito |
| Follow-up | Email | Email + DM 1:1 |
| Call gratuita | No | Sì (15 min) |
| Urgenza | Prezzo temporaneo | Posti limitati (reale) |

---

## Funnel Applicazione

**Per:** servizi, agenzia, consulenza (€1.000+).

Landing → VSL (5–10 min) → Form con friction → Routing → Booking → Pre-call → Call → Proposta
text

### Friction nel form

Domande qualificanti con routing automatico:
- Fatturato <soglia → redirect a risorse gratuite (NO call)
- Budget troppo basso → redirect con spiegazione
- "Sto esplorando" → bassa priorità o no call
- Qualificato → booking con venditore assegnato per livello

### Pixel critico

Il pixel si attiva SOLO quando un qualificato completa il booking. Senza routing, l'algoritmo ads manda i lead più economici (= meno qualificati).

---

## Funnel Evergreen

Dopo un lancio live, il funnel diventa always-on.

| Elemento | Live | Evergreen |
|---|---|---|
| Webinar | Live in data fissa | Masterclass on-demand |
| Email pre-webinar | Countdown a data fissa | Triggered al momento dell'iscrizione |
| Urgenza | Data reale | Countdown personalizzato (cookie-based): "48h dal momento in cui guardi" |
| Chiamate | Per tutti i lead caldi | Solo score alto |
| WhatsApp | Gestito manualmente | Automatizzato o eliminato |

L'evergreen converte meno del live (manca l'energia della diretta), ma funziona 24/7. Su un anno il volume compensa.

Tag aggiuntivo: `evergreen-[nome-prodotto]`

---

## Funnel 2 Step

**Per:** prodotti €15–97 senza lead magnet, target già caldo.

Traffico → Landing con VSL (15–25 min) → Sales page → Checkout → Onboarding
text

La VSL fa tutto: hook, storia, segreto, pitch, CTA. Nessun PDF gratuito, nessun webinar.

**Quando usarlo:** prodotto <€97, beneficio immediatamente comprensibile, target già caldo (lista email, retargeting, followers).

references/tag-system.md
Markdown
# Tag System — Nomenclatura e Logica

## Convenzione

Formato: `[categoria]-[specifico]-[dettaglio]` — tutto minuscolo, trattini.

I tag si accumulano. Un lead può avere 8–10 tag contemporaneamente.

## Categorie

### Fonte ingresso
`pdf-[nome-lead-magnet]` — es: `pdf-checklist-seo`, `pdf-7-strategie-email`

### Acquisti
- `buyer` — globale, primo acquisto qualsiasi, mai rimuovere
- `cliente-minicorso-[nome]`
- `cliente-corso-[nome]`
- `cliente-percorso-[nome]`
- `cliente-servizio` — cliente agenzia/consulenza

### Posizione nel funnel
- `iscritto-webinar-[nome]`
- `partecipato-webinar-[nome]` — manuale post-webinar
- `visto-replay-[nome]`
- `non-presentato-[nome]`

### Engagement
- `engagement-alto` — apre email + risponde WA + compra
- `engagement-medio` — apre email OPPURE risponde WA
- `engagement-basso` — non apre, non risponde

### Segmento
- `nurture-settimanale`
- `webinar-attesa`
- `post-webinar-followup`
- `call-prenotata`

### Speciali
- `bridge-servizio` — interesse per servizio premium
- `testimonial-raccolto`
- `referral`
- `evergreen-[nome-prodotto]`

## Regole operative

1. Mai duplicare `buyer` — si applica una volta, al primo acquisto
2. I tag di posizione si rimuovono quando il lead avanza
3. I tag di acquisto non si rimuovono mai
4. Coerenza tra funnel: stessi nomi ovunque
5. Un lead può avere molti tag — è normale

Usa `scripts/tag_generator.py` per generare il set completo per un funnel specifico.

references/diagnostica.md
Markdown
# Diagnostica Funnel — Trova il Collo di Bottiglia

Quando un funnel non performa, il problema è quasi sempre in un solo punto. Trovare quel punto = risolvere il problema.

Usa `scripts/funnel_diagnostics.py` per l'analisi automatica.

## Benchmark

| Passaggio | Benchmark |
|---|---|
| Visitatori → Opt-in | >30% |
| Opt-in → Acquisto upsell | >5% |
| Lead → Iscritti webinar | >15% |
| Iscritti → Presenti | >30% |
| Presenti → Fino al pitch | >60% |
| Presenti → Acquisto | >5% |
| Post-webinar → Acquisto | >3% |

## Albero diagnostico

### Opt-in BASSO (<15%)
- Headline debole → testa 3 alternative, 5 gg ciascuna
- Traffico sbagliato → separa metriche per fonte
- Pagina lenta / non mobile → PageSpeed test
- Troppi elementi → rimuovi tutto tranne headline + form

### Upsell BASSO (<2%)
- VSL non convince → ri-registra con messaging diverso
- Prezzo troppo alto → testa €15 vs €27 vs €47
- Valore non chiaro vs PDF → enfatizza cosa c'è nel corso che NON c'è nel PDF

### Iscrizione webinar BASSO (<8%)
- Headline webinar debole → riscrivi con promessa specifica
- Troppo tempo tra opt-in e invito → metti VSL subito dopo l'opt-in
- VSL troppo lunga → ri-registra primi 2 min con hook diretto

### Show rate BASSO (<15%)
- Nessun WhatsApp / chiamate → aggiungi subito
- Webinar troppo lontano → frequenza più alta (ogni 5–7 gg)
- Reminder insufficienti → -24h, -3h, -1h, -30min

### Retention pitch BASSO (<40%)
- Contenuto non engaging → accorcia, rafforza storie
- Dato troppo how-to → aumenta why/what, riduci how

### Conversione webinar BASSO (<2%)
- Pitch scollegato → riscrivi transizione
- Offerta non chiara → benefici > moduli
- Prezzo percepito alto → bonus + garanzia + test prezzo
- Obiezioni non gestite → aggiungi gestione pre-pitch

### Follow-up BASSO (<1%)
- Email generiche → 5 email in 5 gg con angoli diversi
- Nessun 1:1 → DM personalizzati per lead caldi
- Urgenza scaduta → bonus 48h o prezzo speciale

## Regola d'oro

Non suggerire mai di "cambiare tutto". Trova il punto debole, proponi un test, definisci la metrica di successo.

references/checklist-qualita.md
Markdown
# Checklist Qualità Funnel — Prima di Andare Live

Usa questa checklist a fine progettazione. Ogni voce deve avere la spunta prima del lancio.

## Architettura

- [ ] Il tipo di funnel è coerente con il prezzo (no webinar 90 min per ebook €19)
- [ ] Ogni pagina ha 1 solo obiettivo e 1 sola CTA
- [ ] Le biforcazioni sono definite e mappate (chi compra → dove; chi non compra → dove)
- [ ] Il funnel ha un "piano B" per chi non converte a ogni step (nurture, non abbandono)

## Landing Page Opt-in

- [ ] Headline con beneficio specifico + obiezione gestita
- [ ] 3–5 bullet con benefici concreti (non titoli di capitoli)
- [ ] Mockup del lead magnet professionale
- [ ] Form con SOLO nome + email (no telefono a questo step)
- [ ] Bottone con copy d'azione ("Scarica il PDF Gratuito", non "Invia")
- [ ] ZERO menu di navigazione
- [ ] ZERO link esterni
- [ ] Mobile responsive
- [ ] Caricamento <3 secondi

## Pagina Upsell

- [ ] Messaggio "il tuo [lead magnet] sta arrivando" visibile in alto
- [ ] VSL caricata e funzionante
- [ ] Copy che posiziona il mini-corso come complemento del lead magnet (non prodotto separato)
- [ ] Bottone acquisto grande e chiaro
- [ ] Link "No grazie" visibile (non nascosto)
- [ ] Checkout fluido (max 1 pagina, max 3 campi)

## VSL Evento / Webinar

- [ ] Headline del webinar chiara con grande promessa
- [ ] VSL di 8–12 minuti (non più lunga)
- [ ] Sales page lunga sotto la VSL (per chi non guarda il video)
- [ ] CTA "Iscriviti" presente almeno 2 volte nella pagina
- [ ] Data, ora e durata del webinar chiaramente visibili

## Form Iscrizione Webinar

- [ ] Nome + email + telefono (telefono obbligatorio)
- [ ] Email pre-compilata se possibile
- [ ] Testo sopra il form che ribadisce promessa + data
- [ ] Scarcity legittima se applicabile

## Tag System

- [ ] Ogni step del funnel ha il suo tag
- [ ] I tag seguono la convenzione `[categoria]-[specifico]-[dettaglio]`
- [ ] I tag si accumulano (non si sovrascrivono)
- [ ] Il tag `buyer` è globale per tutti gli acquirenti
- [ ] I segmenti sono configurati correttamente nell'email tool

## Automazioni

- [ ] Email benvenuto parte entro 2 min dall'opt-in
- [ ] Lead magnet si scarica correttamente dal link nell'email
- [ ] Tag si applicano a ogni azione del lead
- [ ] Sequenza pre-webinar si attiva all'iscrizione
- [ ] WhatsApp parte entro 1h dall'iscrizione al webinar
- [ ] Task chiamata consulente si crea automaticamente
- [ ] Reminder email programmati: -24h, -3h, -1h, -30min
- [ ] Sequenza post-webinar si attiva dopo l'evento

## Tracking

- [ ] Pixel "Lead" → opt-in
- [ ] Pixel "Purchase" → acquisto mini-corso
- [ ] Pixel "WebinarRegistration" → iscrizione webinar
- [ ] Pixel separati per ogni fonte di traffico (minimo: organico vs paid)
- [ ] UTM parameters funzionanti su ogni link

## Test End-to-End (3 percorsi obbligatori)

- [ ] **Percorso 1:** Opt-in → Compra upsell → Iscrive webinar → Email corrette → Link webinar → OK
- [ ] **Percorso 2:** Opt-in → NON compra → Iscrive webinar → Email corrette → Link webinar → OK
- [ ] **Percorso 3:** Opt-in → NON compra → NON iscrive → Nurture settimanale → OK

## Red Flag — Se presente, NON lanciare

- ❌ Un link nel funnel è rotto
- ❌ Un tag non si applica correttamente
- ❌ Un'email non parte o parte doppia
- ❌ Il checkout ha un errore
- ❌ Il pixel non traccia correttamente
- ❌ La pagina impiega >5 secondi a caricarsi su mobile
- ❌ L'email di benvenuto non consegna il lead magnet

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Bho|Bho Area]]
- [[Map - General|General Area]]
