---
Type: PRINCIPI
Status: Active
Tags: #principi #infobusiness #prodotto #produzione #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# Principi — IB-L2-PROD Produzione Prodotti

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — La validazione precede sempre la produzione

Nessun prodotto si crea su intuizione. L'idea passa da IB-PROD-VALID (scoring /100 su 5 criteri
+ MVP test 7gg) prima che una sola riga di MKD venga forgiata. Il materiale raw può essere
bellissimo, la fonte ricca, l'entusiasmo alto: senza score ≥60 e 5 "sì, lo comprerei" reali da
ICP, l'idea resta in BACKLOG.

La prova pratica: il brief validato è il documento di confine. WF-VALIDAZIONE lo firma, WF-CORSO
e WF-EBOOK lo ricevono. Senza brief validato, la pipeline di produzione non parte.

---

## P2 — Il materiale grezzo non si butta: si espande, mai si sintetizza

Il valore di 02-INFO-BUSINESS è il raw già posseduto (registrazioni, PDF, manuali, transcript in
`Formazzione/`). Il MKD copre il 100% degli atomi informativi della fonte. La trasformazione
raw → MKD è espansione, non riassunto: il rapporto lunghezza MKD / lunghezza fonte è ≥1.

Quando un atomo della fonte sembra ridondante, la risposta corretta è ristrutturarlo nel MKD,
non eliminarlo. IB-PROD-QA verifica la copertura con checklist quantitativa: ogni atomo perso è
un FAIL, non una scelta editoriale.

---

## P3 — Ogni lezione è un risultato, non una spiegazione

Una lezione non è completa perché "spiega bene un concetto". È completa quando dichiara 1 outcome
verificabile e misurabile e contiene un esercizio pratico che lo produce. "Capire X" non è un
outcome; "configurare X e mostrare che funziona" lo è.

IB-PROD-CURRIC mappa l'outcome per ogni lezione. IB-PROD-QA verifica che esista e sia misurabile.
Una lezione teorica senza esercizio non passa il gate, anche se il contenuto è eccellente.

---

## P4 — Il confine produzione/integrazione/video non è negoziabile

IB-L2-PROD progetta e scrive il prodotto (MKD, curriculum, script, struttura). 03-CONTENT-FACTORY
monta i video. PLATFORM (formazione-*) costruisce il corso su Supabase+Next.js. Ogni ruolo presidia
la propria responsabilità. Se IB-PROD-WRITER inizia a montare video o IB-PROD-PLATFORM inizia a
riscrivere lo script, il sistema di qualità si rompe.

I confini sono gli handoff contract: `HC-CF-IB-01` verso 03-CF, `HC-PL-IB-01` verso PLATFORM,
`HC-IB-VEND-01` verso IB-L2-VEND. Ogni handoff ha acceptance criteria espliciti.

---

## P5 — Prove non promesse, anche nel prodotto

Il Mandato Art.2 vale dentro il prodotto, non solo nel marketing. Nessuno script di lezione, nessun
capitolo di ebook dichiara un claim ("ottieni X in Y giorni") senza prova o motivazione esplicita.
Il prodotto che vende fumo distrugge il posizionamento DE più di un prodotto mai lanciato.

I [DM] sono onestà: dove un numero non è misurato, si dichiara [DM], non si inventa.

---

## P6 — Nessun lancio di ombre: il prodotto esiste prima del lancio

Il corso esiste sulla piattaforma reale, lo smoke test "studente fantasma" completa il modulo 1
end-to-end senza errori, l'ebook è esportato e scaricabile, prima di qualsiasi consegna a IB-L2-VEND.
Non si annuncia un prodotto che non si può aprire.

IB-PROD-PLATFORM verifica l'esistenza reale; IB-PROD-QA conferma con smoke test. La consegna a
vendite avviene solo su prodotto live e verificato.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-PROD` principi area
- [[README]] · `README.md` — missione del reparto
