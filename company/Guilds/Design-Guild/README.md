# 🎨 Design Guild — Guild

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.2
> **Expertise:** visual identity, empire-style design system (ink/paper/orange #fb4604), template Canva, cover KDP, thumbnail YT
> **Serve:** CONTENT-FACTORY (visual assets), PLATFORM (UI siti, Crea Siti), MULTI-BUSINESS (cover KDP, thumbnail YT)
> **Sponsor C-level:** CMO (empire-cmo)
> Collegato a: [[GRUPPO.md]] · [[company/Mandato/MANDATO-EMPIRE.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **Guild Master** | `design-guild-master` (L5 coordinator, namespace AgentDB: `patterns/design/`) |
| **Tipo** | Guild trasversale — expertise su richiesta, non gerarchia verticale |
| **Deliverable principale** | DE Design System + Template Library (Canva + Figma) |
| **Ingaggio** | Passivo (`memory_search "design system"`) o attivo (guild_request) |

---

## Cosa standardizza

### 1. Empire Design System (DE Design System)

La Design Guild definisce e mantiene il sistema visivo di Digital Empire:

**Palette ufficiale (invariante fino a nuovo ADR):**
| Token | Colore | Uso |
|---|---|---|
| `--ink` | `#1a1a1a` (quasi nero) | testo principale, titoli |
| `--paper` | `#f5f0e8` (bianco caldo) | sfondi, aree di riposo visivo |
| `--orange` | `#fb4604` (arancio Empire) | CTA, accenti, sottolineature chiave |
| `--white` | `#ffffff` | spaziatura, card |

**Tipografia:**
- Titoli: bold, uppercase dove appropriato, niente serif ornamentali
- Body: leggibile, spaziatura generosa — la voce è diretta, il layout supporta la lettura
- Niente font decorativi: il carattere non deve distrarre dal messaggio

**Principi di layout:**
- Whitespace generoso — il vuoto è parte del design, non uno spreco
- Gerarchia visiva esplicita: titolo → sottotitolo → body → CTA — nessuna ambiguità
- Mobile-first per contenuti social e email; desktop per landing e preventivi

### 2. Template per tipo di contenuto

La Guild mantiene i template master (Canva o Figma) per ogni formato ricorrente:

| Formato | Template | Varianti |
|---|---|---|
| Carosello IG 10 slide | DE base + cliente (slot brand_kit) | verticale 1080×1080 |
| Thumbnail YouTube | sfondo `--ink`, testo `--paper`+`--orange`, viso se presente | 1280×720 |
| Cover KDP | layout pulito, titolo dominante, autore sottotitolo | formati standard KDP |
| Landing page section | hero, feature, proof, CTA — palette DE o brand_kit cliente | responsive |
| Email header | logo + `--orange` strip + titolo | larghezza 600px |
| Report/preventivo | cover page, body, tabelle — stile professionale DE | A4 |

**Regola multi-tenant (Pattern #11):** ogni template ha slot per `brand_kit` del cliente. Quando il brand_kit non è `DE`, la palette e la tipografia del cliente sostituiscono quelle DE — ma la struttura del layout e la qualità restano standard Guild.

### 3. Brand Kit Registry

La Guild mantiene i brand kit registrati:
- **DE** (default) — palette ink/paper/orange, voice diretta-provocatoria-trasparente
- **[Cliente X]** — palette, logo, font, regole specifiche (creato a inizio delivery, aggiornato se il cliente cambia brand)

Ogni brand kit è un file YAML in `company/runtime/design/brand-kits/<brand>.yaml` e una entry nel Brain (`identity/brand-kits/`).

### 4. Review visiva (gate Design)

Ogni visual che esce da CONTENT-FACTORY o PLATFORM passa il gate Design:
- Palette conforme al brand_kit dichiarato
- Nessun elemento "fuori voce" visiva (gradients arcobaleno, font decorativi, layout caotico)
- CTA visivamente prominente e unica
- Nessun testo sotto 12pt nelle aree chiave (leggibilità)

---

## Deliverable

- **DE Design System** — documentazione completa palette, tipografia, principi, esempi — `company/runtime/design/DE-design-system.md`
- **Template Library** — link Canva/Figma per ogni formato (accesso condiviso Max+Gael)
- **Brand Kit Registry** — YAML per ogni brand_kit attivo — `company/runtime/design/brand-kits/`
- **Design Gate checklist** — per verify.sh cat.2 (brand conformance visiva)

---

## Come si richiede supporto alla Guild

```json
{
  "from": "<ecosistema_richiedente>",
  "to": "Design-Guild",
  "tipo": "guild_request",
  "sottotipo": "template_request | brand_kit_create | design_review | asset_brief",
  "brief": "necessito template carosello 10 slide per cliente Y (brand_kit: rosso #cc0000, font Inter)",
  "formato": "carosello_ig | thumbnail | cover_kdp | landing | email | preventivo",
  "brand_kit": "DE | <cliente>",
  "contenuto_da_inserire": "titoli e testi già pronti — solo layout",
  "formato_atteso": "link template Canva personalizzato o PNG esportato",
  "deadline": "YYYY-MM-DD"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Template disponibili per formato principale | ≥ 6 (F3) |
| Visual che supera gate Design al primo tentativo | > 80% |
| Brand kit registrati per cliente attivo | 1 per cliente (F3) |
| Uso colori non conformi al brand_kit dichiarato | 0 |
| Tempo di risposta guild_request design review | < 24h (F3) |

---

## Stato

Struttura creata (F1). Agenti L5 da assegnare in F3 (migrazione asset + registro Identity-HR).
Guild Master disponibile in consultazione manuale (F1-F3): usa skill `empire-premium-style` e `canvas-design` per asset immediati.
