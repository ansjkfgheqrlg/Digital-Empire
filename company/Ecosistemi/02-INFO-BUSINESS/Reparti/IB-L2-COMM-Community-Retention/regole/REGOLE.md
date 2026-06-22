---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #community #retention #consenso #IB-L2-COMM
Created: 2026-06-21
Last updated: 2026-06-21
---

# Regole Non Negoziabili — IB-L2-COMM Community & Retention

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Onboarding entro 24h, sempre

Ogni acquirente deve avere accesso piattaforma attivo entro 24h dall'acquisto e l'email di
benvenuto entro 1h. Il GATE di accesso è verificato da formazione-admin / formazione-student.

Se l'accesso non risulta attivo entro 24h → IB-COMM-ONBOARDER apre alert immediato a
IB-COORD-COMMUNITY. Nessun acquirente resta in attesa silenziosa fino al giorno dopo.

**Perché esiste questa regola:** l'acquisto è la consegna del valore (P1). Un onboarding lento
genera richieste di rimborso e brucia il momento di massima motivazione dell'acquirente.

---

## R2 — Nessun outreach automatico sugli studenti

Il cross-sell verso 01-AGENCY avviene SOLO su segnale esplicito dello studente E consenso
documentato. Nessuna lista esportata, nessun invio massivo, nessuna promo automatica.

Questo vale per:
- Domande di implementazione in community.
- Completamento di moduli avanzati (>50%).
- Richieste dirette o risposte positive alla survey.

In ogni caso il contatto cross-sell passa dal gate G-COMM (consenso verificato). Score alto
senza consenso = nessun handoff. La pressione di lancio non è eccezione valida.

---

## R3 — Testimonianze solo su metrica reale e verificabile

Nessuna testimonianza si pubblica senza una metrica reale verificata da IB-COMM-QA (G-COMM).
Niente claim di risultato non sostenuti, niente numeri inventati o gonfiati (Mandato Art.2).

La testimonianza si chiede al milestone di completamento, mai prima. IB-COMM-SOCIAL lega ogni
testimonianza a un dato verificabile (modulo completato, risultato misurato dallo studente).
Testimonianza senza metrica → FAIL automatico al gate, nessuna pubblicazione.

---

## R4 — G-COMM è bloccante su cross-sell e testimonianze

Nessun handoff HC-IB-AG-01 verso AGENCY e nessuna testimonianza pubblicata escono senza gate
verde di IB-COMM-QA. Il gate G-COMM non ha deroga per urgenza.

IB-COMM-QA è indipendente: non riporta agli esecutori che presidia. Ogni gate (PASS/FAIL) è
registrato nel log inviolabile `infobusiness/community/crosssell/g-comm-log/`. Un handoff o una
testimonianza senza riga di log corrispondente è una violazione segnalata a IB-COORD-COMMUNITY.

---

## R5 — Questo reparto NON gestisce dispute commerciali

Reclami, richieste di rimborso e contestazioni d'acquisto NON si gestiscono in autonomia dalla
community. Escalation immediata a IB-DIRECTOR / Board.

La community gestisce relazione, valore ed engagement; non negozia rimborsi né condizioni
commerciali. Un agente che risponde a un reclamo con una promessa commerciale crea esposizione
che nessuno presidia.

---

## R6 — Win-back gentile, mai invasivo

IB-COMM-RETENTION recupera l'inattivo con sequenze di aiuto, non con pressione o sensi di colpa.
Massimo definito di tentativi per studente; oltre la soglia si chiude senza insistere.

Lo scopo è rimuovere friction, non forzare un ritorno (P7). Un win-back invasivo aumenta i
rimborsi e i report negativi: il danno supera il recupero.

---

## R7 — Completion rate critico = problema di prodotto, si segnala

Se una coorte va sotto il 20% di completamento, IB-COORD-COMMUNITY NON tenta di "salvare" il
numero con più rituali: segnala il pattern a IB-L2-PRODUCT (HC-COMM-PROD-01) e a IB-DIRECTOR.

La retention amplifica un corso buono, non compensa uno debole (P6). Nascondere un drop-off
strutturale dietro l'attività della community è una violazione di trasparenza verso IB-DIRECTOR.

---

## R8 — Nessuna PII oltre l'identificativo nei namespace

I file di stato del reparto usano `studente_id` / `lead_id` come riferimento. Email, telefono e
dati personali restano sulla piattaforma corsi / CRM, non vengono copiati nei file AgentDB.

Il dossier cross-sell verso AGENCY contiene `lead_id`, fonte, segnale, score e flag consenso con
data — non il payload PII completo, che AGENCY recupera dal sistema autorizzato dopo l'handoff.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ib-comm-qa]] · `agenti/ib-comm-qa.md` — esecutore del gate G-COMM
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — handoff contract e namespace in dettaglio
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-COMM` — fonte dei principi non negoziabili
