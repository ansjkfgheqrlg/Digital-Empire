---
Owner: Max
Controllore: Claude
Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
---

# 📑 PREVENTIVO TEMPLATE — MODELLO DI PRESENTAZIONE E CHIUSURA (S1 / A3-Preventivi)

> **Governo Art.8 §8.3:** Template ufficiale e tangibile per la composizione e consegna dei preventivi brandizzati (Stream S1 - Concessionari Anticipati luglio / Novacar live). Ancorato all'implementazione tecnica in `Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html`.

## 1. STRUTTURA DEL PREVENTIVO (APSOC Compliant ≥ 92%)

Un preventivo Digital Empire NON è una lista di prezzi. È un documento di chiusura strutturato nei 5 blocchi APSOC:

### [A] Attention — Copertina Brandizzata
- **Intestazione:** Logo del concessionario/cliente + Logo di garanzia tecnologica ("Powered by PreventivoForge / Digital Empire").
- **Titolo Esatto:** `Preventivo Esclusivo — [Nome Modello / Soluzione]`
- **Riferimento Univoco:** Codice Tracciabilità `[PF-2026-XXXX]` (collegato a `00-MEMORY/performances/`).

### [P] Problem — Analisi del Blocco Operativo
- **Il Contesto:** Sintesi della situazione attuale del cliente (es. "Gestione manuale dei lead a luglio/agosto con tempi di risposta > 24 ore e perdita di conversioni sulla campagna estate").
- **Il Costo del Non-Agire:** Quantificazione numerica delle vendite perse o del tempo sprecato senza il sistema.

### [S] Solution — Scheda Tecnica e Intervento (Dettaglio Chirurgico)
- **Architettura Fornita:**
  - Installazione e configurazione app dedicata (clone Novacar engine).
  - Funnel di acquisizione e qualificazione automatica in stile `empire-premium-style`.
  - Motore di rendering PDF immediato e invio automatico al lead in < 3 minuti.
- **Specifiche Tecniche:** Tabella di riepilogo `table.specs` con le caratteristiche esatte della fornitura.

### [O] Offer — Condizioni Economiche e Sconto Partenza Anticipata (Luglio)
- **Investimento Standard (Settembre):** `[Quota Standard] € / mese + [Setup] €`
- **Offerta Speciale Partenza Anticipata (Chiusura Luglio):**
  - Setup agevolato del -50% per chi si attiva prima di agosto.
  - Operatività garantita dal 1° agosto (quando la concorrenza è ferma e prepara il rientro).
- **Tabella di Chiusura:**
  | Voce di Fornitura | Prezzo di Listino | Investimento Partenza Anticipata |
  |---|---|---|
  | Configurazione Engine & GUI Premium | 1.500 € | **750 €** |
  | Licenza Software & Automazione PDF (1 anno) | 290 € / mese | **290 € / mese** (1° mese incluso) |

### [C] Close — Call to Action e Garanzia di Firma
- **Validità dell'Offerta:** 7 giorni dalla data di emissione (scadenza per rientrare nel batch di attivazione luglio).
- **Modalità di Firma e Attivazione:**
  - Conferma immediata via bonifico o link Stripe di attivazione.
  - Avvio del clone all'istante dell'incasso (`/nuovo-concessionario`).
- **Garanzia:** Mandato Art.2 — sistema consegnato funzionante e testato con prove verificabili.

---

## 2. AGGANCIO AL RENDERER HTML/PDF
Per generare il documento finale in formato A4 ad alta risoluzione, invocare il renderer di PreventivoForge:
```python
# Motore di rendering PDF da template HTML
from pathlib import Path
template_path = Path("Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html")
```
