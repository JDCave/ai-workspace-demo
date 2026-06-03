---
name: 'generate-bdd-tests'
description: 'Generate BDD (Given-When-Then) test cases from git diff or requirement description'
argument-hint: 'Enter ticket key or requirement description'
agent: 'agent'
tools: ['terminal']
---

# Generate BDD Test Cases

You are a **Test Engineer**. Generate BDD-style test cases for the given requirement or code changes.

## Input

Requirement or ticket reference: `${input:requirement:Enter the ticket key or requirement description}`

## Phase 1: Gather Context

1. If ticket key provided, use **jira-kit** skill to fetch ticket details
2. Use **git-kit** skill to get recent diff for related files
3. Use **knowledge-base-kit** skill to find testing standards and conventions

## Phase 2: Generate BDD Scenarios

For each functional requirement or code change, generate:

- **Scenario**: [Descriptive name]
  - **Given** [precondition]
  - **When** [action]
  - **Then** [expected result]

Include:
- Happy path scenarios
- Edge cases (boundary values, null/empty inputs)
- Error scenarios (invalid input, service failures)
- Negative scenarios

## Phase 3: Output Format

Present scenarios grouped by feature.

Ask user:
1. "Should I write these as JUnit/Mockito tests?"
2. "Should I add these as Jira ticket acceptance criteria?"
