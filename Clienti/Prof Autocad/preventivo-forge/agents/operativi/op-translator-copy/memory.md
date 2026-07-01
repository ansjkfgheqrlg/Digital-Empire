# Memory — op-translator-copy

## Conoscenza persistente
- Il glossario `glossary_de_it.py` è la memoria viva dell'agente: **ogni termine nuovo tradotto
  va salvato lì**, così il run successivo lo copre automaticamente.
- Namespace memory (se Backbone attivo): `agency/preventivo/translation` per pattern ricorrenti
  (termini frequenti per marca/segmento).

## Lezioni apprese
- 2026-07-01: gli export che perdono gli umlaut (ue/oe/ae) sono comuni → gestione ASCII aggiunta.
- 2026-07-01: i nomi colore costruttore (Kosmosschwarz, Alpinweiß) NON vanno tradotti né messi
  nelle specs (rischio falso residuo tedesco). Esclusi.
- La descrizione di vendita composta dai fatti strutturati è più sicura (Gate B) della traduzione
  della prosa tedesca libera; l'arricchimento LLM resta opzionale e a spesa autorizzata.

## Da ricordare per il cliente Prof Autocad
- Formula prezzo NON è compito di questo agente (è di op-pricer): mai anticiparla nel copy.
- Tono: concessionaria seria, permuta/finanziamento citati in chiusura standard.
