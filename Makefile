.DEFAULT_GOAL := help

.PHONY: help sync install test lint format bump

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

sync: ## Install all dependencies and the package in editable mode
	uv sync

install: sync ## Install pre-commit hooks
	uv run pre-commit install

test: ## Run tests with coverage
	uv run pytest

lint: ## Lint and auto-fix with ruff
	uv run ruff check --fix .
	uv run ruff format .

commit: ## Interactive conventional commit prompt
	uv run cz commit

bump: ## Bump version based on commit history
	uv run cz bump

bump-dry: ## Preview next version bump without applying
	uv run cz bump --dry-run
