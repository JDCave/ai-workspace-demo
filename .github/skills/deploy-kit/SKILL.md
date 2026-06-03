---
name: deploy-kit
description: Manage deployment workflows — build, deploy, rollback, and check deployment status. Use this when the user asks to deploy services, check deployment status, or roll back a release.
allowed-tools: shell
---

# Deployment Automation Skill

You have access to a Python CLI tool for managing deployment workflows including building, deploying, rolling back, and checking deployment status.

## When to Use
- User wants to build a service for deployment
- User wants to deploy a service to a specific environment (dev, staging, prod)
- User wants to check the current deployment status of a service or environment
- User wants to roll back a deployment to a previous version
- User asks about deployment health or release history

## Available Commands

### Build
```bash
python .github/skills/deploy-kit/deploy_tool.py build [--env dev|staging|prod] [--service <name>]
```

**Parameters:**
- `--env` `-e`: Target environment (dev, staging, prod). Default: dev
- `--service` `-s`: Service name to build (e.g. api-gateway, auth-service)

### Deploy
```bash
python .github/skills/deploy-kit/deploy_tool.py deploy --env <env> --service <name> [--version <tag>] [--dry-run]
```

**Parameters:**
- `--env` `-e` (required): Target environment (dev, staging, prod)
- `--service` `-s` (required): Service name to deploy
- `--version` `-v`: Version tag to deploy (e.g. v1.2.3). Default: latest build
- `--dry-run`: Simulate the deployment without executing it

### Rollback
```bash
python .github/skills/deploy-kit/deploy_tool.py rollback --env <env> --service <name> [--version <tag>]
```

**Parameters:**
- `--env` `-e` (required): Target environment (dev, staging, prod)
- `--service` `-s` (required): Service name to roll back
- `--version` `-v`: Version tag to roll back to. Default: previous stable version

### Status
```bash
python .github/skills/deploy-kit/deploy_tool.py status --env <env> [--service <name>]
```

**Parameters:**
- `--env` `-e` (required): Target environment (dev, staging, prod)
- `--service` `-s`: Service name to check. If omitted, shows status for all services in the environment

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--env` | Yes (deploy, rollback, status) | Target environment: `dev`, `staging`, or `prod` |
| `--service` | Yes (deploy, rollback) | Name of the service to operate on |
| `--version` | No | Specific version tag. Defaults to latest build or previous stable |
| `--dry-run` | No | Simulate the operation without making changes |

## Important Rules
- **ALWAYS** run with `--dry-run` first when deploying to `prod` environment
- **ALWAYS** get explicit user confirmation before executing a real deploy or rollback command
- Show the user a preview of what will be deployed (service, version, environment) before confirming
- Report the deployment result including status, version, and any relevant URLs after completion
- When rolling back, confirm the target version with the user before executing

## Configuration
Requires `.env` file with:
```
DEPLOY_TOOL=mock
CI_CD_PLATFORM=github-actions
K8S_CLUSTER=my-cluster
```
