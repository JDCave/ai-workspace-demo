"""
Deployment Automation Tool - Mock Implementation
==================================================
Build, deploy, rollback, and check deployment status.

Usage:
    python deploy_tool.py build --env dev --service api-gateway
    python deploy_tool.py deploy --env staging --service auth-service --version v1.2.0
    python deploy_tool.py deploy --env prod --service api-gateway --dry-run
    python deploy_tool.py rollback --env prod --service auth-service --version v1.1.9
    python deploy_tool.py status --env dev

Replace the mock functions with real CI/CD and Kubernetes API calls.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
except ImportError:
    pass

# ============================================================
# Configuration
# ============================================================

DEPLOY_TOOL = os.getenv("DEPLOY_TOOL", "mock")
CI_CD_PLATFORM = os.getenv("CI_CD_PLATFORM", "github-actions")
K8S_CLUSTER = os.getenv("K8S_CLUSTER", "my-cluster")

# ============================================================
# MOCK: Replace these functions with real CI/CD and K8s calls
# ============================================================

_mock_deployments = {
    "dev": {
        "api-gateway": {"version": "v1.3.2", "status": "running", "replicas": 2, "uptime": "3h 12m"},
        "auth-service": {"version": "v1.1.0", "status": "running", "replicas": 1, "uptime": "6h 45m"},
    },
    "staging": {
        "api-gateway": {"version": "v1.3.1", "status": "running", "replicas": 2, "uptime": "1d 2h"},
        "auth-service": {"version": "v1.1.0", "status": "running", "replicas": 2, "uptime": "1d 2h"},
    },
    "prod": {
        "api-gateway": {"version": "v1.3.0", "status": "running", "replicas": 4, "uptime": "5d 8h"},
        "auth-service": {"version": "v1.0.8", "status": "running", "replicas": 3, "uptime": "5d 8h"},
    },
}

_mock_build_counter = 0


def mock_build(env: str, service: str = None) -> dict:
    """Mock service build."""
    global _mock_build_counter
    _mock_build_counter += 1
    timestamp = datetime.now(timezone.utc).isoformat()
    services = [service] if service else ["api-gateway", "auth-service"]
    builds = []
    for svc in services:
        _mock_build_counter += 1
        builds.append({
            "service": svc,
            "build_id": f"bld-{_mock_build_counter:04d}",
            "version": f"v1.4.{_mock_build_counter}",
            "env": env,
            "status": "success",
            "timestamp": timestamp,
        })
    return {
        "success": True,
        "env": env,
        "builds": builds,
        "message": f"Built {len(builds)} service(s) for {env}"
    }


def mock_deploy(env: str, service: str, version: str = None, dry_run: bool = False) -> dict:
    """Mock service deployment."""
    timestamp = datetime.now(timezone.utc).isoformat()
    current = _mock_deployments.get(env, {}).get(service, {})
    target_version = version or f"v1.4.{_mock_build_counter + 1}"

    if dry_run:
        return {
            "success": True,
            "dry_run": True,
            "env": env,
            "service": service,
            "current_version": current.get("version", "unknown"),
            "target_version": target_version,
            "cluster": K8S_CLUSTER,
            "platform": CI_CD_PLATFORM,
            "message": f"[DRY-RUN] Would deploy {service} {target_version} to {env} on cluster '{K8S_CLUSTER}'"
        }

    # Simulate deployment
    _mock_deployments.setdefault(env, {})[service] = {
        "version": target_version,
        "status": "deploying",
        "replicas": 2 if env == "dev" else 4 if env == "prod" else 2,
        "uptime": "0m",
    }

    return {
        "success": True,
        "dry_run": False,
        "env": env,
        "service": service,
        "previous_version": current.get("version", "unknown"),
        "deployed_version": target_version,
        "status": "deploying",
        "replicas": _mock_deployments[env][service]["replicas"],
        "cluster": K8S_CLUSTER,
        "platform": CI_CD_PLATFORM,
        "timestamp": timestamp,
        "message": f"Deployed {service} {target_version} to {env}"
    }


def mock_rollback(env: str, service: str, version: str = None) -> dict:
    """Mock deployment rollback."""
    timestamp = datetime.now(timezone.utc).isoformat()
    current = _mock_deployments.get(env, {}).get(service, {})
    current_version = current.get("version", "unknown")

    # Simulate previous stable version
    if version is None:
        parts = current_version.lstrip("v").split(".") if current_version != "unknown" else ["1", "0", "0"]
        try:
            patch = int(parts[2]) - 1
            rollback_version = f"v{parts[0]}.{parts[1]}.{max(patch, 0)}"
        except (ValueError, IndexError):
            rollback_version = "v1.0.0"
    else:
        rollback_version = version

    _mock_deployments.setdefault(env, {})[service] = {
        "version": rollback_version,
        "status": "rolling-back",
        "replicas": current.get("replicas", 2),
        "uptime": "0m",
    }

    return {
        "success": True,
        "env": env,
        "service": service,
        "rolled_back_from": current_version,
        "rolled_back_to": rollback_version,
        "status": "rolling-back",
        "cluster": K8S_CLUSTER,
        "platform": CI_CD_PLATFORM,
        "timestamp": timestamp,
        "message": f"Rolled back {service} in {env} from {current_version} to {rollback_version}"
    }


def mock_status(env: str, service: str = None) -> dict:
    """Mock deployment status check."""
    env_deployments = _mock_deployments.get(env, {})
    if service:
        svc_status = env_deployments.get(service)
        if svc_status is None:
            return {
                "success": False,
                "env": env,
                "service": service,
                "error": f"Service '{service}' not found in environment '{env}'",
                "message": f"No deployment found for {service} in {env}"
            }
        return {
            "success": True,
            "env": env,
            "service": service,
            "version": svc_status["version"],
            "status": svc_status["status"],
            "replicas": svc_status["replicas"],
            "uptime": svc_status["uptime"],
            "cluster": K8S_CLUSTER,
        }
    else:
        services = []
        for svc_name, svc_info in env_deployments.items():
            services.append({
                "service": svc_name,
                "version": svc_info["version"],
                "status": svc_info["status"],
                "replicas": svc_info["replicas"],
                "uptime": svc_info["uptime"],
            })
        return {
            "success": True,
            "env": env,
            "cluster": K8S_CLUSTER,
            "total_services": len(services),
            "services": services,
            "message": f"{len(services)} service(s) found in {env}"
        }


# ============================================================
# CLI Entry Points
# ============================================================

def cmd_build(args):
    """Handle build command."""
    result = mock_build(env=args.env, service=args.service)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_deploy(args):
    """Handle deploy command."""
    result = mock_deploy(
        env=args.env,
        service=args.service,
        version=args.version,
        dry_run=args.dry_run
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_rollback(args):
    """Handle rollback command."""
    result = mock_rollback(
        env=args.env,
        service=args.service,
        version=args.version
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_status(args):
    """Handle status command."""
    result = mock_status(env=args.env, service=args.service)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deployment Automation Tool (Mock)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # build
    build_parser = subparsers.add_parser("build", help="Build a service for deployment")
    build_parser.add_argument("--env", "-e", default="dev",
                              choices=["dev", "staging", "prod"],
                              help="Target environment (default: dev)")
    build_parser.add_argument("--service", "-s", default=None,
                              help="Service name to build")

    # deploy
    deploy_parser = subparsers.add_parser("deploy", help="Deploy a service to an environment")
    deploy_parser.add_argument("--env", "-e", required=True,
                               choices=["dev", "staging", "prod"],
                               help="Target environment")
    deploy_parser.add_argument("--service", "-s", required=True,
                               help="Service name to deploy")
    deploy_parser.add_argument("--version", "-v", default=None,
                               help="Version tag to deploy (default: latest build)")
    deploy_parser.add_argument("--dry-run", action="store_true", default=False,
                               help="Simulate deployment without executing")

    # rollback
    rollback_parser = subparsers.add_parser("rollback", help="Roll back a service deployment")
    rollback_parser.add_argument("--env", "-e", required=True,
                                 choices=["dev", "staging", "prod"],
                                 help="Target environment")
    rollback_parser.add_argument("--service", "-s", required=True,
                                 help="Service name to roll back")
    rollback_parser.add_argument("--version", "-v", default=None,
                                 help="Version tag to roll back to (default: previous stable)")

    # status
    status_parser = subparsers.add_parser("status", help="Check deployment status")
    status_parser.add_argument("--env", "-e", required=True,
                               choices=["dev", "staging", "prod"],
                               help="Target environment")
    status_parser.add_argument("--service", "-s", default=None,
                               help="Service name (omit for all services)")

    args = parser.parse_args()

    if args.command == "build":
        cmd_build(args)
    elif args.command == "deploy":
        cmd_deploy(args)
    elif args.command == "rollback":
        cmd_rollback(args)
    elif args.command == "status":
        cmd_status(args)
    else:
        parser.print_help()
