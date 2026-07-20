from __future__ import annotations

import importlib.util

from .config import OS_ROOT, Settings
from .meta import MetaClient
from .state import StateStore


def run_doctor(settings: Settings, *, online: bool = False, client: MetaClient | None = None) -> dict:
    settings.ensure_local_dirs()
    store = StateStore(settings.state_db)
    checks: list[dict] = []

    def signal(name: str, status: str, detail: str) -> None:
        checks.append({"name": name, "status": status, "detail": detail})

    def check(name: str, ok: bool, detail: str) -> None:
        signal(name, "PASS" if ok else "FAIL", detail)

    signal("python_runtime", "PASS", "stdlib disponibile")
    check("config_brand", (OS_ROOT / "config" / "brand-kit.json").is_file(), "brand-kit.json")
    check("config_policy", (OS_ROOT / "config" / "operating-policy.json").is_file(), "operating-policy.json")
    check("state_db", settings.state_db.parent.is_dir(), str(settings.state_db))
    signal("pillow", "PASS" if importlib.util.find_spec("PIL") is not None else "WARN",
           "necessario solo per conversione PNG→JPEG")
    signal("public_media", "PASS" if settings.public_media_dir and settings.public_media_base_url else "WARN",
           "necessario per pubblicare asset locali; non blocca dry-run")
    mode = store.get_control("autonomy_mode", "SHADOW")
    if settings.live_publish_enabled and mode not in {"SUPERVISED", "CERTIFIED_AUTO"}:
        signal("live_interlock", "WARN", f"flag live aperto mentre mode={mode}")
    else:
        signal("live_interlock", "PASS", "chiuso" if not settings.live_publish_enabled else "aperto in modalità consentita")
    signal("autonomy_mode", "PASS", mode)
    check("kill_switch", store.get_control("kill_switch") == "ACTIVE", store.get_control("kill_switch"))

    online_payload = None
    if online:
        api = client or MetaClient(settings)
        try:
            online_payload = api.account_health()
            expected = str(online_payload.get("username", "")).casefold() == "mentalita.brutale"
            check("meta_account", expected, f"@{online_payload.get('username', '?')} / {online_payload.get('account_type', '?')}")
            if settings.ig_user_id:
                api.publishing_limit(settings.ig_user_id)
                check("publishing_limit_endpoint", True, "endpoint raggiungibile")
            else:
                check("publishing_limit_endpoint", False, "MB_IG_USER_ID mancante")
        except Exception as exc:
            check("meta_online", False, f"{type(exc).__name__}: {str(exc)[:240]}")

    blocking_names = {"config_brand", "config_policy", "state_db", "kill_switch"}
    if online:
        blocking_names.update({"meta_account", "publishing_limit_endpoint", "meta_online"})
    blocking_failures = [item for item in checks if item["name"] in blocking_names and item["status"] == "FAIL"]
    return {
        "status": "PASS" if not blocking_failures else "FAIL",
        "online": online,
        "checks": checks,
        "account": online_payload,
        "note": "WARN indica prerequisiti live assenti; il dry-run resta operativo.",
    }
