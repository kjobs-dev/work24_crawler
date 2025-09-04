# Essential Development Commands

## Package Management (UV)
```bash
# Sync dependencies
uv sync

# Add a package (NEVER update pyproject.toml directly)
uv add package_name

# Add development dependency
uv add --dev package_name

# Remove a package
uv remove package_name

# Run commands in virtual environment
uv run python script.py
```

## Running the Crawler
```bash
# Run the job crawler
uv run python src/main.py

# Note: Site selection and search filters are configured in src/main.py
```

## Testing Commands
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Run specific tests with verbose output
uv run pytest tests/test_module.py -v
```

## Code Quality Commands (MUST RUN AFTER ANY CHANGES)
```bash
# Format code (required before commit)
uv run ruff format .

# Check linting (required before commit)
uv run ruff check .

# Fix linting issues automatically
uv run ruff check --fix .

# Type checking (required before commit)
uv run mypy src/
```

## Environment Setup
```bash
# Copy environment configuration
cp .env.example .env
# Edit .env with your credentials

# Always use the virtual environment for Python commands
source .venv/bin/activate  # or use uv run
```

## System Commands (Linux-specific)
- Standard Unix commands: `ls`, `cd`, `grep`, `find`, `git`
- **CRITICAL**: Always use `rg` (ripgrep) instead of `grep` for better performance
- Use `tree` for directory structure visualization