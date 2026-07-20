#!/usr/bin/env python3
"""
SKILL 5 — YouTube Script Factory PRO
Backlog Manager — Gestione contenuti, priorità, performance, piano settimanale.
"""

import json
from datetime import datetime, timedelta
from typing import Optional
from collections import Counter


# ═══════════════════════════════════════════════════
# COSTANTI E CONFIGURAZIONE
# ═══════════════════════════════════════════════════

TIPI_VIDEO = {
    "anchor": {"nome": "Anchor (Tutorial)", "target_mix": 70, "emoji": "📚"},
    "shift": {"nome": "Shift (Reframe)", "target_mix": 20, "emoji": "🔄"},
    "conversion": {"nome": "Conversion (Case Study)", "target_mix": 10, "emoji": "📊"}
}

PILASTRI = {
    1: {"nome": "Fondamenti CRO", "target_mix": 20, "emoji": "🎯"},
    2: {"nome": "Landing Page & Copy", "target_mix": 30, "emoji": "✍️"},
    3: {"nome": "Funnel & Metriche", "target_mix": 20, "emoji": "📈"},
    4: {"nome": "Testing & Ottimizzazione", "target_mix": 15, "emoji": "🧪"},
    5: {"nome": "Casi Studio & BTS", "target_mix": 15, "emoji": "🎬"}
}

STATI = ["idea", "backlog", "scriptato", "registrato", "pubblicato", "analizzato"]

PRIORITA = {
    "alta": {"emoji": "🔴", "valore": 3},
    "media": {"emoji": "🟡", "valore": 2},
    "bassa": {"emoji": "🟢", "valore": 1}
}

# Benchmark performance
BENCHMARK_CTR = {"eccellente": 8.0, "buono": 5.0, "medio": 3.0}
BENCHMARK_RETENTION = {"eccellente": 50.0, "buono": 40.0, "medio": 30.0}


# ═══════════════════════════════════════════════════
# CLASSE PRINCIPALE
# ═══════════════════════════════════════════════════

class BacklogManager:
    """Gestisce il backlog contenuti YouTube Script Factory."""

    def __init__(self, file_path: str = "backlog_youtube.json"):
        self.file_path = file_path
        self.videos = []
        self._load()

    def _load(self):
        """Carica il backlog da file JSON."""
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.videos = data.get("videos", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.videos = []

    def save(self):
        """Salva il backlog su file JSON."""
        data = {
            "versione": "1.0",
            "ultimo_aggiornamento": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "totale_video": len(self.videos),
            "videos": self.videos
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # ─────────────────────────────────────────────
    # CRUD OPERATIONS
    # ─────────────────────────────────────────────

    def aggiungi_video(
        self,
        titolo: str,
        tipo: str,
        pilastro: int,
        topic: str,
        keyword: str = "",
        credenza: str = "",
        caso_studio: str = "",
        priorita: str = "media",
        note: str = "",
        cta: str = "lead_magnet",
        lead_magnet: str = "",
        takeaway: str = "",
        durata_target: int = 10
    ) -> dict:
        """Aggiunge un video al backlog."""

        video_id = f"V{len(self.videos) + 1:04d}"

        video = {
            "id": video_id,
            "titolo": titolo,
            "tipo": tipo.lower(),
            "pilastro": pilastro,
            "topic": topic,
            "keyword": keyword,
            "credenza": credenza,
            "caso_studio": caso_studio,
            "priorita": priorita.lower(),
            "stato": "idea",
            "note": note,
            "cta": cta,
            "lead_magnet": lead_magnet,
            "takeaway": takeaway,
            "durata_target": durata_target,
            "creato_il": datetime.now().strftime("%d/%m/%Y"),
            "aggiornato_il": datetime.now().strftime("%d/%m/%Y"),
            "pubblicato_il": None,
            "performance": None,
            "quality_score": None
        }

        self.videos.append(video)
        self.save()
        return video

    def aggiorna_stato(self, video_id: str, nuovo_stato: str) -> Optional[dict]:
        """Aggiorna lo stato di un video."""
        video = self._find(video_id)
        if video and nuovo_stato in STATI:
            video["stato"] = nuovo_stato
            video["aggiornato_il"] = datetime.now().strftime("%d/%m/%Y")
            if nuovo_stato == "pubblicato":
                video["pubblicato_il"] = datetime.now().strftime("%d/%m/%Y")
            self.save()
        return video

    def aggiorna_performance(
        self,
        video_id: str,
        views: int = 0,
        ctr: float = 0.0,
        avg_retention: float = 0.0,
        avg_view_duration_sec: int = 0,
        likes: int = 0,
        comments: int = 0,
        shares: int = 0,
        subscribers_gained: int = 0,
        click_link_desc: int = 0,
        leads_generati: int = 0
    ) -> Optional[dict]:
        """Aggiorna le metriche di performance di un video pubblicato."""
        video = self._find(video_id)
        if not video:
            return None

        video["performance"] = {
            "views": views,
            "ctr": ctr,
            "avg_retention_pct": avg_retention,
            "avg_view_duration_sec": avg_view_duration_sec,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "subscribers_gained": subscribers_gained,
            "click_link_desc": click_link_desc,
            "leads_generati": leads_generati,
            "engagement_rate": round(((likes + comments + shares) / max(views, 1)) * 100, 2),
            "lead_rate": round((leads_generati / max(views, 1)) * 100, 3),
            "aggiornato_il": datetime.now().strftime("%d/%m/%Y %H:%M"),
            # Valutazioni automatiche
            "ctr_rating": _valuta_metrica(ctr, BENCHMARK_CTR),
            "retention_rating": _valuta_metrica(avg_retention, BENCHMARK_RETENTION)
        }

        video["stato"] = "analizzato"
        video["aggiornato_il"] = datetime.now().strftime("%d/%m/%Y")
        self.save()
        return video

    def aggiorna_quality_score(self, video_id: str, score: int, max_score: int = 45) -> Optional[dict]:
        """Collega il quality score dalla checklist qualità."""
        video = self._find(video_id)
        if video:
            video["quality_score"] = {
                "score": score,
                "max": max_score,
                "percentuale": round((score / max_score) * 100)
            }
            self.save()
        return video

    def elimina_video(self, video_id: str) -> bool:
        """Rimuove un video dal backlog."""
        video = self._find(video_id)
        if video:
            self.videos.remove(video)
            self.save()
            return True
        return False

    def _find(self, video_id: str) -> Optional[dict]:
        """Trova un video per ID."""
        return next((v for v in self.videos if v["id"] == video_id), None)

    # ─────────────────────────────────────────────
    # VISUALIZZAZIONI E REPORT
    # ─────────────────────────────────────────────

    def lista_backlog(self, filtro_stato: str = None, filtro_tipo: str = None,
                      filtro_pilastro: int = None, filtro_priorita: str = None) -> str:
        """Lista il backlog con filtri opzionali."""

        filtered = self.videos
        if filtro_stato:
            filtered = [v for v in filtered if v["stato"] == filtro_stato]
        if filtro_tipo:
            filtered = [v for v in filtered if v["tipo"] == filtro_tipo.lower()]
        if filtro_pilastro:
            filtered = [v for v in filtered if v["pilastro"] == filtro_pilastro]
        if filtro_priorita:
            filtered = [v for v in filtered if v["priorita"] == filtro_priorita.lower()]

        # Ordina: priorità (alta prima) → tipo → pilastro
        sorted_videos = sorted(
            filtered,
            key=lambda v: (-PRIORITA.get(v["priorita"], {}).get("valore", 0),
                           v["tipo"], v["pilastro"])
        )

        lines = []
        lines.append("═" * 70)
        lines.append(f"  📋 BACKLOG YOUTUBE — {len(sorted_videos)} video")
        if any([filtro_stato, filtro_tipo, filtro_pilastro, filtro_priorita]):
            filtri = []
            if filtro_stato: filtri.append(f"stato={filtro_stato}")
            if filtro_tipo: filtri.append(f"tipo={filtro_tipo}")
            if filtro_pilastro: filtri.append(f"pilastro={filtro_pilastro}")
            if filtro_priorita: filtri.append(f"priorità={filtro_priorita}")
            lines.append(f"  Filtri: {', '.join(filtri)}")
        lines.append("═" * 70)

        if not sorted_videos:
            lines.append("  (nessun video trovato)")
            return "\n".join(lines)

        for v in sorted_videos:
            tipo_info = TIPI_VIDEO.get(v["tipo"], {})
            pil_info = PILASTRI.get(v["pilastro"], {})
            pri_info = PRIORITA.get(v["priorita"], {})

            stato_emoji = {
                "idea": "💡", "backlog": "📝", "scriptato": "📄",
                "registrato": "🎥", "pubblicato": "🚀", "analizzato": "📊"
            }.get(v["stato"], "❓")

            lines.append(f"\n  {v['id']} {pri_info.get('emoji', '')} [{v['stato'].upper()}] {stato_emoji}")
            lines.append(f"  │ {v['titolo']}")
            lines.append(f"  │ Tipo: {tipo_info.get('emoji', '')} {tipo_info.get('nome', v['tipo'])} "
                         f"| Pilastro: {pil_info.get('emoji', '')} P{v['pilastro']}")

            if v.get("keyword"):
                lines.append(f"  │ Keyword: {v['keyword']}")
            if v.get("credenza"):
                lines.append(f"  │ Credenza: {v['credenza']}")
            if v.get("quality_score"):
                qs = v["quality_score"]
                lines.append(f"  │ Quality: {qs['score']}/{qs['max']} ({qs['percentuale']}%)")
            if v.get("performance"):
                p = v["performance"]
                lines.append(f"  │ Views: {p['views']} | CTR: {p['ctr']}% ({p['ctr_rating']}) "
                             f"| Retention: {p['avg_retention_pct']}% ({p['retention_rating']})")
            if v.get("note"):
                lines.append(f"  │ Note: {v['note'][:60]}{'...' if len(v.get('note', '')) > 60 else ''}")

        lines.append(f"\n{'═' * 70}")
        return "\n".join(lines)

    def analisi_mix(self) -> str:
        """Analizza il mix attuale vs target per tipo e pilastro."""

        lines = []
        lines.append("═" * 70)
        lines.append("  📊 ANALISI MIX CONTENUTI")
        lines.append("═" * 70)

        totale = len(self.videos)
        if totale == 0:
            lines.append("  (backlog vuoto)")
            return "\n".join(lines)

        # ─── MIX PER TIPO ───
        lines.append("\n  MIX PER TIPO VIDEO:")
        lines.append("  " + "─" * 50)

        tipo_counts = Counter(v["tipo"] for v in self.videos)
        for tipo_key, tipo_info in TIPI_VIDEO.items():
            count = tipo_counts.get(tipo_key, 0)
            pct_attuale = round((count / totale) * 100)
            pct_target = tipo_info["target_mix"]
            diff = pct_attuale - pct_target
            status = "✅" if abs(diff) <= 10 else ("⬆️" if diff > 0 else "⬇️")

            bar_att = "█" * (pct_attuale // 5) + "░" * (20 - pct_attuale // 5)
            lines.append(
                f"  {tipo_info['emoji']} {tipo_info['nome']:<25} "
                f"{count:>3} ({pct_attuale:>3}%) target:{pct_target}% {status}"
            )
            lines.append(f"     [{bar_att}]")

        # ─── MIX PER PILASTRO ───
        lines.append("\n  MIX PER PILASTRO:")
        lines.append("  " + "─" * 50)

        pil_counts = Counter(v["pilastro"] for v in self.videos)
        for pil_key, pil_info in PILASTRI.items():
            count = pil_counts.get(pil_key, 0)
            pct_attuale = round((count / totale) * 100)
            pct_target = pil_info["target_mix"]
            diff = pct_attuale - pct_target
            status = "✅" if abs(diff) <= 10 else ("⬆️" if diff > 0 else "⬇️")

            lines.append(
                f"  {pil_info['emoji']} P{pil_key} {pil_info['nome']:<25} "
                f"{count:>3} ({pct_attuale:>3}%) target:{pct_target}% {status}"
            )

        # ─── STATO PIPELINE ───
        lines.append("\n  PIPELINE:")
        lines.append("  " + "─" * 50)

        stato_counts = Counter(v["stato"] for v in self.videos)
        stato_emoji = {
            "idea": "💡", "backlog": "📝", "scriptato": "📄",
            "registrato": "🎥", "pubblicato": "🚀", "analizzato": "📊"
        }
        for stato in STATI:
            count = stato_counts.get(stato, 0)
            emoji = stato_emoji.get(stato, "")
            bar = "█" * count + "░" * max(0, 10 - count)
            lines.append(f"  {emoji} {stato:<15} {count:>3} [{bar}]")

        # ─── RACCOMANDAZIONI ───
        lines.append("\n  RACCOMANDAZIONI:")
        lines.append("  " + "─" * 50)
        recs = self._genera_raccomandazioni(tipo_counts, pil_counts, totale)
        for r in recs:
            lines.append(f"  → {r}")

        lines.append(f"\n{'═' * 70}")
        return "\n".join(lines)

    def _genera_raccomandazioni(self, tipo_counts, pil_counts, totale) -> list:
        """Genera raccomandazioni basate sul mix attuale."""
        recs = []

        # Check tipo video
        for tipo_key, tipo_info in TIPI_VIDEO.items():
            count = tipo_counts.get(tipo_key, 0)
            pct = round((count / max(totale, 1)) * 100)
            target = tipo_info["target_mix"]
            if pct < target - 15:
                recs.append(f"Servono più video {tipo_info['nome']} (attuale: {pct}%, target: {target}%)")

        # Check pilastri
        for pil_key, pil_info in PILASTRI.items():
            count = pil_counts.get(pil_key, 0)
            pct = round((count / max(totale, 1)) * 100)
            target = pil_info["target_mix"]
            if pct < target - 15:
                recs.append(f"Pilastro P{pil_key} ({pil_info['nome']}) sotto-rappresentato: {pct}% vs {target}%")

        # Check priorità alta non scriptati
        alta_non_scriptati = [v for v in self.videos
                              if v["priorita"] == "alta" and v["stato"] in ("idea", "backlog")]
        if alta_non_scriptati:
            recs.append(f"{len(alta_non_scriptati)} video ad alta priorità ancora da scriptare!")

        if not recs:
            recs.append("Mix bilanciato! ✅ Continua così.")

        return recs

    def performance_report(self) -> str:
        """Report performance dei video pubblicati/analizzati."""

        published = [v for v in self.videos if v.get("performance")]
        if not published:
            return "  (nessun video con dati performance)"

        lines = []
        lines.append("═" * 70)
        lines.append("  📊 PERFORMANCE REPORT")
        lines.append("═" * 70)

        # Medie
        avg_ctr = sum(v["performance"]["ctr"] for v in published) / len(published)
        avg_retention = sum(v["performance"]["avg_retention_pct"] for v in published) / len(published)
        total_views = sum(v["performance"]["views"] for v in published)
        total_leads = sum(v["performance"]["leads_generati"] for v in published)
        total_subs = sum(v["performance"]["subscribers_gained"] for v in published)

        lines.append(f"\n  MEDIE (su {len(published)} video):")
        lines.append(f"  │ CTR medio: {avg_ctr:.1f}% ({_valuta_metrica(avg_ctr, BENCHMARK_CTR)})")
        lines.append(f"  │ Retention media: {avg_retention:.1f}% ({_valuta_metrica(avg_retention, BENCHMARK_RETENTION)})")
        lines.append(f"  │ Views totali: {total_views:,}")
        lines.append(f"  │ Lead totali: {total_leads}")
        lines.append(f"  │ Iscritti guadagnati: {total_subs}")

        # Top performers
        top_ctr = sorted(published, key=lambda v: v["performance"]["ctr"], reverse=True)[:3]
        lines.append(f"\n  TOP 3 PER CTR:")
        for i, v in enumerate(top_ctr, 1):
            lines.append(f"  {i}. [{v['id']}] {v['titolo'][:40]} — CTR: {v['performance']['ctr']}%")

        top_views = sorted(published, key=lambda v: v["performance"]["views"], reverse=True)[:3]
        lines.append(f"\n  TOP 3 PER VIEWS:")
        for i, v in enumerate(top_views, 1):
            lines.append(f"  {i}. [{v['id']}] {v['titolo'][:40]} — Views: {v['performance']['views']:,}")

        # Performance per tipo
        lines.append(f"\n  PERFORMANCE PER TIPO:")
        lines.append("  " + "─" * 50)
        for tipo_key in TIPI_VIDEO:
            tipo_videos = [v for v in published if v["tipo"] == tipo_key]
            if tipo_videos:
                t_ctr = sum(v["performance"]["ctr"] for v in tipo_videos) / len(tipo_videos)
                t_ret = sum(v["performance"]["avg_retention_pct"] for v in tipo_videos) / len(tipo_videos)
                t_views = sum(v["performance"]["views"] for v in tipo_videos) / len(tipo_videos)
                lines.append(
                    f"  {TIPI_VIDEO[tipo_key]['emoji']} {TIPI_VIDEO[tipo_key]['nome']:<25} "
                    f"CTR:{t_ctr:.1f}% | Ret:{t_ret:.0f}% | Avg Views:{t_views:.0f}"
                )

        # Performance per pilastro
        lines.append(f"\n  PERFORMANCE PER PILASTRO:")
        lines.append("  " + "─" * 50)
        for pil_key in PILASTRI:
            pil_videos = [v for v in published if v["pilastro"] == pil_key]
            if pil_videos:
                p_ctr = sum(v["performance"]["ctr"] for v in pil_videos) / len(pil_videos)
                p_views = sum(v["performance"]["views"] for v in pil_videos) / len(pil_videos)
                lines.append(
                    f"  {PILASTRI[pil_key]['emoji']} P{pil_key} {PILASTRI[pil_key]['nome']:<25} "
                    f"CTR:{p_ctr:.1f}% | Avg Views:{p_views:.0f}"
                )

        # Correlazione quality score ↔ performance
        with_quality = [v for v in published if v.get("quality_score")]
        if len(with_quality) >= 3:
            lines.append(f"\n  CORRELAZIONE QUALITY SCORE → PERFORMANCE:")
            lines.append("  " + "─" * 50)
            high_q = [v for v in with_quality if v["quality_score"]["percentuale"] >= 80]
            low_q = [v for v in with_quality if v["quality_score"]["percentuale"] < 80]
            if high_q and low_q:
                hq_ctr = sum(v["performance"]["ctr"] for v in high_q) / len(high_q)
                lq_ctr = sum(v["performance"]["ctr"] for v in low_q) / len(low_q)
                lines.append(f"  Quality ≥80%: CTR medio {hq_ctr:.1f}% ({len(high_q)} video)")
                lines.append(f"  Quality <80%: CTR medio {lq_ctr:.1f}% ({len(low_q)} video)")

        lines.append(f"\n{'═' * 70}")
        return "\n".join(lines)

    def piano_settimanale(self, video_per_settimana: int = 2) -> str:
        """Genera il piano settimanale basato su priorità e mix."""

        lines = []
        lines.append("═" * 70)
        lines.append(f"  📅 PIANO SETTIMANALE — {video_per_settimana} video/settimana")
        lines.append(f"  Settimana del {datetime.now().strftime('%d/%m/%Y')}")
        lines.append("═" * 70)

        # Seleziona candidati: stato = idea o backlog, ordinati per priorità
        candidati = [v for v in self.videos if v["stato"] in ("idea", "backlog")]
        candidati.sort(key=lambda v: (
            -PRIORITA.get(v["priorita"], {}).get("valore", 0),
            v.get("creato_il", "")
        ))

        if not candidati:
            lines.append("  ⚠️ Nessun video in coda! Aggiungi idee al backlog.")
            return "\n".join(lines)

        # Scegli bilanciando il mix
        selezionati = self._seleziona_bilanciato(candidati, video_per_settimana)

        for i, v in enumerate(selezionati, 1):
            tipo_info = TIPI_VIDEO.get(v["tipo"], {})
            pil_info = PILASTRI.get(v["pilastro"], {})
            pri_info = PRIORITA.get(v["priorita"], {})

            lines.append(f"\n  VIDEO {i}/{video_per_settimana}")
            lines.append(f"  {'─' * 50}")
            lines.append(f"  ID: {v['id']} {pri_info.get('emoji', '')} Priorità {v['priorita'].upper()}")
            lines.append(f"  Titolo: {v['titolo']}")
            lines.append(f"  Tipo: {tipo_info.get('emoji', '')} {tipo_info.get('nome', '')}")
            lines.append(f"  Pilastro: {pil_info.get('emoji', '')} P{v['pilastro']} {pil_info.get('nome', '')}")
            lines.append(f"  Durata target: {v.get('durata_target', 10)} min")

            # Prerequisiti
            lines.append(f"\n  PREREQUISITI:")
            if v["tipo"] == "anchor":
                lines.append(f"  □ Keyword: {v.get('keyword', '⚠️ DA DEFINIRE')}")
            elif v["tipo"] == "shift":
                lines.append(f"  □ Credenza: {v.get('credenza', '⚠️ DA DEFINIRE')}")
            elif v["tipo"] == "conversion":
                lines.append(f"  □ Caso studio: {v.get('caso_studio', '⚠️ DA DEFINIRE')}")

            lines.append(f"  □ CTA: {v.get('cta', 'lead_magnet')}")
            lines.append(f"  □ Lead magnet: {v.get('lead_magnet', '⚠️ DA DEFINIRE')}")
            lines.append(f"  □ Takeaway: {v.get('takeaway', '⚠️ DA DEFINIRE')}")

            # Timeline
            lines.append(f"\n  TIMELINE:")
            lines.append(f"  □ Giorno 1: Ricerca + 3 hook + 5 titoli")
            lines.append(f"  □ Giorno 2: Script completo + quality check")
            lines.append(f"  □ Giorno 3: Registrazione")
            lines.append(f"  □ Giorno 4: Editing + thumbnail")
            lines.append(f"  □ Giorno 5: Pubblicazione + pinned comment")

        # Prossimi in coda
        restanti = [v for v in candidati if v not in selezionati][:3]
        if restanti:
            lines.append(f"\n\n  PROSSIMI IN CODA:")
            lines.append("  " + "─" * 50)
            for v in restanti:
                pri = PRIORITA.get(v["priorita"], {}).get("emoji", "")
                lines.append(f"  {pri} [{v['id']}] {v['titolo'][:50]}")

        lines.append(f"\n{'═' * 70}")
        return "\n".join(lines)

    def _seleziona_bilanciato(self, candidati: list, n: int) -> list:
        """Seleziona video bilanciando il mix tipo/pilastro."""
        selezionati = []
        tipi_usati = []

        for v in candidati:
            if len(selezionati) >= n:
                break
            # Evita troppi dello stesso tipo nella stessa settimana
            if v["tipo"] in tipi_usati and len(selezionati) < n - 1:
                continue
            selezionati.append(v)
            tipi_usati.append(v["tipo"])

        # Se non abbiamo abbastanza, aggiungi i rimanenti per priorità
        if len(selezionati) < n:
            for v in candidati:
                if v not in selezionati and len(selezionati) < n:
                    selezionati.append(v)

        return selezionati

    def suggerisci_prossimo_video(self) -> str:
        """Suggerisce il prossimo video da produrre basandosi su gap nel mix."""

        lines = []
        lines.append("═" * 70)
        lines.append("  💡 SUGGERIMENTO PROSSIMO VIDEO")
        lines.append("═" * 70)

        totale = max(len(self.videos), 1)

        # Trova tipo più carente
        tipo_counts = Counter(v["tipo"] for v in self.videos)
        tipo_gap = {}
        for t_key, t_info in TIPI_VIDEO.items():
            attuale = round((tipo_counts.get(t_key, 0) / totale) * 100)
            tipo_gap[t_key] = t_info["target_mix"] - attuale

        tipo_suggerito = max(tipo_gap, key=tipo_gap.get)

        # Trova pilastro più carente
        pil_counts = Counter(v["pilastro"] for v in self.videos)
        pil_gap = {}
        for p_key, p_info in PILASTRI.items():
            attuale = round((pil_counts.get(p_key, 0) / totale) * 100)
            pil_gap[p_key] = p_info["target_mix"] - attuale

        pil_suggerito = max(pil_gap, key=pil_gap.get)

        lines.append(f"\n  Tipo suggerito: {TIPI_VIDEO[tipo_suggerito]['emoji']} "
                     f"{TIPI_VIDEO[tipo_suggerito]['nome']} "
                     f"(gap: {tipo_gap[tipo_suggerito]:+d}%)")
        lines.append(f"  Pilastro suggerito: {PILASTRI[pil_suggerito]['emoji']} "
                     f"P{pil_suggerito} {PILASTRI[pil_suggerito]['nome']} "
                     f"(gap: {pil_gap[pil_suggerito]:+d}%)")

        # Prerequisiti per tipo
        lines.append(f"\n  PREREQUISITI:")
        if tipo_suggerito == "anchor":
            lines.append(f"  □ Keyword target (ricerca Google, YouTube)")
        elif tipo_suggerito == "shift":
            lines.append(f"  □ Credenza sbagliata da smontare (dai commenti, call, ricerca)")
        elif tipo_suggerito == "conversion":
            lines.append(f"  □ Caso studio con numeri (progetto completato)")

        lines.append(f"  □ Lead magnet da collegare")
        lines.append(f"  □ Takeaway memorabile")

        # Video esistenti in questo gap
        gap_videos = [v for v in self.videos
                      if v["tipo"] == tipo_suggerito and v["pilastro"] == pil_suggerito
                      and v["stato"] in ("idea", "backlog")]
        if gap_videos:
            lines.append(f"\n  VIDEO GIÀ IN BACKLOG per questo gap:")
            for v in gap_videos[:3]:
                lines.append(f"  → [{v['id']}] {v['titolo']}")

        lines.append(f"\n{'═' * 70}")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════
# UTILITY
# ═══════════════════════════════════════════════════

def _valuta_metrica(valore: float, benchmark: dict) -> str:
    """Valuta una metrica contro i benchmark."""
    if valore >= benchmark["eccellente"]:
        return "🌟 Eccellente"
    elif valore >= benchmark["buono"]:
        return "✅ Buono"
    elif valore >= benchmark["medio"]:
        return "🟡 Medio"
    else:
        return "🔴 Basso"


# ═══════════════════════════════════════════════════
# ESEMPIO DI UTILIZZO COMPLETO
# ═══════════════════════════════════════════════════

if __name__ == "__main__":

    bm = BacklogManager("demo_backlog.json")

    # ─── POPOLA BACKLOG DEMO ───
    print("=" * 70)
    print("  STEP 1: POPOLO IL BACKLOG")
    print("=" * 70)

    bm.aggiungi_video(
        titolo="3 errori che uccidono le tue conversioni",
        tipo="anchor",
        pilastro=2,
        topic="errori landing page",
        keyword="errori landing page conversioni",
        priorita="alta",
        cta="doppia",
        lead_magnet="Checklist CRO Gratuita",
        takeaway="Il copy batte il design. Sempre.",
        durata_target=10
    )

    bm.aggiungi_video(
        titolo="Perché spendere di più in ads è il peggior consiglio",
        tipo="shift",
        pilastro=3,
        topic="traffico vs conversione",
        credenza="Più traffico = più vendite",
        priorita="alta",
        cta="lead_magnet",
        lead_magnet="Calcolatore ROI CRO",
        takeaway="Non serve più traffico, serve convertire meglio quello che hai.",
        durata_target=12
    )

    bm.aggiungi_video(
        titolo="Da 0.8% a 3.2% di CR in 14 giorni",
        tipo="conversion",
        pilastro=5,
        topic="caso studio e-commerce moda",
        caso_studio="E-commerce moda, €50K/mese ads, CR raddoppiato",
        priorita="media",
        cta="call",
        lead_magnet="Template Audit CRO",
        takeaway="3 modifiche chirurgiche > 1 redesign completo.",
        durata_target=12
    )

    bm.aggiungi_video(
        titolo="Come leggere un heatmap per trovare i leak",
        tipo="anchor",
        pilastro=4,
        topic="heatmap analisi",
        keyword="come leggere heatmap",
        priorita="media",
        cta="lead_magnet",
        lead_magnet="Checklist CRO Gratuita",
        takeaway="I dati ti dicono dove guardare. I heatmap ti dicono COSA guardare.",
        durata_target=8
    )

    bm.aggiungi_video(
        titolo="La tua headline non vende? Ecco il framework",
        tipo="anchor",
        pilastro=2,
        topic="come scrivere headline che convertono",
        keyword="headline landing page",
        priorita="media",
        lead_magnet="Template Headline CRO",
        takeaway="La headline non deve essere creativa. Deve essere chiara.",
        durata_target=10
    )

    bm.aggiungi_video(
        titolo="Cos'è il CRO e perché ti serve",
        tipo="anchor",
        pilastro=1,
        topic="introduzione al CRO",
        keyword="cos'è il CRO",
        priorita="bassa",
        cta="lead_magnet",
        lead_magnet="Checklist CRO Gratuita",
        takeaway="Il CRO è l'unica leva che moltiplica TUTTO il resto.",
        durata_target=8
    )

    bm.aggiungi_video(
        titolo="Il bel design non vende (te lo dimostro)",
        tipo="shift",
        pilastro=1,
        topic="design vs conversione",
        credenza="Un sito bello vende di più",
        priorita="bassa",
        cta="doppia",
        lead_magnet="Checklist CRO Gratuita",
        takeaway="La conversione non dipende da quanto è bello, ma da quanto è chiaro.",
        durata_target=10
    )

    print(f"  ✅ {len(bm.videos)} video aggiunti al backlog")

    # ─── SIMULA AVANZAMENTO ───
    bm.aggiorna_stato("V0001", "scriptato")
    bm.aggiorna_quality_score("V0001", 38, 45)
    bm.aggiorna_stato("V0001", "registrato")
    bm.aggiorna_stato("V0001", "pubblicato")
    bm.aggiorna_performance("V0001",
        views=1250, ctr=6.2, avg_retention=42.0,
        avg_view_duration_sec=252, likes=45, comments=12,
        shares=3, subscribers_gained=8, click_link_desc=35,
        leads_generati=12
    )

    bm.aggiorna_stato("V0002", "scriptato")
    bm.aggiorna_quality_score("V0002", 41, 45)
    bm.aggiorna_stato("V0002", "pubblicato")
    bm.aggiorna_performance("V0002",
        views=2100, ctr=8.5, avg_retention=48.0,
        avg_view_duration_sec=345, likes=89, comments=28,
        shares=11, subscribers_gained=22, click_link_desc=52,
        leads_generati=18
    )

    # ─── REPORT ───
    print("\n")
    print(bm.lista_backlog())
    print("\n")
    print(bm.analisi_mix())
    print("\n")
    print(bm.performance_report())
    print("\n")
    print(bm.piano_settimanale(video_per_settimana=2))
    print("\n")
    print(bm.suggerisci_prossimo_video())

    print(f"\n✅ Backlog salvato in {bm.file_path}")
