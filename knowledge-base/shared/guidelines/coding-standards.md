# Coding Standards & Design Guidelines

## General Principles
1. Follow SOLID principles
2. Prefer composition over inheritance
3. Write self-documenting code — comments explain "why", not "what"
4. All public APIs must have OpenAPI documentation
5. Minimum 80% unit test coverage for new code

## API Design
- Use RESTful conventions (unless event-driven is more appropriate)
- Response format: JSON with consistent envelope `{ "data": ..., "meta": ..., "errors": ... }`
- Error codes: Follow RFC 7807 (Problem Details)
- Pagination: Cursor-based for large datasets, offset for small datasets
- Versioning: URL-based (`/api/v1/`, `/api/v2/`)

## Code Review Checklist
- [ ] Meets acceptance criteria
- [ ] No security vulnerabilities (SQL injection, XSS, etc.)
- [ ] Proper error handling and logging
- [ ] Performance considerations (N+1 queries, caching)
- [ ] Backward compatibility maintained
- [ ] Documentation updated

## Git Workflow
- Branch naming: `feature/<ticket-key>-<brief-description>`
- Commit messages: `type(<scope>): description` (Conventional Commits)
- Squash merge to main
- Minimum 2 approvals before merge

## Technology Stack Defaults
| Layer | Technology | Version |
|-------|-----------|---------|
| Backend (JVM) | Java + Spring Boot | 17 / 3.x |
| Backend (Python) | Python + FastAPI | 3.11+ |
| Frontend | React + TypeScript | 18 / 5.x |
| Database (RDBMS) | PostgreSQL | 15+ |
| Database (NoSQL) | MongoDB | 7+ |
| Cache | Redis | 7+ |
| Message Queue | Apache Kafka | 3.x |
| Container Runtime | Docker + Kubernetes | Latest LTS |
