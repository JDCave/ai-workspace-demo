# AI Workspace Demo

> An AI-assisted SDLC workbench built on VSCode Copilot native customization features. Covers the **full Software Development Lifecycle** — from requirements to operations — with 8 skills, 8 agents, and 8 prompt commands.

## 🎯 Purpose

In an enterprise environment where only VSCode/IDEA Copilot plugins are allowed, this workspace leverages **5 native VSCode Copilot customization mechanisms** to build Agent-like capabilities across the entire SDLC.

**No MCP required.** No extra extensions needed.

## 🏗️ Architecture

```
                    VSCode Copilot Chat (Agent Mode)
                               │
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
    ▼                          ▼                          ▼
┌────────────┐         ┌─────────────┐           ┌─────────────┐
│ ① System   │         │ ② Condition │           │ ③ Prompts   │
│ Instructions│        │ Instructions│           │ / command   │
│ Always-On  │         │ Auto-apply  │           │ One-shot    │
└────────────┘         └─────────────┘           └─────────────┘

    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
    ▼                          ▼                          ▼
┌────────────┐         ┌─────────────┐           ┌─────────────┐
│ ④ Skills   │         │ ⑤ Agents    │           │ ⑥ Knowledge │
│ Auto-loaded│         │ Custom roles│           │ @workspace  │
│ SKILL.md   │         │ Handoffs    │           │ Markdown    │
└────────────┘         └─────────────┘           └─────────────┘
        │                      │
        ▼                      ▼
  ┌───────────────────────────────────┐
  │ Python scripts live INSIDE skills │
  │ Copilot executes via terminal     │
  └──────┬──────┬──────┬─────────────┘
         ▼      ▼      ▼
    Confluence  Jira  Git / CI/CD / Monitoring
```

### 5 Native VSCode Copilot Customization Mechanisms

| # | Mechanism | Directory | Loading | Purpose |
|---|-----------|-----------|---------|---------|
| ① | **System Instructions** | `.github/copilot-instructions.md` | Always-On | Define agent role and SDLC workflow |
| ② | **Conditional Instructions** | `.github/instructions/*.instructions.md` | Auto-apply | Coding standards by file type |
| ③ | **Prompt Files** | `.github/prompts/*.prompt.md` | `/` trigger | Reusable prompt templates |
| ④ | **Agent Skills** | `.github/skills/*/SKILL.md` | Auto-match | Specialized capabilities |
| ⑤ | **Custom Agents** | `.github/agents/*.agent.md` | Chat dropdown | Custom roles with Handoff workflows |

## 🔄 SDLC Workflow

Agents are connected via **Handoff chains** forming a complete SDLC pipeline with feedback loops:

```
requirement-analyst ──→ jira-creator ──→ tech-designer
       ↑                                    ↓
       │                             code-reviewer
       ↑                                    ↓
       │                             test-engineer
       ↑                                    ↓
       └──────── ops-responder ←── release-manager
```

**Back loops** close the SDLC:
- `code-reviewer` → `requirement-analyst` (requirement clarification)
- `ops-responder` → `requirement-analyst` (incident-driven new requirements)

## 📁 Directory Structure

```
ai-workspace-demo/
├── .github/
│   ├── copilot-instructions.md               # ① System instructions (Always-On)
│   ├── instructions/
│   │   └── python-tools.instructions.md      # ② Conditional instructions
│   ├── prompts/                              # ③ Prompt templates (type / in Chat)
│   │   ├── search-confluence.prompt.md       #   Search Confluence wikis
│   │   ├── search-knowledge-base.prompt.md   #   Search local team docs
│   │   ├── analyze-requirement.prompt.md     #   Structured requirement analysis
│   │   ├── create-jira-ticket.prompt.md      #   Create Jira tickets
│   │   ├── generate-bdd-tests.prompt.md      #   Generate BDD test cases
│   │   ├── review-my-code.prompt.md          #   Full code review
│   │   ├── check-pipeline.prompt.md          #   CI/CD pipeline health check
│   │   └── production-support.prompt.md      #   Production incident workflow
│   ├── skills/                               # ④ Agent Skills (self-contained)
│   │   ├── confluence-kit/                   #   Confluence search & read
│   │   │   ├── SKILL.md
│   │   │   └── confluence_tool.py
│   │   ├── jira-kit/                         #   Jira ticket CRUD
│   │   │   ├── SKILL.md
│   │   │   └── jira_tool.py
│   │   ├── knowledge-base-kit/               #   Local KB search
│   │   │   ├── SKILL.md
│   │   │   └── kb_tool.py
│   │   ├── git-kit/                          #   Git operations
│   │   │   ├── SKILL.md
│   │   │   └── git_tool.py
│   │   ├── test-runner-kit/                  #   Test execution & coverage
│   │   │   ├── SKILL.md
│   │   │   └── test_tool.py
│   │   ├── code-review-kit/                  #   Code review & security scan
│   │   │   ├── SKILL.md
│   │   │   └── review_tool.py
│   │   ├── deploy-kit/                       #   Build, deploy, rollback
│   │   │   ├── SKILL.md
│   │   │   └── deploy_tool.py
│   │   └── monitor-kit/                      #   Health, metrics, alerts
│   │       ├── SKILL.md
│   │       └── monitor_tool.py
│   └── agents/                               # ⑤ Custom Agents
│       ├── requirement-analyst.agent.md      #   Requirements → Design → Jira
│       ├── jira-creator.agent.md             #   Jira ticket creation
│       ├── knowledge-searcher.agent.md       #   Cross-source knowledge search
│       ├── tech-designer.agent.md            #   Technical design documents
│       ├── code-reviewer.agent.md            #   Code review & analysis
│       ├── test-engineer.agent.md            #   Test execution & coverage
│       ├── release-manager.agent.md          #   Release & deployment
│       └── ops-responder.agent.md            #   Incident response
├── knowledge-base/                           # Local knowledge repository
│   ├── team-alpha/{architecture,runbooks,meeting-notes}/
│   ├── team-beta/{architecture,runbooks,meeting-notes}/
│   └── shared/{templates,guidelines}/
├── docs/                                     # Documentation
├── .vscode/
├── .env.example
└── README.md
```

## 🚀 Quick Start

```bash
git clone <repo> ai-workspace-demo && cd ai-workspace-demo
cp .env.example .env  # Fill in credentials (Confluence/Jira/Git URLs and PATs)
pip install python-dotenv
code .                # Open in VSCode
```

### Usage

Open Copilot Chat in VSCode (`Ctrl+Alt+I`, Agent Mode):

#### Option 1: Trigger Prompts via `/`

```
/search-confluence          → Search Confluence
/search-knowledge-base      → Search local knowledge base
/analyze-requirement        → Structured requirement analysis
/create-jira-ticket         → Create Jira ticket
/generate-bdd-tests         → Generate BDD (Given-When-Then) test cases
/review-my-code             → Full code review with standards & security checks
/check-pipeline             → CI/CD pipeline and deployment health check
/production-support         → Production incident response
```

#### Option 2: Select a Custom Agent

Choose from the Chat input dropdown to start a **multi-step Handoff workflow**:

| Agent | Role | Handoff → |
|-------|------|-----------|
| **Requirement Analyst** | Analyze requirements with team context | → Jira Creator → Tech Designer |
| **Jira Creator** | Create structured Jira tickets | → Tech Designer |
| **Knowledge Searcher** | Cross-source search (KB + Confluence) | — |
| **Tech Designer** | Produce technical design documents | → Code Reviewer |
| **Code Reviewer** | Analyze code changes, detect issues | → Test Engineer |
| **Test Engineer** | Run tests, analyze coverage | → Release Manager |
| **Release Manager** | Build, deploy, rollback | → Ops Responder |
| **Ops Responder** | Incident response, monitoring | → Requirement Analyst (loop-back) |

#### Option 3: Natural Language

```
@workspace Search Confluence for "New Joiner Guide"
@workspace Analyze requirement: Add OAuth2 SSO to the User Service
@workspace Review my code against the main branch
@workspace Check deployment status in staging
@workspace What active alerts are there in production?
```

Copilot auto-matches the relevant skill based on your query.

## 📝 Feature Matrix

| Scenario | How to Use | SDLC Phase |
|----------|-----------|------------|
| Search Confluence | `/search-confluence` or skill auto-match | All phases |
| Search local docs | `/search-knowledge-base` or `@workspace` | All phases |
| Requirement → Ticket | Select **Requirement Analyst** Agent (with Handoff) | Requirements |
| Create ticket directly | `/create-jira-ticket` or **Jira Creator** Agent | Requirements |
| Technical design | Select **Tech Designer** Agent | Design |
| Code review | `/review-my-code` or **Code Reviewer** Agent | Code Review |
| Generate BDD tests | `/generate-bdd-tests` | Testing |
| Run tests & coverage | **Test Engineer** Agent | Testing |
| Check pipeline health | `/check-pipeline` | Release |
| Deploy / Rollback | **Release Manager** Agent | Release |
| Production incident | `/production-support` or **Ops Responder** Agent | Operations |
| Monitor health & alerts | **Ops Responder** Agent | Operations |

## 🔌 Replace Mock with Real APIs

All skill scripts ship with **mock data** by default. To connect to real services:

1. Place your kit code into `.github/skills/<skill-name>/lib/`
2. Edit the corresponding `*_tool.py` — import kit and replace `mock_*` functions
3. CLI interface stays the same — no changes needed to skills, prompts, or agents
4. Update `.env` with real credentials

Currently supported mock endpoints:
- Confluence REST API
- Jira REST API
- Git CLI
- Test runners (JUnit, pytest)
- Code analysis tools (SonarQube, CodeClimate)
- CI/CD platforms (Jenkins, GitHub Actions)
- Monitoring platforms (Datadog, Prometheus)

## 📊 Asset Inventory

| Type | Count | Details |
|------|-------|---------|
| **Skills** | 8 | confluence-kit, jira-kit, knowledge-base-kit, git-kit, test-runner-kit, code-review-kit, deploy-kit, monitor-kit |
| **Agents** | 8 | requirement-analyst, jira-creator, knowledge-searcher, tech-designer, code-reviewer, test-engineer, release-manager, ops-responder |
| **Prompts** | 8 | /search-confluence, /search-knowledge-base, /analyze-requirement, /create-jira-ticket, /generate-bdd-tests, /review-my-code, /check-pipeline, /production-support |
| **Instructions** | 2 | copilot-instructions.md (system), python-tools.instructions.md (conditional) |

## 🔧 Extension Guide

### Add a New Skill
1. Create `.github/skills/<skill-name>/SKILL.md`
2. Include YAML frontmatter: `name`, `description`, `allowed-tools`
3. Add Python scripts in the same directory — Copilot auto-discovers all files

### Add a New Agent
1. Create `.github/agents/<name>.agent.md`
2. Define frontmatter: `tools`, `handoffs`
3. Chain with other agents via Handoffs

### Add a New Prompt
1. Create `.github/prompts/<name>.prompt.md`
2. Trigger in Chat via `/`

## 🔒 Security

- `.env` is in `.gitignore` — never committed
- PAT/Tokens stored locally in `.env` only
- Jira creation and production deployment always require dry-run confirmation
