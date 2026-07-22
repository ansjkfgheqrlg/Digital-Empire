---
Owner: Max
Controllore: Claude
Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
---

# 📊 DASHBOARD ESTATE REVENUE — CRUSCOTTO OPERATIVO KPI (S1..S6)

> **Governo Art.8 §8.3:** Tabella reale di monitoraggio quantificato e numerico per le revenue e le metriche di conversione del Mandato Estate. Dati ancorati a `PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md`.

## 1. CRUSCOTTO SINTESI STREAM (S1..S6)

| Stream | Descrizione | Obiettivo / Target | Stato Attuale | Certezza | Next Step Immediato |
|---|---|---|---|---|---|
| **S1** | Concessionari Anticipati (Novacar live) | 2-3 chiusure a luglio (sconto setup/mese anticipato) | 7 lead caldi in pipeline | **≥95%** | Chiamata di Max con script `ag-a5-script` / A8-Closing |
| **S2** | Manuale Claude Code per il Business (203pp) | Chiusura B-003 (prezzo) e funnel live | Prodotto pronto, prezzo da definire (B-003) | 60-80% | Lancio funnel `empire-premium-style` + checkout Stripe/Gumroad |
| **S3** | Pagine Lancio (`crea.illtuo_impero` & co.) | 1 carosello/giorno/pagina automatico | Audit P0.2 in corso / motore carousel-factory attivo | Media | Collegamento link in bio al funnel S2 + batch settimanale |
| **S4** | Mentalità Brutale (`mentalita.brutale`) | Riattivazione con automazione 100% | Config brand pronto in carousel-factory (`ADR-003`) | Media | Configurazione pipeline pubblicazione automatica e report QA |
| **S5** | YouTube Fliki Automation (canali auto) | 1 video generato e tracciato end-to-end (P12) | Architettura 7-file e swarm `yt-factory` integrati | Medio-Lungo | Test run con API Fliki (`.env`) e generazione checkpoint |
| **S6** | Outreach e Sequenze Delivery | Conversione lead freddi/tepidi in call/vendite | Sequenze email pronte in `05-TEMPLATES-E-KIT/` | Alta | Attivazione motore di invio sequenza di pre-framing e follow-up |

---

## 2. METRICHE DELLA SETTIMANA E MONITORAGGIO LIVE

| Metrica | Minimo Accettabile | Target Ottimale | Valore Attuale | Esito Gate |
|---|---|---|---|---|
| **Anticipi concessionari chiusi (S1)** | 1 | 2 - 3 | 0 (In partenza) | 🟡 In Corso |
| **Revenue complessiva estate** | > 0 € (primo incasso) | [DM] target di chiusura | 0 € | 🟡 In Corso |
| **Chiusura Backlog B-003 (Prezzo S2)** | Decisione presa | Decisione + Stripe link | Aperto | 🔴 Bloccante |
| **Pagine social attive e automatizzate** | 1 (`crea.illtuo_impero`) | 2 (`+ mentalita.brutale`) | 0 (In audit) | 🟡 In Corso |
| **Video YouTube prodotti (S5)** | 1 test P12 | 1 + WF documentato | 0 | 🟡 In Corso |
| **Score Checklist APSOC nei copy** | ≥ 92% | ≥ 95% | N/A (da validare) | 🟢 Pronto |

---

## 3. REGOLE DI ACCERTAMENTO DATI (CPB / APSOC)

1. **Assenza di Stime Fittizie:** Ogni numero inserito in questa dashboard deve essere verificabile da log di Stripe, preventivi firmati in Novacar/PreventivoForge o record `PERF-*.md` in `00-MEMORY/performances/`.
2. **Aggiornamento Obbligatorio:** Dopo ogni run di chiusura o di campagna, l'agente responsabile (o Max) deve aggiornare questa tabella e salvare lo stato di checkpoint in `company/Memory/STATO-EMPIRE.md`.
