# Selenium Job Crawler

A sophisticated, stealth-enabled job crawler that mimics human behavior to avoid detection while scraping job postings from major job sites like LinkedIn and Indeed.

## Features

- **Stealth Browsing**: Uses undetected-chromedriver with anti-detection measures
- **Human-like Behavior**: Random delays, mouse movements, typing patterns, and reading pauses
- **Multi-site Support**: LinkedIn and Indeed (easily extensible)
- **Smart Login**: Handles authentication with popup/banner dismissal
- **Advanced Filtering**: Job type, experience level, location, salary, and date filters
- **Detailed Extraction**: Comprehensive job data including requirements, benefits, and skills
- **Excel Export**: Professional Excel reports with formatting and summary statistics
- **Error Resilience**: Robust error handling and session recovery

## Quick Start

1. **Install UV** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Set up the project**:
```bash
# Create virtual environment and install dependencies
uv sync

# Copy environment configuration
cp .env.example .env
# Edit .env with your credentials
```

3. **Configure credentials** in `.env`:
```bash
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
INDEED_EMAIL=your_email@example.com
INDEED_PASSWORD=your_password
```

4. **Run the crawler**:
```bash
uv run python src/main.py
```

The crawler will guide you through:
1. **Site Selection**: Choose LinkedIn, Indeed, or Work24
2. **Login Credentials**: Enter your account information
3. **Output Directory**: Set where Excel files will be saved (cross-platform)
4. **Search Keywords**: Define what jobs to search for
5. **Result Limit**: How many jobs to collect

## 📁 Project Structure

```
├── README.md                   # This file
├── src/                       # Source code
├── docs/                      # 📋 Documentation
├── scripts/                   # 🛠️ Build scripts
├── assets/                    # 🎨 Images & resources
├── tests/                     # 🧪 Test files
├── output/                    # 📊 Generated Excel files
├── logs/                      # 📝 Application logs
└── release/                   # 📦 Built executables
```

## 📚 Documentation

- **[Build Instructions](docs/BUILD_INSTRUCTIONS.md)** - How to create Windows .exe
- **[Development Guide](docs/CLAUDE.md)** - Complete development documentation
- **[Batch Implementation](docs/BATCH_IMPLEMENTATION_SUMMARY.md)** - Batch saving details

## Configuration

Edit `src/main.py` to customize your search:

```python
search_filters = SearchFilters(
    keywords="python developer",
    location="San Francisco, CA",
    job_type=JobType.FULL_TIME,
    experience_level=ExperienceLevel.MID_LEVEL,
    date_posted="7d",  # Last 7 days
    remote_only=False,
    max_results=100
)
```

## Anti-Detection Features

- **Undetected ChromeDriver**: Bypasses basic bot detection
- **User Agent Rotation**: Random user agents for each session
- **Human Timing**: Realistic delays between actions (2-5 seconds)
- **Mouse Simulation**: Random mouse movements and hover effects
- **Reading Pauses**: Content-based reading time simulation
- **Typing Simulation**: Human-like keystroke timing
- **Browser Behavior**: Occasional back/forward navigation
- **Viewport Randomization**: Random window sizes

## Development Commands

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=html

# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Type checking
uv run mypy src/
```

## Architecture

```
src/crawler/
├── core/
│   ├── base_crawler.py     # Stealth browser management
│   ├── auth.py            # Login and authentication
│   ├── search_engine.py   # Search and filtering
│   ├── job_extractor.py   # Data extraction
│   ├── config.py          # Settings and site configurations
│   └── models.py          # Data models
├── utils/
│   ├── human_behavior.py  # Anti-detection behaviors
│   └── excel_exporter.py  # Excel export functionality
└── main_crawler.py        # Main orchestrator
```

## Safety & Ethics

- **Rate Limiting**: Built-in delays to avoid overwhelming servers
- **Respectful Crawling**: Follows robots.txt principles
- **No Spam**: Single-session, targeted data collection
- **Privacy Conscious**: No storage of personal information beyond job postings
- **Terms Compliance**: Designed for legitimate job search purposes

## Troubleshooting

**Chrome/ChromeDriver Issues**:
- Ensure Chrome is installed and up to date
- Try setting `HEADLESS=true` in .env for server environments

**Login Failures**:
- Verify credentials in .env file
- Check if 2FA is enabled (currently not supported)
- Some sites may require manual CAPTCHA solving

**No Jobs Found**:
- Adjust search filters (broader keywords, location)
- Check if site structure has changed
- Verify site selectors in `config.py`

## Extending the Crawler

To add a new job site:

1. Add site configuration to `JobSiteConfig.SITES` in `config.py`
2. Add credentials to settings in `config.py`
3. Implement site-specific extraction in `job_extractor.py`
4. Test with the new site name in `main.py`