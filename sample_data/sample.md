# Project Overview
This project is a modular web application designed to help users manage digital workflows. The application is built using a Python back-end with Flask and a React front-end.

## Architecture Summary
- **Backend**: Python (Flask), PostgreSQL
- **Frontend**: React, Redux
- **Authentication**: JWT with OAuth 2.0 support
- **Deployment**: Docker containers, deployed via GitHub Actions

---

# Coding Standards
## Python
- Follow PEP8 guidelines.
- All functions must include docstrings.
- Use type hints where possible.

## JavaScript/React
- Use functional components and React Hooks.
- Follow Airbnb ESLint rules.
- Use PropTypes or TypeScript for component validation.

---

# Sprint Workflow
- Sprints last two weeks.
- All tasks must be estimated in story points.
- Each sprint starts with a planning session and ends with a demo and retrospective.

## Ticket Lifecycle
1. Backlog grooming
2. Sprint planning
3. Development
4. Code review
5. QA verification
6. Done

---

# Code Review Policy
- At least one peer review required.
- Use GitHub pull requests with linked Jira tickets.
- PRs should contain:
  - Description of the change
  - Screenshots or test outputs
  - Reference to any breaking changes

---

# CI/CD Pipeline Rules
- Unit tests and lint checks must pass before merge.
- Builds run automatically on push to `main`.
- Artifacts are stored for 14 days in GitHub Actions.
- Production deploys only allowed from `release` branch.

---

# Testing Guidelines
- Use `pytest` for backend tests.
- Use `Jest` and `React Testing Library` for frontend.
- Maintain 80% code coverage.
- Include test plans in pull requests.

---

# Error Handling
- Use global error handler in Flask.
- Log exceptions with stack trace using `structlog`.
- Frontend should display user-friendly error messages.

---

# Feature Flags
- Use `launchdarkly` for controlled rollouts.
- Default all new features to `off` in production.

---

# API Standards
- Use RESTful conventions.
- All endpoints must return JSON.
- Use `snake_case` in keys and document each endpoint in Swagger.

---

# Deployment Checklist
1. Run unit and integration tests
2. Merge to `release` branch
3. Bump version in `version.txt`
4. Update `changelog.md`
5. Monitor logs post-deployment

---

# Security Practices
- Sanitize all user input
- Use HTTPS in all environments
- Apply rate-limiting on sensitive endpoints
- Rotate API keys every 90 days

---

# Onboarding New Developers
- Set up local dev environment using Docker Compose
- Review internal wiki on project architecture
- Complete the 3 onboarding tasks in Jira
- Attend a shadow code review session

---

# Common Questions

### What database migrations tool do we use?
We use Alembic for managing schema migrations in Python projects.

### How are environment variables managed?
All sensitive variables are stored in `.env` files. Production secrets are handled through GitHub Secrets.

### How do I rollback a deployment?
Use the `rollback` command in the deploy script. This restores the previous Docker image version.

### Can I work on weekends?
No. Unless approved by your team lead, all work must be scheduled during business hours.

---