---
name: carousel-machine-premium-black-red-grain
description: Genera caroselli Instagram 1080x1350 con qualità reference esatta Digital Empire - background nero #000000 con film grain 35% + glow rosso-arancione #FF3B1F angolare, tipografia mix sans bold bianco granuloso + serif italic rosso, pill mono con icona rossa, layout 64px margini, standard premium agenzia high-end.
---

# OBIETTIVO
Produrre prompt immagine per Arena.ai che replicano AL PIXEL la qualità delle 8 slide reference fornite: nero profondo con grana film granulosa pesante (35% overlay), glow rosso-arancione #FF3B1F blur angolare, tipologia contrasto sans extrabold bianco testurizzato + serif italic rosso #FF3B1F per accent words, pill superiore con border rgba(255,255,255,0.25) e icona rossa, footer con numero pagina mono "3/8" e logo E gradient arancione, qualità premium editorial 120+ post, zero flat digitale, score coerenza ≥9.5/10 vs reference.

# TRIGGER
Questa skill si attiva quando:
- Utente fornisce 5-8 immagini reference e dice "Devono avere questa qualità, questa grana, questo stile"
- Input contiene pill label come "LA VERITÀ", "CONTENT FACTORY", "IL PROBLEMA", "LA SOLUZIONE", "COME FUNZIONA", "IL RISULTATO", "LA DOMANDA VERA", "INIZIA ORA" con icone rosse
- Planner rileva intent = carousel-machine e reference contiene nero + rosso + grain texture (non blu notte)
- Utente menziona "grana", "texture", "qualità ai roselli [caroselli]", "stile Digital Empire nero rosso"
- È richiesto carosello 8 slide formato 1080x1350 per Content Factory / Digital Empire con metrica "Da 3 ore a 4 minuti"

# REGOLE FERREE
1. MAI usare gradient blu notte #0A1931 o oro #D4AF37 per questo progetto - PALETTE OBBLIGATORIA: background #000000 puro + film grain noise 35% + glow #FF3B1F / #FF4D2E radial angolari top-right e bottom-left blur 120px 40-60% opacity - pena esclusione qualità
2. TIPOGRAFIA CONTRASTO OBBLIGATORIA: headline sans extrabold 800-900 (Satoshi / General Sans / Inter Tight) 110-140pt bianco #F5F5F0 con grain texture 3% (non flat #FFFFFF) MISTA a parole accent in serif italic elegante (Instrument Serif Italic / Playfair Display Italic) 110-140pt colore #FF3B1F rosso - MAI tutto sans o tutto serif
3. PILL SUPERIORE replicata esattamente: height 36px, border 1px rgba(255,255,255,0.25), radius 24px, padding 12px 20px, icona rossa #FF3B1F (occhio per LA VERITÀ, ingranaggi per CONTENT FACTORY, stella per LA SOLUZIONE, nodo per COME FUNZIONA, grafico per IL RISULTATO, scudo ? per LA DOMANDA VERA, fulmine per INIZIA ORA, orologio per IL PROBLEMA) + testo monospace JetBrains Mono uppercase 13-15pt tracking 0.12em colore #E5E5E5
4. LAYOUT FISSO 1080x1350 con margini 64px tutti i lati: top pill a 64px, headline inizia 180px, larghezza 952px, max 4 righe, body 22-26pt gray #9CA3AF 24px gap sotto headline, footer bottom 64px con sinistra "2/8" mono 14pt #6B7280 destra logo E quadrato 48x48 rounded 12px gradient #FF8A5B->#FFFFFF + "Digital Empire" 18pt
5. EFFETTI PREMIUM NON NEGOZIABILI: 
   - Film grain overlay 35% su TUTTA immagine 1-2px noise
   - Vignette 15% dark
   - Text headline con texture grain leggera (effetto stampa)
   - Card dark background rgba(15,15,15,0.9) border rgba(255,255,255,0.08) radius 20-24px padding 32px inner highlight top rgba(255,255,255,0.15)
   - Card light gradient #F5F5F2->#FFB088 135deg per slide soluzione
   - Niente 3D pacchiano, niente icone stock, niente vettoriale flat pulito - DEVE sembrare fotografico con grana
6. TESTO ESATTO preservato: quando utente dice Testo esatto che deve comparire, copiarlo letteralmente incluso punteggiatura e accent italic - se contiene parole da evidenziare in rosso, applicare regola accent: es. "Non hai un problema di idee." → "problema" in rosso italic serif resto bianco sans bold
7. COERENZA 8 SLIDE: stesso nero grain, stesso glow rosso posizionato coerente (se top-right glow slide 2, mantenilo simile slide 3), stesso font, stesso footer, stessa dimensione pill - critica coerenza deve essere ≥9.5 altrimenti rigenera

# WORKFLOW OPERATIVO

## STEP 1: INTAKE & ANALISI REFERENCE PIXEL-PERFECT
1.1 Input: 8 immagini reference + testi slide richiesti (es. "Non hai un problema di idee..." ecc)
1.2 Azione Analyst:
   - Estrai palette esatta con eyedropper: #000000, #FF3B1F, #F5F5F0, #9CA3AF
   - Identifica tipografia: sans extrabold + serif italic red accent ratio ~70/30
   - Mappare pill labels: LA VERITÀ (eye), CONTENT FACTORY (gears), LA SOLUZIONE (star), COME FUNZIONA (node), IL RISULTATO (chart), LA DOMANDA VERA (shield ?), INIZIA ORA (lightning), IL PROBLEMA (clock)
   - Misurare layout: margini 64px, headline 110-140pt, grain 35%
   - Salva style guide in reference/STYLE_GUIDE.md
1.3 Output: style_json = {palette, typography {sans, serif_italic, mono}, layout {margins, pill, footer}, effects {grain 35%, glow #FF3B1F 500px blur, vignette 15%}, components {pill, card_dark, card_light, button_gradient, metrics_cards}}

## STEP 2: GENERAZIONE PROMPT CHIRURGICO PER ARENA (MODELLO GPT-4o / CLAUDE 3.5 SONNET IMAGE GEN)
2.1 Per ogni slide richiesta:
   Input: slide_text + slide_number + slide_role (es. 3/8 LA VERITÀ) + style_json
   Azione Writer - Template prompt potenziato per match reference:
   
   """
   Sei Art Director premium Digital Empire. Replica ESATTAMENTE lo stile reference nero rosso grain.

   SLIDE {NUMERO}/8 - Label: "{PILL_LABEL}" Icon: {ICONA} rossa #FF3B1F

   Testo esatto da renderizzare: "{TESTO_SLIDE}" 
   - Applica regola contrasto: parole "{PAROLE_ROSSE}" devono essere in serif italic elegante colore #FF3B1F #FF3B1F (Instrument Serif Italic / Playfair Display Italic 120pt italic), resto in sans extrabold 800 Satoshi/General Sans 120pt bianco #F5F5F0 con grain texture 3%
   - Layout: 1080x1350px, background #000000 puro con HEAVY film grain noise texture overlay 35% opacity 1-2px (EFFETTO OBBLIGATORIO, non pulito), radial glow rosso-arancione #FF3B1F 500-600px blur 120px opacity 50% angolo top-right (0% top 100% right) e bottom-left, vignette dark 15% subtitle
   - Top: pill 36px height border 1px rgba(255,255,255,0.25) radius 24px padding 12px 20px, icona rossa {ICONA} 16px + testo monospace JetBrains Mono uppercase 14pt tracking 0.12em #E5E5E5 "{PILL_LABEL}"
   - Headline: margin 64px left/right, start 180px top, width 952px, line-height 0.9 tight, letter-spacing -0.03em, max 4 lines, mix sans bold + serif italic rosso
   - Body se presente: Inter regular 24pt #9CA3AF line-height 1.4, 24px gap sotto headline
   - Se tipo "COME FUNZIONA": 3 dark cards 01/02/03 - numero serif italic red 90pt left, linea verticale sottile divider, card background rgba(15,15,15,0.9) border rgba(255,255,255,0.08) radius 20px padding 32px
   - Se tipo "IL RISULTATO": 3 cards metric affiancate gap 16px ratio 1:1:1 dark cards con titolo mono 12pt #6B7280 + numero grande 68pt white/red + body 14pt gray
   - Se tipo "LA SOLUZIONE": una card light grande gradient #F5F5F2->#FFB088 peach 135deg radius 24px padding 36px con header pill black + contenuto + checkmarks
   - Se tipo "LA DOMANDA VERA": virgolette «» rosse #FF3B1F 40pt + headline + dark card grande con lista check verdi/rossi
   - Se tipo "INIZIA ORA": card offer dark con prezzo barrato #6B7280 barrato rosso + prezzo grande €3.200 white bold 64pt + pill -50% red bg + features mono + bottone gradient #FFFFFF->#FF8A5B text black bold "PRENOTA LA CALL GRATUITA →" rounded 16px padding 20px 32px glow arancione outer
   - Footer fisso: bottom 64px left page number "{NUMERO}/8" JetBrains Mono 14pt #6B7280 right logo E 48x48px square rounded 12px gradient #FF8A5B->#FFE5D9 white E bold + "Digital Empire" 18pt #E5E5E5
   - Effetti finali: heavy grain, non flat vector, premium editorial agency, photoreal noise, no 3D cheesy, no stock icons
   - Output: solo immagine PNG 1080x1350 300DPI con grain
   """

   Output: prompt_arena_pronto 600-900 parole, ultra-dettagliato con valori esadecimali esatti

2.2 Validazione: verifica che prompt contenga #000000, #FF3B1F, film grain 35%, 1080x1350, Satoshi + Instrument Serif Italic, pill border rgba(255,255,255,0.25)

## STEP 3: ESECUZIONE MASSIVA BATCH
3.1 Input: array 8 prompt_arena_pronto
3.2 Azione Orchestrator RuFLO:
   - Carica in arena_generator.py stream=S1-reference-quality
   - Modello: GPT-4o (best per text rendering con grain) o Claude 3.5 Sonnet
   - Esecuzione: genera sequenziale con 2s delay per evitare rate limit, salva in outputs/carousel/reference_quality/slide_{n}.png
   - Per ogni immagine generata, esegui check visivo: ha grain? ha glow rosso? testo leggibile? Se no -> Refiner con prompt potenziato +20% dettagli grain
3.3 Checkpoint dopo ogni slide per resume

## STEP 4: QUALITY GATE PIXEL-PERFECT VS REFERENCE
4.1 Critic valuta ogni slide generata:
   - Background nero con grain? (threshold ≥9)
   - Glow rosso-arancione angolare presente blur? 
   - Tipografia contrasto sans bold white + serif italic red? 
   - Pill mono con icona rossa border esatto?
   - Footer  x/8 + logo E?
   - Grana generale 35% o sembra flat pulito? (se flat → FAIL)
   - Coerenza con reference: side-by-side comparison score
4.2 Se score medio <9.0: Refiner aggiunge "heavy film grain noise 40% more visible, add orange-red glow stronger, add texture to white text"
4.3 Output finale: 8 PNG + prompt usati + report coerenza + style guide JSON per riutilizzo futuro batch
4.4 Salva in Memory L3 strategia "carousel-black-red-grain-premium" success_rate = score medio con tag "reference-quality"
