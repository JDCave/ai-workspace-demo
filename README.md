# AI Workspace Demo

> An AI-assisted workspace built on VSCode Copilot native customization features. Supports Confluence search, local knowledge base retrieval, and requirement analysis with Jira ticket creation.

## 🎯 Purpose

In an enterprise environment where only VSCode/IDEA Copilot plugins are allowed, this workspace leverages **5 native VSCode Copilot customization mechanisms** to build Agent-like capabilities.

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
                               │                          │
                               ▼                          ▼
                        ┌──────────────────────────────────┐
                        │   Python scripts in each skill   │
                        │   Copilot executes via terminal   │
                        └──────┬──────────┬────────────────┘
                               ▼          ▼
                          Confluence    Jira
                           REST API    REST API
```

### 5 Native VSCode Copilot Customization Mechanisms

| # | Mechanism | Directory | Loading | Purpose |
|---|-----------|-----------|---------|---------|
| ① | **System Instructions** | `.github/copilot-instructions.md` | Always-On | Define agent role and behavior rules |
| ② | **Conditional Instructions** | `.github/instructions/*.instructions.md` | Auto-apply | Coding standards by file type |
| ③ | **Prompt Files** | `.github/prompts/*.prompt.md` | `/` trigger | Reusable prompt templates |
| ④ | **Agent Skills** | `.github/skills/*/SKILL.md` | Auto-match | Specialized capabilities (Confluence/Jira/KB) |
| ⑤ | **Custom Agents** | `.github/agents/*.agent.md` | Chat dropdown | Custom roles with Handoff workflows |

## 📁 Directory Structure

```
ai-workspace-demo/
├── .github/
│   ├── copilot-instructions.md               # ① System instructions (Always-On)
│   ├── instructions/
│   │   └── python-tools.instructions.md      # ② Conditional instructions
│   ├── prompts/                              # ③ Prompt templates
│   │   ├── search-confluence.prompt.md
│   │   ├── search-knowledge-base.prompt.md
│   │   ├── analyze-requirement.prompt.md
│   │   ├── create-jira-ticket.prompt.md
│   │   └── production-support.prompt.md
│   ├── skills/                               # ④ Agent Skills (self-contained)
│   │   ├── confluence-kit/
│   │   │   ├── SKILL.md                      #   Usage instructions
│   │   │   └── confluence_tool.py            #   Python script (mock)
│   │   ├── jira-kit/
│   │   │   ├── SKILL.md
│   │   │   └── jira_tool.py
│   │   └── knowledge-base-kit/
│   │       ├── SKILL.md
│   │       └── kb_tool.py
│   └── agents/                               # ⑤ Custom Agents
│       ├── requirement-analyst.agent.md      #   Analysis → Handoff → Jira
│       ├── jira-creator.agent.md
│       └── knowledge-searcher.agent.md
├── knowledge-base/                           # Local knowledge repository
│   ├── team-alpha/{architecture,runbooks,meeting-notes}/
│   ├── team-beta/{architecture,runbooks,meeting-notes}/
│   └── shared/{templates,guidelines}/
├── .vscode/
├── .env.example
└── README.md
```

## 🚀 Quick Start

```bash
git clone <repo> ai-workspace-demo && cd ai-workspace-demo
cp .env.example .env  # Fill in Confluence/Jira server URL and PAT
pip install python-dotenv
code .                # Open in VSCode
```

### Usage

Open Copilot Chat in VSCode (`Ctrl+Alt+I`, Agent Mode):

#### Option 1: Trigger Prompts via `/`
```
/search-confluence          → Search Confluence
/search-knowledge-base      → Search local knowledge base
/analyze-requirement        → Requirement analysis
/create-jira-ticket         → Create Jira ticket
/production-support         → Production incident response
```

#### Option 2: Select a Custom Agent
Choose from the Chat input dropdown:
- **Requirement Analyst** — Analyze requirements, then Handoff to Jira Creator
- **Jira Creator** — Create tickets directly
- **Knowledge Searcher** — Cross-source search

#### Option 3: Natural Language
```
@workspace Search Confluence for "New Joiner Guide"
@workspace Analyze requirement: Add OAuth2 SSO to the User Service
```
Copilot auto-matches the relevant skill based on your query.

## 🔌 Replace Mock with Real APIs

### Using your existing confluence-kit and jira-kit
1. Place kit code into `.github/skills/confluence-kit/lib/` and `.github/skills/jira-kit/lib/`
2. Edit `confluence_tool.py` / `jira_tool.py` — import kit and replace `mock_*` functions
3. CLI interface stays the same — `.github/skills/` and `.github/prompts/` require no changes

## 📝 Feature Matrix

| Scenario | How to Use |
|----------|-----------|
| Search Confluence | `/search-confluence` or skill auto-match |
| Search local docs | `/search-knowledge-base` or `@workspace` |
| Requirement → Ticket | Select **Requirement Analyst** Agent (with Handoff) |
| Create ticket directly | `/create-jira-ticket` or **Jira Creator** Agent |
| Production incident | `/production-support` |
| Edit Python scripts | Conditional instructions auto-apply |

## 🔧 Extension Guide

### Add a New Skill
1. Create `.github/skills/<skill-name>/SKILL.md`
2. Include YAML frontmatter: `name`, `description`, `allowed-tools`
3. Add scripts in the same directory — Copilot auto-discovers all files

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
- Jira creation always requires dry-run confirmation
