# Data_downloader Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-11-02

## Active Technologies
- Python 3.11 + pandas, `metastock2pd` (002-metastock-data-provider)
- Local file system (002-metastock-data-provider)
- Python 3.11 + `pandas`, `yfinance` (003-yahoo-finance-downloader)
- Filesystem (CSV) (003-yahoo-finance-downloader)

- Python 3.11 + `MetaTrader5`, `pandas` (001-metatrader5-downloader)

## Project Structure

```text
src/
tests/
```

## Commands

cd src; pytest; ruff check .

## Code Style

Python 3.11: Follow standard conventions

## Recent Changes
- 003-yahoo-finance-downloader: Added Python 3.11 + `pandas`, `yfinance`
- 002-metastock-data-provider: Added Python 3.11 + pandas, `metastock2pd`. Fixed data download and saving for Metastock provider.

- 001-metatrader5-downloader: Added Python 3.11 + `MetaTrader5`, `pandas`. Ensured date column is saved without time information.

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
