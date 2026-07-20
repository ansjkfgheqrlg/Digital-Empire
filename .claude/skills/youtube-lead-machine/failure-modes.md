# FAILURE-MODES — youtube-lead-machine (regola R3 reparto: come fallisce QUESTA skill)

| # | Modo di fallimento | Sintomo precoce | Causa | Contromisura nella skill | Verifica al gate |
|---|---|---|---|---|---|
| F1 | Deriva a "consigli di views" (algoritmo, trend, viralità) | risposta parla di reach prima che di call | obiettivo percepito sbagliato | Regola §0.1 + tabella funnel + ANALYTICS ordine metriche | scenario E4 (G1) |
| F2 | Script improvvisato senza factory | output = script nuovo senza struttura 7-componenti | pigrizia del percorso breve | kernel §3: modalità `script` → delega esplicita + vincoli | scenario E2 |
| F3 | Salta il gate 3-domande | propone "mandagli subito la call" a lead non qualificato | troppa generosità percepita | LEAD-MAGNET-OPS §gate + regola declina-con-valore | scenario E3 (G3) |
| F4 | Risposta più povera della sorgente (R1 violata) | risposta generica senza numeri/verifiche | riassunti invece di references | progressive disclosure: 5 reference separati, kernel solo rotta | E7 + check R1 |
| F5 | Duplica la strategia invece di puntarla | output ricopia pezzi di STRATEGIA | non-applicare ADR-003 | header kernel + G5 negli evals | G5 |
| F6 | Confina male con dossier 16 S5 (Fliki/faceless) | consiglia pipeline automatica TTS in una domanda organica | sovrapposizione percepita | kernel header §confine + lipsum E6 | scenario E6 |
| F7 | Marketing-guru (clickbait, promesse gonfiate, tecnichese) | titolo/CTA che Max boccerebbe | perdere TOV sotto pressione creativa | §0.5 TOV + Libreria anti-pattern + QA copy ≥85 | E1/E2 QA |
| F8 | Skill che invecchia zitta: batch #1 finito, nessun aggiornamento | risposte puntano a V01-V06 quando sono già online | stato non aggiornato | §7 "stato del canale" + loop wiki + owner FORGE-AGENT-SKILL | check registro al gate |

**Anti-recidiva:** qualsiasi FAIL reale capita durante l'uso → si scrive qui la riga (causa+fix+regola)
prima di continuare (cultura REGISTRO-ERRORI, dossier 15). Diff del vendor = 0 (verificato al gate: le
cartelle sorgente `Formazzione/`, `copy-workflow/`, `SKILL & Agenti/` non sono state toccate).
