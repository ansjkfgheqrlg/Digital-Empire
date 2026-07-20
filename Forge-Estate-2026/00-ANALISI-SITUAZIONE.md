# 00 — ANALISI DELLA SITUAZIONE (2026-07-20)

> Fotografia onesta di dove siamo con PreventivoForge prima di partire con la spinta estiva.

---

## 1. Il prodotto — cosa abbiamo in mano

**PreventivoForge**: app Windows per concessionarie che importano auto dalla Germania.
Il venditore incolla il link di un annuncio **mobile.de** (tedesco) → in ~2 minuti ottiene un
**preventivo PDF professionale in italiano**: foto, scheda tecnica tradotta, descrizione
riscritta col copy che vende, **prezzo finale nel titolo** calcolato con la formula del dealer
(default: `esposto × 1.03 + 1.500 + 1.500` — es. 18.000 € → 21.540 €).

### Stato tecnico (verificato nei doc di progetto)
- ✅ **Core testato live**: annuncio reale Mercedes GLA → PDF conforme, gate qualità verdi.
- ✅ **Multi-tenant by design**: un solo motore, ogni dealer ha config (nome, P.IVA, logo, colori, formula prezzo). Nuovo dealer = 1 comando (`nuovo_concessionario.py`) → app brandizzata pronta.
- ✅ **Kill-switch licenze**: blocco/sblocco da remoto in ~1 min (Gist online). Con la vendita una tantum si riusa come leva sul saldo 50/50 e sul piano assistenza (§5).
- ✅ **Consegna semplice**: cartella portabile, zero installazione; serve solo Chrome + linea internet normale (mobile.de blocca IP datacenter/VPN — per questo è app desktop e non SaaS).
- ✅ **Onboarding replicabile**: skill `/nuovo-concessionario` già pronta → firmare il 3° o il 30° cliente costa la stessa fatica.
- ⚠️ **Da fare prima della scala**: test exe su PC pulito (certificare che gira senza ambiente dev) — già segnalato in CONSEGNA-NOVACAR §6.
- ⚠️ **Dipendenza strutturale**: se mobile.de cambia layout il parser si aggiorna lato nostro → è un argomento di VENDITA (assistenza) non solo un rischio (§5).

## 2. Clienti — dove siamo

| Cliente | Stato | Note |
|---|---|---|
| **Novacar srl** (prof-autocad) | ✅ Primo cliente, prodotto in uso | **Dati reali e testimonianza DISPONIBILI** (confermato da Max 2026-07-20) → raccogliere SUBITO i numeri per il case study |
| Altre concessionarie | ⬜ Nessuna | Il piano estivo parte da qui |

Siamo nella fase "1 cliente → N clienti": il prodotto esiste e funziona, manca **il motore commerciale sul vertical**.

## 3. Asset già esistenti (non ripartiamo da zero)

| Asset | Stato | Uso nel piano |
|---|---|---|
| Macchina outreach (email 22 agenti + LinkedIn 6 + Instagram 6) | ✅ Attiva MA tarata su agency/infobusiness | Va **ri-tarata sul vertical concessionarie** (nuovo settore, keyword, angoli) → file 04 |
| 458 email in coda (vecchio target) | ⚠️ Fuori target | NON sprecare sul vertical auto: valutare solo le agency automotive |
| Sistema copy APSOC/CPB (copy-workflow) | ✅ Completo | Usato per script, email, contenuti |
| Carousel factory | ✅ Attiva | Produzione caroselli IG/LinkedIn del piano contenuti |
| Skill `/case-study-forge` | ✅ Pronta | Caso studio Novacar (prove non promesse) |
| Landing `presentazione-empire.vercel.app` | ✅ Online | Generica agency — valutare pagina dedicata Forge (low priority) |
| Team: Max (strategy/volto) + Gael (tech) + **Neri (nuovo, chiamate)** | 🟡 Neri da formare | Onboarding 5 giorni nel file 03 |

## 4. Gap critici (cosa MANCAVA — coperto da questo piano)

1. ~~ICP vertical concessionarie~~ → file 02
2. ~~Script chiamate a freddo + formazione caller~~ → file 03 + skill `/cold-call-forge`
3. ~~Sequenze outreach sul vertical~~ → file 04
4. ~~Piano contenuti estate~~ → file 05
5. **Case study Novacar scritto e approvato** → azione n.1 della Settimana 1
6. **Pagina/demo dedicata** (anche solo un video demo 2 min) → Settimana 1-2
7. Prezzo pubblico e condizioni (una tantum) → da CONFERMARE da Max (proposta in file 01 §2)

## 5. Posizionamento e modello commerciale

### Chi NON siamo
Non siamo un gestionale (DealerK & co.), non siamo "un'agenzia AI" generica, non vendiamo "consulenza".
### Chi siamo
> **"Dalla Germania al preventivo firmabile in 2 minuti."**
> L'unico strumento che fa UNA cosa sola — l'annuncio mobile.de diventa preventivo italiano professionale — e la fa al 100%.

### Modello: UNA TANTUM (deciso 2026-07-20)
- **Listino: €2.900** una tantum · **Offerta "prime 5 concessionarie": €2.400** (scarsità vera: sono i prezzi di lancio).
- Pagamento **50% all'ordine / 50% alla consegna** → qui il kill-switch fa da garanzia sul saldo (nessuna rata = app sospesa, riattiva al saldo).
- **Garanzia 30 giorni soddisfatto o rimborsato** (abbatte l'unica obiezione vera: la fiducia).
- **Assistenza e aggiornamenti parser inclusi 12 mesi**; dal 13° mese piano assistenza opzionale **€490/anno** (chi non lo rinnova tiene l'app ma senza aggiornamenti quando mobile.de cambia).
- ⚠️ *Questi numeri sono la proposta operativa del piano: Max conferma o corregge prima del go-live (Settimana 2).*

### Perché l'una tantum regge l'obiezione prezzo
- Margine medio su un'importazione: ~€2.500-3.000+ → **una vendita in più in un anno e l'investimento è ripagato.**
- Tempo risparmiato: preventivo manuale 30-60 min vs 2 min → a 10 preventivi/settimana sono **~7 ore/settimana restituite a un venditore**.
- Nessun canone = argomento contro i gestionali in abbonamento ("con loro paghi per sempre, con noi una volta").

## 6. Concorrenza (onesta)

| Alternativa | Perché non basta |
|---|---|
| **Farlo a mano** (Word/Excel + Google Translate) | 30-60 min a preventivo, errori di calcolo, look amatoriale che brucia fiducia |
| **Gestionali dealer** (DealerK, ecc.) | Ottimi per parco auto/fatture, ma NON fanno il salto mobile.de→preventivo: niente scraping annuncio, niente traduzione+copy, costano canone e mesi di setup |
| **Lo stagista** | Costa più del software in 3 mesi, sbaglia, e a ferragosto non c'è |
| **Niente preventivo** ("te lo dico a voce") | Il cliente esce e compra dove il preventivo è arrivato scritto e bello |

## 7. Rischi estate + contromisure

| Rischio | Probabilità | Contromisura |
|---|---|---|
| **Agosto morto** (chiusure 8-23 ago circa) | Certa | Piano costruito attorno: blitz prima (27 lug-7 ago) e dopo (24 ago→set), in agosto solo contenuti + automazioni leggere |
| Neri nuovo → ramp-up lento, prime chiamate rigide | Alta | 5 giorni onboarding + roleplay + script parola-per-parola + shadowing; KPI personali dolci le prime 2 settimane |
| Prezzo una tantum percepito alto | Media | Garanzia 30 gg + rateizzazione 50/50 + ancoraggio ROI (un'auto in più = ripagato) |
| Case study Novacar senza numeri "wow" | Bassa | Regola "prove non promesse": usiamo i numeri veri che abbiamo, anche piccoli (tempo/preventivo è già fortissimo) |
| mobile.de cambia layout / anti-bot | Media | Assistenza 12 mesi inclusa = parte dell'offerta; parser aggiornato lato nostro |
| Compliance cold outreach (GDPR) | Bassa | Solo recapiti business pubblici, legittimo interesse B2B, opt-out immediato → nota in file 04 §7 |

## 8. Numeri del piano (sintesi — dettagli file 01)

- Obiettivo: **3-5 firme** × €2.400-2.900 = **€7.200–14.500** entro il 30 settembre.
- Funnel necessario: ~500-700 chiamate + ~400 email + LinkedIn/IG → **25-40 demo** → 3-5 firme.
- La metrica regina: **demo fissate** (unica cosa che conta fino a settembre).
