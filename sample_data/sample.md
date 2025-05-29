# Project Overview

This project is a local AI assistant designed to help developers query internal documentation using natural language. It integrates Notion-based documentation with a locally run large language model via Ollama.

# Development Guidelines

- Follow PEP8 standards.
- All code must be commented and documented.
- Use `pytest` for unit testing.
- Do not hard-code credentials or API keys.

# Merge Policy

- Pull requests (PRs) must be reviewed by at least two team members.
- CI checks must pass before merging.
- All PRs must include a link to the related Jira ticket.

# Security Practices

- Only run models locally (no external API calls).
- Validate user input to avoid prompt injection attacks.
- Use a `config.yaml` to manage model settings securely.

# Weekly Summary - Week 4

- Completed basic CLI interface for user input.
- Integrated `ollama` CLI for local model access.
- Created initial version of `prompt_builder.py`.
