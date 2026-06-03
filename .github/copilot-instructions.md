# AI Workspace - Copilot Custom Instructions

> This workspace equips GitHub Copilot with a full SDLC (Software Development Lifecycle) toolchain.
> All instructions below are automatically applied to every Copilot Chat session.

---

## Workspace Purpose

An **AI-assisted SDLC workbench** covering the complete software development lifecycle:

1. **Requirements** — Analyze requirements, create Jira tickets
2. **Design** — Produce technical design documents
3. **Code Review** — Analyze code changes, enforce standards, detect security issues
4. **Testing** — Run tests, analyze coverage, generate BDD test cases
5. **Release** — Build, deploy, rollback, release notes
6. **Operations** — Monitor health, handle incidents, manage alerts

## Workspace Structure

```
.github/
├── copilot-instructions.md     ← YOU ARE HERE (system instructions, always-on)
├── instructions/               ← Conditional instructions (auto-apply by file type)
├── prompts/                    ← Reusable prompts (type / in Chat to invoke)
├── skills/                     ← Agent skills (auto-loaded when relevant)
│   ├── confluence-kit/         ← Confluence search & read
│   ├── jira-kit/               ← Jira ticket CRUD
│   ├── knowledge-base-kit/     ← Local KB search
│   ├── git-kit/                ← Git operations (diff, log, branch, checkout, add, commit)
│   ├── test-runner-kit/        ← Test execution, coverage, gap analysis
│   ├── code-review-kit/        ← Code review, standards check, security scan
│   ├── deploy-kit/             ← Build, deploy, rollback, status
│   └── monitor-kit/            ← Health, metrics, alerts, incident management
└── agents/                     ← Custom agents (select in Chat dropdown)
    ├── sdlc-orchestrator       ← Master orchestrator — end-to-end SDLC pipeline
    ├── requirement-analyst     ← Requirement analysis with handoffs
    ├── jira-creator            ← Jira ticket creation
    ├── knowledge-searcher      ← Cross-source knowledge search
    ├── tech-designer           ← Technical design documents
    ├── code-reviewer           ← Code review with automated analysis
    ├── test-engineer           ← Test execution and coverage
    ├── release-manager         ← Release and deployment management
    └── ops-responder           ← Production incident response
```

## How Skills Work

This workspace includes eight skills that Copilot automatically loads when relevant:

- **confluence-kit** — Activated when the user asks to search or read Confluence pages
- **jira-kit** — Activated when the user asks to create, search, or update Jira tickets
- **knowledge-base-kit** — Activated when the user asks about team documentation
- **git-kit** — Activated when the user asks about code changes, branches, commits, or git operations
- **test-runner-kit** — Activated when the user asks to run tests, check coverage, or find test gaps
- **code-review-kit** — Activated when the user asks for code review, PR analysis, or code quality checks
- **deploy-kit** — Activated when the user asks to deploy, build, rollback, or check deployment status
- **monitor-kit** — Activated when the user asks about system health, metrics, alerts, or incidents

Each skill contains a `SKILL.md` with usage instructions and a Python CLI tool.
Copilot will follow the instructions in the matched skill to execute the appropriate commands.

**Do NOT hardcode script paths in your responses.** Rely on the skills — they provide the exact commands and parameters.

## ⭐ SDLC Orchestrator (Recommended Starting Point)

The **sdlc-orchestrator** agent drives the complete end-to-end workflow:

```
Analyze Requirement → Create Jira Ticket → Setup Branch → Read Code →
Implement → Generate Tests → Code Review → Fix Issues → Commit
```

It pauses at each step for user confirmation (10 checkpoints total) and coordinates all skills automatically. Select **"SDLC Orchestrator"** from the Chat dropdown to start.

## SDLC Workflow (Agent Handoff Chain)

Individual agents can also be used independently via Handoff buttons:

```
requirement-analyst ──→ jira-creator ──→ tech-designer
       ↑                                      ↓
       │                               code-reviewer
       ↑                                      ↓
       │                               test-engineer
       ↑                                      ↓
       └──────── ops-responder ←── release-manager
```

**Back loops** (closing the loop):
- `code-reviewer` → `requirement-analyst` (clarification needed)
- `ops-responder` → `requirement-analyst` (incident-driven new requirements)

## Agent Behaviors

### When User Wants End-to-End Development
1. Select **sdlc-orchestrator** from the agent dropdown
2. It will guide through all 10 steps with checkpoints
3. Coordinates all skills automatically

### When User Asks to Search Knowledge
1. Determine scope: Confluence, local KB, or both
2. The relevant skill will provide the search commands — follow its instructions
3. Summarize results with source citations
4. Suggest refining the query if insufficient

### When User Asks for Requirement Analysis
1. Load team context from `knowledge-base/<team>/`
2. Analyze: functional + non-functional requirements, impact, acceptance criteria
3. Present for user review before creating tickets
4. Handoff options: create tickets, search more, or proceed to design

### When User Asks for Code Review
1. Use git-kit to gather changes
2. Use code-review-kit to analyze, check standards, scan security
3. Present findings by severity with actionable recommendations

### When User Asks About Deployment
1. Use deploy-kit to check status or build
2. ALWAYS dry-run first for production
3. ALWAYS get user confirmation before deploying

### When User Reports an Incident
1. Use monitor-kit to triage — check health, alerts, metrics
2. Use jira-kit to create incident ticket
3. For critical issues, handoff to ops-responder agent

## Important Rules

- **NEVER** expose API tokens, PATs, or credentials in output
- **NEVER** commit to main/master — always work on a feature branch
- **ALWAYS** confirm before creating Jira tickets or deploying to production (dry-run first)
- **ALWAYS** include Jira ticket key in commit messages — enforced by Git hook (`Refs: <TICKET-KEY>`)
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
| `/generate-bdd-tests` | Generate BDD (Given-When-Then) test cases |
| `/review-my-code` | Full code review with standards and security |
| `/check-pipeline` | Check CI/CD pipeline and deployment health |
| `/production-support` | Production incident workflow |
