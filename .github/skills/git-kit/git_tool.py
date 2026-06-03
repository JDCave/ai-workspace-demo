"""
Git Operations Tool - Mock Implementation
==========================================
Perform common Git operations: diff, log, branch, blame, status.

Usage:
    python git_tool.py diff [--branch main] [--stat]
    python git_tool.py log [--count 10] [--branch main] [--author] [--since]
    python git_tool.py branch [--list] [--create <name>] [--delete <name>]
    python git_tool.py blame --file <path> [--lines]
    python git_tool.py status

Replace the mock functions with real git commands or API calls as needed.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
except ImportError:
    pass


def get_repo_path() -> str:
    """Return the configured repository path, defaulting to cwd."""
    return os.getenv("GIT_REPO_PATH", os.getcwd())


# ============================================================
# MOCK: Replace these functions with real git operations
# ============================================================

def mock_diff(branch: str = "main", stat: bool = False) -> dict:
    """Mock git diff against a target branch."""
    if stat:
        return {
            "success": True,
            "branch": branch,
            "stat": [
                {"file": "src/api/auth.py", "insertions": 24, "deletions": 8},
                {"file": "src/api/routes.py", "insertions": 12, "deletions": 3},
                {"file": "tests/test_auth.py", "insertions": 45, "deletions": 0},
                {"file": "README.md", "insertions": 2, "deletions": 1}
            ],
            "summary": "4 files changed, 83 insertions(+), 12 deletions(-)"
        }

    return {
        "success": True,
        "branch": branch,
        "diffs": [
            {
                "file": "src/api/auth.py",
                "changes": [
                    {
                        "old_line": 42,
                        "new_line": 42,
                        "content": "-        token = generate_token(user)",
                        "action": "removed"
                    },
                    {
                        "old_line": None,
                        "new_line": 43,
                        "content": "+        token = generate_jwt_token(user, expires=3600)",
                        "action": "added"
                    }
                ]
            },
            {
                "file": "src/api/routes.py",
                "changes": [
                    {
                        "old_line": 15,
                        "new_line": 15,
                        "content": "-    return jsonify({'status': 'ok'})",
                        "action": "removed"
                    },
                    {
                        "old_line": None,
                        "new_line": 16,
                        "content": "+    return jsonify({'status': 'ok', 'version': '2.1.0'})",
                        "action": "added"
                    }
                ]
            }
        ],
        "summary": "4 files changed, 83 insertions(+), 12 deletions(-)"
    }


def mock_log(count: int = 10, branch: str = "main",
             author: str = None, since: str = None) -> dict:
    """Mock git log with commit history."""
    now = datetime.now(tz=None)
    commits = [
        {
            "hash": "a1b2c3d",
            "author": "john.doe <john.doe@example.com>",
            "date": (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "message": "feat: add JWT token refresh endpoint",
            "branch": branch
        },
        {
            "hash": "e4f5g6h",
            "author": "jane.smith <jane.smith@example.com>",
            "date": (now - timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
            "message": "fix: resolve memory leak in data processor",
            "branch": branch
        },
        {
            "hash": "i7j8k9l",
            "author": "john.doe <john.doe@example.com>",
            "date": (now - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "message": "refactor: extract validation logic into separate module",
            "branch": branch
        },
        {
            "hash": "m0n1o2p",
            "author": "alice.wang <alice.wang@example.com>",
            "date": (now - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "message": "docs: update API documentation for v2 endpoints",
            "branch": branch
        },
        {
            "hash": "q3r4s5t",
            "author": "jane.smith <jane.smith@example.com>",
            "date": (now - timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"),
            "message": "chore: upgrade dependencies to latest versions",
            "branch": branch
        }
    ]

    if author:
        commits = [c for c in commits if author.lower() in c["author"].lower()]

    return {
        "success": True,
        "branch": branch,
        "count": len(commits[:count]),
        "commits": commits[:count]
    }


def mock_branch(list_branches: bool = False, create: str = None,
                delete: str = None) -> dict:
    """Mock git branch operations."""
    branches = [
        {"name": "main", "is_current": True, "is_remote": False},
        {"name": "develop", "is_current": False, "is_remote": False},
        {"name": "feature/auth", "is_current": False, "is_remote": False},
        {"name": "feature/api-v2", "is_current": False, "is_remote": False},
        {"name": "hotfix/memory-leak", "is_current": False, "is_remote": False},
        {"name": "origin/main", "is_current": False, "is_remote": True},
        {"name": "origin/develop", "is_current": False, "is_remote": True}
    ]

    if create:
        branches.append({"name": create, "is_current": False, "is_remote": False})
        return {
            "success": True,
            "action": "create",
            "branch": create,
            "message": f"Branch '{create}' created successfully"
        }

    if delete:
        return {
            "success": True,
            "action": "delete",
            "branch": delete,
            "message": f"Branch '{delete}' deleted successfully"
        }

    return {
        "success": True,
        "action": "list",
        "branches": branches
    }


def mock_blame(file_path: str, lines: str = None) -> dict:
    """Mock git blame for a file."""
    all_lines = [
        {"line": 1, "hash": "a1b2c3d", "author": "john.doe", "date": "2025-05-20", "content": "\"\"\"Authentication module.\"\"\""},
        {"line": 2, "hash": "a1b2c3d", "author": "john.doe", "date": "2025-05-20", "content": ""},
        {"line": 3, "hash": "e4f5g6h", "author": "jane.smith", "date": "2025-06-01", "content": "import os"},
        {"line": 4, "hash": "e4f5g6h", "author": "jane.smith", "date": "2025-06-01", "content": "import hashlib"},
        {"line": 5, "hash": "a1b2c3d", "author": "john.doe", "date": "2025-05-20", "content": "from datetime import datetime, timedelta"},
        {"line": 6, "hash": "a1b2c3d", "author": "john.doe", "date": "2025-05-20", "content": ""},
        {"line": 7, "hash": "i7j8k9l", "author": "john.doe", "date": "2025-06-02", "content": "def generate_jwt_token(user, expires=3600):"},
        {"line": 8, "hash": "i7j8k9l", "author": "john.doe", "date": "2025-06-02", "content": "    payload = {'sub': user.id, 'exp': datetime.utcnow() + timedelta(seconds=expires)}"},
        {"line": 9, "hash": "i7j8k9l", "author": "john.doe", "date": "2025-06-02", "content": "    return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')"},
        {"line": 10, "hash": "a1b2c3d", "author": "john.doe", "date": "2025-05-20", "content": ""}
    ]

    if lines:
        try:
            parts = lines.split("-")
            start, end = int(parts[0]), int(parts[1])
            all_lines = [ln for ln in all_lines if start <= ln["line"] <= end]
        except (ValueError, IndexError):
            pass

    return {
        "success": True,
        "file": file_path,
        "blame": all_lines
    }


def mock_status() -> dict:
    """Mock git status showing working tree state."""
    return {
        "success": True,
        "branch": "main",
        "staged": [
            {"file": "src/api/auth.py", "status": "modified"},
            {"file": "src/api/routes.py", "status": "modified"}
        ],
        "unstaged": [
            {"file": "tests/test_auth.py", "status": "modified"},
            {"file": "README.md", "status": "modified"}
        ],
        "untracked": [
            {"file": "src/utils/validation.py"},
            {"file": "docs/api-v2-guide.md"}
        ],
        "summary": "2 staged, 2 unstaged, 2 untracked"
    }


# ============================================================
# CLI Entry Points
# ============================================================

def cmd_diff(args):
    """Handle diff command."""
    result = mock_diff(branch=args.branch, stat=args.stat)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_log(args):
    """Handle log command."""
    result = mock_log(
        count=args.count,
        branch=args.branch,
        author=args.author,
        since=args.since
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_branch(args):
    """Handle branch command."""
    result = mock_branch(
        list_branches=args.list,
        create=args.create,
        delete=args.delete
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_blame(args):
    """Handle blame command."""
    if not args.file:
        print(json.dumps({"success": False, "error": "--file is required for blame"}, indent=2))
        sys.exit(1)
    result = mock_blame(file_path=args.file, lines=args.lines)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_status(args):
    """Handle status command."""
    result = mock_status()
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Git Operations Tool (Mock)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # diff
    diff_parser = subparsers.add_parser("diff", help="Show diff between branches")
    diff_parser.add_argument("--branch", "-b", default="main", help="Target branch (default: main)")
    diff_parser.add_argument("--stat", "-s", action="store_true", help="Show stat summary only")

    # log
    log_parser = subparsers.add_parser("log", help="Show commit history")
    log_parser.add_argument("--count", "-n", type=int, default=10, help="Number of commits (default: 10)")
    log_parser.add_argument("--branch", "-b", default="main", help="Branch to inspect (default: main)")
    log_parser.add_argument("--author", "-a", default=None, help="Filter by author name or email")
    log_parser.add_argument("--since", default=None, help="Only commits after this date (e.g. 2025-01-01)")

    # branch
    branch_parser = subparsers.add_parser("branch", help="Manage branches")
    branch_parser.add_argument("--list", "-l", action="store_true", help="List all branches")
    branch_parser.add_argument("--create", "-c", default=None, metavar="NAME", help="Create a new branch")
    branch_parser.add_argument("--delete", "-d", default=None, metavar="NAME", help="Delete a branch")

    # blame
    blame_parser = subparsers.add_parser("blame", help="Show blame annotation for a file")
    blame_parser.add_argument("--file", "-f", required=True, help="File path to blame")
    blame_parser.add_argument("--lines", "-L", default=None, help="Line range (e.g. 10-20)")

    # status
    status_parser = subparsers.add_parser("status", help="Show working tree status")

    args = parser.parse_args()

    if args.command == "diff":
        cmd_diff(args)
    elif args.command == "log":
        cmd_log(args)
    elif args.command == "branch":
        cmd_branch(args)
    elif args.command == "blame":
        cmd_blame(args)
    elif args.command == "status":
        cmd_status(args)
    else:
        parser.print_help()
