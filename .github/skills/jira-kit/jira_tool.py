"""
Jira Integration Tool - Mock Implementation
=============================================
Create, search, and update Jira tickets.

Usage:
    python jira_tool.py create --project PROJ --summary "Fix login bug" --type Bug
    python jira_tool.py search --jql "project=PROJ AND status=Open"
    python jira_tool.py comment --ticket PROJ-123 --comment "Updated with findings"

Replace the mock functions with real Jira API calls using your jira-kit skills.
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
# MOCK: Replace these functions with real jira-kit calls
# ============================================================

_ticket_counter = 100

def mock_create_ticket(project: str, summary: str, description: str, 
                       issue_type: str = "Story", labels: list = None,
                       assignee: str = None, priority: str = "Medium") -> dict:
    """Mock Jira ticket creation."""
    global _ticket_counter
    _ticket_counter += 1
    ticket_key = f"{project}-{_ticket_counter}"
    
    return {
        "success": True,
        "ticket_key": ticket_key,
        "summary": summary,
        "type": issue_type,
        "status": "To Do",
        "priority": priority,
        "labels": labels or [],
        "assignee": assignee,
        "url": f"{os.getenv('JIRA_BASE_URL', 'https://jira.example.com')}/browse/{ticket_key}",
        "message": f"Ticket {ticket_key} created successfully"
    }


def mock_search_tickets(jql: str, limit: int = 20) -> dict:
    """Mock Jira ticket search."""
    mock_tickets = [
        {
            "key": "PROJ-101",
            "summary": "Implement user authentication module",
            "type": "Story",
            "status": "In Progress",
            "priority": "High",
            "assignee": "john.doe",
            "labels": ["auth", "security"]
        },
        {
            "key": "PROJ-102",
            "summary": "Fix memory leak in data processor",
            "type": "Bug",
            "status": "Open",
            "priority": "Critical",
            "assignee": None,
            "labels": ["performance", "backend"]
        },
        {
            "key": "PROJ-103",
            "summary": "Update API documentation for v2 endpoints",
            "type": "Task",
            "status": "Done",
            "priority": "Low",
            "assignee": "jane.smith",
            "labels": ["docs"]
        }
    ]
    return {
        "success": True,
        "jql": jql,
        "total": len(mock_tickets),
        "results": mock_tickets[:limit]
    }


def mock_add_comment(ticket: str, comment: str) -> dict:
    """Mock adding comment to Jira ticket."""
    return {
        "success": True,
        "ticket": ticket,
        "comment": comment,
        "message": f"Comment added to {ticket}"
    }


def mock_update_ticket(ticket: str, fields: dict) -> dict:
    """Mock updating Jira ticket fields."""
    return {
        "success": True,
        "ticket": ticket,
        "updated_fields": list(fields.keys()),
        "message": f"Ticket {ticket} updated successfully"
    }


# ============================================================
# CLI Entry Points
# ============================================================

def cmd_create(args):
    """Handle create command."""
    labels = args.labels.split(",") if args.labels else []
    result = mock_create_ticket(
        project=args.project,
        summary=args.summary,
        description=args.description or "",
        issue_type=args.type,
        labels=labels,
        assignee=args.assignee,
        priority=args.priority
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_search(args):
    """Handle search command."""
    result = mock_search_tickets(args.jql, args.limit)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_comment(args):
    """Handle comment command."""
    result = mock_add_comment(args.ticket, args.comment)
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_update(args):
    """Handle update command."""
    fields = json.loads(args.fields) if args.fields else {}
    result = mock_update_ticket(args.ticket, fields)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jira Integration Tool (Mock)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # create
    create_parser = subparsers.add_parser("create", help="Create a Jira ticket")
    create_parser.add_argument("--project", "-p", required=True, help="Project key (e.g. PROJ)")
    create_parser.add_argument("--summary", "-s", required=True, help="Ticket summary")
    create_parser.add_argument("--description", "-d", default="", help="Ticket description")
    create_parser.add_argument("--type", "-t", default="Story", choices=["Story", "Bug", "Task", "Epic", "Sub-task"], help="Issue type")
    create_parser.add_argument("--labels", "-l", default=None, help="Comma-separated labels")
    create_parser.add_argument("--assignee", "-a", default=None, help="Assignee username")
    create_parser.add_argument("--priority", default="Medium", choices=["Highest", "High", "Medium", "Low", "Lowest"], help="Priority")
    
    # search
    search_parser = subparsers.add_parser("search", help="Search Jira tickets")
    search_parser.add_argument("--jql", "-j", required=True, help="JQL query")
    search_parser.add_argument("--limit", "-n", type=int, default=20, help="Max results")
    
    # comment
    comment_parser = subparsers.add_parser("comment", help="Add comment to ticket")
    comment_parser.add_argument("--ticket", "-t", required=True, help="Ticket key (e.g. PROJ-101)")
    comment_parser.add_argument("--comment", "-c", required=True, help="Comment text")
    
    # update
    update_parser = subparsers.add_parser("update", help="Update ticket fields")
    update_parser.add_argument("--ticket", "-t", required=True, help="Ticket key")
    update_parser.add_argument("--fields", "-f", required=True, help="JSON object of fields to update")
    
    args = parser.parse_args()
    
    if args.command == "create":
        cmd_create(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "comment":
        cmd_comment(args)
    elif args.command == "update":
        cmd_update(args)
    else:
        parser.print_help()
