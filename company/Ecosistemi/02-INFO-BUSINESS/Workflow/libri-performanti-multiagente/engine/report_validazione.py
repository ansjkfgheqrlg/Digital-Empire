"""
Report di validazione unificato (Snippet 1 e 6 del piano del 2026-08-10).

Prima i validatori venivano chiamati singolarmente e i risultati finivano in un dizionario
sparso: funzionava, ma non c'era un punto unico che dicesse "questo libro e' pubblicabile
si'/no" ne' un modo pulito di distinguere fra "da correggere subito" e "da guardare".

Qui la distinzione e' esplicita:
- **bloccante** = il libro non si pubblica cosi' (pagine sotto target, copertina senza titolo)
- **errore** = difetto reale ma non impeditivo
- **avviso** = da guardare con l'occhio umano (i trattini, che in inglese sono spesso corretti)
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

    def aggiungi(self, etichetta: str, esiti: list[str], gravita: str = "avviso") -> None:
        """Aggiunge in blocco l'esito di un validatore, prefissandolo con la sua etichetta."""
        for e in esiti:
            messaggio = f"[{etichetta}] {e}"
            {"bloccante": self.blocca, "errore": self.errore}.get(gravita, self.avvisa)(messaggio)

    def riepilogo(self) -> str:
        righe = ["=" * 62,
                 f"VALIDAZIONE: {'PUBBLICABILE' if self.pubblicabile else 'NON PUBBLICABILE'}",
                 "=" * 62,
                 f"Bloccanti: {len(self.bloccanti)} | Errori: {len(self.errori)} | Avvisi: {len(self.avvisi)}"]
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
                "bloccanti": self.bloccanti, "errori": self.errori, "avvisi": self.avvisi}

    def salva(self, path: Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
        return path
