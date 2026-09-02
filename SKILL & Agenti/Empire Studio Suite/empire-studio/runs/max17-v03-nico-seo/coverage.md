# Coverage Report — E8Ax92etrMc (Nico | AI Ranking — Keyword Research System)

## Riepilogo
- **Frame totali nella run**: 400 (`frame-001.png` → `frame-400.png`, 1 ogni 2 secondi, video di 800s / 13m20)
- **Frame letti con tool Read**: **400/400 — coverage 100%**
- **Frame saltati**: 0 (nessuno)
- **Frame illeggibili/corrotti**: 0 (nessuno — tutti i 400 file si sono aperti e mostrato contenuto visivo valido)
- **Metodo di lettura**: batch sequenziali di 20 frame per messaggio, in ordine stretto 001→400, nessun salto:
  - 001–020, 021–040, 041–060, 061–080, 081–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–380, 381–400 (20 batch × 20 frame = 400)
- **Verifica secondaria**: dopo il primo passaggio completo, sono stati ri-letti singolarmente 14 frame chiave (frame-005, 020, 024, 030, 036, 090, 093, 108, 128, 133, 138, 142, 148, 152, 155, 158, 244, 247, 253, 292, 295, 342, 343, 344) per confermare testo esatto (nomi tool, URL, prompt, numeri) prima della trascrizione finale — nessun frame nuovo aggiunto, solo conferma di dati già coperti nel passaggio 001→400.

## Fonte audio ausiliaria
- Sottotitoli auto-generati `E8Ax92etrMc.en.vtt` letti integralmente (766 righe uniche dopo deduplica del formato karaoke), usati come riscontro incrociato della narrazione — non sostituiscono la lettura visiva, la integrano per la trascrizione di frasi pronunciate senza testo a schermo.

## Frame con contenuto testuale denso (verificati con attenzione extra)
- frame-024, frame-030, frame-036 (@ 0:46–1:10): prima comparsa parziale del report "Site Plan from Customer Language"
- frame-090, frame-093, frame-096, frame-100 (@ 2:58–3:18): setup Zernio + connettore MCP
- frame-108 (@ 3:34): lista skill Claude
- frame-152 (@ 5:02): prompt esatto della demo
- frame-155 (@ 5:08): header e contatori sommario del report
- frame-292, frame-295, frame-342, frame-343, frame-344 (@ 9:42–11:26): sezioni dettagliate del piano per-pagina e legenda di routing
- frame-321–340 (@ 10:40–11:18): tabella sentiment recensioni
- frame-347–360 (@ 11:32–11:58): aside "AI Search Kickstarter"
- frame-378 (@ 12:34): card statistiche "The First Live Run"
- frame-388 (@ 12:54): card di chiusura concettuale

## Frame ripetitivi/statici (talking head su schermo fermo, contenuto invariato)
Diverse sequenze mostrano lo stesso screenshot fermo per 10-20 frame consecutivi mentre il narratore parla in webcam a schermo intero o quasi (es. frame-181→frame-240, frame-296→frame-320, frame-361→frame-377). Tutti questi frame sono stati comunque letti singolarmente come da regola NO-SALTI; non hanno aggiunto testo nuovo oltre a quanto già trascritto dal frame in cui l'elemento a schermo è comparso per la prima volta.

## Dichiarazione di conformità
- Nessun frame è stato descritto senza essere stato letto (regola NO-FINTO rispettata).
- Ogni comando, prompt, nome file, URL e metrica numerica riportato in `video-analysis.md` e `atoms.json` è tracciato a un frame specifico + timestamp.
- Le inferenze (marcate `➕` in `video-analysis.md` e `"confidenza":"inferito"` in `atoms.json`) sono limitate a: (a) l'identificazione del report "Roofing, Dallas, Texas" come esempio precostituito e non output della demo live "plumbing, Austin, Texas"; (b) l'incertezza sulla relazione tra la skill `keyword-fanout-map` (visibile nella libreria personale di Nico) e il file regalato `keyword-language.zip`; (c) l'irrilevanza presunta dell'icona "vidiQ" visibile nell'interfaccia chat.
