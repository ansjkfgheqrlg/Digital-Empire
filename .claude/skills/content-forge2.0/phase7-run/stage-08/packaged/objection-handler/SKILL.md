---
name: objection-handler
description: >-
  Aiuta copywriter, founder, marketer e venditori a identificare e gestire le
  obiezioni dei prospect dentro sales page, VSL, email di vendita, landing
  page. Applica il framework CPB (Claim-Proof-Benefit) e seleziona la prova
  giusta dal catalogo (prima&dopo, bandwagon, processi logici, showoff con 7
  template, garanzie reali/finte, menzioni media, recensioni, studi). Triggera
  su frasi tipo "come gestisco l'obiezione X", "il mio copy non converte, perché",
  "perché il mio prezzo sembra troppo alto", "il prospect non si fida", "ho
  scritto questa sales page, manca qualcosa", "voglio strutturare una sezione
  obiezioni", "what objections am I missing in this copy". Make sure to use this
  skill whenever the user is writing OR reviewing copy that needs to persuade
  someone to act (buy, signup, opt-in), even if they don't say the word
  "objection" — frasi tipo "non converte" o "il prospect esita" sono trigger
  validi. DO NOT use for: generic copywriting tips not tied to specific
  objections, copy editing without persuasion intent, content marketing for
  awareness, or sources <300 words.
---

# Objection Handler — Skill kernel

> Comando suggerito: `/obj` (o invocazione naturale).
> Skill specializzata nella gestione delle obiezioni del prospect, basata sul Manuale 4 della strategia APSOC.

---

## ⚠️ Invarianti

1. **Identifica l'obiezione prima di gestirla.** Mai applicare una prova a un'obiezione che non hai esplicitato.
2. **Ordina per importanza** (dalla più forte alla più debole). Mai gestire deboli prima delle forti.
3. **Più prove per obiezioni forti.** Una sola prova per le deboli.
4. **Etica esplicita.** Quando proponi showoff o garanzie finte, marca chiaramente che sono "borderline etici".
5. **Non inventare dati.** Se proponi una prova "studi e ricerche", chiedi all'utente la fonte vera. Mai inventare Harvard/Oxford/Stanford.

---

## 🎯 Quando triggerare

Si attiva quando l'utente:
- Sta scrivendo copy persuasivo (sales page, VSL, email, landing, ads)
- Sta facendo review di copy esistente
- Chiede "perché non converte"
- Cita obiezioni esplicite ("il prezzo sembra alto", "non si fidano")
- Vuole strutturare una sezione obiezioni

**NON** si attiva per:
- Tips generici di copywriting (titolo, lead, CTA in astratto)
- Content marketing per awareness
- Copy editing puro (grammar, tono)
- Sorgenti <300 parole (poco materiale)

---

## 🔄 Loop principale

```
1. IDENTIFICAZIONE
   ├── Leggi il copy/contesto fornito dall'utente
   ├── Elenca le obiezioni implicite ed esplicite
   └── Classifica nelle 11 categorie (vedi references/categorie-obiezioni.md)

2. PRIORIZZAZIONE
   ├── Per ogni obiezione, valuta forza (alta/media/bassa)
   ├── Ordina dalla più forte alla più debole
   └── Decidi quante gestire (default: top 3-5)

3. SCELTA PROVE
   ├── Per ogni obiezione, leggi references/catalogo-prove.md
   ├── Seleziona 1-3 prove di categorie diverse
   └── Verifica coerenza con target audience

4. APPLICAZIONE CPB
   ├── Costruisci Claim — Proof — Benefit
   ├── Posiziona nel copy (forti in alto)
   └── Consegna proposta + razionale

5. SELF-CHECK (anti-pitfall)
   ├── Hai generato nuove obiezioni nel testo proposto?
   ├── La gestione è proporzionata alla forza?
   └── Hai marcato le prove "borderline etiche"?
```

---

## 🗺 Routing

| Sei a... | Vai a... |
|---|---|
| Identificare obiezioni implicite | `references/categorie-obiezioni.md` |
| Capire CPB nel dettaglio | `references/processes/cpb-workflow.md` |
| Scegliere quale prova usare | `references/catalogo-prove.md` |
| Vedere template di showoff | `references/patterns/showoff-templates.md` |
| Etica delle prove finte | `references/conventions/etica-prove.md` |
| Esempi end-to-end | `assets/templates/` |
| Test della skill | `evals/evals.json` |

---

## 📥 Input attesi

L'utente può fornire:
- **Copy esistente** (sales page, email, ads) da rivedere
- **Brief del prodotto** (target, prezzo, USP) + richiesta di scrivere sezione obiezioni
- **Singola obiezione** isolata da gestire (es. "come gestisco 'il prezzo è troppo alto'?")

Se il contesto è insufficiente, chiedere all'utente:
1. Cosa vendi (prodotto/servizio) e a chi (target audience)?
2. Prezzo (importante per priorizzare obiezione prezzo)?
3. Stai scrivendo da zero o rivedendo?

---

## 🚦 Anti-trigger (cosa NON fare)

- Tip generici di copywriting (vai su una skill più ampia)
- "Scrivi una sales page completa" (questa skill copre solo la sezione obiezioni)
- Editing grammaticale puro
- Riassunti di teoria copywriting (questa skill è operativa, non didattica)

---

## 📖 Per chi esegue la skill

Leggi le references nell'ordine: 1) `categorie-obiezioni.md` → 2) `catalogo-prove.md` → 3) `processes/cpb-workflow.md`. Il resto on-demand.

Tutto il materiale tecnico viene dal Manuale 4 della strategia APSOC (vedi `references/external-source.md`).
