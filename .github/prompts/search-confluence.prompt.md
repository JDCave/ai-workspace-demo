---
name: 'search-confluence'
description: 'Search company Confluence knowledge base and find wiki pages'
agent: 'agent'
tools: ['terminal']
---

# Search Confluence Knowledge Base

You are helping the user search the company Confluence knowledge base.

## Workflow

### Step 1: Clarify
Ask the user:
- What topic are you searching for?
- Do you know which Confluence space? (e.g., ENG, HR, OPS) — optional
- How many results do you need? (default: 10)

### Step 2: Execute Search
Use the **confluence-kit** skill to search Confluence. Follow the commands provided in the skill.

### Step 3: Present Results
Format each result as:
- **[Page Title]**(URL)
  - Space: `SPACE_KEY` | Last modified: YYYY-MM-DD
  - Excerpt: *...relevant snippet...*

### Step 4: Deep Dive (if user wants)
If the user wants to read a specific page, use the **confluence-kit** skill to read the full page content.

### Step 5: Cross-Reference
Also use the **knowledge-base-kit** skill to search the local knowledge base for related documents.
