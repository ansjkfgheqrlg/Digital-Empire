
import React from 'react';
import { Quote, Target, Bot, Book, Activity, Zap, TrendingUp, Check } from 'lucide-react';
import { ChapterTitle, DataBlock, StrategyCard, StoryBox, InsightBox, ActionList, EmpireQuote, SilverBody } from '../components/blog/BlogParts';

export const blogPosts = [
    {
        id: 1,
        title: "la macchina da soldi: copywriting scientifico",
        excerpt: "perché le aziende bruciano budget in marketing inutile e come l'arte della persuasione scritta è l'unica competenza che ti separa dal fallimento.",
        readTime: "25 min",
        category: "strategia",
        image: "https://images.unsplash.com/photo-1610375460993-d2d7b50075b4?auto=format&fit=crop&q=80&w=1600",
        highlight: "PlatinumGold",
        themeColor: "gold",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-gold-500 pl-6 lowercase">
                    "se i copywriter non esistessero, le aziende farebbero prima a bruciare i soldi al posto di investirli in marketing."
                </p>

                <p>immagina di essere il titolare di <strong>wiko</strong>, un'azienda che crea e vende smartphone. Sul mercato la concorrenza è feroce: apple, samsung, xiaomi, huawei. hai bisogno di una strategia che ti aiuti a diventare rilevante e acquisire nuovi clienti.</p>
                <p>certamente, puoi creare prodotti più economici, migliori, più belli... ma c'è un limite. Non puoi ridurre il prezzo oltre un certo limite altrimenti andrai in perdita. Non puoi creare telefoni tecnologicamente superiori a samsung se hai un decimo del loro budget r&d.</p>
                <p>quindi... cosa fai? <strong>il prodotto non si vende da solo.</strong> Contrariamente a ciò che dicono i "guru" della silicon valley, un ottimo prodotto senza un ottimo marketing è solo un magazzino pieno di merce invenduta.</p>

                <ChapterTitle number="01">il ruolo del copywriter</ChapterTitle>
                <p>assumi una grande agenzia di marketing per delle pubblicità su facebook, instagram, pinterest. Ma la domanda è... <strong>chi scriverà i testi che verranno inseriti dentro questi contenuti?</strong></p>
                <p>non può farlo il tuo designer: lui si occupa di estetica, non di psicologia della vendita. Non puoi farlo tu: sei troppo coinvolto emotivamente nel prodotto.</p>
                <p>ti serve un <strong>copywriter</strong>. Una persona che nella vita fa solo una cosa: usa le parole per spostare soldi dalle tasche dei clienti alle tue.</p>

                <DataBlock label="roi incremento medio (copy pro)" value="+340%" delta="vs testi generici" color="gold" />

                <ChapterTitle number="02">la sacra formula: a.p.s.o.c.</ChapterTitle>
                <p>non scriviamo a caso. usiamo protocolli. il 99% del marketing di successo della storia segue questa formula, direttamente o indirettamente. memorizzala, tatuala, fanne il tuo mantra.</p>

                <StrategyCard
                    title="protocollo apsoc"
                    steps={[
                        "attenzione: se non ti guardano, non puoi vendere. Devi fermare lo scroll.",
                        "problema: definisci il dolore del cliente meglio di come saprebbe farlo lui.",
                        "soluzione: presenta il tuo prodotto non come un oggetto, ma come l'unica via d'uscita logica al problema.",
                        "obiezioni: anticipa i dubbi (costo, fiducia, tempo) e distruggili prima che nascano.",
                        "call to action (cta): dì loro esattamente cosa fare. Le persone hanno bisogno di ordini."
                    ]}
                />

                <ChapterTitle number="03">la differenza tra problema e pain point</ChapterTitle>
                <p>molti marketer falliscono qui. Confondono l'evento con il dolore. se vendi un servizio finanziario, il problema è "non ho soldi". ma il <strong>pain point</strong> è "la vergogna che provo quando la mia carta viene rifiutata al ristorante davanti alla mia fidanzata".</p>
                <p>vedi la differenza? il problema è logico. Il pain point è viscerale. Noi vendiamo risolvendo il dolore, non il problema matematico.</p>

                <StoryBox title="l'esempio del ginocchio">
                    <p>immagina di essere caduto dalle scale. <br /><br />
                        <strong>l'evento:</strong> caduta.<br />
                        <strong>il problema:</strong> ginocchio rotto, non riesci a camminare.<br />
                        <strong>il pain point:</strong> il dolore fisico atroce, certo. Ma soprattutto il fatto che <em>non potrai giocare la finale del torneo di calcetto</em> per cui ti sei allenato un anno. la frustrazione di guardare i tuoi amici giocare dalla panchina.<br /><br />
                        un cattivo copywriter ti vende "gesso per ginocchia rotte".<br />
                        Un copywriter d'élite ti vende "torna in campo prima della finale".</p>
                </StoryBox>

                <ChapterTitle number="04">headline: il tuo unico obiettivo</ChapterTitle>
                <p>un famoso dato statistico dice che l'80% delle persone si fermano ai titoli. Solo il 20% legge il resto. se il tuo titolo fa schifo, hai buttato l'80% del tuo budget media.</p>
                <p>usa la curiosità. usa la controversia. usa la paura.</p>
                <p><em>esempio banale:</em> "nuovo metodo per dimagrire". (noioso, ignorato).<br />
                    <em>esempio copywriter:</em> "mangia di più e perdi peso: la dieta che i nutrizionisti odiano". (stop allo scroll).</p>

                <ActionList items={[
                    "riscrivi la headline della tua landing page usando la formula 'come [risultato] senza [sacrificio]'.",
                    "identifica 3 pain point emotivi profondi del tuo target, non solo problemi superficiali.",
                    "controlla se il tuo copy attuale segue la struttura apsoc. Se manca uno step, riscrivilo."
                ]} />
            </>
        )
    },
    {
        id: 2,
        title: "psicologia della vendita: manipolare eticamente",
        excerpt: "le persone comprano con le emozioni e giustificano con la logica. impara a bypassare la corteccia prefrontale per parlare direttamente al cervello rettiliano.",
        readTime: "22 min",
        category: "psicologia",
        image: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&q=80&w=1600",
        highlight: "AnodizedRed",
        themeColor: "red",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-red-500 pl-6 lowercase">
                    "non stiamo vendendo prodotti. stiamo vendendo <strong className="text-red-500">dopamina</strong> confezionata."
                </p>

                <p>il tuo cliente non è un essere razionale. È una scimmia evoluta che indossa un completo. Se cerchi di vendere usando solo dati, specifiche tecniche e logica, stai parlando alla parte sbagliata del suo cervello. Stai parlando alla corteccia prefrontale, che è scettica, lenta e analitica.</p>
                <p>per vendere davvero, devi parlare al <strong>cervello rettiliano</strong>. quella parte antica che gestisce la sopravvivenza, la paura, il sesso e lo status. quella parte decide in millisecondi.</p>

                <ChapterTitle number="01">il mito della razionalità</ChapterTitle>
                <p>neuroscienze applicate: il 95% delle decisioni d'acquisto avviene nel subconscio. La logica interviene solo <strong>dopo</strong> per giustificare la scelta emotiva che è già stata fatta.</p>
                <p>nessuno compra una ferrari perché "ha un motore efficiente". La comprano per lo status, per sentirsi potenti, per attrarre partner. Poi, quando glielo chiedi, ti parleranno dei cavalli e dell'aerodinamica per non sembrare superficiali.</p>

                <InsightBox title="principio fondamentale">
                    <p>vendi l'emozione (il 'perché'), giustifica con la logica (il 'cosa'). Invertire questo ordine è fatale.</p>
                </InsightBox>

                <ChapterTitle number="02">scarsità e urgenza: la paura di perdere</ChapterTitle>
                <p>l'essere umano ha più paura di perdere 100€ che desiderio di guadagnarne 100. Si chiama <strong>loss aversion</strong>. Se il tuo prodotto è sempre disponibile per tutti, non ha valore percepito.</p>
                <p>devi creare scarsità reale. Non finta. "solo 3 posti rimasti" funziona solo se è vero. Se domani sono ancora lì, hai perso la tua credibilità.</p>

                <DataBlock label="tasso conversione con scarsità" value="+220%" delta="vs offerta aperta" color="red" />

                <ChapterTitle number="03">social proof: il gregge ha sempre ragione</ChapterTitle>
                <p>se entri in una città sconosciuta e vedi due ristoranti: uno vuoto e uno con la fila fuori, dove vai? Vai dove c'è la fila. Anche se il cibo fa schifo. Il nostro cervello è programmato per seguire la massa per sopravvivere.</p>
                <p>sul tuo sito, le testimonianze non sono un "extra". Sono la <strong>prova</strong> che non sei un predatore. usa video. usa screenshot reali. niente frasi finte tipo "ottimo servizio - mario rossi".</p>

                <ActionList items={[
                    "inserisci un elemento di scarsità (tempo o quantità) nella tua offerta principale.",
                    "sostituisci le descrizioni tecniche con descrizioni dei benefici emotivi.",
                    "raccogli 5 video-testimonianze di clienti che parlano del risultato emotivo, non del servizio."
                ]} />
            </>
        )
    },
    {
        id: 3,
        title: "direct response: la matematica del profitto",
        excerpt: "basta branding vago. il direct response marketing è l'unica disciplina che ti permette di tracciare ogni centesimo. impara a vendere in modo binario: sì o no.",
        readTime: "18 min",
        category: "tecnica",
        image: "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&q=80&w=1600",
        highlight: "DeepEmerald",
        themeColor: "blue",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-cyan-500 pl-6 lowercase">
                    "la creatività senza conversione è solo <strong className="text-cyan-500">arte costosa</strong>. noi non siamo banchieri, siamo artisti."
                </p>

                <p>coca-cola può permettersi di fare "branding". Può spendere milioni per mostrare orsi polari che bevono bibite solo per "essere top of mind". Tu no. Se non sei una multinazionale con budget infinito, ogni euro che spendi in pubblicità deve portarti indietro almeno due euro. Subito. Non tra un anno.</p>
                <p>questo è il <strong>direct response marketing</strong>. Marketing progettato per evocare una risposta immediata e tracciabile.</p>

                <ChapterTitle number="01">la regola dell'uno</ChapterTitle>
                <p>la complessità uccide la conversione. Se la tua pubblicità cerca di vendere 3 cose diverse, non ne venderà nessuna. la regola aurea del direct response è:</p>
                <p><strong>un annuncio, un obiettivo, una call to action.</strong></p>
                <p>non chiedere di "mettere like, condividere e comprare". Chiedi di comprare. punto.</p>

                <StrategyCard
                    title="il ciclo del profitto"
                    steps={[
                        "acquisizione: comprare un cliente a breakeven (o leggera perdita) sulla prima transazione.",
                        "monetizzazione: vendere un upsell immediato per andare in profitto.",
                        "ritenzione: vendere ripetutamente alla lista clienti a costo zero.",
                        "riattivazione: recuperare i clienti persi con offerte irresistibili."
                    ]}
                />

                <ChapterTitle number="02">se non puoi misurarlo, non esiste</ChapterTitle>
                <p>nel branding, il successo è vago ("ci conoscono di più"). Nel direct response, il successo è binario. cpa (costo per acquisizione) vs ltv (lifetime value).</p>
                <p>se ti costa 50€ acquisire un cliente e lui te ne porta 100€ nel tempo, hai una macchina da soldi infinita. Puoi spendere quanto vuoi. Se te ne porta 40€, stai fallendo. Non servono opinioni, serve un foglio excel.</p>

                <DataBlock label="precisione tracciamento" value="99.9%" delta="pixel based" color="blue" />

                <StoryBox title="la lezione di claude hopkins">
                    <p>claude hopkins, padre del marketing scientifico, usava i coupon nei giornali nel 1920 per tracciare quale titolo funzionesse meglio. Se il titolo a portava 500 coupon e il titolo b ne portava 200, il titolo b veniva eliminato. <br /><br />
                        Oggi facciamo lo stesso con facebook ads e google analytics. La tecnologia cambia, la matematica resta.</p>
                </StoryBox>

                <ActionList items={[
                    "installa pixel di tracciamento su ogni pagina del tuo funnel.",
                    "calcola il tuo cpa (costo per acquisizione) attuale. Se non lo sai, ferma le ads.",
                    "crea un'offerta di front-end a basso costo per acquisire clienti, poi vendi il servizio costoso."
                ]} />
            </>
        )
    },
    {
        id: 4,
        title: "storytelling: il cavallo di troia",
        excerpt: "i dati attivano la logica, le storie attivano i sogni. come strutturare narrazioni che bypassano le difese critiche e installano il desiderio d'acquisto.",
        readTime: "20 min",
        category: "copywriting",
        image: "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format\u0026fit=crop\u0026q=80\u0026w=1600",
        highlight: "PlatinumGold",
        themeColor: "gold",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-gold-500 pl-6 lowercase">
                    "i fatti raccontano, le storie vendono. nessuno ha mai marciato in guerra per un grafico a torta."
                </p>

                <p>quando presenti dei dati a un cliente, il suo cervello entra in modalità analitica. Alza le difese. Cerca l'errore. Vuole smentirti.</p>
                <p>quando racconti una storia, il cervello entra in modalità passiva. Abbassa le difese. Vuole sapere come va a finire. La storia è un <strong>cavallo di troia</strong>: usi la narrazione per trasportare il tuo messaggio di vendita oltre le mura della diffidenza.</p>

                <ChapterTitle number="01">il viaggio dell'eroe (cliente)</ChapterTitle>
                <p>l'errore numero uno delle aziende: si pongono come l'eroe della storia. "siamo leader dal 1990", "abbiamo vinto premi", "siamo fantastici".</p>
                <p>al cliente non frega niente di te. Lui vuole essere l'eroe. Tu non sei luke skywalker. Tu sei yoda. Tu sei la guida. Il tuo prodotto è la spada laser.</p>

                <InsightBox title="ruoli narrativi">
                    <p><strong>eroe:</strong> il tuo cliente (confuso, con un problema). <br />
                        <strong>villain:</strong> il problema (esterno, interno, filosofico). <br />
                        <strong>guida:</strong> il tuo brand (empatico, autoritario). <br />
                        <strong>piano:</strong> il tuo prodotto.</p>
                </InsightBox>

                <ChapterTitle number="02">conflitto = interesse</ChapterTitle>
                <p>una storia senza conflitto è noiosa. "Mario si è alzato, ha comprato il nostro software e vissero felici" non funziona.</p>
                <p>devi drammatizzare il problema. Devi mostrare cosa succede se <strong>non</strong> comprano. Il fallimento deve essere un'opzione reale e spaventosa. Solo così il successo finale ha valore.</p>

                <EmpireQuote text="se non c'è rischio di morte (fisica o sociale), non è una storia. è un verbale." author="Robert McKee" />

                <ChapterTitle number="03">la trasformazione</ChapterTitle>
                <p>non vendi il prodotto, vendi la trasformazione dell'identità del cliente. da "imprenditore stressato che non dorme" a "ceo in controllo che fa scalare l'azienda". Il prodotto è solo il ponte tra lo stato a e lo stato b.</p>

                <ActionList items={[
                    "riscrivi la tua 'chi siamo' page mettendo il cliente al centro, non l'azienda.",
                    "identifica il 'villain' nella vita del tuo cliente. Cosa gli impedisce di dormire?",
                    "mostra il 'paradiso' (dopo l'acquisto) e l' 'inferno' (senza acquisto) nei tuoi materiali."
                ]} />
            </>
        )
    },
    {
        id: 5,
        title: "l'era dell'inutilità umana: ai \u0026 automazione",
        excerpt: "perché assumere staff quando il software lavora gratis, non dorme e non sbaglia mai? benvenuti nella rivoluzione industriale digitale.",
        readTime: "15 min",
        category: "automazione",
        image: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format\u0026fit=crop\u0026q=80\u0026w=1600",
        highlight: "NeonPurple",
        themeColor: "purple",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-purple-500 pl-6 lowercase">
                    "l'essere umano è lento, emotivo, costoso e incline all'errore. l'ai è istantanea, stoica, economica e perfetta. <strong className="text-purple-500">fai la tua scelta.</strong>"
                </p>

                <p>non è cattiveria, è darwinismo aziendale. Se il tuo concorrente usa l'ai per qualificare i lead in 3 secondi a costo zero, e tu paghi una segretaria per richiamarli il giorno dopo... sei estinto. Non lo sai ancora, ma sei già morto.</p>
                <p>stiamo vivendo la più grande ridistribuzione di ricchezza della storia. Chi automatizza vince tutto. Chi resiste perde tutto.</p>

                <ChapterTitle number="01">velocità di esecuzione</ChapterTitle>
                <p>un lead che compila un form online si aspetta una risposta immediata. Dopo 5 minuti, la probabilità di contatto scende del 90%. Un umano non può competere. Un'automazione ti manda un whatsapp, una mail e un sms nell'istante in cui premono "invio".</p>

                <DataBlock label="tempo risposta medio umano" value="48 min" delta="vs 2 sec AI" color="purple" />

                <ChapterTitle number="02">eliminare l'errore umano</ChapterTitle>
                <p>quante volte un venditore si è dimenticato di richiamare? Quante volte un dato è stato trascritto male nel crm? L'automazione non dimentica. Non ha "giornate no". Non ha mal di testa. esegue il protocollo con precisione militare, ogni singola volta.</p>

                <StrategyCard
                    title="stack automazione base"
                    steps={[
                        "lead capture: i dati dal sito finiscono automaticamente nel crm.",
                        "nurturing: sequenze email automatiche educano il cliente per mesi.",
                        "booking: l'ai propone slot liberi e fissa appuntamenti sul calendario.",
                        "onboarding: appena pagano, ricevono contratti e accessi senza che tu muova un dito."
                    ]}
                />

                <ChapterTitle number="03">scalabilità infinita</ChapterTitle>
                <p>se vuoi gestire 10 volte più clienti con il metodo tradizionale, devi assumere 10 volte più staff. Costi enormi, problemi di gestione. con l'automazione, gestire 10 clienti o 10.000 clienti costa quasi uguale. Il software scala, le persone no.</p>

                <ActionList items={[
                    "mappa tutti i processi ripetitivi della tua azienda.",
                    "implementa un autoresponder immediato per ogni richiesta di contatto.",
                    "collega il tuo calendario al sito per eliminare il ping-pong di email per fissare appuntamenti."
                ]} />
            </>
        )
    },
    {
        id: 6,
        title: "il tuo sito è un cimitero?",
        excerpt: "il 99% dei siti web sono bellissimi funerali digitali. nessuno li visita, nessuno compra. ecco come trasformare una vetrina statica in una macchina da guerra.",
        readTime: "19 min",
        category: "web design",
        image: "https://images.unsplash.com/photo-1550439062-609e1531270e?auto=format\u0026fit=crop\u0026q=80\u0026w=1600",
        highlight: "MatrixGreen",
        themeColor: "emerald",
        content: (
            <>
                <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-emerald-500 pl-6 lowercase">
                    "il web design non è arte. è architettura di vendita. se è bello ma non converte, è solo <strong className="text-emerald-500">spazzatura decorativa</strong>."
                </p>

                <p>la maggior parte delle web agency ti truffa. Ti vendono siti "vetrina". Belli, pieni di animazioni, con foto stock sorridenti. Ma completamente inutili. Un sito vetrina aspetta che qualcuno entri. Un sito <strong>funnel</strong> prende il visitatore per il collo e lo trascina alla cassa.</p>
                <p>il tuo sito ha un solo compito: convertire traffico freddo in lead caldi. Tutto il resto è vanità.</p>

                <ChapterTitle number="01">la regola dei 3 secondi</ChapterTitle>
                <p>un utente decide se restare sul tuo sito in meno di 3 secondi. Se in quel tempo non capisce: 1) cosa fai, 2) perché serve a lui, 3) cosa deve fare... se ne va. </p>
                <p>elimina slider, video pesanti in autoplay, menu complessi. Headline chiara. Sottotitolo di beneficio. Bottone enorme.</p>

                <InsightBox title="morte allo slider">
                    <p>gli slider in home page sono il cancro della conversione. Nessuno guarda la seconda slide. Nascondono le informazioni vitali. Usa una <strong>hero section</strong> statica e potente.</p>
                </InsightBox>

                <ChapterTitle number="02">mobile first o morte</ChapterTitle>
                <p>il 90% del tuo traffico arriva da smartphone. Eppure i designer progettano su schermi da 27 pollici. Follia. Il tuo sito deve essere perfetto su un iphone vecchio, con connessione lenta, mentre l'utente è distratto in metro. se funziona lì, funziona ovunque.</p>

                <DataBlock label="traffico mobile globale" value="92%" delta="trend in crescita" color="green" />

                <ChapterTitle number="03">ogni pagina ha un solo scopo</ChapterTitle>
                <p>la home page serve a smistare. La landing page serve a vendere. Il blog serve a educare. Non mischiare gli obiettivi. Su una landing page di vendita, togli il menu di navigazione. Non dare vie di fuga. O comprano o chiudono.</p>

                <ActionList items={[
                    "controlla la velocità del tuo sito su google pagespeed. Se è sotto 90, stai perdendo soldi.",
                    "togli ogni link social dall'header. Perché vuoi mandarli via dal tuo sito?",
                    "metti una call to action chiara in ogni singola sezione della pagina."
                ]} />
            </>
        )
    }
];
