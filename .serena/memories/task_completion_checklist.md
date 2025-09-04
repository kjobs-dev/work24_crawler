# Task Completion Checklist

## MANDATORY Steps After Any Code Changes

### 1. Code Quality Checks (REQUIRED)
```bash
# Format code - MUST run
uv run ruff format .

# Check linting - MUST run  
uv run ruff check .

# Fix linting issues if any
uv run ruff check --fix .

# Type checking - MUST run
uv run mypy src/
```

### 2. Testing (REQUIRED)
```bash
# Run all tests - MUST pass
uv run pytest

# Run with coverage if needed
uv run pytest --cov=src --cov-report=html
```

### 3. Virtual Environment Usage
- **ALWAYS use `uv run`** for Python commands
- **Use `.venv` virtual environment** for all Python operations
- **Never run Python commands outside the virtual environment**

## Pre-Commit Verification
1. All tests must pass
2. Ruff formatting must be applied
3. Ruff linting must pass with no errors
4. MyPy type checking must pass
5. Code follows project conventions from CLAUDE.md

## Crawler-Specific Considerations
- **Test with small result sets first** (max_results=5-10)
- **Verify anti-detection measures** are working (delays, human behavior)
- **Check Excel output formatting** if modifying export functionality
- **Ensure credentials are not committed** to version control

## File Limits Check
- Files should not exceed 500 lines
- Functions should not exceed 50 lines  
- Classes should not exceed 100 lines
- Consider refactoring if approaching these limits

## Documentation Updates
- Update docstrings for any modified public functions/classes
- Keep CLAUDE.md updated with new patterns or dependencies
- Update README.md if adding new features or changing setup