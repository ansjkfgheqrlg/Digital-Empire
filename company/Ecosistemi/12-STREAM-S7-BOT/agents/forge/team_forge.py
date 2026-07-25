"""
╔══════════════════════════════════════════════════════════════╗
║         🔨 TEAM FORGE — Ingestione & Costruzione Conoscenza  ║
║                                                              ║
║  Acquisisce dati grezzi: on-chain, social, news, websocket.  ║
║  Costruisce Master Knowledge Documents strutturati.          ║
║  Alimenta la memoria strategica del sistema.                 ║
╚══════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import hashlib
import json
import time
import uuid
from typing import Dict, Any, List, Optional

from event_bus import global_bus
from memory_interface import global_memory


class ForgeTeam:
    """
    🔨 Team Forge — Costruisce la conoscenza operativa del sistema.

    Agenti nel team:
    - IngestionAgent: ingerisce dati da fonti esterne (WebSocket, API, file)
    - MKDBuilder: costruisce Master Knowledge Documents dai dati grezzi
    - KnowledgeIndexer: indicizza e deduplicazione nella memoria

    Principio: Garbage in, garbage out.
               Ogni dato entra con una fonte, un timestamp e un confidence score.
    """

    SUPPORTED_SOURCES = ["solana_wss", "twitter", "telegram", "api_rest", "file", "manual"]

    def __init__(self, team_id: str = "FORGE-TEAM-1"):
        self.team_id = team_id
        self.ingestion_count: int = 0
        self.mkd_count: int = 0
        self._ingestion_buffer: List[Dict[str, Any]] = []
        self._known_hashes: set = set()  # deduplicazione

        global_bus.subscribe(
            "task.created",
            self._on_task_assigned,
            subscriber_id=f"{team_id}.task_in",
        )

        print(f"[{self.team_id}] Team Forge pronto. "
              f"Sorgenti supportate: {', '.join(self.SUPPORTED_SOURCES)}")

    # ------------------------------------------------------------------ #
    # Ingestion Agent — acquisisce dati grezzi
    # ------------------------------------------------------------------ #

    def ingest(
        self,
        raw_data: Any,
        source: str,
        source_type: str = "api_rest",
        confidence: float = 1.0,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Ingerisce un dato grezzo nel sistema.

        Passaggi:
        1. Normalizza il dato in un record standard
        2. Calcola hash per deduplicazione
        3. Assegna confidence score
        4. Scrive in memoria (layer knowledge)
        5. Pubblica su Event Bus per chi è in ascolto

        Ritorna il record normalizzato con il suo ID.
        """
        if source_type not in self.SUPPORTED_SOURCES:
            source_type = "manual"

        # Normalizzazione
        content_str = json.dumps(raw_data, sort_keys=True, default=str)
        content_hash = hashlib.sha256(content_str.encode()).hexdigest()[:16]

        # Deduplicazione
        if content_hash in self._known_hashes:
            return {"status": "DUPLICATE", "hash": content_hash, "ingested": False}

        self._known_hashes.add(content_hash)

        record = {
            "record_id": f"ING-{uuid.uuid4().hex[:8].upper()}",
            "hash": content_hash,
            "source": source,
            "source_type": source_type,
            "raw": raw_data,
            "confidence": round(max(0.0, min(1.0, confidence)), 3),
            "ingested_at": time.time(),
            "metadata": metadata or {},
            "status": "INGESTED",
        }

        self._ingestion_buffer.append(record)
        self.ingestion_count += 1

        # Scrive in memoria con importanza proporzionale alla confidence
        importance = 0.5 + (confidence * 0.4)  # range: 0.5 - 0.9
        global_memory.write("knowledge", record, self.team_id, importance=importance)

        global_bus.publish("data.ingested", {
            "record_id": record["record_id"],
            "source": source,
            "source_type": source_type,
            "confidence": confidence,
        })

        print(f"[{self.team_id}] 📥 Ingerito {record['record_id']} da {source} "
              f"(confidence: {confidence:.0%})")

        return record

    # ------------------------------------------------------------------ #
    # MKD Builder — costruisce documenti strutturati
    # ------------------------------------------------------------------ #

    def build_mkd(
        self,
        topic: str,
        records: List[Dict[str, Any]],
        purpose: str = "STRATEGY",
    ) -> Dict[str, Any]:
        """
        Master Knowledge Document: il documento definitivo su un argomento.

        Struttura un MKD da una lista di record ingeriti.
        Un MKD è la fonte di verità che gli altri agenti consumano.

        Non riassume: ESPANDE e struttura.
        """
        if not records:
            return {"status": "ERROR", "reason": "Nessun record fornito"}

        # Filtra per confidence minima (dati di bassa qualità non entrano nel MKD)
        quality_records = [r for r in records if r.get("confidence", 0) >= 0.5]

        if not quality_records:
            return {
                "status": "REJECTED",
                "reason": "Tutti i record sotto confidence threshold 0.5",
            }

        avg_confidence = sum(r.get("confidence", 0) for r in quality_records) / len(quality_records)
        sources = list({r.get("source", "unknown") for r in quality_records})

        mkd = {
            "mkd_id": f"MKD-{uuid.uuid4().hex[:8].upper()}",
            "topic": topic,
            "purpose": purpose,
            "built_at": time.time(),
            "source_records": len(quality_records),
            "sources": sources,
            "avg_confidence": round(avg_confidence, 3),
            "sections": self._extract_sections(topic, quality_records),
            "status": "READY",
        }

        self.mkd_count += 1

        # Un MKD è un asset strategico di alta importanza
        global_memory.write("strategies", mkd, self.team_id, importance=0.85)

        global_bus.publish("mkd.ready", {
            "mkd_id": mkd["mkd_id"],
            "topic": topic,
            "purpose": purpose,
            "confidence": avg_confidence,
        })

        print(f"[{self.team_id}] 📄 MKD {mkd['mkd_id']} costruito su '{topic}' "
              f"({len(quality_records)} record, confidence media {avg_confidence:.0%})")

        return mkd

    def _extract_sections(
        self, topic: str, records: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Organizza i record in sezioni tematiche del MKD."""
        by_source_type: Dict[str, List] = {}
        for r in records:
            st = r.get("source_type", "unknown")
            by_source_type.setdefault(st, []).append(r.get("raw"))

        return {
            "overview": f"Knowledge document su: {topic}",
            "total_signals": len(records),
            "by_source": by_source_type,
            "confidence_distribution": {
                "high": sum(1 for r in records if r.get("confidence", 0) >= 0.8),
                "medium": sum(1 for r in records if 0.5 <= r.get("confidence", 0) < 0.8),
                "low": sum(1 for r in records if r.get("confidence", 0) < 0.5),
            },
        }

    # ------------------------------------------------------------------ #
    # Flush del buffer (pulizia periodica)
    # ------------------------------------------------------------------ #

    def flush_buffer(self, max_age_seconds: float = 300.0) -> int:
        """Rimuove record vecchi dal buffer in-memory. Non tocca la memoria persistente."""
        now = time.time()
        before = len(self._ingestion_buffer)
        self._ingestion_buffer = [
            r for r in self._ingestion_buffer
            if now - r.get("ingested_at", 0) < max_age_seconds
        ]
        removed = before - len(self._ingestion_buffer)
        if removed:
            print(f"[{self.team_id}] 🧹 Buffer: rimossi {removed} record scaduti.")
        return removed

    # ------------------------------------------------------------------ #
    # Reazione agli eventi del bus
    # ------------------------------------------------------------------ #

    def _on_task_assigned(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        if payload.get("assigned_team") != "forge":
            return

        task_id = payload.get("task_id")
        description = payload.get("description", "")
        print(f"[{self.team_id}] 🔨 Ricevuto task {task_id}: {description[:60]}...")

        global_bus.publish("task.completed", {
            "task_id": task_id,
            "agent_id": self.team_id,
            "output": f"Forge: ingestione e strutturazione dati per: {description}",
            "assigned_team": "forge",
        })

    # ------------------------------------------------------------------ #
    # Stato
    # ------------------------------------------------------------------ #

    def status(self) -> Dict[str, Any]:
        return {
            "team": self.team_id,
            "ingestion_count": self.ingestion_count,
            "mkd_count": self.mkd_count,
            "buffer_size": len(self._ingestion_buffer),
            "unique_hashes": len(self._known_hashes),
        }


# Istanza globale
forge_team = ForgeTeam()
