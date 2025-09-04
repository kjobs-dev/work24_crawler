# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Selenium-based job crawler** designed to scrape job postings from major job sites (LinkedIn, Indeed) while mimicking human behavior to avoid detection. The crawler logs in, applies filters, searches for jobs, extracts detailed information, and exports results to Excel.

### Key Features
- **Stealth Crawling**: Anti-detection with undetected-chromedriver
- **Human Behavior Simulation**: Random delays, mouse movements, typing patterns
- **Multi-site Support**: LinkedIn and Indeed (extensible)
- **Smart Authentication**: Login with popup/banner handling
- **Advanced Filtering**: Job type, location, experience, salary, date filters
- **Detailed Data Extraction**: Job descriptions, requirements, benefits, skills
- **Excel Export**: Professional reports with statistics and formatting

## Core Development Philosophy

### KISS (Keep It Simple, Stupid)

Simplicity should be a key goal in design. Choose straightforward solutions over complex ones whenever possible. Simple solutions are easier to understand, maintain, and debug.

### YAGNI (You Aren't Gonna Need It)

Avoid building functionality on speculation. Implement features only when they are needed, not when you anticipate they might be useful in the future.

### Design Principles

- **Dependency Inversion**: High-level modules should not depend on low-level modules. Both should depend on abstractions.
- **Open/Closed Principle**: Software entities should be open for extension but closed for modification.
- **Single Responsibility**: Each function, class, and module should have one clear purpose.
- **Fail Fast**: Check for potential errors early and raise exceptions immediately when issues occur.

## 🧱 Code Structure & Modularity

### File and Function Limits

- **Never create a file longer than 500 lines of code**. If approaching this limit, refactor by splitting into modules.
- **Functions should be under 50 lines** with a single, clear responsibility.
- **Classes should be under 100 lines** and represent a single concept or entity.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Line lenght should be max 100 characters** ruff rule in pyproject.toml
- **Use venv_linux** (the virtual environment) whenever executing Python commands, including for unit tests.

### Project Architecture

**Selenium Job Crawler Architecture:**

```
src/crawler/
    __init__.py
    main_crawler.py          # Main orchestrator - coordinates entire crawl process
    
    core/                    # Core crawler functionality
        __init__.py
        base_crawler.py      # StealthCrawler - undetected Chrome setup & stealth features
        auth.py             # AuthenticationManager - handles login for different sites
        search_engine.py    # SearchEngine - applies filters and navigates search pages
        job_extractor.py    # JobExtractor - extracts job data from listings and detail pages
        config.py           # Settings (CrawlerSettings) and site configs (JobSiteConfig)
        models.py           # Pydantic models: JobListing, SearchFilters, CrawlerSession
        
    utils/                  # Utility modules
        __init__.py
        human_behavior.py   # HumanBehaviorSimulator - anti-detection behaviors
        excel_exporter.py   # ExcelExporter - exports jobs to formatted Excel files
        
    sites/                  # Site-specific implementations (future)
        __init__.py
        
output/                     # Generated Excel files
logs/                      # Log files
.env                       # Environment variables (credentials, settings)
```

**Key Classes:**
- `StealthCrawler`: Main browser controller with anti-detection
- `AuthenticationManager`: Site-specific login handling
- `SearchEngine`: Search and filter application
- `JobExtractor`: Data extraction from job pages
- `HumanBehaviorSimulator`: Human-like behavior patterns
- `ExcelExporter`: Excel report generation

## 🛠️ Development Environment

### UV Package Management

This project uses UV for blazing-fast Python package and environment management.

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Sync dependencies
uv sync

# Add a package ***NEVER UPDATE A DEPENDENCY DIRECTLY IN PYPROJECT.toml***
# ALWAYS USE UV ADD
uv add requests

# Add development dependency
uv add --dev pytest ruff mypy

# Remove a package
uv remove requests

# Run commands in the environment
uv run python script.py
uv run pytest
uv run ruff check .

# Install specific Python version
uv python install 3.12
```

### Crawler Commands

```bash
# Install dependencies
uv sync

# Run the job crawler
uv run python src/main.py

# Run with specific site (modify main.py)
# Available sites: "linkedin", "indeed"

# Set up environment
cp .env.example .env
# Edit .env with your job site credentials

# Install Chrome (if not present)
# Ubuntu/Debian: sudo apt-get install google-chrome-stable
# macOS: brew install --cask google-chrome
```

### Development Commands

```bash
# Run all tests
uv run pytest

# Run specific tests with verbose output
uv run pytest tests/test_module.py -v

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Fix linting issues automatically
uv run ruff check --fix .

# Type checking
uv run mypy src/

# Run pre-commit hooks
uv run pre-commit run --all-files
```

## 📋 Style & Conventions

### Python Style Guide

- **Follow PEP8** with these specific choices:
  - Line length: 100 characters (set by Ruff in pyproject.toml)
  - Use double quotes for strings
  - Use trailing commas in multi-line structures
- **Always use type hints** for function signatures and class attributes
- **Format with `ruff format`** (faster alternative to Black)
- **Use `pydantic` v2** for data validation and settings management

### Docstring Standards

Use Google-style docstrings for all public functions, classes, and modules:

```python
def calculate_discount(
    price: Decimal,
    discount_percent: float,
    min_amount: Decimal = Decimal("0.01")
) -> Decimal:
    """
    Calculate the discounted price for a product.

    Args:
        price: Original price of the product
        discount_percent: Discount percentage (0-100)
        min_amount: Minimum allowed final price

    Returns:
        Final price after applying discount

    Raises:
        ValueError: If discount_percent is not between 0 and 100
        ValueError: If final price would be below min_amount

    Example:
        >>> calculate_discount(Decimal("100"), 20)
        Decimal('80.00')
    """
```

### Naming Conventions

- **Variables and functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private attributes/methods**: `_leading_underscore`
- **Type aliases**: `PascalCase`
- **Enum values**: `UPPER_SNAKE_CASE`

## 🧪 Testing Strategy

### Test-Driven Development (TDD)

1. **Write the test first** - Define expected behavior before implementation
2. **Watch it fail** - Ensure the test actually tests something
3. **Write minimal code** - Just enough to make the test pass
4. **Refactor** - Improve code while keeping tests green
5. **Repeat** - One test at a time

### Testing Best Practices

```python
# Always use pytest fixtures for setup
import pytest
from datetime import datetime

@pytest.fixture
def sample_user():
    """Provide a sample user for testing."""
    return User(
        id=123,
        name="Test User",
        email="test@example.com",
        created_at=datetime.now()
    )

# Use descriptive test names
def test_user_can_update_email_when_valid(sample_user):
    """Test that users can update their email with valid input."""
    new_email = "newemail@example.com"
    sample_user.update_email(new_email)
    assert sample_user.email == new_email

# Test edge cases and error conditions
def test_user_update_email_fails_with_invalid_format(sample_user):
    """Test that invalid email formats are rejected."""
    with pytest.raises(ValidationError) as exc_info:
        sample_user.update_email("not-an-email")
    assert "Invalid email format" in str(exc_info.value)
```

### Test Organization

- Unit tests: Test individual functions/methods in isolation
- Integration tests: Test component interactions
- End-to-end tests: Test complete user workflows
- Keep test files next to the code they test
- Use `conftest.py` for shared fixtures
- Aim for 80%+ code coverage, but focus on critical paths

## ⚠️ CURRENT DEVELOPMENT STATUS - BATCH SAVING FEATURE

### 🚧 INCOMPLETE IMPLEMENTATION DETECTED

**CRITICAL NOTE**: The codebase contains a **partially implemented batch saving feature** that was interrupted during development. The system was implementing the ability to save jobs in batches of 10 to prevent data loss during long crawling sessions.

#### Current Implementation Status

**✅ COMPLETED Components:**
1. **ExcelExporter.save_incremental_batch()** - Method for saving job batches incrementally
2. **ExcelExporter._append_to_excel()** - Method for appending data to existing Excel files
3. **ExcelExporter.export_jobs()** - Enhanced with `append_mode` parameter support

**❌ MISSING Implementation:** ~~COMPLETED~~
1. ~~**Batch logic in main crawler**~~ - ✅ `_crawl_all_pages()` method now uses configurable batch saving
2. ~~**No periodic saves**~~ - ✅ Jobs saved every N jobs (configurable batch size)
3. ~~**Batch counter management**~~ - ✅ Full tracking with batch numbers and incremental saves
4. ✅ **BONUS: Duplicate detection** - Automatically skips duplicate job IDs within session and across sessions

#### Required Implementation Steps

```python
# In JobCrawler._crawl_all_pages(), need to add:
BATCH_SIZE = 10
batch_jobs = []
batch_num = 1
base_filename = None

# After each job extraction:
if detailed_job:
    batch_jobs.append(detailed_job)
    
    # Save every 10 jobs
    if len(batch_jobs) >= BATCH_SIZE:
        if batch_num == 1:
            # First batch - create new file
            excel_path = exporter.save_incremental_batch(
                batch_jobs, batch_num, base_filename, is_first_batch=True
            )
            base_filename = excel_path.stem  # Store base name
        else:
            # Subsequent batches - append
            exporter.save_incremental_batch(
                batch_jobs, batch_num, base_filename, is_first_batch=False
            )
        
        batch_jobs = []  # Clear batch
        batch_num += 1
```

#### Enhanced Safety Benefits
- **Data Loss Prevention**: Maximum loss is now `batch_size - 1` jobs (default: 9) instead of entire session
- **Memory Efficiency**: Reduces memory footprint during long crawls
- **Progress Tracking**: Users see incremental progress in Excel files during crawling
- **Duplicate Prevention**: Automatically skips duplicate job IDs within session and across sessions
- **Single File Per Session**: Each crawl creates one timestamped Excel file (e.g., `work24_채용정보_20250903_142530.xlsx`)
- **Cross-Session Awareness**: Loads existing job IDs from recent Excel files for duplicate detection
- **Configurable Batch Size**: Default 10, customizable via `BATCH_SAVE_SIZE` environment variable

#### Files Requiring Updates
- `src/crawler/main_crawler.py` - Add batch saving logic to `_crawl_all_pages()`
- Consider adding batch size to `CrawlerSettings` in `config.py`

**⚠️ IMPORTANT**: The current code will lose ALL crawled data if interrupted, as it only saves at the very end!

## 🔧 WORK24 LOGIN ISSUE & FIX

### 🚨 Issue Identified
Work24 Korean job site shows a **success confirmation popup** after login:
```
Alert Text: 로그인 성공하였습니다.
민원신청 서비스 이용시 상향된 본인인증 방식으로 재 인증이 필요할 수 있습니다.
```

The previous code treated this **success alert as a failure** due to poor alert handling timing.

### ✅ Fix Implemented
**Updated `AuthenticationManager._standard_login()` in `src/crawler/core/auth.py`:**

1. **Immediate Alert Check**: Check for alerts immediately after clicking login button
2. **Success Keywords**: Flexible success detection with keywords: `["성공", "Success", "로그인 성공", "성공하였습니다"]`
3. **Proper Alert Handling**: Accept success alerts and continue, only fail on actual error messages
4. **Fallback Logic**: If alert handling fails, fall back to standard verification

### 🔍 Key Changes
- **Before**: Alert caused `UnexpectedAlertPresentException` → Login failure
- **After**: Success alert properly detected → Alert dismissed → Login success

### 🧪 Testing
```bash
# Test Work24 login specifically
uv run python src/main.py
# Select option 3 (Work24)
# Set custom output directory
# Verify login succeeds without alert errors
```

## 📁 USER OUTPUT DIRECTORY SELECTION

### 🎯 Feature Added
Users can now **set a custom output directory** for Excel files during crawler startup.

### 🔧 Implementation Details
**Location**: Asked after credentials, before search keywords
**Cross-Platform Support**: Windows, Mac, Linux compatible
**Features**:
- **Path Examples**: Shows platform-specific examples
- **Home Directory Expansion**: Handles `~/Desktop/folder` on Mac/Linux  
- **Permission Testing**: Verifies write access before proceeding
- **Directory Creation**: Auto-creates directories if they don't exist
- **Default Fallback**: Uses `./output` if user presses Enter
- **Error Handling**: Retries on invalid paths or permission errors

### 🖥️ User Experience
```
📁 Excel 파일 저장 경로를 설정하세요:
💡 팁: 경로 예시:
   Windows: C:\Users\사용자명\Desktop\채용공고
   Mac/Linux: /Users/사용자명/Desktop/채용공고 또는 ~/Desktop/채용공고
   현재 폴더: . (점 하나)

📂 저장 경로를 입력하세요 (엔터 = 현재 폴더의 output): ~/Desktop/jobs
✅ 설정된 경로: /Users/username/Desktop/jobs
✅ 경로 확인 완료! 파일 저장 가능합니다.
```

## 📦 WINDOWS EXECUTABLE CREATION

### 🎯 Windows .exe File Generation
The project includes complete build tools to create a **standalone Windows executable** with the AI-noye logo.

### 🛠️ Build Files Created
- **`build_exe.spec`**: PyInstaller configuration with AI-noye logo
- **`build_exe.py`**: Cross-platform build script  
- **`build_exe.bat`**: Windows batch file for easy building
- **`build_exe.sh`**: Linux/Mac shell script for building

### 🏗️ How to Build
#### **On Windows:**
```cmd
REM Double-click or run in cmd
build_exe.bat
```

#### **On Linux/Mac:**
```bash
# Make executable and run
chmod +x build_exe.sh
./build_exe.sh
```

#### **Manual Build:**
```bash
# Install dependencies and run build script
uv sync
uv run python build_exe.py
```

### 📂 Build Output
```
release/
├── AI-noye_Job_Crawler.exe    # Main executable (Windows)
├── ai-noye-logo.png          # Company logo
└── README.txt                # User instructions
```

### 🎨 Features of the Executable
- **Custom Icon**: Uses `ai-noye-logo.png` as the executable icon
- **Single File**: All dependencies bundled (no installation needed)
- **Size**: ~52MB standalone executable
- **Console App**: Interactive terminal interface
- **Auto-detects Chrome**: Uses installed Chrome browser
- **Cross-platform Build**: Can be built on Linux/Mac/Windows

### 📋 Build Requirements
- **Python 3.11+** with UV package manager
- **PyInstaller 6.15+** (auto-installed)
- **AI-noye logo** (`ai-noye-logo.png` in root directory)

### 🚀 Distribution
The `release/` folder contains everything needed for distribution:
1. Copy the entire `release/` folder to target machine
2. User double-clicks `AI-noye_Job_Crawler.exe`
3. No Python installation required on target machine

## 🚨 Error Handling

### Exception Best Practices

```python
# Create custom exceptions for your domain
class PaymentError(Exception):
    """Base exception for payment-related errors."""
    pass

class InsufficientFundsError(PaymentError):
    """Raised when account has insufficient funds."""
    def __init__(self, required: Decimal, available: Decimal):
        self.required = required
        self.available = available
        super().__init__(
            f"Insufficient funds: required {required}, available {available}"
        )

# Use specific exception handling
try:
    process_payment(amount)
except InsufficientFundsError as e:
    logger.warning(f"Payment failed: {e}")
    return PaymentResult(success=False, reason="insufficient_funds")
except PaymentError as e:
    logger.error(f"Payment error: {e}")
    return PaymentResult(success=False, reason="payment_error")

# Use context managers for resource management
from contextlib import contextmanager

@contextmanager
def database_transaction():
    """Provide a transactional scope for database operations."""
    conn = get_connection()
    trans = conn.begin_transaction()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()
```

### Logging Strategy

```python
import logging
from functools import wraps

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Log function entry/exit for debugging
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Entering {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Exiting {func.__name__} successfully")
            return result
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
```

## 🔧 Configuration Management

### Environment Variables and Settings

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings with validation."""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str
    redis_url: str = "redis://localhost:6379"
    api_key: str
    max_connections: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

# Usage
settings = get_settings()
```

## 🏗️ Data Models and Validation

### Example Pydantic Models strict with pydantic v2

```python
from pydantic import BaseModel, Field, validator, EmailStr
from datetime import datetime
from typing import Optional, List
from decimal import Decimal

class ProductBase(BaseModel):
    """Base product model with common fields."""
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    price: Decimal = Field(..., gt=0, decimal_places=2)
    category: str
    tags: List[str] = []

    @validator('price')
    def validate_price(cls, v):
        if v > Decimal('1000000'):
            raise ValueError('Price cannot exceed 1,000,000')
        return v

    class Config:
        json_encoders = {
            Decimal: str,
            datetime: lambda v: v.isoformat()
        }

class ProductCreate(ProductBase):
    """Model for creating new products."""
    pass

class ProductUpdate(BaseModel):
    """Model for updating products - all fields optional."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class Product(ProductBase):
    """Complete product model with database fields."""
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True  # Enable ORM mode
```

## 🔄 Git Workflow

### Branch Strategy

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation updates
- `refactor/*` - Code refactoring
- `test/*` - Test additions or fixes

### Commit Message Format

Never include claude code, or written by claude code in commit messages

```
<type>(<scope>): <subject>

<body>

<footer>
``
Types: feat, fix, docs, style, refactor, test, chore

Example:
```

feat(auth): add two-factor authentication

- Implement TOTP generation and validation
- Add QR code generation for authenticator apps
- Update user model with 2FA fields

Closes #123

````

## 🗄️ Database Naming Standards

### Entity-Specific Primary Keys
All database tables use entity-specific primary keys for clarity and consistency:

```sql
-- ✅ STANDARDIZED: Entity-specific primary keys
sessions.session_id UUID PRIMARY KEY
leads.lead_id UUID PRIMARY KEY
messages.message_id UUID PRIMARY KEY
daily_metrics.daily_metric_id UUID PRIMARY KEY
agencies.agency_id UUID PRIMARY KEY
````

### Field Naming Conventions

```sql
-- Primary keys: {entity}_id
session_id, lead_id, message_id

-- Foreign keys: {referenced_entity}_id
session_id REFERENCES sessions(session_id)
agency_id REFERENCES agencies(agency_id)

-- Timestamps: {action}_at
created_at, updated_at, started_at, expires_at

-- Booleans: is_{state}
is_connected, is_active, is_qualified

-- Counts: {entity}_count
message_count, lead_count, notification_count

-- Durations: {property}_{unit}
duration_seconds, timeout_minutes
```

### Repository Pattern Auto-Derivation

The enhanced BaseRepository automatically derives table names and primary keys:

```python
# ✅ STANDARDIZED: Convention-based repositories
class LeadRepository(BaseRepository[Lead]):
    def __init__(self):
        super().__init__()  # Auto-derives "leads" and "lead_id"

class SessionRepository(BaseRepository[AvatarSession]):
    def __init__(self):
        super().__init__()  # Auto-derives "sessions" and "session_id"
```

**Benefits**:

- ✅ Self-documenting schema
- ✅ Clear foreign key relationships
- ✅ Eliminates repository method overrides
- ✅ Consistent with entity naming patterns

### Model-Database Alignment

Models mirror database fields exactly to eliminate field mapping complexity:

```python
# ✅ STANDARDIZED: Models mirror database exactly
class Lead(BaseModel):
    lead_id: UUID = Field(default_factory=uuid4)  # Matches database field
    session_id: UUID                               # Matches database field
    agency_id: str                                 # Matches database field
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        alias_generator=None  # Use exact field names
    )
```

### API Route Standards

```python
# ✅ STANDARDIZED: RESTful with consistent parameter naming
router = APIRouter(prefix="/api/v1/leads", tags=["leads"])

@router.get("/{lead_id}")           # GET /api/v1/leads/{lead_id}
@router.put("/{lead_id}")           # PUT /api/v1/leads/{lead_id}
@router.delete("/{lead_id}")        # DELETE /api/v1/leads/{lead_id}

# Sub-resources
@router.get("/{lead_id}/messages")  # GET /api/v1/leads/{lead_id}/messages
@router.get("/agency/{agency_id}")  # GET /api/v1/leads/agency/{agency_id}
```

For complete naming standards, see [NAMING_CONVENTIONS.md](./NAMING_CONVENTIONS.md).

## 📝 Documentation Standards

### Code Documentation

- Every module should have a docstring explaining its purpose
- Public functions must have complete docstrings
- Complex logic should have inline comments with `# Reason:` prefix
- Keep README.md updated with setup instructions and examples
- Maintain CHANGELOG.md for version history

### API Documentation

```python
from fastapi import APIRouter, HTTPException, status
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

@router.get(
    "/",
    response_model=List[Product],
    summary="List all products",
    description="Retrieve a paginated list of all active products"
)
async def list_products(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None
) -> List[Product]:
    """
    Retrieve products with optional filtering.

    - **skip**: Number of products to skip (for pagination)
    - **limit**: Maximum number of products to return
    - **category**: Filter by product category
    """
    # Implementation here
```

## 🚀 Performance Considerations

### Optimization Guidelines

- Profile before optimizing - use `cProfile` or `py-spy`
- Use `lru_cache` for expensive computations
- Prefer generators for large datasets
- Use `asyncio` for I/O-bound operations
- Consider `multiprocessing` for CPU-bound tasks
- Cache database queries appropriately

### Example Optimization

```python
from functools import lru_cache
import asyncio
from typing import AsyncIterator

@lru_cache(maxsize=1000)
def expensive_calculation(n: int) -> int:
    """Cache results of expensive calculations."""
    # Complex computation here
    return result

async def process_large_dataset() -> AsyncIterator[dict]:
    """Process large dataset without loading all into memory."""
    async with aiofiles.open('large_file.json', mode='r') as f:
        async for line in f:
            data = json.loads(line)
            # Process and yield each item
            yield process_item(data)
```

## 🛡️ Security Best Practices

### Security Guidelines

- Never commit secrets - use environment variables
- Validate all user input with Pydantic
- Use parameterized queries for database operations
- Implement rate limiting for APIs
- Keep dependencies updated with `uv`
- Use HTTPS for all external communications
- Implement proper authentication and authorization

### Example Security Implementation

```python
from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def generate_secure_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token."""
    return secrets.token_urlsafe(length)
```

## 🔍 Debugging Tools

### Debugging Commands

```bash
# Interactive debugging with ipdb
uv add --dev ipdb
# Add breakpoint: import ipdb; ipdb.set_trace()

# Memory profiling
uv add --dev memory-profiler
uv run python -m memory_profiler script.py

# Line profiling
uv add --dev line-profiler
# Add @profile decorator to functions

# Debug with rich traceback
uv add --dev rich
# In code: from rich.traceback import install; install()
```

## 📊 Monitoring and Observability

### Structured Logging

```python
import structlog

logger = structlog.get_logger()

# Log with context
logger.info(
    "payment_processed",
    user_id=user.id,
    amount=amount,
    currency="USD",
    processing_time=processing_time
)
```

## 🕷️ Crawler-Specific Guidance

### Anti-Detection Best Practices

- **Always use human-like delays**: 2-5 seconds between actions
- **Simulate reading behavior**: Use `reading_pause()` based on content length
- **Random mouse movements**: Call `random_mouse_movements()` periodically
- **Vary user agents**: Enable `user_agent_rotation` in settings
- **Respect rate limits**: Never reduce `crawl_delay_min` below 2 seconds

### Adding New Job Sites

1. **Add site config** to `JobSiteConfig.SITES` in `src/crawler/core/config.py`:
```python
"newsite": {
    "base_url": "https://newsite.com",
    "login_url": "https://newsite.com/login",
    "jobs_url": "https://newsite.com/jobs",
    "selectors": {
        "email_input": "#email",
        "password_input": "#password",
        "login_button": "[type='submit']",
        "job_card": ".job-card",
        # ... more selectors
    }
}
```

2. **Add credentials** to `CrawlerSettings` in `config.py`
3. **Implement site-specific extraction** in `job_extractor.py`
4. **Test thoroughly** with small result sets first

### Configuration Files

- **`.env`**: Site credentials and crawler behavior settings
- **`pyproject.toml`**: Dependencies and tool configurations
- **`src/crawler/core/config.py`**: Site selectors and application settings

### Common Crawler Operations

```python
# Initialize crawler for LinkedIn
crawler = JobCrawler("linkedin")

# Define search criteria
filters = SearchFilters(
    keywords="python developer",
    location="San Francisco, CA",
    job_type=JobType.FULL_TIME,
    experience_level=ExperienceLevel.MID_LEVEL,
    max_results=50
)

# Start crawling
excel_file = crawler.crawl_jobs(filters)
```

## 📚 Useful Resources

### Crawler-Specific Tools

- Selenium Documentation: https://selenium-python.readthedocs.io/
- Undetected ChromeDriver: https://github.com/ultrafunkamsterdam/undetected-chromedriver
- Pandas Excel Export: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
- OpenPyXL Formatting: https://openpyxl.readthedocs.io/

### Essential Tools

- UV Documentation: https://github.com/astral-sh/uv
- Ruff: https://github.com/astral-sh/ruff
- Pytest: https://docs.pytest.org/
- Pydantic: https://docs.pydantic.dev/

### Python Best Practices

- PEP 8: https://pep8.org/
- PEP 484 (Type Hints): https://www.python.org/dev/peps/pep-0484/
- The Hitchhiker's Guide to Python: https://docs.python-guide.org/

## ⚠️ Important Notes

### Crawler-Specific Warnings

- **NEVER reduce delays below 2 seconds** - Risk of detection and IP blocking
- **ALWAYS test with small result sets first** (max_results=5-10)
- **NEVER commit credentials** - Keep .env out of version control
- **Check robots.txt compliance** - Respect site crawling policies
- **Monitor for CAPTCHA** - Stop crawling if encountered
- **Handle rate limiting gracefully** - Increase delays if receiving 429 errors

### General Development

- **NEVER ASSUME OR GUESS** - When in doubt, ask for clarification
- **Always verify file paths and module names** before use
- **Keep CLAUDE.md updated** when adding new patterns or dependencies
- **Test your code** - No feature is complete without tests
- **Document your decisions** - Future developers (including yourself) will thank you

## 🔍 Search Command Requirements

**CRITICAL**: Always use `rg` (ripgrep) instead of traditional `grep` and `find` commands:

```bash
# ❌ Don't use grep
grep -r "pattern" .

# ✅ Use rg instead
rg "pattern"

# ❌ Don't use find with name
find . -name "*.py"

# ✅ Use rg with file filtering
rg --files | rg "\.py$"
# or
rg --files -g "*.py"
```

**Enforcement Rules:**

```
(
    r"^grep\b(?!.*\|)",
    "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
),
(
    r"^find\s+\S+\s+-name\b",
    "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
),
```

## 🚀 GitHub Flow Workflow Summary

main (protected) ←── PR ←── feature/your-feature
↓ ↑
deploy development

### Daily Workflow:

1. git checkout main && git pull origin main
2. git checkout -b feature/new-feature
3. Make changes + tests
4. git push origin feature/new-feature
5. Create PR → Review → Merge to main

---

_This document is a living guide. Update it as the project evolves and new patterns emerge._