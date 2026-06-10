# tiktok-trend-scout - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Tutto intrattenimento | niente di pratico | soglia pertinenza | shortlist vuota | allarga o segnala assenza |
| Engagement fuorviante | viral ma irrilevante | pertinenza > viralita' | match debole | declassa i viral off-topic |
| Hashtag ambigui | tema confuso | incrocia piu' segnali | hashtag generici | usa anche descrizione |
| Contenuti rimossi | link morti | verifica disponibilita' | 404 | rimuovi dalla shortlist |
| Lista enorme | migliaia di video | cap + recency | troppi entry | prendi i top N recenti pertinenti |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
