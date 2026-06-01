---
name: confluence-kit
description: Search and read Confluence wiki pages. Use this when the user asks to search company knowledge base, find wiki pages, or look up Confluence documentation.
allowed-tools: shell
---

# Confluence Knowledge Search Skill

You have access to a Python CLI tool for searching and reading Confluence pages.

## When to Use
- User asks to search company wiki / knowledge base
- User needs to find specific Confluence pages (e.g., "New Joiner Guide", "Production Support Runbook")
- User references a Confluence page by name or topic

## Available Commands

### Search Confluence Pages
```bash
python .github/skills/confluence-kit/confluence_tool.py search --query "<search terms>" [--space <SPACE_KEY>] [--limit 10]
```

**Parameters:**
- `--query` (required): Search keywords
- `--space`: Filter by Confluence space key (e.g., ENG, HR, OPS)
- `--limit`: Max results, default 10

**Output:** JSON array of matching pages with title, URL, excerpt, last_modified, author.

### Read a Specific Page
```bash
python .github/skills/confluence-kit/confluence_tool.py read --page-id <PAGE_ID>
```

**Output:** Full page content in Markdown format.

## Response Guidelines
- Always include the page title and URL when referencing Confluence content
- Summarize long pages rather than dumping raw content
- If search returns no results, suggest alternative search terms or different spaces
- Cite sources: `[Source: Confluence - "<page title>" (<url>)]`

## Configuration
Requires `.env` file with:
```
CONFLUENCE_BASE_URL=https://your-company.atlassian.net/wiki
CONFLUENCE_PAT=your_personal_access_token
CONFLUENCE_DEFAULT_SPACE=ENG
```

## Troubleshooting
- If `401 Unauthorized`: Check CONFLUENCE_PAT in .env
- If `404 Not Found`: Page ID may be incorrect
- If connection refused: Check CONFLUENCE_BASE_URL and VPN connection
