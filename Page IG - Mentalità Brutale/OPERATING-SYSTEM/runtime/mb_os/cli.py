from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .analytics import AnalyticsService
from .auth import authorization_url, exchange_code, refresh_token, update_dotenv
from .config import Settings
from .doctor import run_doctor
from .gates import gate_report
from .meta import MetaClient
from .models import ContentManifest
from .orchestrator import LIVE_CONFIRMATION, Operator
from .state import StateStore

MODES = ("SHADOW", "SUPERVISED", "CERTIFIED_AUTO", "PAUSED")


def dump(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, default=str))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Mentalità Brutale Social Operating System")
    sub = root.add_subparsers(dest="command", required=True)

    sub.add_parser("init")
    doctor = sub.add_parser("doctor")
    doctor.add_argument("--online", action="store_true")

    sub.add_parser("auth-url")
    exchange = sub.add_parser("exchange-code")
    exchange.add_argument("--code", required=True)
    exchange.add_argument("--write-dotenv", action="store_true")
    refresh = sub.add_parser("refresh-token")
    refresh.add_argument("--write-dotenv", action="store_true")

    for name in ("validate", "plan", "enqueue"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--manifest", required=True)
    run = sub.add_parser("run")
    run.add_argument("--manifest", required=True)
    run.add_argument("--live", action="store_true")
    run.add_argument("--confirm-publish")
    due = sub.add_parser("run-due")
    due.add_argument("--live", action="store_true")
    due.add_argument("--limit", type=int, default=20)

    mode = sub.add_parser("set-mode")
    mode.add_argument("--mode", choices=MODES, required=True)
    pause = sub.add_parser("pause")
    pause.add_argument("--reason", required=True)
    sub.add_parser("resume")
    sub.add_parser("status")
    certify = sub.add_parser("certify")
    certify.add_argument("--evidence", required=True)

    collect = sub.add_parser("collect")
    collect.add_argument("--content-id", required=True)
    collect.add_argument("--media-id", required=True)
    collect.add_argument("--media-type", choices=("REEL", "FEED", "CAROUSEL"), required=True)
    report = sub.add_parser("report")
    report.add_argument("--days", type=int, default=28)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    settings = Settings.from_env()
    store = StateStore(settings.state_db)
    operator = Operator(settings, store=store)

    try:
        if args.command == "init":
            dump({"status": "INITIALIZED", "state_db": str(settings.state_db), "mode": store.get_control("autonomy_mode")})
        elif args.command == "doctor":
            dump(run_doctor(settings, online=args.online))
        elif args.command == "auth-url":
            url, state = authorization_url(settings)
            dump({"authorization_url": url, "csrf_state": state, "instruction": "Verificare che state ritorni identico nel callback."})
        elif args.command == "exchange-code":
            result = exchange_code(settings, args.code)
            if args.write_dotenv:
                update_dotenv(str(result["access_token"]), str(result.get("user_id", "")) or None)
            dump({"status": "TOKEN_RECEIVED", "expires_in": result.get("expires_in"), "user_id": result.get("user_id"),
                  "stored": bool(args.write_dotenv), "token": "[REDACTED]"})
        elif args.command == "refresh-token":
            result = refresh_token(settings)
            if args.write_dotenv:
                update_dotenv(str(result["access_token"]))
            dump({"status": "TOKEN_REFRESHED", "expires_in": result.get("expires_in"), "stored": bool(args.write_dotenv), "token": "[REDACTED]"})
        elif args.command in {"validate", "plan", "enqueue", "run"}:
            manifest = ContentManifest.load(args.manifest)
            if args.command == "validate":
                dump(gate_report(manifest))
            elif args.command == "plan":
                dump(operator.plan(manifest))
            elif args.command == "enqueue":
                dump({"status": "ENQUEUED" if store.enqueue(manifest) else "DUPLICATE_SKIPPED", "content_hash": manifest.content_hash})
            else:
                dump(operator.run(manifest, live=args.live, confirmation=args.confirm_publish))
        elif args.command == "run-due":
            dump(operator.run_due(live=args.live, limit=args.limit))
        elif args.command == "set-mode":
            if args.mode == "CERTIFIED_AUTO":
                raise ValueError("Usare certify con evidence; set-mode non può bypassare il gate")
            store.set_control("autonomy_mode", args.mode)
            dump({"status": "OK", "mode": args.mode})
        elif args.command == "pause":
            store.set_control("kill_switch", "PAUSED")
            store.event("PAUSED", {"reason": args.reason})
            dump({"status": "PAUSED", "reason": args.reason})
        elif args.command == "resume":
            store.set_control("kill_switch", "ACTIVE")
            dump({"status": "ACTIVE", "mode": store.get_control("autonomy_mode")})
        elif args.command == "status":
            dump({"mode": store.get_control("autonomy_mode"), "kill_switch": store.get_control("kill_switch"),
                  "live_env": settings.live_publish_enabled, "state_db": str(settings.state_db)})
        elif args.command == "certify":
            evidence = json.loads(Path(args.evidence).read_text(encoding="utf-8"))
            operator.certify(evidence)
            dump({"status": "CERTIFIED_AUTO", "approved_by": evidence.get("approved_by")})
        elif args.command == "collect":
            service = AnalyticsService(MetaClient(settings), store)
            dump(service.collect(args.content_id, args.media_id, args.media_type))
        elif args.command == "report":
            dump(AnalyticsService(MetaClient(settings), store).report(args.days))
        return 0
    except Exception as exc:
        dump({"status": "ERROR", "error_type": type(exc).__name__, "message": str(exc)})
        return 1


if __name__ == "__main__":
    sys.exit(main())