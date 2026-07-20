# 02 — ICP CONCESSIONARIE (chi chiamiamo, chi no)

> Scheda ICP per il vertical PreventivoForge, formato compatibile con la skill `/icp-radar`.
> Neri la studia il giorno 1: **ogni lead in lista deve rispettare questi criteri.**

---

## 1. Il cliente ideale in una frase

> **Autosalone indipendente italiano (2-20 persone) che compra usato/km0 in Germania — tipicamente via mobile.de — e rivende in Italia, dove il TITOLARE o un venditore senior fa ancora i preventivi a mano.**

## 2. Scheda ICP operativa

```yaml
icp:
  nicchia: "concessionarie indipendenti importazione Germania → Italia"
  versione: "1.0"
  aggiornato_at: "2026-07-20"

  criteri_qualifica:
    must_have:
      - "autosalone/concessionaria INDIPENDENTE (no store ufficiali di marca unica)"
      - "importa attivamente: annunci che citano Germania/mobile.de/'su ordinazione dall'estero'"
      - "dimensione: 2-20 persone (sotto 2 = troppo piccolo; sopra 20 = procurement lento)"
      - "recapito business pubblico raggiungibile (telefono fisso del salone + email/PEC)"
      - "decisore identificabile: titolare, socio, responsabile vendite (nome trovabile online)"
    nice_to_have:
      - "sito web attivo ma preventivi chiaramente artigianali (PDF brutti/scansi in vetrina)"
      - "attivo su AutoScout24/Subito/Instagram con annunci di importazione"
      - "parla di 'importazione', 'km 0 tedesche', 'auto su ordinazione' nei testi"
      - "nord/centro Italia (Lombardia, Veneto, Emilia-R., Piemonte, Toscana) = densità importatori"
    esclusioni:
      - "concessionarie ufficiali di rete (VW, BMW store...): gestionale imposto dalla casa madre"
      - "grandi gruppi multi-sede (processo decisionale lungo, gare)"
      - "solo auto italiane di ritiro permute (niente import → niente pain)"
      - "noleggio a lungo termine puro / broker senza salone fisico"

  score_threshold: 60

  scoring_matrix:
    - criterio: "importa dalla Germania (segnale esplicito negli annunci/sito)"
      peso: 35
    - criterio: "decisore raggiungibile (nome titolare trovato)"
      peso: 20
    - criterio: "dimensione in range 2-20"
      peso: 15
    - criterio: "recapiti business pubblici validi (tel + email)"
      peso: 15
    - criterio: "segnale dolore visibile (preventivi artigianali, sito datato, traduzioni maccheroni)"
      peso: 15

  angolo_outreach:
    problema_principale: "Ogni preventivo su un'auto da importare costa 30-60 minuti di lavoro manuale: tradurre il tedesco, copiare foto e dati, calcolare il prezzo col margine giusto, impaginare qualcosa di decente. E mentre lo prepari, il cliente ha già chiesto ad altri 3."
    hook_di_attacco: "'Quanto tempo perde il vostro venditore migliore a fare preventivi su Word invece di vendere? Noi lo abbiamo ridotto a 2 minuti: incolla il link mobile.de, esce il PDF in italiano col vostro logo e il prezzo finale già calcolato.'"
    prova_da_usare: "Case study Novacar (numeri reali — vedi file 05 §3) + preventivo-demo fatto col LORO annuncio"

  obiezioni_tipiche_di_nicchia:
    - obiezione: "Facciamo già tutto con Excel/Word, gratis"
      risposta_provata: "file 03 §5, obiezione 2 (CPB tempo)"
    - obiezione: "Ho già il gestionale"
      risposta_provata: "file 03 §5, obiezione 5 (non sostituisce, fa la parte che il gestionale non fa)"
    - obiezione: "Costa troppo per un programma"
      risposta_provata: "file 03 §5, obiezione 1 (ancoraggio margine un'auto)"
    - obiezione: "Non mi fido dell'intelligenza artificiale"
      risposta_provata: "file 03 §5, obiezione 6 (l'app è vostra, gira sul vostro PC, i prezzi li decidete voi)"
```

---

## 3. Dove trovarli (fonti lista lead)

| Fonte | Come | Resa attesa |
|---|---|---|
| **AutoScout24 / Subito.it / automobile.it** | Cerca annunci con "importazione", "Germania", "su ordinazione", "km 0 tedesca" → risali al dealer (pagina rivenditore) | ⭐ altissima: segnale import GARANTITO |
| **Google Maps** | Query: "autosalone usato", "concessionaria multimarca", "importazione auto germania" per provincia (MI, BS, VR, TV, MO, RE, TO, FI...) | Alta |
| **Instagram** | Autosaloni che postano auto con caption tipo "in arrivo dalla Germania" → profilo attivo = anche canale DM | Media-alta (migliore per DM) |
| **LinkedIn** | Titolari "titolare presso autosalone X", "dealer", "automotive" + filtro PMI | Media |
| **Albi/elenchi** | Camera di Commercio / elenchi pubblici rivenditori | Bulk freddo (score basso, da filtrare) |

**Regole raccolta:** mai comprare liste · ogni lead annota la FONTE e il segnale import · recapiti solo business pubblici (mai cellulari privati trovati chissà dove).

**Target lista:** 300 lead entro 27/07 (lista 1) + altri 300 entro 24/08 (lista 2).

---

## 4. I 3 archetipi che incontrerà Neri

| Archetipo | Come lo riconosci | Come gli parli |
|---|---|---|
| **Il Titolare-padrone** (50-65 anni) | "Qui decido io", scettico, al telefono 30 secondi | Zero tecnicismi. Solo: tempo perso, soldi, "se non le piace la rimborso". Nome di Novacar subito |
| **Il Figlio/Responsabile vendite** (28-40) | Digitale, ha già visto tool, fa domande tecniche | Entusiasta ma preciso: app locale, formula prezzo vostra, demo col vostro annuncio |
| **La Centralinista/Segretaria** | Filtra le chiamate del titolare | Alleata, non ostacolo: script gatekeeper file 03 §3 (mai mentirle, darle un motivo concreto) |

---

## 5. Aggiornamento ICP (loop)
- Ogni venerdì Neri segnala: obiezioni nuove, archetipi nuovi, segnali che predicono demo alta.
- Dopo le prime 10 demo: Max ricalibra score/pesi.
- Regola: l'ICP si riscrive coi dati di campo, mai a sensazione.
