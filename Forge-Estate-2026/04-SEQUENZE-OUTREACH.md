# 04 — SEQUENZE OUTREACH VERTICAL CONCESSIONARIE

> Adattamento della macchina outreach esistente (34 componenti, `Outreach/`) al vertical auto-import.
> Regole che NON cambiano: volumi prudenti (25-30 email/gg), framework 5 Pilastri, personalizzazione Barnum, "prove non promesse".

---

## 1. Setup tecnico della macchina (Gael + Max, Settimana 1)

La macchina oggi è tarata su agency/infobusiness/coach. Interventi per il vertical:

| Componente | Cosa cambiare |
|---|---|
| Scraper/Apify/Google Maps (`scraper.py`, `google_scraper.py`, `outscraper_scraper.py`, `apify_leads_finder.py`) | **Nuovo settore `concessionari_import`**: query "autosalone usato", "concessionaria multimarca", "importazione auto germania" + province target (MI, MB, BS, BG, VR, VI, TV, PD, MI, MO, RE, PR, TO, AT, FI, BO). Estrarre anche URL annunci AutoScout/Subito del dealer (segnale import) |
| `qualifier.py` | Nuovi must-have da ICP file 02: segnale import (+35), decisore noto (+20), dimensione 2-20. Escludere: reti ufficiali (parole chiave "store ufficiale", marchi unici), gruppi >20 dipendenti, NLT |
| `copy_knowledge.py` | Glossario vertical: *mobile.de, importazione Germania, km 0 tedesca, prezzo chiavi in mano, pratica immatricolazione, margine, piazzale* — termine anti-AI-slop di settore |
| `strategist.py` | Angolo fisso del vertical = **"fine dei preventivi a mano"** (file 02, `angolo_outreach`) |
| `bibbia_team.py` / regole | Mantenere: link consentito, volume 25-30/gg, doppio controllo anti-AI-slop |
| Personalizer IG/LinkedIn | Nuovo blocco "segnale" da bio/annunci: *"ho visto la vostra [auto] in arrivo dalla Germania"* |

⚠️ **Le 458 email in coda del vecchio target**: NON mescolare. Code separate per settore (la metrica si legge pulita).

---

## 2. EMAIL — sequenza E1 → E2 (giorno 3) → E3 (giorno 7)

> Framework: Pain Hook → Analisi → Solution → Social Proof → Action. Max 120 parole. Un link solo (video demo o preventivo-demo). Prima riga SEMPRE personalizzata col segnale vero del dealer.

### E1 — Prima email (giorno 0)
**Oggetto:** `i preventivi delle auto dalla Germania, [Nome Salone]` *(alt: `2 minuti invece di 40, [Nome]` / `la [BMW X] che avete su AutoScout`)*

> Buongiorno [Nome],
>
> ho visto che [SEGNALE VERO: "importate regolarmente dalla Germania — ho incrociato il vostro annuncio della BMW 320 su AutoScout"]. Quindi questa la capisce al volo.
>
> Ogni preventivo su un'auto da importare oggi costa a un vostro venditore 30-60 minuti: tradurre l'annuncio tedesco, copiare foto e dati, rifare i conti del margine, impaginare. Nel frattempo il cliente ha chiesto ad altri tre.
>
> **PreventivoForge** chiude quel buco: incollate il link mobile.de e in 2 minuti avete un PDF italiano professionale — foto, scheda tradotta, descrizione che vende — col vostro logo e il prezzo finale già calcolato col vostro margine.
>
> Lo usa già Novacar. Gli abbiamo fatto fare [DATO VERO — es. "il primo preventivo in 2 minuti invece di 40"].
>
> Se mi manda un link di un vostro annuncio, le preparo il preventivo col vostro logo e glielo mando: così giudica sui fatti, non sulle parole.
>
> Neri — Digital Empire
> [firma + link video demo 2 min]

### E2 — Follow-up giorno 3 (angolo: il conto del tempo)
**Oggetto:** `re: i preventivi delle auto dalla Germania · 40 min × 10`

> Buongiorno [Nome],
>
> un conto rapido, poi la smetto di disturbarla. Se fate 10 preventivi a settimana su auto da importare e ognuno prende 40 minuti, sono **26 ore al mese**. Un venditore intero una settimana al mese a fare il copia-incolla dal tedesco invece di stare in piazzale.
>
> PreventivoForge le ridà quelle ore: link mobile.de → PDF in 2 minuti, col vostro logo e il vostro margine. Una tantum, niente canoni.
>
> Le lascio il caso vero di Novacar in allegato [PDF case study]. Se merita 15 minuti, prenoti qui [link] — o mi risponde "chiamami" e faccio io.
>
> Neri

### E3 — Chiusura cerchio giorno 7 (angolo: settembre / rottura dignitosa)
**Oggetto:** `settembre arriva per tutti (chiudo qui)`

> Buongiorno [Nome],
>
> ultima mia, promesso. Settembre è il vostro mese forte: chi risponde per primo e col documento migliore, vende. Con PreventivoForge il preventivo perfetto esce in 2 minuti dal link mobile.de — chieda a Novacar.
>
> Se il tema la sfiora anche solo al 10%, mi dica "ne parliamo" e ci mettiamo 15 minuti. Altrimenti la cancello dalla lista e buona stagione di vendite 🏁
>
> Neri — Digital Empire

**Follow-up "ripresa" (versione per la settimana 24-30 ago):** stesso scheletro E3, hook = *"rientro dalle ferie: quanti preventivi vi aspettano?"*

---

## 3. LINKEDIN — sequenza

**Priorità assoluta: TITOLARI e responsabili vendite di autosaloni indipendenti.**

### Nota connessione (≤300 char, Barnum sul verticale)
> Buongiorno [Nome], seguo i dealer che importano dalla Germania — ho visto [segnale: il profilo/il salone/l'annuncio]. Costruiamo strumenti solo per quel mestiere lì. Mi farebbe piacere collegarmi, niente vendita lampo promesso 🙂

### DM post-accettazione (giorno dopo)
> Grazie del collegamento [Nome]! Una domanda da curiosi: i preventivi delle auto che prendete su mobile.de — quanto tempo vi tengono in ufficio oggi? Lo chiedo perché abbiamo costruito una cosa che li fa in 2 minuti (PDF in italiano, vostro logo, prezzo finale automatico). Se le mando un esempio fatto con un vostro annuncio, mi regala un parere da addetto ai lavori?

### Follow-up F1 (giorno 4)
> [Nome], le lascio il caso di Novacar in 6 righe: [DATO VERO]. Se il tema preventivi-import le fischia anche solo un po', 15 minuti e glielo faccio vedere sul VOSTRO annuncio. Link o gli mando il video da 2 min qui in chat, come preferisce.

### Follow-up F2 (giorno 8, chiusura)
> Chiudo il cerchio, [Nome]. Se i preventivi da importazione oggi vanno bene così, nessun problema — resto collegato e mi vedrà pubblicare casi veri. Se invece vuole partire a settembre già attrezzato, mi scriva "15 min" e ci organizziamo. In bocca al lupo per la stagione 🏁

**Comment warming (componente esistente `comment_posts.py`):** 20-30 commenti/settimana su post di dealer, associazioni auto, temi importazione/incentivi → visibilità organica nel graph giusto.

---

## 4. INSTAGRAM — DM autosaloni

Gli autosaloni indipendenti sono su IG (postano le auto). Angle: hanno già il riflesso "foto bella = vendo".

**DM1** (dopo qualifica: post/annunci di importazione presenti):
> Ciao [Nome/team salone]! Vi seguo da un po', bel parco auto 👏 Domanda veloce: le auto che vi arrivano dalla Germania — i preventivi ai clienti li fate ancora a mano? Noi abbiamo una cosa che dal link mobile.de fa il PDF in italiano in 2 minuti, col vostro logo. Se mi girate un annuncio vostro vi mando l'esempio fatto, giudicate voi 😎

**DM2 (follow-up, giorno 3-4):**
> Riecco! Vi giro il video da 90 secondi così vedete il risultato [link]. Se vi incuriosisce, 15 min in videochiamata e lo proviamo su una VOSTRA auto. Se no, tranquilli, continuo a seguirvi che le auto sono belle 😄

**Hashtag da presidiare (componente `hashtag_scout.py`):** #autosalone #usatogarantito #importazioneeauto #concessionaria #autousate + geotag province target.

---

## 5. LA MOSSA FINALE: il preventivo-demo personalizzato

Per i **top-10 lead della settimana** (score ICP più alto) — prima dell'invio/chiamata:
1. Prendi un loro annuncio reale (AutoScout/Subito/sito) di auto importata.
2. Fallo girare in PreventivoForge con brand generico… oppure, meglio, ricostruisci logo/colori a mano sul PDF per l'effetto wow.
3. Mandalo (mail/WhatsApp business) con: *"Questo l'abbiamo fatto noi in 2 minuti partendo dal vostro annuncio. Immaginate farlo voi, ogni volta, col vostro margine già dentro."*

⚠️ Correttezza: il logo si usa SOLO per quella demo al singolo dealer, mai pubblicato. Costo: ~5 min a lead. Conversione attesa: altissima. Fallo solo per lead che valgono.

---

## 6. Tracciamento + loop obiezioni

- Tracker unico (stesso del file 01 §3): ogni email/DM/chiamata → riga. Esiti standard: `inviato · aperto · risposto +/− · demo · perso · vinto`.
- Ogni risposta di tipo OBIEZIONE/DOMANDA (il `conversation_manager.py` già classifica) → girare a Max entro 24h → Neri aggiorna il suo §5 con la risposta provata.
- Report venerdì: per canale → inviati/risposte/demo. Si taglia il canale peggiore dopo 3 settimane sotto soglia.

## 7. Compliance (breve, non negoziabile)

- Solo recapiti **business pubblici** (salone, PEC pubblica, profilo aziendale). Mai cellulari/mail private.
- Base giuridica: **legittimo interesse B2B** (offerta pertinente al ruolo). Sempre opt-out chiaro: "se non interessa, la cancello" — e se dicono stop, STOP davvero e si segna.
- Nessuna lista comprata. Nessun dato nel gist/licenze oltre l'id dealer.
- Per casi particolari (PEC massive, registro opposizioni) la parola finale è del consulente: questo file non è consulenza legale.
