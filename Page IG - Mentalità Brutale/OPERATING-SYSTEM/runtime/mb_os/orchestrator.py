from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Settings
from .gates import gate_report
from .meta import MetaClient
from .models import ContentManifest
from .staging import AssetStager
from .state import StateStore, utc_now

LIVE_CONFIRMATION = "MENTALITA_BRUTALE_LIVE"


class LiveGuardError(RuntimeError):
    pass


def _quota_usage(payload: Any) -> int | None:
    """Find Meta's quota_usage defensively across response envelope versions."""
    if isinstance(payload, dict):
        value = payload.get("quota_usage")
        if isinstance(value, (int, float)):
            return int(value)
        for child in payload.values():
            found = _quota_usage(child)
            if found is not None:
                return found
    elif isinstance(payload, list):
        for child in payload:
            found = _quota_usage(child)
            if found is not None:
                return found
    return None


class Operator:
    def __init__(self, settings: Settings, store: StateStore | None = None,
                 meta: MetaClient | None = None, stager: AssetStager | None = None):
        self.settings = settings
        self.settings.ensure_local_dirs()
        self.store = store or StateStore(settings.state_db)
        self.meta = meta or MetaClient(settings)
        self.stager = stager or AssetStager(settings)

    def plan(self, manifest: ContentManifest) -> dict[str, Any]:
        report = gate_report(manifest, for_live=False)
        return {
            "mode": "DRY_RUN",
            "side_effects": False,
            "content_id": manifest.content_id,
            "content_hash": manifest.content_hash,
            "scheduled_at_utc": manifest.scheduled_datetime().isoformat().replace("+00:00", "Z"),
            "format": manifest.format,
            "gate_report": report,
            "staging_plan": self.stager.plan(manifest),
            "pipeline": [
                "validate", "token_health", "publishing_limit", "stage_https",
                "create_container", "wait_ready", "media_publish", "postcheck", "record",
            ],
        }

    def _assert_live_allowed(self, manifest: ContentManifest, confirmation: str | None,
                             scheduler: bool = False) -> dict:
        report = gate_report(manifest, for_live=True)
        if report["status"] != "PASS":
            raise LiveGuardError(f"Gate live FAIL ({report['failures']} failure)")
        if not self.settings.live_publish_enabled:
            raise LiveGuardError("MB_LIVE_PUBLISH_ENABLED deve valere YES")
        mode = self.store.get_control("autonomy_mode", "SHADOW")
        kill_switch = self.store.get_control("kill_switch", "ACTIVE")
        if kill_switch != "ACTIVE":
            raise LiveGuardError(f"Kill switch non ACTIVE: {kill_switch}")
        allowed_modes = {"CERTIFIED_AUTO"} if scheduler else {"SUPERVISED", "CERTIFIED_AUTO"}
        if mode not in allowed_modes:
            raise LiveGuardError(f"Modalità {mode} non consente questa pubblicazione")
        if not scheduler and confirmation != LIVE_CONFIRMATION:
            raise LiveGuardError("Conferma live esatta mancante")
        if not self.settings.ig_user_id:
            raise LiveGuardError("MB_IG_USER_ID mancante")
        if not self.settings.access_token:
            raise LiveGuardError("MB_IG_ACCESS_TOKEN mancante")
        if self.store.publications_last_24h() >= 3:
            raise LiveGuardError("Cap interno raggiunto: 3 pubblicazioni nelle ultime 24 ore")
        return report

    def run(self, manifest: ContentManifest, *, live: bool = False,
            confirmation: str | None = None, scheduler: bool = False) -> dict:
        existing = self.store.find_publication(manifest.content_hash)
        if existing:
            return {"status": "IDEMPOTENT_SKIP", "publication": existing}
        if not live:
            plan = self.plan(manifest)
            self.store.event("DRY_RUN", {"status": plan["gate_report"]["status"], "hash": manifest.content_hash}, manifest.content_id)
            return plan

        report = self._assert_live_allowed(manifest, confirmation, scheduler=scheduler)
        self.store.update_job(manifest.content_hash, "PUBLISHING", increment_attempt=True)
        try:
            health = self.meta.account_health()
            username = str(health.get("username", ""))
            if username and username.casefold() != "mentalita.brutale":
                raise LiveGuardError(f"Token associato all'account inatteso: @{username}")
            limit = self.meta.publishing_limit(self.settings.ig_user_id)
            quota_usage = _quota_usage(limit)
            if quota_usage is not None and quota_usage >= 100:
                raise LiveGuardError("Meta publishing limit raggiunto (100/24h)")
            urls = self.stager.stage_all(manifest)
            media_preflight = self.stager.preflight_all(urls)
            container_id = self._build_container(manifest, urls)
            self.meta.wait_until_ready(container_id)
            media_id = self.meta.publish_container(self.settings.ig_user_id, container_id)
            details = self.meta.media_details(media_id)
            result = {
                "status": "PUBLISHED",
                "content_id": manifest.content_id,
                "content_hash": manifest.content_hash,
                "container_id": container_id,
                "media_id": media_id,
                "permalink": details.get("permalink"),
                "published_at": details.get("timestamp", utc_now()),
                "media_details": details,
                "media_preflight": media_preflight,
                "publishing_limit_snapshot": limit,
                "gate_report": report,
            }
            self.store.record_publication(manifest, result)
            self.store.update_job(manifest.content_hash, "PUBLISHED")
            return result
        except Exception as exc:
            job = self.store.get_job(manifest.content_hash)
            attempts = int(job["attempts"]) if job else 1
            next_status = "FAILED_TERMINAL" if attempts >= 3 else "RETRY"
            self.store.update_job(manifest.content_hash, next_status, str(exc))
            self.store.event("PUBLISH_FAILED", {
                "error_type": type(exc).__name__, "message": str(exc)[:500],
                "attempts": attempts, "next_status": next_status,
            }, manifest.content_id)
            raise

    def _build_container(self, manifest: ContentManifest, urls: list[str]) -> str:
        ig_id = self.settings.ig_user_id
        if manifest.format == "IMAGE":
            return self.meta.create_image_container(
                ig_id, urls[0], caption=manifest.caption, alt_text=manifest.media[0].alt_text or ""
            )
        if manifest.format == "REEL":
            return self.meta.create_video_container(ig_id, urls[0], caption=manifest.caption, reel=True)

        children: list[str] = []
        for asset, url in zip(manifest.media, urls):
            if asset.media_type == "VIDEO" or Path(url.split("?", 1)[0]).suffix.lower() in {".mp4", ".mov"}:
                child = self.meta.create_video_container(ig_id, url, is_carousel_item=True)
            else:
                child = self.meta.create_image_container(
                    ig_id, url, alt_text=asset.alt_text or "", is_carousel_item=True
                )
            self.meta.wait_until_ready(child)
            children.append(child)
        return self.meta.create_carousel_container(ig_id, children, manifest.caption)

    def run_due(self, *, live: bool = False, limit: int = 20) -> list[dict]:
        results: list[dict] = []
        for row in self.store.due_jobs(limit=limit):
            manifest = ContentManifest.from_dict(json.loads(row["manifest_json"]))
            try:
                result = self.run(manifest, live=live, scheduler=live)
                if not live:
                    # A scheduler dry-run is observational and must not consume the job.
                    result["job_status"] = "QUEUED"
                results.append(result)
            except Exception as exc:
                results.append({"content_id": manifest.content_id, "status": "ERROR", "error": str(exc)})
        return results

    def certify(self, evidence: dict) -> None:
        required_true = (
            "token_health_pass", "sandbox_publish_pass", "postcheck_pass",
            "insights_pass", "security_scan_pass",
        )
        if int(evidence.get("dry_runs_passed", 0)) < 5:
            raise LiveGuardError("Servono almeno 5 dry-run PASS")
        missing = [key for key in required_true if evidence.get(key) is not True]
        if missing:
            raise LiveGuardError(f"Evidence certificazione mancanti: {', '.join(missing)}")
        if not evidence.get("approved_by"):
            raise LiveGuardError("approved_by mancante")
        self.store.set_control("autonomy_mode", "CERTIFIED_AUTO")
        self.store.event("CERTIFIED_AUTO", {"evidence": evidence, "ts": utc_now()})
