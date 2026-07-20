# Prompt Engineering Avanzato — Workshop Transcript

> Sorgente finto realistico usato come input comune per tutti gli esempi end-to-end
> in `assets/examples/<target>/`.
> Simula un transcript YouTube/workshop con timestamp, filler, ripetizioni.

---

00:00:00 Allora, ciao a tutti, oggi parliamo di, uh, prompt engineering avanzato. Vediamo le tecniche che funzionano davvero in produzione, non quelle, sai, da blog post da 5 minuti.

00:00:30 Partiamo dal contesto. Quando si lavora con LLM in produzione, il prompt non è una stringa che butti lì. È un'interfaccia. È, è il modo in cui dici al modello cosa fare. E come ogni interfaccia, ha le sue regole, i suoi pattern, i suoi anti-pattern.

00:01:15 La prima tecnica che voglio mostrare è il few-shot prompting. Few-shot vuol dire dare al modello 2-5 esempi di input/output prima della richiesta vera. Esempio classico: se vuoi che il modello generi commit message in formato Conventional Commits, gli mostri 3 esempi tipo "Added user login" → "feat(auth): implement user login", e poi gli dai la tua descrizione. Lui impara il pattern dagli esempi.

00:02:30 Perché funziona? Perché il modello fa in-context learning. Non sta imparando nel senso del fine-tuning, sta solo, sai, riconoscendo il pattern e replicandolo. Funziona meglio quando gli esempi sono rappresentativi e diversi tra loro, non tutti uguali.

00:03:30 Ok, secondo: chain-of-thought, CoT. Tecnica famosa dal paper di Wei et al. del 2022. L'idea è semplice: invece di chiedere la risposta diretta, chiedi al modello di ragionare step by step. "Pensa passo passo" funziona, anche se sembra magia. Migliora drammaticamente su problemi di ragionamento, matematica, logica.

00:04:45 Però attenzione, CoT non è gratis. Costa più token (il ragionamento è output) e su task semplici può addirittura peggiorare la performance. Su MMLU di pattern matching, modelli istruiti spesso fanno meglio in zero-shot diretto. Quindi: CoT sì per task multi-step, no per task triviali.

00:06:00 Terza tecnica: self-consistency. Estende CoT. Invece di una sola chain of thought, ne generi N (tipo 5-10) con temperatura > 0, poi prendi la risposta che compare più spesso. È majority voting su ragionamenti diversi. Costa N volte di più, ma migliora su task hard.

00:07:30 Quarta cosa importante: structured output. Quando vuoi che il modello restituisca JSON o XML o markdown strutturato, usa delimiters chiari, dai uno schema esplicito, mostra esempi. E se possibile usa il JSON mode dell'API o function calling. Funziona molto meglio del "respond in JSON" sperato.

00:08:45 Aggiungo: i delimiters. Non sottovalutate. Usare """ o ``` o tag XML tipo <example>...</example> per separare contesto, istruzioni, esempi, dati di input. Il modello capisce meglio dove finisce una cosa e inizia l'altra. Senza, mescola.

00:09:30 Adesso, anti-pattern. Cose che NON funzionano. Primo: "be creative" o "be helpful". Sono vuote. Il modello non sa cosa significhi creative per te. Sostituisci con esempi: "rispondi in tono come questo esempio" e mostri l'esempio.

00:10:30 Secondo anti-pattern: prompt giganti. Se il tuo prompt è 4000 parole, il modello si perde. Le istruzioni importanti vanno all'inizio e alla fine. Quelle in mezzo vengono "ignorate" (è il lost-in-the-middle problem documentato da Liu et al.).

00:11:45 Terzo: assumere context implicito. Tipo "fai come l'ultima volta". Il modello non ha memoria tra conversazioni separate (a meno che tu non gliela passi esplicitamente).

00:13:00 Ora un pattern operativo: prompt come codice. Versionali. Testali. Quando cambi un prompt in produzione, fa un A/B test, misura. Non assumere che la modifica migliori solo perché ti suona meglio. Il modello è una black box, sorprende sempre.

00:14:30 Ultimo punto, e poi chiudo. Il modello come collega cooperativo nuovo del progetto. Sa tutto in astratto, ma del tuo contesto specifico non sa nulla. Trattalo così: dagli contesto, esempi, vincoli. Se a un collega umano serviva un esempio, al modello serve un esempio. Non trattarlo come un motore di ricerca o un oracolo. Dagli abbastanza per ragionare.

00:15:30 Bene, è tutto, grazie a tutti, ci vediamo alla prossima.
