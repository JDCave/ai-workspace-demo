"""
Confluence Search Tool - Mock Implementation
=============================================
Search Confluence pages by keyword, retrieve page content.

Usage:
    python search.py --query "New Joiner Guide" --space ENG --limit 10
    python read_page.py --page-id 12345

Replace the mock functions with real Confluence API calls using your
confluence-kit skills. The interface contract remains the same.
"""

import argparse
import json
import sys
import os

# Load .env if python-dotenv is available
try:
    from dotenv import load_dotenv
os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
except ImportError:
    pass

# ============================================================
# MOCK: Replace these functions with real confluence-kit calls
# ============================================================

def mock_search_pages(query: str, space: str = None, limit: int = 10) -> list:
    """Mock Confluence search - returns sample results."""
    mock_results = [
        {
            "page_id": "100001",
            "title": "New Joiner Guide - Engineering Team",
            "space": "ENG",
            "url": f"{os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.example.com')}/pages/viewpage.action?pageId=100001",
            "excerpt": "Welcome to the Engineering team! This guide covers your first week including setup, tools access, and team introductions...",
            "last_modified": "2026-05-15",
            "author": "hr-team"
        },
        {
            "page_id": "100002",
            "title": "Production Support Runbook",
            "space": "ENG",
            "url": f"{os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.example.com')}/pages/viewpage.action?pageId=100002",
            "excerpt": f"This runbook covers standard procedures for production support incidents, including escalation paths and communication templates for '{query}'...",
            "last_modified": "2026-05-20",
            "author": "ops-team"
        },
        {
            "page_id": "100003",
            "title": "Architecture Decision Records (ADR)",
            "space": "ENG",
            "url": f"{os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.example.com')}/pages/viewpage.action?pageId=100003",
            "excerpt": "Collection of architecture decision records. Includes microservice boundaries, database choices, and API design patterns...",
            "last_modified": "2026-04-10",
            "author": "arch-team"
        }
    ]
    if space:
        mock_results = [r for r in mock_results if r["space"] == space]
    return mock_results[:limit]


def mock_read_page(page_id: str) -> dict:
    """Mock Confluence page read - returns sample page content."""
    mock_pages = {
        "100001": {
            "page_id": "100001",
            "title": "New Joiner Guide - Engineering Team",
            "space": "ENG",
            "content": """# New Joiner Guide - Engineering Team

## Day 1: Getting Started
- Complete HR onboarding checklist
- Collect laptop and equipment from IT (Room 3F-201)
- Setup VPN access via IT Portal

## Day 2: Environment Setup
- Install required development tools (see Tools Setup Guide)
- Clone team repositories from GitLab
- Request access to JIRA project boards

## Day 3: Team Introduction
- Meet your assigned buddy
- Attend team standup (daily 10:00 AM)
- Review team wiki and documentation standards

## Week 1 Checklist
- [ ] Complete all access requests
- [ ] Setup local development environment
- [ ] Build and run the main service locally
- [ ] Submit your first code review
- [ ] Attend Architecture 101 session

## Key Contacts
- Team Lead: See Confluence team page
- IT Support: helpdesk@company.com
- HR: hr@company.com
""",
            "url": f"{os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.example.com')}/pages/viewpage.action?pageId=100001",
            "last_modified": "2026-05-15"
        },
        "100002": {
            "page_id": "100002",
            "title": "Production Support Runbook",
            "space": "ENG",
            "content": """# Production Support Runbook

## Severity Levels
- **SEV1 (Critical)**: Service completely down, data loss risk
- **SEV2 (High)**: Major feature broken, significant user impact
- **SEV3 (Medium)**: Minor feature issue, workaround available
- **SEV4 (Low)**: Cosmetic or non-urgent

## Incident Response Flow
1. **Detect**: Automated alerting via PagerDuty
2. **Acknowledge**: On-call engineer acknowledges within 15 min
3. **Triage**: Assess severity and scope
4. **Communicate**: Post to #incident-response Slack channel
5. **Mitigate**: Apply fix or rollback
6. **Resolve**: Confirm service restored
7. **Post-Mortem**: Document within 48 hours

## Escalation Path
- L1: On-call engineer
- L2: Team lead
- L3: Engineering manager
- L4: VP Engineering

## Communication Templates
See: /shared/templates/incident-communication.md
""",
            "url": f"{os.getenv('CONFLUENCE_BASE_URL', 'https://confluence.example.com')}/pages/viewpage.action?pageId=100002",
            "last_modified": "2026-05-20"
        }
    }
    return mock_pages.get(page_id, {"error": f"Page {page_id} not found"})


# ============================================================
# CLI Entry Points
# ============================================================

def cmd_search(args):
    """Handle search command."""
    results = mock_search_pages(args.query, args.space, args.limit)
    output = {
        "success": True,
        "query": args.query,
        "total": len(results),
        "results": results
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


def cmd_read(args):
    """Handle read page command."""
    page = mock_read_page(args.page_id)
    output = {
        "success": "error" not in page,
        "page": page
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Confluence Search Tool (Mock)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # search
    search_parser = subparsers.add_parser("search", help="Search Confluence pages")
    search_parser.add_argument("--query", "-q", required=True, help="Search query")
    search_parser.add_argument("--space", "-s", default=None, help="Space key filter")
    search_parser.add_argument("--limit", "-l", type=int, default=10, help="Max results")
    
    # read
    read_parser = subparsers.add_parser("read", help="Read a specific page")
    read_parser.add_argument("--page-id", "-p", required=True, help="Page ID to read")
    
    args = parser.parse_args()
    
    if args.command == "search":
        cmd_search(args)
    elif args.command == "read":
        cmd_read(args)
    else:
        parser.print_help()
