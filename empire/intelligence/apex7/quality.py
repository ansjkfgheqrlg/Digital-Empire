"""Quality Scoring — matrice multi-dimensionale (Livello 5 / Intelligence)."""

# Peso + soglia per dimensione. Somma pesi = 1.0
MATRIX = {
    "completezza":   {"weight": 0.25, "threshold": 8.0},
    "precisione":    {"weight": 0.25, "threshold": 8.0},
    "creativita":    {"weight": 0.20, "threshold": 7.0},
    "actionability": {"weight": 0.20, "threshold": 8.0},
    "coerenza":      {"weight": 0.10, "threshold": 9.0},
}


class QualityScorer:
    def score(self, scores: dict) -> float:
        total = 0.0
        for dim, meta in MATRIX.items():
            total += float(scores.get(dim, 0.0)) * meta["weight"]
        return round(total, 2)

    def passed(self, scores: dict, threshold: float = 7.5) -> bool:
        return self.score(scores) >= threshold

    def weakest(self, scores: dict) -> str:
        return min(MATRIX, key=lambda d: scores.get(d, 0.0))
