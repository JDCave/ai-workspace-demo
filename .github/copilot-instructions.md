# AI Workspace - Copilot Custom Instructions

> This workspace equips GitHub Copilot with knowledge-search and Jira-integration capabilities.
> All instructions below are automatically applied to every Copilot Chat session.

---

## Workspace Purpose

An **AI-assisted workbench** providing three core capabilities:

1. **Confluence Knowledge Search** — Search internal Confluence wikis
2. **Local Knowledge Base** — Search team-specific documents in `knowledge-base/`
3. **Requirement Analysis → Jira Ticket** — Analyze requirements with team context, create structured tickets

## Workspace Structure

```
.github/
├── copilot-instructions.md     ← YOU ARE HERE (system instructions, always-on)
├── instructions/               ← Conditional instructions (auto-apply by file type)
├── prompts/                    ← Reusable prompts (type / in Chat to invoke)
├── skills/                     ← Agent skills (auto-loaded when relevant)
│   ├── confluence-kit/         ← Confluence search & read
│   ├── jira-kit/               ← Jira ticket CRUD
│   └── knowledge-base-kit/     ← Local KB search
└── agents/                     ← Custom agents (select in Chat dropdown)
    ├── requirement-analyst     ← Requirement analysis with handoffs
    ├── jira-creator            ← Jira ticket creation
    └── knowledge-searcher      ← Cross-source knowledge search
```

## How Skills Work

This workspace includes three skills that Copilot automatically loads when relevant:

- **confluence-kit** — Activated when the user asks to search or read Confluence pages
- **jira-kit** — Activated when the user asks to create, search, or update Jira tickets
- **knowledge-base-kit** — Activated when the user asks about team documentation

Each skill contains a `SKILL.md` with usage instructions and a Python CLI tool.
Copilot will follow the instructions in the matched skill to execute the appropriate commands.

**Do NOT hardcode script paths in your responses.** Rely on the skills — they provide the exact commands and parameters.

## Agent Behaviors

### When User Asks to Search Knowledge
1. Determine scope: Confluence, local KB, or both
2. The relevant skill will provide the search commands — follow its instructions
3. Summarize results with source citations
4. Suggest refining the query if insufficient

### When User Asks for Requirement Analysis
1. Load team context from `knowledge-base/<team>/`
2. Analyze: functional + non-functional requirements, impact, acceptance criteria
3. Present for user review before creating tickets

### When User Asks to Create Jira Tickets
1. Confirm project key, ticket type, team
2. Generate structured content
3. **Always dry-run first** — show preview, get confirmation
4. Create and report ticket URL

## Important Rules

- **NEVER** expose API tokens, PATs, or credentials in output
- **ALWAYS** confirm before creating Jira tickets (dry-run first)
- **ALWAYS** cite sources: `[Source: knowledge-base/team-alpha/xxx.md]` or `[Source: Confluence - "page title" (url)]`
- Prefer local KB first (faster), then Confluence
- Handle script errors gracefully, suggest manual steps
- Default team: `team-alpha` unless specified

## Available Prompts (type / in Chat)

| Command | Description |
|---------|-------------|
| `/search-confluence` | Search Confluence wikis |
| `/search-knowledge-base` | Search local team docs |
| `/analyze-requirement` | Structured requirement analysis |
| `/create-jira-ticket` | Create Jira tickets |
| `/production-support` | Production incident workflow |
