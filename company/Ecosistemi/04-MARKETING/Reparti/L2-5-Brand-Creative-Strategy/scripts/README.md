---
Type: CONCEPT
Status: Active
Tags: #scripts #brand #automation #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# SCRIPTS — L2.5 Brand & Creative Strategy

> Script di supporto del reparto. Tutti deterministici, nessun side-effect su file esistenti
> senza conferma esplicita. Target V2 (build dopo skill P0 `brand-strategy-gate`).
>
> **Stato attuale:** progettati, non ancora costruiti. Priorità: dopo skill P0 in M1.

---

## Script 1 — `brand-kit-builder.ps1`

**Stato:** target V2 — da costruire in M2 dopo WF-BRAND-KIT-BUILD validato
**Scopo:** crea la struttura cartella per un nuovo brand_kit in modo deterministico.
**Logica:**
1. Riceve `brand_kit_id` come argomento.
2. Verifica che l'ID non esista già in `marketing/brand/kits/` (idempotenza).
3. Crea la cartella con i 4 file template vuoti: `voice_guide.md`, `visual_brief.md`,
   `icp.md`, `tone_chart.md`, `_metadata.json`.
4. Popola `_metadata.json` con: brand_kit_id, version "1.0", data_creazione, stato "in_progress".
5. Aggiorna `state/README.md`: aggiunge il kit alla lista in stato "in_progress".
6. Output: conferma path creato o errore se il kit esiste già.

```
Utilizzo: .\brand-kit-builder.ps1 -BrandKitId "cliente-nomecliente"
Output: "Kit creato in marketing/brand/kits/cliente-nomecliente/ — pronto per WF-BRAND-KIT-BUILD"
```

**Dipendenze:** nessuna — script standalone.
**Side-effect:** crea cartella + file vuoti + aggiorna state/README.md.

---

## Script 2 — `competitor-scanner.ps1`

**Stato:** target V2 — da costruire in M2 dopo BR4 validato
**Scopo:** avvia una scansione rapida di 3-5 competitor per un brand_kit specificato.
**Logica:**
1. Riceve `brand_kit_id` e lista competitor (file .txt o argomento) come input.
2. Verifica in `marketing/brand/audit/` se esiste un dossier_competitor recente (< 30gg).
3. Se esiste e recente: output "dossier aggiornato — usa quello" (no lavoro duplicato).
4. Se non esiste o vecchio: crea il file `dossier_competitor_YYYYMMDD.json` con struttura
   vuota pre-compilata da riempire da BR4 (non popola dati automaticamente — deterministico).
5. Aggiorna `state/README.md`: aggiunge task "competitor scan pending" per brand_kit_id.

```
Utilizzo: .\competitor-scanner.ps1 -BrandKitId "cliente-X" -Competitor "agenzia1,agenzia2,agenzia3"
Output: "Template dossier creato in marketing/brand/audit/cliente-X/ — da completare da BR4"
```

**Dipendenze:** nessuna — script standalone, non chiama API esterne.
**Nota:** non raccoglie dati in autonomia — crea la struttura che BR4 riempie. Dry-run safe.

---

## Script 3 — `consistency-check.ps1`

**Stato:** target V2 — da costruire dopo skill `brand-strategy-gate` (P0)
**Scopo:** verifica batch coerenza brand su un set di output recenti contro il brand_kit dichiarato.
Uso tipico: check periodico anti-deriva (mensile o su trigger di BRAND-LEAD).
**Logica:**
1. Riceve `brand_kit_id` e path di una cartella con output da verificare.
2. Per ogni file .md/.txt nella cartella:
   - Carica il brand_kit da `marketing/brand/kits/{brand_kit_id}/`
   - Applica check sintetico (presence di parole vietate, absence di proof_point su claim)
   - Produce: `output_id`, `warning_count`, `tipo_warning_principale`
3. Output: report CSV in `marketing/brand/audit/consistency_check_YYYYMMDD.csv`
4. Se warning_count > soglia configurabile: segnala a BRAND-LEAD (entry in log).

```
Utilizzo: .\consistency-check.ps1 -BrandKitId "DE" -OutputFolder "path/agli/output"
Output: "consistency_check_20260618.csv — 12 output verificati, 2 warning (vedere report)"
```

**Dipendenze:** skill `brand-strategy-gate` (P0) — questo script la invoca per ogni file.
**Nota:** produce warning, non modifica niente. Zero side-effect sui file esaminati.

---

## Note generali

- Tutti gli script usano PowerShell (coerente con l'infrastruttura DE su Windows).
- Nessuno script modifica file di contenuto senza conferma dell'utente.
- Tutti producono output in path deterministici (no creazione path casuali).
- Gli script sono idempotenti: rieseguiti sullo stesso input, producono lo stesso output.
- Costruzione: dopo skill `brand-strategy-gate` P0 (M1) e WF-BRAND-KIT-BUILD validato (M2).

---

## Connessioni

- [[state-readme]] · `state/README.md`
- [[skills-md]] · `skills/SKILLS.md`
- [[br4-brand-analyst]] · `agenti/br4-brand-analyst.md`
- [[br-qa-brand-consistency-verifier]] · `agenti/br-qa-brand-consistency-verifier.md`
