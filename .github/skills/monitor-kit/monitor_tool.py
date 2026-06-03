#!/usr/bin/env python3
"""
Monitor Kit - CLI tool for monitoring application health, metrics, and alerts.
Outputs JSON to stdout. Uses mock data by default.
"""

import argparse
import json
import os
import sys
import random
import uuid
from datetime import datetime, timedelta, timezone

UTC = timezone.utc

# Load .env via dotenv (optional dependency)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed; read .env manually as fallback
    env_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
    if os.path.isfile(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip())

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
MONITORING_PLATFORM = os.getenv("MONITORING_PLATFORM", "mock")
ALERT_WEBHOOK = os.getenv("ALERT_WEBHOOK", "")

# ---------------------------------------------------------------------------
# Mock Data Store
# ---------------------------------------------------------------------------
MOCK_SERVICES = ["api-gateway", "auth-service", "payment-service", "user-service", "notification-service"]
MOCK_ENVS = ["production", "staging", "development"]

# In-memory incident store for mock mode
_INCIDENTS = []


def _mock_service_health(service: str | None, env: str) -> dict:
    """Generate mock health data."""
    services = [service] if service else MOCK_SERVICES
    results = []
    for svc in services:
        status = random.choice(["healthy", "healthy", "healthy", "degraded", "unhealthy"])
        uptime = round(random.uniform(95.0, 99.99), 2)
        response_time_ms = round(random.uniform(20, 500), 1)
        results.append({
            "service": svc,
            "status": status,
            "uptime_percent": uptime,
            "response_time_ms": response_time_ms,
            "last_check": datetime.now(UTC).isoformat() + "Z",
        })
    overall = "healthy" if all(r["status"] == "healthy" for r in results) else (
        "degraded" if any(r["status"] == "degraded" for r in results) else "unhealthy"
    )
    return {
        "platform": MONITORING_PLATFORM,
        "environment": env,
        "overall_status": overall,
        "checked_at": datetime.now(UTC).isoformat() + "Z",
        "services": results,
    }


def _mock_metrics(service: str, period: str, metric_type: str | None) -> dict:
    """Generate mock metric data."""
    period_hours = {"1h": 1, "6h": 6, "24h": 24, "7d": 168}
    hours = period_hours.get(period, 24)
    now = datetime.now(UTC)

    data_points = []
    interval_minutes = max(1, (hours * 60) // 12)
    for i in range(12):
        ts = now - timedelta(minutes=interval_minutes * (12 - i))
        point = {"timestamp": ts.isoformat() + "Z"}
        if metric_type in (None, "cpu"):
            point["cpu_percent"] = round(random.uniform(10, 85), 1)
        if metric_type in (None, "memory"):
            point["memory_percent"] = round(random.uniform(30, 90), 1)
        if metric_type in (None, "latency"):
            point["latency_ms"] = round(random.uniform(20, 300), 1)
        if metric_type in (None, "errors"):
            point["error_rate_percent"] = round(random.uniform(0, 5), 2)
        data_points.append(point)

    summary = {}
    if metric_type in (None, "cpu"):
        vals = [p["cpu_percent"] for p in data_points]
        summary["cpu_avg"] = round(sum(vals) / len(vals), 1)
        summary["cpu_max"] = max(vals)
    if metric_type in (None, "memory"):
        vals = [p["memory_percent"] for p in data_points]
        summary["memory_avg"] = round(sum(vals) / len(vals), 1)
        summary["memory_max"] = max(vals)
    if metric_type in (None, "latency"):
        vals = [p["latency_ms"] for p in data_points]
        summary["latency_avg_ms"] = round(sum(vals) / len(vals), 1)
        summary["latency_p99_ms"] = round(max(vals) * random.uniform(1.1, 1.5), 1)
    if metric_type in (None, "errors"):
        vals = [p["error_rate_percent"] for p in data_points]
        summary["error_rate_avg"] = round(sum(vals) / len(vals), 2)
        summary["error_rate_max"] = max(vals)

    return {
        "platform": MONITORING_PLATFORM,
        "service": service,
        "period": period,
        "type": metric_type or "all",
        "fetched_at": now.isoformat() + "Z",
        "summary": summary,
        "data_points": data_points,
    }


def _mock_alerts(status: str, severity: str | None) -> dict:
    """Generate mock alert data."""
    alert_templates = [
        {"name": "High CPU Usage", "service": "api-gateway", "severity": "critical"},
        {"name": "Memory Threshold Exceeded", "service": "auth-service", "severity": "warning"},
        {"name": "Elevated Error Rate", "service": "payment-service", "severity": "critical"},
        {"name": "Slow Response Time", "service": "user-service", "severity": "warning"},
        {"name": "Disk Usage Warning", "service": "notification-service", "severity": "info"},
        {"name": "SSL Certificate Expiring", "service": "api-gateway", "severity": "warning"},
        {"name": "Database Connection Pool Low", "service": "auth-service", "severity": "critical"},
        {"name": "Queue Depth High", "service": "notification-service", "severity": "info"},
    ]

    now = datetime.now(UTC)
    alerts = []
    for i, tpl in enumerate(alert_templates):
        alert_status = random.choice(["active", "active", "active", "resolved"])
        if status != "all" and alert_status != status:
            continue
        if severity and tpl["severity"] != severity:
            continue
        alerts.append({
            "id": f"ALT-{1001 + i}",
            "name": tpl["name"],
            "service": tpl["service"],
            "severity": tpl["severity"],
            "status": alert_status,
            "started_at": (now - timedelta(minutes=random.randint(5, 720))).isoformat() + "Z",
            "resolved_at": (now - timedelta(minutes=random.randint(1, 60))).isoformat() + "Z" if alert_status == "resolved" else None,
            "description": f"{tpl['name']} detected on {tpl['service']}.",
        })

    return {
        "platform": MONITORING_PLATFORM,
        "filter_status": status,
        "filter_severity": severity or "all",
        "total": len(alerts),
        "fetched_at": now.isoformat() + "Z",
        "alerts": alerts,
    }


def _mock_incident_list() -> dict:
    """Return stored incidents (seeded with a few examples)."""
    if not _INCIDENTS:
        now = datetime.now(UTC)
        _INCIDENTS.extend([
            {
                "id": "INC-001",
                "title": "Payment processing failures",
                "severity": "critical",
                "status": "investigating",
                "created_at": (now - timedelta(hours=2)).isoformat() + "Z",
                "updated_at": (now - timedelta(minutes=15)).isoformat() + "Z",
                "description": "Users reporting failed payment transactions.",
                "affected_services": ["payment-service", "api-gateway"],
            },
            {
                "id": "INC-002",
                "title": "Auth service intermittent 503s",
                "severity": "warning",
                "status": "identified",
                "created_at": (now - timedelta(hours=5)).isoformat() + "Z",
                "updated_at": (now - timedelta(hours=1)).isoformat() + "Z",
                "description": "Intermittent 503 errors on auth-service endpoints.",
                "affected_services": ["auth-service"],
            },
        ])
    return {
        "platform": MONITORING_PLATFORM,
        "total": len(_INCIDENTS),
        "fetched_at": datetime.now(UTC).isoformat() + "Z",
        "incidents": _INCIDENTS,
    }


def _mock_incident_create(title: str, severity: str, description: str | None) -> dict:
    """Create a new mock incident."""
    now = datetime.now(UTC)
    incident = {
        "id": f"INC-{str(uuid.uuid4())[:8].upper()}",
        "title": title,
        "severity": severity,
        "status": "investigating",
        "created_at": now.isoformat() + "Z",
        "updated_at": now.isoformat() + "Z",
        "description": description or "",
        "affected_services": [],
    }
    _INCIDENTS.append(incident)
    return {
        "platform": MONITORING_PLATFORM,
        "action": "create",
        "incident": incident,
        "webhook_notified": bool(ALERT_WEBHOOK),
    }


def _mock_incident_update(incident_id: str, new_status: str) -> dict:
    """Update an existing mock incident."""
    for inc in _INCIDENTS:
        if inc["id"] == incident_id:
            inc["status"] = new_status
            inc["updated_at"] = datetime.now(UTC).isoformat() + "Z"
            return {
                "platform": MONITORING_PLATFORM,
                "action": "update",
                "incident": inc,
                "webhook_notified": bool(ALERT_WEBHOOK),
            }
    return {
        "error": f"Incident {incident_id} not found",
        "valid_ids": [i["id"] for i in _INCIDENTS],
    }


# ---------------------------------------------------------------------------
# Command Handlers
# ---------------------------------------------------------------------------

def cmd_health(args: argparse.Namespace) -> dict:
    return _mock_service_health(args.service, args.env)


def cmd_metrics(args: argparse.Namespace) -> dict:
    if not args.service:
        return {"error": "--service is required for metrics command"}
    return _mock_metrics(args.service, args.period, args.type)


def cmd_alerts(args: argparse.Namespace) -> dict:
    return _mock_alerts(args.status, args.severity)


def cmd_incident(args: argparse.Namespace) -> dict:
    if args.action == "list":
        return _mock_incident_list()
    elif args.action == "create":
        if not args.title:
            return {"error": "--title is required for create action"}
        if not args.severity:
            return {"error": "--severity is required for create action"}
        return _mock_incident_create(args.title, args.severity, args.description)
    elif args.action == "update":
        if not args.id:
            return {"error": "--id is required for update action"}
        if not args.status:
            return {"error": "--status is required for update action"}
        return _mock_incident_update(args.id, args.status)
    else:
        return {"error": f"Unknown action: {args.action}. Valid actions: list, create, update"}


# ---------------------------------------------------------------------------
# CLI Definition
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="monitor_tool",
        description="Monitor Kit CLI — application health, metrics, and alerts",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # health
    health_parser = subparsers.add_parser("health", help="Check service health")
    health_parser.add_argument("--service", default=None, help="Specific service name (omit for all)")
    health_parser.add_argument("--env", default="production", help="Target environment (default: production)")

    # metrics
    metrics_parser = subparsers.add_parser("metrics", help="View service metrics")
    metrics_parser.add_argument("--service", required=True, help="Service name (required)")
    metrics_parser.add_argument("--period", default="24h", choices=["1h", "6h", "24h", "7d"], help="Time period (default: 24h)")
    metrics_parser.add_argument("--type", default=None, choices=["cpu", "memory", "latency", "errors"], help="Metric type filter")

    # alerts
    alerts_parser = subparsers.add_parser("alerts", help="View and filter alerts")
    alerts_parser.add_argument("--status", default="active", choices=["active", "resolved", "all"], help="Alert status filter (default: active)")
    alerts_parser.add_argument("--severity", default=None, choices=["critical", "warning", "info"], help="Severity filter")

    # incident
    incident_parser = subparsers.add_parser("incident", help="Manage incidents")
    incident_parser.add_argument("--action", required=True, choices=["list", "create", "update"], help="Action to perform")
    incident_parser.add_argument("--id", default=None, help="Incident ID (required for update)")
    incident_parser.add_argument("--title", default=None, help="Incident title (for create)")
    incident_parser.add_argument("--severity", default=None, choices=["critical", "warning", "info"], help="Incident severity")
    incident_parser.add_argument("--status", default=None, help="New status (for update: investigating, identified, monitoring, resolved)")
    incident_parser.add_argument("--description", default=None, help="Incident description (for create)")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    handlers = {
        "health": cmd_health,
        "metrics": cmd_metrics,
        "alerts": cmd_alerts,
        "incident": cmd_incident,
    }

    handler = handlers.get(args.command)
    if handler is None:
        print(json.dumps({"error": f"Unknown command: {args.command}"}))
        sys.exit(1)

    result = handler(args)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
