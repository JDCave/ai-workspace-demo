---
name: jira-kit
description: Create, search, and manage Jira tickets. Use this when the user asks to create Jira tickets, search issues, add comments, or manage project tasks.
allowed-tools: shell
---

# Jira Integration Skill

You have access to a Python CLI tool for Jira ticket management.

## When to Use
- User wants to create a new Jira ticket (Story, Bug, Task, Epic)
- User wants to search existing Jira tickets by JQL
- User wants to add comments or update tickets
- After requirement analysis, user confirms creating Jira tickets

## Available Commands

### Create Ticket
```bash
python .github/skills/jira-kit/jira_tool.py create \
  --project <PROJECT_KEY> \
  --summary "<ticket summary>" \
  --description "<detailed description>" \
  --type <Story|Bug|Task|Epic|Sub-task> \
  [--labels "label1,label2"] \
  [--assignee <username>] \
  [--priority <Highest|High|Medium|Low|Lowest>]
```

**Parameters:**
- `--project` (required): Jira project key (e.g., PROJ, ENG, OPS)
- `--summary` (required): Brief summary (under 100 chars)
- `--description`: Full ticket description in Markdown
- `--type`: Issue type, default Story
- `--labels`: Comma-separated labels
- `--assignee`: Assignee username
- `--priority`: Priority level, default Medium

### Search Tickets
```bash
python .github/skills/jira-kit/jira_tool.py search --jql "<JQL query>" [--limit 20]
```

### Add Comment
```bash
python .github/skills/jira-kit/jira_tool.py comment --ticket <TICKET_KEY> --comment "<comment text>"
```

### Update Ticket
```bash
python .github/skills/jira-kit/jira_tool.py update --ticket <TICKET_KEY> --fields '{"field": "value"}'
```

## Ticket Description Templates

### Story
```
## Context
[Why this work is needed]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Technical Notes
[Implementation approach]
```

### Bug
```
## Bug Description
[What's wrong]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
[Environment details]
```

## Important Rules
- **ALWAYS** dry-run first: show the user a preview of the ticket before creating
- **ALWAYS** get user confirmation before executing the create command
- Generate well-structured descriptions using the templates above
- Report the created ticket key and URL after creation

## Configuration
Requires `.env` file with:
```
JIRA_BASE_URL=https://your-company.atlassian.net
JIRA_PAT=your_personal_access_token
JIRA_DEFAULT_PROJECT=PROJ
```
