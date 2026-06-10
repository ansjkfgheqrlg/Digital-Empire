# mcp-installer

> Source: File system (`SKILL & Agenti\SKILL\Agente Max\skills\mcp-installer.md`)
> Collected: 2026-05-06
> Published: Unknown

# MCP-INSTALLER — Protocollo Installazione e Configurazione MCP

Usa questo protocollo quando devi installare un nuovo MCP, configurarne uno esistente, ottimizzarne il peso nel contesto, o decidere se un MCP è la scelta giusta rispetto a una skill.

**Riferimento KB:** K08-mcp.md (Capitoli 31-34) per teoria e dettagli.

---

## FASE 1 — DECISION TREE: MCP VS SKILL

Prima di installare qualsiasi MCP, esegui questa valutazione:

```
DOMANDA 1: L'operazione richiede accesso DINAMICO a dati in tempo reale?
  SÌ → Considera MCP (es: leggere email live, interagire con browser, API real-time)
  NO → Considera skill (es: scrivere email secondo un template, analizzare testo)

DOMANDA 2: L'operazione sarà ripetuta molte volte?
  SÌ →  Il costo MCP si moltiplica. Valuta skill per ridurre costo a lungo termine.
  NO (una tantum) → MCP è accettabile

DOMANDA 3: Il MCP consumerà >15% del contesto?
  SÌ → RED FLAG. Verifica se l'alternativa skill copre l'80% dei casi d'uso.
  NO → Procedi con MCP

DOMANDA 4: Hai già usato il MCP in passato per questo tipo di task?
  SÌ → Hai già capito la procedura. Crea una skill che la replica.
  NO → Usa il MCP per la prima volta, poi valuta se creare la skill.
```

**Principio dal Capitolo 33:** "Usa l'MCP per imparare COME fare qualcosa. Poi codifica quella procedura come skill. Usa la skill infinitamente al costo di ~€0.01."

---

## FASE 2 — PESO MCP NEL CONTESTO

### MCP noti e peso stimato:

```
MCP                    | Peso stimato | Consiglio
───────────────────────|──────────────|──────────────────────
ClickUp                | ~27%         | ❌ PESANTISSIMO — solo se essenziale
Chrome Dev Tool        | ~0.1%        | ✅ CONSIGLIATO — leggerissimo
GitHub MCP             | ~5-8%        | ⚠️ Installare per-progetto, non global
Notion MCP             | ~10-15%      | ⚠️ Solo se usato quotidianamente
Filesystem MCP         | ~1-2%        | ✅ Accettabile
Sequential Thinking    | ~2-3%        | ✅ Accettabile
Brave Search           | ~1-2%        | ✅ Accettabile
```

**Regola:** MCP >15% → configura per-progetto, NON globale. MCP >25% → valuta seriamente l'alternativa skill.

---

## FASE 3 — INSTALLAZIONE GUIDE

### Struttura del file di configurazione:

Il file di configurazione MCP si trova in:
- **Globale:** `C:\Users\Utente\.claude\settings.json`
- **Per-progetto:** `[root-progetto]\.claude\settings.json`

### Formato JSON per aggiungere un MCP:

```json
{
  "mcpServers": {
    "nome-mcp": {
      "command": "npx",
      "args": ["-y", "@package/nome-mcp"],
      "env": {
        "API_KEY": "tua-chiave-api"
      }
    }
  }
}
```

### Passaggi di installazione standard:

**Step 1 — Verifica prerequisiti:**
```bash
# Verifica Node.js installato
node --version

# Verifica npm installato
npm --version
```

**Step 2 — Leggi la configurazione esistente:**
```
Read: C:\Users\Utente\.claude\settings.json
```
Se il file non esiste, crealo con `{}` come contenuto base.

**Step 3 — Aggiungi la configurazione MCP:**
Modifica `settings.json` aggiungendo il nuovo MCP nella sezione `mcpServers`.

**Step 4 — Riavvia Claude Code:**
Chiudi e riapri Claude Code. Il nuovo MCP sarà disponibile.

**Step 5 — Verifica:**
Usa il comando `/mcp` in Claude Code per vedere la lista degli MCP attivi e verificare che il nuovo appaia.

---

## FASE 4 — CHROME DEV TOOL MCP (consigliato)

L'unico MCP consigliato per la maggior parte degli utenti. Peso: ~0.1% del contesto.

**Cosa fa:** Permette a Claude Code di:
- Fare screenshot del browser
- Interagire con pagine web (cliccare, compilare form)
- Leggere il DOM e il console log
- Fare visual inspection per sviluppo frontend

**Installazione:**

```json
{
  "mcpServers": {
    "chrome-dev-tool": {
      "command": "npx",
      "args": ["-y", "@claude-dev-tool/mcp-server"]
    }
  }
}
```

Dopo l'installazione, avvia il server Chrome DevTools seguendo le istruzioni specifiche del package.

**Uso tipico con lo Screenshot Loop:**
1. Modifica la UI nel codice
2. Chiedi a Claude di fare screenshot con il Chrome Dev Tool MCP
3. Claude analizza lo screenshot e identifica problemi visivi
4. Correggi e ripeti

---

## FASE 5 — OPTIMIZATION STRATEGIES

### Attivazione selettiva (per MCP pesanti):

Invece di installare un MCP pesante (es: ClickUp 27%) nel settings.json globale, installa SOLO nel progetto che lo necessita:

**Rimuovi dal global:**
`C:\Users\Utente\.claude\settings.json` → elimina la entry del MCP pesante

**Aggiungi al locale del progetto:**
`[progetto]\.claude\settings.json` → aggiungi la entry del MCP pesante

Risultato: il MCP è disponibile quando apri quel progetto, ma non consuma contesto in tutti gli altri.

### Disabilitare temporaneamente senza disinstallare:

Aggiungi `"disabled": true` alla configurazione del MCP:

```json
{
  "mcpServers": {
    "nome-mcp": {
      "command": "npx",
      "args": ["-y", "@package/nome-mcp"],
      "disabled": true
    }
  }
}
```

Per riabilitarlo: rimuovi `"disabled": true`.

### Monitorare il peso in real-time:

1. Usa `/context` per vedere la distribuzione del contesto
2. La sezione "Tool" mostra quanto ogni MCP occupa
3. Se un MCP supera il 10%, considera se è necessario per la sessione corrente

---

## FASE 6 — TROUBLESHOOTING

### MCP non appare in Claude Code:
1. Verifica che il settings.json sia valido JSON (nessuna virgola finale, graffe bilanciaste)
2. Verifica che il comando (npm, npx) sia nel PATH di sistema
3. Riavvia Claude Code completamente
4. Esegui `/mcp` per vedere i log di errore

### MCP connesso ma non funziona:
1. Verifica che le variabili d'ambiente (API_KEY, token) siano corrette
2. Controlla i permessi dell'account (es: API key scaduta o senza i permessi giusti)
3. Verifica che il servizio esterno sia raggiungibile (status page del servizio)

### Conflitti tra MCP:
1. Due MCP che espongono tool con lo stesso nome possono confliggere
2. Soluzione: rinomina uno dei due cambiando la chiave in `mcpServers` (es: "github-1" e "github-2")
3. Claude Code userà il prefisso come disambiguatore

---

## INSTALLAZIONE CONSIGLIATA PER DIGITAL EMPIRE

Setup minimale consigliato per l'ecosistema Digital Empire:

```json
{
  "mcpServers": {
    "chrome-dev-tool": {
      "command": "npx",
      "args": ["-y", "@claude-dev-tool/mcp-server"]
    }
  }
}
```

Tutto il resto si gestisce con skill interne. Questo mantiene il contesto pre-occupato <5%.
