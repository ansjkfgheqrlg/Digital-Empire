# Schemi — La Bibbia dei Messaggi

Raccolta consultabile di tutti gli schemi generati in `master.md`.

## 1. Inbound vs Outbound (Content Fallacy)
```
Post pubblico (inbound)          Outreach attivo (outbound)
────────────────────             ──────────────────────────
Costruisce autorità nel tempo    Genera pipeline ORA
Passivo, aspetta che ti notino   Proattivo, tu scegli il target
< 5% delle entrate reali         > 95% del "lavoro sporco" che converte
```

## 2. Meccanismo Effetto Barnum
```mermaid
flowchart LR
  A[Frase Barnum] -->|sembra specifica| B(Lettore)
  B -->|si riconosce| C{"Come fa a conoscermi così bene?"}
  C --> D[Barriera diffidenza abbassata]
```

## 3. Pilastro 3 — flusso valore anticipato
```
SENZA case study reale → NON dire "sono bravo" → CREA un case study artificiale
                                                  (lavoro gratuito mirato al lead specifico)
                                                  → poi chiedi un micro-commitment
```

## 4. Checklist di validazione (5 Pilastri) — riusata identica da rule-keeper e writer
| Pilastro | Presente? | Come verificarlo |
|---|---|---|
| 1. Personalizzazione | ? | C'è Barnum/Rainbow/variabile di nicchia nella prima riga? |
| 2. Chiarezza 3 sec | ? | Chi+perché comprensibili nei primi ~100 caratteri? |
| 3. Valore anticipato | ? | C'è un'offerta concreta PRIMA di qualunque richiesta? |
| 4. Micro-commitment | ? | La richiesta è minima (non una call)? |
| 5. Basso attrito | ? | L'azione richiesta è completabile in <10 secondi? |

## 5. Sequenza di follow-up (timeline)
```mermaid
sequenceDiagram
    participant W as Writer
    participant L as Lead
    W->>L: Messaggio 1 (giorno 0)
    Note over L: ~20% rispondono qui
    W->>L: Messaggio 2 (giorno 2-3, angolo diverso)
    Note over L: ~40% rispondono qui — IL PICCO
    W->>L: Messaggio 3 - breakup (giorno 5-7)
    Note over L: ~30% rispondono qui (scarsità reale)
```

## 6. Cross-reference generale del framework
```mermaid
flowchart TD
  CF[Content Fallacy] -->|prova con| SP[Stats Proof]
  SLOP[AI slop] --> BARNUM[Effetto Barnum]
  SLOP --> RAINBOW[Inganno Arcobaleno]
  BARNUM --> P1[Pilastro 1: Personalizzazione]
  RAINBOW --> P1
  NICHE[Variabile hard-coded nicchia] --> P1
  P1 --> P2[Pilastro 2: Chiarezza 3 sec]
  P2 --> P3[Pilastro 3: Valore anticipato]
  P3 --> P4[Pilastro 4: Micro-commitment]
  P4 --> P5[Pilastro 5: Basso attrito]
  P5 --> FU[Sequenza follow-up 20/40/30]
  P1 & P2 & P3 & P4 & P5 -.violati da.-> SHAKIL[Caso Shakil]
  P3 -.violato da.-> VEBAD[Video Editor v1]
  P1 & P2 & P3 & P4 & P5 ==soddisfatti da==> VEGOOD[Video Editor v2]
  FU -.violato per assenza da.-> OPEX[Operation Executive]
```
