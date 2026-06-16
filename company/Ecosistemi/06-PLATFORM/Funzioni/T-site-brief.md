> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# T-site-brief — Funzione L4: Brief di Progetto Sito

> Funzione L4 · Reparto L2: WEB-ENGINEERING · Workflow: WF-SITE-FULL
> Ecosistema: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md`

---

## Scopo

Trasformare il mandato ricevuto da AGENCY (o da un altro ecosistema committente) in un brief strutturato e completo che possa avviare le funzioni downstream (T-site-architecture, T-site-design). Il brief è il contratto di scope: nessuna funzione successiva lavora senza brief validato.

---

## Input

```json
{
  "mandato_source": "01-AGENCY | 04-MARKETING | ...",
  "brief_cliente": {
    "nome_progetto": "string",
    "brand_kit": "brands/<slug>/brand-kit.json",
    "icp": "brands/<slug>/icp.json",
    "scope": "landing | sito-5-sezioni | ...",
    "deadline": "YYYY-MM-DD",
    "budget_crediti": 200
  }
}
```

Campi obbligatori: `brand_kit`, `icp`, `scope`, `deadline`, `budget_crediti`. Mandato incompleto → blocco con richiesta strutturata al committente.

---

## Output

```json
{
  "brief_id": "PLT-BRIEF-YYYY-NNN",
  "progetto": "string",
  "sezioni_attese": ["hero", "about", "servizi", "portfolio", "cta"],
  "tone_of_voice": "dai brand-kit",
  "palette": "ink/orange/silver | custom",
  "stack": "Next.js 15 + Tailwind v4 | da specificare",
  "copy_source": "04-MARKETING | cliente | scritto",
  "deadline_interna": "YYYY-MM-DD",
  "budget_check": "ok | warning | blocco"
}
```

---

## Processo

1. Legge `brand-kit.json` e `icp.json` → estrae tone, palette, key differentiators
2. Verifica scope vs budget dichiarato: se stima > budget → segnala immediatamente
3. Compila brief strutturato (sezioni, copy source, stack ipotizzato)
4. Salva in `orders/PLT-BRIEF-YYYY-NNN/brief.json`
5. Trigger su T-site-architecture

---

## Skill usate

- skill `site-brief` (Crea Siti)
- skill `site-plan` — pianificazione sezioni
- `memory_search("platform/patterns", brand+tipo_sito)` — pattern precedenti

---

## Agente responsabile

`plt-site-architect` (coordina il brief in collaborazione con `plt-cc-master`)

---

## KPI

| KPI | Target |
|---|---|
| Brief completi al primo invio (senza iterazioni) | ≥ 85% |
| Tempo mandato → brief validato | ≤ 2h |

## Connessioni

- [[06-PLATFORM/Reparti/Web-Engineering.md]] — reparto padre
- [[06-PLATFORM/Funzioni/T-site-architecture.md]] — funzione successiva
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo
