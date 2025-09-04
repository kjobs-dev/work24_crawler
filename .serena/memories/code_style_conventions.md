# Code Style and Conventions

## Python Style Guide
- **Follow PEP8** with specific project choices
- **Line length: 100 characters** (enforced by Ruff in pyproject.toml)
- **Use double quotes for strings**
- **Use trailing commas in multi-line structures**
- **Always use type hints** for function signatures and class attributes
- **Format with `ruff format`** (faster alternative to Black)

## Naming Conventions
- **Variables and functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private attributes/methods**: `_leading_underscore`
- **Type aliases**: `PascalCase`
- **Enum values**: `UPPER_SNAKE_CASE`

## Documentation Standards
- **Google-style docstrings** for all public functions, classes, and modules
- **Every module should have a docstring** explaining its purpose
- **Public functions must have complete docstrings**
- **Complex logic should have inline comments** with `# Reason:` prefix

## Code Structure Limits
- **Files: max 500 lines** - refactor by splitting into modules if approaching
- **Functions: max 50 lines** with single, clear responsibility
- **Classes: max 100 lines** representing a single concept
- **Organize code into clearly separated modules** by feature/responsibility

## Pydantic Models (v2)
- Use Pydantic v2 for data validation and settings management
- Models should mirror database fields exactly to eliminate mapping complexity
- Use `Field()` for validation constraints and metadata

## Error Handling
- Create custom exceptions for domain-specific errors
- Use specific exception handling with proper logging
- Implement fail-fast principle - check for errors early

## Development Philosophy
- **KISS**: Keep It Simple, Stupid - choose straightforward solutions
- **YAGNI**: You Aren't Gonna Need It - implement features only when needed
- **Single Responsibility**: Each function/class/module has one clear purpose
- **Dependency Inversion**: High-level modules depend on abstractions