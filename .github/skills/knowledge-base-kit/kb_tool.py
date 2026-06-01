"""
Knowledge Base Search Tool
==========================
Full-text search across the local knowledge-base/ directory.
Uses simple keyword matching (mock). Replace with Elasticsearch,
Meilisearch, or vector search for production use.

Usage:
    python kb_tool.py search --query "incident response"
    python kb_tool.py search --query "deploy" --team team-alpha
    python kb_tool.py list --team team-alpha
"""

import argparse
import json
import os
import glob

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
except ImportError:
    pass

# Resolve knowledge base root path
KB_ROOT = os.getenv("KB_ROOT_PATH", os.path.join(os.path.dirname(__file__), "..", "..", "..", "knowledge-base"))
KB_ROOT = os.path.abspath(KB_ROOT)


def search_knowledge_base(query: str, team: str = None, limit: int = 10) -> dict:
    """Search knowledge base markdown files by keyword."""
    query_terms = query.lower().split()
    results = []
    
    # Determine search scope
    if team:
        search_pattern = os.path.join(KB_ROOT, team, "**", "*.md")
    else:
        search_pattern = os.path.join(KB_ROOT, "**", "*.md")
    
    for filepath in glob.glob(search_pattern, recursive=True):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            content_lower = content.lower()
            title = os.path.basename(filepath)
            
            # Calculate simple relevance score
            score = sum(content_lower.count(term) for term in query_terms)
            
            if score > 0:
                # Extract a snippet around first match
                first_term = query_terms[0]
                idx = content_lower.find(first_term)
                start = max(0, idx - 100)
                end = min(len(content), idx + 200)
                snippet = content[start:end].replace("\n", " ").strip()
                if start > 0:
                    snippet = "..." + snippet
                if end < len(content):
                    snippet = snippet + "..."
                
                rel_path = os.path.relpath(filepath, KB_ROOT)
                results.append({
                    "file": rel_path,
                    "title": title.replace(".md", ""),
                    "score": score,
                    "snippet": snippet,
                    "team": rel_path.split(os.sep)[0] if os.sep in rel_path else "shared"
                })
        except Exception:
            continue
    
    # Sort by relevance
    results.sort(key=lambda x: x["score"], reverse=True)
    return {
        "success": True,
        "query": query,
        "team_filter": team,
        "total": len(results[:limit]),
        "results": results[:limit]
    }


def list_knowledge_base(team: str = None) -> dict:
    """List all documents in the knowledge base."""
    if team:
        search_pattern = os.path.join(KB_ROOT, team, "**", "*.md")
    else:
        search_pattern = os.path.join(KB_ROOT, "**", "*.md")
    
    files = []
    for filepath in sorted(glob.glob(search_pattern, recursive=True)):
        rel_path = os.path.relpath(filepath, KB_ROOT)
        title = os.path.basename(filepath).replace(".md", "")
        files.append({
            "file": rel_path,
            "title": title,
        })
    
    return {
        "success": True,
        "team_filter": team,
        "total": len(files),
        "files": files
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Knowledge Base Search Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # search
    search_parser = subparsers.add_parser("search", help="Search knowledge base")
    search_parser.add_argument("--query", "-q", required=True, help="Search query")
    search_parser.add_argument("--team", "-t", default=None, help="Team filter (team-alpha, team-beta, shared)")
    search_parser.add_argument("--limit", "-l", type=int, default=10, help="Max results")
    
    # list
    list_parser = subparsers.add_parser("list", help="List knowledge base documents")
    list_parser.add_argument("--team", "-t", default=None, help="Team filter")
    
    args = parser.parse_args()
    
    if args.command == "search":
        result = search_knowledge_base(args.query, args.team, args.limit)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.command == "list":
        result = list_knowledge_base(args.team)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        parser.print_help()
