# Glossario

> Termini chiave usati nella guida. Estratti dal sorgente, espansi.

## Chain-of-thought (CoT)
Tecnica di prompting in cui si chiede al modello di ragionare step by step esplicitando il ragionamento intermedio, invece di chiedere la risposta diretta. Originale: Wei et al. 2022.

## Delimiters
Marker espliciti (`"""`, ` ``` `, `<tag>...</tag>`) per separare contesto, istruzioni, esempi, input nel prompt. Riducono ambiguità e mescolamento di sezioni.

## Few-shot prompting
Dare al modello 2-5 esempi di input/output prima della richiesta vera, per fargli apprendere e replicare il pattern. Sfrutta l'in-context learning.

## Function calling
Meccanismo nativo delle API LLM moderne per ottenere output strutturato (JSON) garantito tramite schema dichiarato. Più affidabile di "respond in JSON" nel prompt.

## In-context learning (ICL)
Capacità del modello di apprendere e replicare un pattern dagli esempi forniti nel prompt, senza fine-tuning. È pattern recognition runtime, non apprendimento permanente.

## JSON mode
Modalità delle API LLM (`response_format={'type': 'json_object'}`) che forza output JSON sintatticamente valido. Da combinare con schema esplicito + esempi per accuracy semantica.

## Lost-in-the-middle
Fenomeno (Liu et al.) per cui istruzioni nel mezzo di un prompt lungo vengono "ignorate" dal modello, rispetto a quelle all'inizio o alla fine.

## Self-consistency
Estensione di CoT: generi N chain-of-thought (T>0) e prendi la risposta che compare più spesso. Majority voting su ragionamenti diversi.
