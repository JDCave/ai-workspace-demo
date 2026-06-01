---
name: knowledge-base-kit
description: Search and browse the local team knowledge base stored in knowledge-base/. Use this when the user asks about team architecture, runbooks, meeting notes, coding standards, or any team-specific documentation.
---

# Local Knowledge Base Skill

You have access to a local knowledge base stored in the `knowledge-base/` directory, organized by team.

## When to Use
- User asks about team architecture, system design
- User needs runbook or incident response procedures
- User references meeting notes or decisions
- User asks about coding standards or guidelines
- You need team context for requirement analysis

## Knowledge Base Structure

```
knowledge-base/
├── team-alpha/
│   ├── architecture/     # System architecture docs
│   ├── runbooks/         # Operational runbooks
│   └── meeting-notes/    # Sprint reviews, decisions
├── team-beta/
│   ├── architecture/
│   ├── runbooks/
│   └── meeting-notes/
└── shared/
    ├── templates/        # Shared templates (incident comms, etc.)
    └── guidelines/       # Coding standards, design guidelines
```

## Search Methods

### Method 1: Python Search Tool (Keyword Match)
```bash
python .github/skills/knowledge-base-kit/kb_tool.py search --query "<keywords>" [--team <team-name>] [--limit 10]
```

### Method 2: List All Documents
```bash
python .github/skills/knowledge-base-kit/kb_tool.py list [--team <team-name>]
```

### Method 3: Direct File Read
Read the Markdown file directly from the workspace:
- Use `#codebase` or `@workspace` to find relevant files
- Read the file content and present it formatted

## Response Guidelines
- Always cite the source file path: `[Source: knowledge-base/team-alpha/architecture/system-overview.md]`
- For architecture questions, load all files in the team's `architecture/` directory
- For incident response, check both team `runbooks/` and `shared/templates/`
- For requirement analysis, read `shared/guidelines/` for standards and the team's `architecture/` for system context
- If the user doesn't specify a team, default to `team-alpha`
