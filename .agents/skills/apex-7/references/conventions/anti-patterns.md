# ANTI-PATTERNS — Cosa NON Fare in APEX-7

> Catalogo completo degli anti-pattern che il sistema deve attivamente evitare.

---

## AP01 — Output Senza Critica

**Descrizione:** Produrre output che raggiunge l'utente o lo stage successivo senza passare per CRITIC.

**Perché è sbagliato:** Viola P2 (Autocritica Obbligatoria). Ogni output non criticato è un rischio.

**Come evitarlo:** ORCHESTRATOR verifica che ogni draft passi per CRITIC prima di procedere.

---

## AP02 — Agente che Fa Lavoro Altrui

**Descrizione:** Un agente esegue task che appartengono a un altro agente. Es: ORCHESTRATOR genera contenuto, PLANNER esegue analisi.

**Perché è sbagliato:** Viola P3 (Un Agente, Una Responsabilità). Crea confusione, riduce qualità, impedisce specializzazione.

**Come evitarlo:** Ogni agente ha capability boundaries esplicite nel system prompt.

---

## AP03 — Placeholder e Omissioni

**Descrizione:** Usare "ecc.", "...", "[...]", "e così via" nell'output invece di completare il contenuto.

**Perché è sbagliato:** Viola P4 (Qualità Prima della Velocità). L'output non è usabile.

**Come evitarlo:** Regola WRITER: o scrivi tutto, o non scrivere. CRITIC flagga ogni placeholder come BLOCCANTE.

---

## AP04 — Self-Review Completamente Positiva

**Descrizione:** WRITER valuta il proprio output come perfetto senza identificare dubbi o aree di miglioramento.

**Perché è sbagliato:** Viola P2. La self-review onesta è la prima difesa. Se WRITER non trova problemi, non sta cercando abbastanza.

**Come evitarlo:** WRITER deve sempre elencare almeno 2 "dubbi personali" nella self-review.

---

## AP05 — Cancellazione in Memoria

**Descrizione:** Eliminare record dalla memoria invece di archiviarli.

**Perché è sbagliato:** Viola Regola 2. La conoscenza viene persa. I fallimenti non insegnano più.

**Come evitarlo:** Memory Interface permette solo ARCHIVE, mai DELETE. Ogni archivio ha `archived_reason` e `superseded_by`.

---

## AP06 — Saltare il Piano

**Descrizione:** ORCHESTRATOR procede direttamente all'esecuzione senza passare per PLANNER.

**Perché è sbagliato:** Viola il workflow. Senza piano, l'esecuzione è disorganica e non misurabile.

**Come evitarlo:** Stage 1 (PLANNING) è obbligatorio. ORCHESTRATOR non può spawnare WRITER prima del PLAN.

---

## AP07 — Ignorare il Context Package

**Descrizione:** WRITER produce output senza usare il Context Package di ANALYST.

**Perché è sbagliato:** L'output manca di insight, pattern, e contesto dalla memoria. È meno ricco e meno informato.

**Come evitarlo:** WRITER STEP W1 include obbligatoriamente la lettura del Context Package.

---

## AP08 — Gate Permissivo

**Descrizione:** GATE AGENT fa passare output che non soddisfano i criteri, specialmente ai livelli safety.

**Perché è sbagliato:** Viola Regola 7. Ai livelli L5→L6 e L6→L7 la tolleranza è ZERO. Un gate permissivo può causare output pericolosi.

**Come evitarlo:** Safety gate sono binari: ogni criterio è PASS o FAIL. Nessun PARTIAL.

---

## AP09 — Evoluzione Non Controllata

**Descrizione:** META AGENT modifica più variabili simultaneamente senza test adeguati.

**Perché è sbagliato:** Viola Regola 8. Impossibile determinare quale modifica ha causato miglioramento/peggioramento. Instabilità.

**Come evitarlo:** Regola ferrea: UNA variabile alla volta. Test su 3 campioni. Documenta tutto.

---

## AP10 — Silenzio Operativo

**Descrizione:** Agenti eseguono task senza comunicare lo stato all'utente.

**Perché è sbagliato:** Viola P6 (Trasparenza Totale). L'utente non sa cosa sta succedendo.

**Come evitarlo:** ORCHESTRATOR comunica sempre: agente attivo, step corrente, progresso.
