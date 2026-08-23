"""
Report di validazione unificato (Snippet 1 e 6 del piano del 2026-08-10).

Prima i validatori venivano chiamati singolarmente e i risultati finivano in un dizionario
sparso: funzionava, ma non c'era un punto unico che dicesse "questo libro e' pubblicabile
si'/no" ne' un modo pulito di distinguere fra "da correggere subito" e "da guardare".

Qui la distinzione e' esplicita:
- **bloccante** = il libro non si pubblica cosi' (pagine sotto target, copertina senza titolo)
- **errore** = difetto reale ma non impeditivo
- **avviso** = da guardare con l'occhio umano (i trattini, che in inglese sono spesso corretti)
- **non verificato** = il controllo NON E' STATO ESEGUITO, perche' manca lo strumento
  (Tesseract per l'OCR, Word per il PDF). Non e' un esito: e' l'assenza di un esito.

QUARTA CATEGORIA, aggiunta il 2026-08-23. Prima un controllo che non poteva girare
ritornava un avviso "VERIFICA A MANO" e finiva mescolato ai trattini da guardare a occhio:
un pacchetto usciva `pubblicabile: true` con avvisi in fondo, e nessuno vedeva la
differenza fra "controllato e a posto" e "non controllato affatto". Su questo progetto e'
la distinzione piu' importante che ci sia — esiste per non dichiarare numeri che nessuno
ha misurato.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ReportValidazione:
    bloccanti: list[str] = field(default_factory=list)
    errori: list[str] = field(default_factory=list)
    avvisi: list[str] = field(default_factory=list)
    non_verificati: list[str] = field(default_factory=list)
    # Il numero su cui si e' deciso, scritto accanto al verdetto (2026-08-23). Prima
    # `validazione.json` diceva "pubblicabile: true" senza dire su quante pagine: per
    # sapere il dato che aveva deciso bisognava riaprire il PDF. None = non misurato.
    pagine_reali: int | None = None

    @property
    def pubblicabile(self) -> bool:
        """True se non c'e' nulla che impedisca di caricare il libro su KDP."""
        return not self.bloccanti

    def blocca(self, messaggio: str) -> None:
        self.bloccanti.append(messaggio)

    def errore(self, messaggio: str) -> None:
        self.errori.append(messaggio)

    def avvisa(self, messaggio: str) -> None:
        self.avvisi.append(messaggio)

    def non_verificato(self, messaggio: str) -> None:
        """Il controllo non e' stato eseguito. Non conta come promosso ne' come bocciato."""
        self.non_verificati.append(messaggio)

    def aggiungi(self, etichetta: str, esiti: list[str], gravita: str = "avviso") -> None:
        """Aggiunge in blocco l'esito di un validatore, prefissandolo con la sua etichetta."""
        for e in esiti:
            messaggio = f"[{etichetta}] {e}"
            {"bloccante": self.blocca, "errore": self.errore,
             "non_verificato": self.non_verificato}.get(gravita, self.avvisa)(messaggio)

    def riepilogo(self) -> str:
        righe = ["=" * 62,
                 f"VALIDAZIONE: {'PUBBLICABILE' if self.pubblicabile else 'NON PUBBLICABILE'}",
                 "=" * 62,
                 f"Bloccanti: {len(self.bloccanti)} | Errori: {len(self.errori)} | "
                 f"Avvisi: {len(self.avvisi)} | NON verificati: {len(self.non_verificati)}"]
        if self.non_verificati:
            righe.append("\n--- CONTROLLI NON ESEGUITI (manca lo strumento) ---")
            righe += [f"  {i}. {v}" for i, v in enumerate(self.non_verificati, 1)]
        for titolo, voci in (("BLOCCANTI", self.bloccanti), ("ERRORI", self.errori)):
            if voci:
                righe.append(f"\n--- {titolo} ---")
                righe += [f"  {i}. {v}" for i, v in enumerate(voci, 1)]
        if self.avvisi:
            righe.append(f"\n--- AVVISI ({len(self.avvisi)}, primi 5) ---")
            righe += [f"  {i}. {v}" for i, v in enumerate(self.avvisi[:5], 1)]
        righe.append("=" * 62)
        return "\n".join(righe)

    def to_dict(self) -> dict:
        return {"pubblicabile": self.pubblicabile,
                "pagine_reali": self.pagine_reali,
                "bloccanti": self.bloccanti, "errori": self.errori,
                "verifiche_non_eseguite": self.non_verificati,
                "avvisi": self.avvisi}

    def salva(self, path: Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
        return path
