---
name: 'search-knowledge-base'
description: 'Search local team knowledge base documents'
agent: 'agent'
tools: ['terminal']
---

# Search Local Knowledge Base

You are helping the user search the local team knowledge base (`knowledge-base/` directory).

## Workflow

### Step 1: Clarify
Ask the user:
- What topic are you searching for?
- Which team? (team-alpha, team-beta, shared, or all) — default: all
- Looking for a specific document type? (architecture, runbooks, meeting-notes, guidelines)

### Step 2: Execute Search
Use the **knowledge-base-kit** skill to search local documentation. Follow the commands provided in the skill.

You can also list all documents for a team if the user wants to browse.

### Step 3: Present Results
Format each result as:
- **Document title** (`knowledge-base/team-xxx/path/file.md`)
  - Relevance: N | Snippet: *...matching context...*

### Step 4: Read Full Document
If the user wants to see a specific document, read the file directly from the workspace and present it formatted.

### Step 5: Suggest Related
Based on results, suggest related documents that might also be relevant.
