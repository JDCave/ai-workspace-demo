"""
Code Review Tool - Mock Implementation
========================================
Analyze diffs, check coding standards, detect security issues,
and generate review comments.

Usage:
    python review_tool.py analyze --source feature-branch --target main --severity warning
    python review_tool.py standards --path src/utils.py --ruleset strict
    python review_tool.py security --path src/ --severity medium
    python review_tool.py comment --file src/app.py --line 42 --message "Consider using a constant here"

Replace the mock functions with real tooling integrations (linters, SAST, GitHub API) as needed.
"""

import argparse
import json
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
except ImportError:
    pass

# ============================================================
# MOCK: Replace these functions with real integrations
# ============================================================

def mock_analyze(source: str, target: str = "main", severity: str = "warning") -> dict:
    """Mock diff analysis between source and target."""
    severity_levels = {"info": 0, "warning": 1, "error": 2}
    min_level = severity_levels.get(severity, 1)

    findings = [
        {
            "file": "src/auth/login.py",
            "line": 23,
            "severity": "error",
            "rule": "unused-import",
            "message": "Unused import 'os' detected"
        },
        {
            "file": "src/auth/login.py",
            "line": 47,
            "severity": "warning",
            "rule": "complex-function",
            "message": "Function 'authenticate' has cyclomatic complexity of 12 (max 10)"
        },
        {
            "file": "src/api/handlers.py",
            "line": 112,
            "severity": "warning",
            "rule": "long-function",
            "message": "Function 'process_request' exceeds 50 lines"
        },
        {
            "file": "src/api/handlers.py",
            "line": 89,
            "severity": "info",
            "rule": "naming-convention",
            "message": "Variable 'x' does not follow snake_case naming convention"
        },
        {
            "file": "src/models/user.py",
            "line": 15,
            "severity": "error",
            "rule": "missing-type-hint",
            "message": "Function 'get_user' is missing return type annotation"
        }
    ]

    filtered = [f for f in findings if severity_levels.get(f["severity"], 0) >= min_level]

    return {
        "success": True,
        "source": source,
        "target": target,
        "files_changed": 3,
        "total_findings": len(findings),
        "filtered_findings": len(filtered),
        "severity_threshold": severity,
        "findings": filtered
    }


def mock_standards(path: str, ruleset: str = "default") -> dict:
    """Mock coding standards check."""
    strict_extra = [
        {
            "file": "src/auth/login.py",
            "line": 5,
            "severity": "warning",
            "rule": "docstring-missing",
            "message": "Module-level docstring is missing"
        },
        {
            "file": "src/auth/login.py",
            "line": 34,
            "severity": "warning",
            "rule": "line-too-long",
            "message": "Line exceeds 80 characters (92 chars)"
        },
        {
            "file": "src/api/handlers.py",
            "line": 8,
            "severity": "info",
            "rule": "trailing-whitespace",
            "message": "Trailing whitespace detected"
        }
    ]

    base_violations = [
        {
            "file": "src/auth/login.py",
            "line": 23,
            "severity": "error",
            "rule": "unused-import",
            "message": "Unused import 'os' detected"
        },
        {
            "file": "src/api/handlers.py",
            "line": 45,
            "severity": "warning",
            "rule": "missing-docstring",
            "message": "Public function 'handle_request' is missing a docstring"
        },
        {
            "file": "src/models/user.py",
            "line": 30,
            "severity": "info",
            "rule": "naming-convention",
            "message": "Variable 'tmp' is too generic"
        }
    ]

    violations = base_violations + (strict_extra if ruleset == "strict" else [])

    return {
        "success": True,
        "path": path,
        "ruleset": ruleset,
        "files_scanned": 3,
        "total_violations": len(violations),
        "violations": violations
    }


def mock_security(path: str, severity: str = "medium") -> dict:
    """Mock security vulnerability scan."""
    severity_levels = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    min_level = severity_levels.get(severity, 1)

    vulnerabilities = [
        {
            "file": "src/auth/login.py",
            "line": 56,
            "severity": "critical",
            "rule": "sql-injection",
            "message": "Potential SQL injection: string concatenation in SQL query",
            "cwe": "CWE-89"
        },
        {
            "file": "src/auth/login.py",
            "line": 72,
            "severity": "high",
            "rule": "hardcoded-secret",
            "message": "Possible hardcoded secret or API key detected",
            "cwe": "CWE-798"
        },
        {
            "file": "src/api/handlers.py",
            "line": 34,
            "severity": "medium",
            "rule": "unsafe-deserialization",
            "message": "Use of pickle.load() may lead to arbitrary code execution",
            "cwe": "CWE-502"
        },
        {
            "file": "src/api/handlers.py",
            "line": 98,
            "severity": "medium",
            "rule": "insecure-transport",
            "message": "HTTP connection used instead of HTTPS",
            "cwe": "CWE-319"
        },
        {
            "file": "src/utils/helpers.py",
            "line": 12,
            "severity": "low",
            "rule": "weak-random",
            "message": "Use of random module instead of secrets for security-sensitive context",
            "cwe": "CWE-338"
        }
    ]

    filtered = [v for v in vulnerabilities if severity_levels.get(v["severity"], 0) >= min_level]

    return {
        "success": True,
        "path": path,
        "severity_threshold": severity,
        "files_scanned": 3,
        "total_vulnerabilities": len(vulnerabilities),
        "filtered_vulnerabilities": len(filtered),
        "vulnerabilities": filtered
    }


def mock_comment(file: str, line: int, message: str) -> dict:
    """Mock review comment generation."""
    return {
        "success": True,
        "comment": {
            "file": file,
            "line": line,
            "message": message,
            "author": os.getenv("GITHUB_USER", "reviewer-bot"),
            "type": "review-comment"
        },
        "message": f"Review comment prepared for {file}:{line}"
    }


# ============================================================
# CLI Entry Points
# ============================================================

def cmd_analyze(args):
    """Handle analyze command."""
    result = mock_analyze(
        source=args.source,
        target=args.target,
        severity=args.severity
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_standards(args):
    """Handle standards command."""
    result = mock_standards(
        path=args.path,
        ruleset=args.ruleset
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_security(args):
    """Handle security command."""
    result = mock_security(
        path=args.path,
        severity=args.severity
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_comment(args):
    """Handle comment command."""
    result = mock_comment(
        file=args.file,
        line=args.line,
        message=args.message
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Code Review Tool (Mock)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Analyze diff between source and target")
    analyze_parser.add_argument("--source", "-s", required=True, help="Source branch or commit hash")
    analyze_parser.add_argument("--target", "-t", default="main", help="Target branch (default: main)")
    analyze_parser.add_argument("--severity", default="warning",
                                choices=["info", "warning", "error"],
                                help="Minimum severity level (default: warning)")

    # standards
    standards_parser = subparsers.add_parser("standards", help="Check coding standards")
    standards_parser.add_argument("--path", "-p", required=True, help="File or directory to check")
    standards_parser.add_argument("--ruleset", "-r", default="default",
                                  choices=["default", "strict"],
                                  help="Ruleset to apply (default: default)")

    # security
    security_parser = subparsers.add_parser("security", help="Scan for security vulnerabilities")
    security_parser.add_argument("--path", "-p", required=True, help="File or directory to scan")
    security_parser.add_argument("--severity", "-s", default="medium",
                                 choices=["low", "medium", "high", "critical"],
                                 help="Minimum severity to report (default: medium)")

    # comment
    comment_parser = subparsers.add_parser("comment", help="Generate a review comment")
    comment_parser.add_argument("--file", "-f", required=True, help="Target file path")
    comment_parser.add_argument("--line", "-l", required=True, type=int, help="Line number")
    comment_parser.add_argument("--message", "-m", required=True, help="Comment text")

    args = parser.parse_args()

    if args.command == "analyze":
        cmd_analyze(args)
    elif args.command == "standards":
        cmd_standards(args)
    elif args.command == "security":
        cmd_security(args)
    elif args.command == "comment":
        cmd_comment(args)
    else:
        parser.print_help()
