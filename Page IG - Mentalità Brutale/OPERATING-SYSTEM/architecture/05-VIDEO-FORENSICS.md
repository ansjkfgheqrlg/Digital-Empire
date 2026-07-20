# Video Forensics — protocollo “guardare davvero”

## Stato evidence

| Fonte | Disponibilità | Letta integralmente | Stato |
|---|---:|---:|---|
| video nel checkout Git | 0 file | n/a | ASSENTE |
| Drive `reel` indicato dal vecchio runtime | 1 `.mp4`, ~1,5 MB visibile nel listing pubblico | no | PENDING_DOWNLOAD |
| screenshot Story competitor `disciplina.elite` | 1 screenshot | sì, frame singolo | EVIDENZA PARZIALE |
| post statici MB | 5 immagini | campione letto | OSSERVATO |

**Divieto:** non chiamare “pattern video Mentalità Brutale” ciò che deriva da un frame competitor o da un'ipotesi.

## Pipeline Empire Studio obbligatoria

Per ogni Reel:

1. acquisire il file originale senza salvarlo in Git;
2. hash SHA-256 + durata/codec/dimensioni;
3. estrarre frame ogni 1s e frame su cambio scena;
4. trascrivere audio e leggere VTT integralmente;
5. leggere almeno 12 frame distribuiti, più tutti i visual passage densi;
6. segmentare hook/body/payoff/CTA con timestamp;
7. annotare testo on-screen, B-roll, camera/motion, musica/SFX, watermark;
8. produrre knowledge atoms con source locator;
9. confrontare ≥10 Reel prima di forgiare pattern;
10. versare dossier in wiki e Memory Empire; poi `/forge` verso skill/workflow.

## Schema di analisi

```json
{
  "video_id": "sha256:...",
  "duration_seconds": 0,
  "source": "owned|competitor|licensed",
  "segments": [
    {
      "start": 0.0,
      "end": 1.2,
      "role": "HOOK",
      "spoken": "...",
      "onscreen_text": "...",
      "visual": "...",
      "audio": "...",
      "frame_refs": ["frame-0001.png"],
      "confidence": "observed"
    }
  ],
  "claims": [{"claim": "...", "source_locator": "00:04.200"}],
  "rights": {"reuse": false, "transformation_only": true}
}
```

## Cosa estrarre (non copiare)

- velocità con cui appare la tesi;
- densità parole/secondo;
- posizione e contrasto del testo;
- numero e durata scene;
- rapporto visual astratto/reale;
- musica come tensione, non traccia specifica;
- tipo di payoff;
- CTA e transizione;
- comment signal e retention quando disponibili.

Il contenuto competitor alimenta **principi trasformativi**, non clonazione di script, footage, audio o identità.

## Evidenza preliminare dal frame competitor

Osservato nel singolo screenshot:

- footage scenico caldo e riconoscibile;
- testo bianco centrale, più blocchi;
- parole selettive in bold per guidare la scansione;
- watermark visibile;
- lettura possibile senza audio.

Non osservato:

- hook iniziale;
- montaggio;
- audio;
- durata completa;
- CTA;
- performance.

## Gate per creare Reel Pattern Extractor

Chief-Forge può aprire la build solo quando:

- ≥10 Reel integrali osservati;
- ≥120 frame letti complessivamente;
- transcript/VTT completo dove presente;
- ≥3 esempi per ogni pattern candidato;
- rights/anti-copy rule esplicita;
- coverage report e no-finto-pass verdi.
