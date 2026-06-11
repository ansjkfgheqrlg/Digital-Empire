# 📡 BUS — Message Bus inter-ecosistema

> **Backbone component.** Gestisce la comunicazione tra ecosistemi via handoff contract.
> Ispirato a `gbus.sh` di AION GROUP. Da costruire in F2 (task 2.3).

## Funzione

Ogni passaggio di lavoro tra ecosistemi è un messaggio strutturato sul BUS.
Il BUS garantisce: tracciabilità, acceptance criteria, cost attribution, retry logic.

## Struttura cartelle (da popolare in F2)

```
Bus/
├── handoffs/        ← messaggi in transito (JSON files)
├── fulfilled/       ← handoff completati (archivio)
├── rejected/        ← handoff falliti con motivo
├── contracts/       ← template HC per ogni coppia ecosistemi
└── bus.sh           ← motore (da creare in F2)
```

## Contratti attivi (da registrare)

I contratti HC-XX-YY-NN sono documentati nei BACKBONE.md dei rispettivi ecosistemi.
Registro master: da creare in F2 come `Bus/contracts/registry.yaml`.

## Stato: DA COSTRUIRE (F2, task 2.3)
