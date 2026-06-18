---
Type: CONCEPT
Status: Active
Tags: #state #brand #namespace #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# STATE — L2.5 Brand & Creative Strategy

> Stato operativo del reparto: catalogo brand_kit attivi, namespace memoria, regole di integrità.
> Aggiornare questo file dopo ogni workflow completato (WF-BRAND-KIT-BUILD / WF-BRAND-AUDIT /
> WF-BRAND-EVOLUTION) e dopo ogni modifica allo stato di un brand_kit.

---

## Namespace memoria del reparto

```
marketing/brand/
├── kits/
│   ├── DE/
│   │   ├── voice_guide.md      → voce DE: diretta, provocatoria, trasparente (Mandato Art.2)
│   │   ├── visual_brief.md     → palette, font, mood, reference visual DE
│   │   ├── icp.md              → ICP principale DE: imprenditore/info-producer che vuole autonomia
│   │   ├── tone_chart.md       → tono per canale: email/ads/social/video
│   │   └── _metadata.json      → version, data_creazione, data_review, stato
│   └── {cliente_id}/           → ogni cliente agency onboardato riceve il suo kit (struttura identica)
├── audit/
│   ├── {brand_id}_audit_YYYYMMDD.md  → report audit completo (WF-BRAND-AUDIT)
│   ├── {brand_id}/
│   │   ├── dossier_competitor.json   → analisi competitiva BR4
│   │   ├── gap_analysis.md           → gap posizionamento BR1
│   │   ├── voice_audit.md            → audit coerenza voce BR2
│   │   └── visual_audit.md           → audit coerenza visual BR3
│   └── g5-log/
│       └── {output_id}_g5_YYYYMMDD.json  → log di ogni check BR-QA (PASS/FAIL + feedback)
└── evolution/
    └── ADR-DRAFT-BRAND-EVOLUTION-YYYYMMDD.md  → bozze proposte evolutive (→ Max per approvazione)
```

---

## Catalogo brand_kit attivi (aggiornare dopo ogni WF-BRAND-KIT-BUILD)

| brand_kit_id | Stato | Versione | Data creazione | Data ultimo aggiornamento | Data review pianificata | Owner |
|---|---|---|---|---|---|---|
| `DE` | Attivo | 1.0 | 2026-06-18 | 2026-06-18 | 2026-09-18 | BRAND-LEAD |

*Nota: il brand_kit DE versione 1.0 è il kit iniziale che codifica il Mandato Art.2 come
brand_kit operativo. È il kit di default per tutti gli output Digital Empire. Prima di M1
(build M1 = scaffolding + motore), il kit DE deve essere completato con i 4 artefatti
(voice_guide, visual_brief, icp, tone_chart) da BR2 e BR3.*

---

## Regole di integrità (obbligatorie per chiunque scriva in questo namespace)

1. **Nessun brand_kit si modifica in autonomia** — ogni modifica a un kit esistente passa
   per BRAND-LEAD. Per il kit DE: obbligatoria approvazione Max via ADR.
2. **Versioning esplicito** — ogni modifica a un kit aggiorna `_metadata.json` con la nuova
   versione (1.0 → 1.1 per fix/aggiornamenti minori; 2.0 per evoluzioni fondamentali).
3. **Date di review** — ogni kit ha una data di review pianificata (default: ogni 90gg).
   Kit scaduti non aggiornati vengono segnalati da BRAND-LEAD a MKT-Conductor.
4. **Il g5-log è inviolabile** — nessun file nel g5-log/ viene modificato post-check.
   Un check eseguito produce un record permanente.
5. **I namespace AgentDB sono speculari a questa struttura** — il contenuto di
   `marketing/brand/kits/` è la fonte di verità; AgentDB indicizza per ricerca semantica.
   In conflitto: vince il file markdown (wiki-first, ADR-002).

---

## Stato audit per brand_kit (aggiornare dopo ogni WF-BRAND-AUDIT)

| brand_kit_id | Ultimo audit | Stato voce (score) | Stato visual | Gap aperti | Prossimo audit |
|---|---|---|---|---|---|
| `DE` | 2026-06-18 (primo setup) | Da misurare (M1) | Da misurare (M1) | Nessuno — kit nuovo | 2026-09-18 |

---

## Log workflow recenti (aggiornare dopo ogni run)

| Data | Workflow | Brand kit | Esito | Note |
|---|---|---|---|---|
| 2026-06-18 | Setup iniziale reparto L2.5 | DE (v1.0 scaffolding) | Struttura creata | Kit DE da completare con i 4 artefatti in M1 |

---

## Integrità namespace — check periodico

Comandi per verificare lo stato del namespace (da eseguire manualmente o via `consistency-check.ps1`
quando costruito):

```powershell
# Verifica che ogni brand_kit abbia i 4 file richiesti
Get-ChildItem "marketing/brand/kits/" -Directory | ForEach-Object {
    $kit = $_.Name
    $files = @("voice_guide.md", "visual_brief.md", "icp.md", "tone_chart.md", "_metadata.json")
    $files | ForEach-Object {
        if (-not (Test-Path "marketing/brand/kits/$kit/$_")) {
            Write-Warning "KIT $kit manca il file: $_"
        }
    }
}
```

---

## Connessioni

- [[README]] · `README.md`
- [[KPI]] · `kpi/KPI.md`
- [[WF-BRAND-KIT-BUILD]] · `workflow/WF-BRAND-KIT-BUILD.md`
- [[brand-lead]] · `agenti/brand-lead.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — invariante del kit DE)
