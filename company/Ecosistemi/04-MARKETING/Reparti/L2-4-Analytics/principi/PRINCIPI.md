---
Type: PRINCIPI
Status: Active
Tags: #principi #analytics #ottimizzazione #anti-rumore #dati #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# Principi Operativi — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2

---

## P1 — Dati, non opinioni

Ogni revisione di copy, ogni verdetto di campagna, ogni pattern distillato deve
essere ancorato a dati misurabili. "Mi sembra che funzioni meglio" non è una diagnosi:
è un'opinione. Il reparto L2.4 esiste per sostituire le opinioni con evidenze.

In pratica: nessun agente di L2.4 emette una raccomandazione di modifica senza citare
almeno una metrica con il suo valore (CTR, open rate, opt-in rate, p-value).

---

## P2 — Il verdetto inconclusivo è un risultato valido

Se il campione non è sufficiente per raggiungere la soglia statistica, il risultato
è "INCONCLUSIVO". Non è un fallimento del processo: è informazione. Significa che
la differenza tra varianti è inferiore a quella attesa, o che il traffico non è
sufficiente per rilevare quella differenza.

Forzare un verdetto da un campione insufficiente è peggio dell'inconclusivo: porta
a revisioni di copy basate sul rumore, non sul segnale.

---

## P3 — Pattern guadagnati, non assunti

Un pattern nella ReasoningBank deve essere guadagnato: almeno 2 run indipendenti
con la stessa ICP, stesso formato, stessa osservazione. Un singolo risultato
eccezionale — anche ottimo — va in stato come "segnale da monitorare".

La ReasoningBank vale quanto l'evidenza che la sostiene. Un namespace pieno di
pattern da un singolo run è rumore organizzato, non conoscenza.

---

## P4 — Chirurgia, non demolizione

Quando AN2/AN5 diagnosticano una sezione APSOC debole, il rework è chirurgico:
si interviene sulla sezione identificata, non si riscrive tutto.

Un copy che ha sezione A debole ma sezione P/S/O forte non si butta: si riscrive
solo la sezione A. Riscrivere tutto resetta il segnale e obbliga a ricominciare
il ciclo di ottimizzazione da zero.

---

## P5 — Il ciclo non si ferma

Il loop di ottimizzazione (WF-OPTIMIZATION-LOOP) è continuo: ogni campagna major
live da ≥7 giorni con dati sufficienti entra nel ciclo. Non esiste una campagna
"troppo piccola per ottimizzare": ogni run produce dati che alimentano la ReasoningBank.

AN-OBSERVER monitora che nessuna campagna major rimanga fuori dal loop per >14 giorni.

---

## P6 — Wiki-first per la conoscenza consolidata

I pattern con evidenza forte (n_run ≥ 3, metriche consistenti) non vivono solo
nel namespace AgentDB: vengono anche trascritti in pagine wiki (`concepts/` o `synthesis/`)
e logati in `wiki/log.md`. In conflitto tra wiki e AgentDB: vince la wiki.

La wiki è leggibile dagli umani. Il namespace è interrogabile dagli agenti.
La conoscenza deve essere accessibile a entrambi.

---

## Connessioni

- [[regole/REGOLE]] · `regole/REGOLE.md` — regole operative non negoziabili
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
