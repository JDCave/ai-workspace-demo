---
name: monitor-kit
description: 'Monitor application health, view metrics, and manage alerts. Use this when the user asks about system health, error rates, response times, alerts, or incident investigation.'
allowed-tools: shell
---

# Monitoring and Alerting Skill

You have access to a Python CLI tool for monitoring application health, viewing metrics, and managing alerts.

## When to Use
- User wants to check the health status of services or the overall system
- User asks about error rates, response times, CPU/memory usage, or latency
- User wants to view, filter, or manage active alerts
- User is investigating an incident and needs to list, create, or update incidents
- User asks about system reliability or performance trends

## Available Commands

### Health Check
```bash
python .github/skills/monitor-kit/monitor_tool.py health [--service <name>] [--env <env>]
```

**Parameters:**
- `--service`: Specific service name to check (omit for all services)
- `--env`: Environment to check (e.g., production, staging, development). Default: production

### Metrics
```bash
python .github/skills/monitor-kit/monitor_tool.py metrics --service <name> [--period 1h|6h|24h|7d] [--type cpu|memory|latency|errors]
```

**Parameters:**
- `--service` (required): Service name to fetch metrics for
- `--period`: Time period for metrics (1h, 6h, 24h, 7d). Default: 24h
- `--type`: Metric type to display (cpu, memory, latency, errors). Default: returns all types

### Alerts
```bash
python .github/skills/monitor-kit/monitor_tool.py alerts [--status active|resolved|all] [--severity critical|warning|info]
```

**Parameters:**
- `--status`: Filter alerts by status (active, resolved, all). Default: active
- `--severity`: Filter by severity level (critical, warning, info). Default: all severities

### Incident Management
```bash
python .github/skills/monitor-kit/monitor_tool.py incident --action list|create|update --id <incident_id>
```

**Parameters:**
- `--action` (required): Action to perform
  - `list`: List all incidents
  - `create`: Create a new incident (requires `--title` and `--severity`)
  - `update`: Update an existing incident (requires `--id` and `--status`)
- `--id`: Incident ID (required for update action)
- `--title`: Incident title (used with create action)
- `--severity`: Incident severity (critical, warning, info — used with create action)
- `--status`: New status for the incident (investigating, identified, monitoring, resolved — used with update action)
- `--description`: Incident description (optional, used with create action)

## Parameters

| Parameter | Command | Required | Description |
|-----------|---------|----------|-------------|
| `--service` | health, metrics | For metrics | Service name to query |
| `--env` | health | No | Target environment (default: production) |
| `--period` | metrics | No | Time window: 1h, 6h, 24h, 7d (default: 24h) |
| `--type` | metrics | No | Metric type: cpu, memory, latency, errors |
| `--status` | alerts | No | Alert status filter (default: active) |
| `--severity` | alerts, incident | No | Severity filter: critical, warning, info |
| `--action` | incident | Yes | list, create, or update |
| `--id` | incident | For update | Incident identifier |

## Important Rules
- **ALWAYS** start with a health check when investigating issues to get an overview of the system state
- **ALWAYS** review active alerts before creating a new incident — avoid duplicates
- Summarize metrics in human-readable form; highlight anomalies and trends
- When creating incidents, include clear titles and detailed descriptions
- Correlate alerts with metrics data when assisting in incident investigation
- Escalate critical alerts immediately and suggest remediation steps when possible

## Configuration
Requires `.env` file with:
```
MONITORING_PLATFORM=datadog
ALERT_WEBHOOK=https://hooks.example.com/alerts
```

Supported `MONITORING_PLATFORM` values: `datadog`, `grafana`, `prometheus`, `mock` (default: mock)
