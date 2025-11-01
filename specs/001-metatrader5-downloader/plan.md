# Implementation Plan: Metatrader5 Data Downloader

**Branch**: `001-metatrader5-downloader` | **Date**: 2025-11-01 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-metatrader5-downloader/spec.md`

## Summary

The user wants to create a Python application to download historical stock data from Metatrader5. The application should be modular to support additional data providers in the future. Data will be stored in CSV files.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: `MetaTrader5`, `pandas`
**Storage**: CSV files
**Testing**: `pytest`
**Target Platform**: Windows
**Project Type**: Single project
**Performance Goals**: [NEEDS CLARIFICATION: What is the expected performance? (e.g., time to download data for 1000 tickers)]
**Constraints**: Requires a running Metatrader5 terminal with valid credentials.
**Scale/Scope**: [NEEDS CLARIFICATION: What is the expected number of tickers to be downloaded in a single run?]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

*   **Data Fetching**: The application must fetch financial data from specified APIs. (✅)
*   **Data Storage**: Downloaded data must be stored locally in a structured and easily accessible format. All data must be saved in .csv files, one file for each ticker. (✅)
*   **Configuration**: API keys and other settings must be managed externally from the code (e.g., via environment variables). (✅)
*   **Modular Design**: The code should be organized logically, with separate modules for each data source and for data storage. (✅)
*   **Error Handling**: The application must gracefully handle common errors, such as API connection failures, invalid symbols, or rate limits. (✅)
*   **Ticker Management**: The application shall use one .csv file for the list of tickers to download. In this file will be specified the data provider. (✅)
*   **Data Format**: The .csv format for stocks data must be "Data, Open, Close, High, Low" and need to be adjusted for dividends, splits, etc. The data for other financial data must be saved in a specific format. (✅)

## Project Structure

### Documentation (this feature)

```text
specs/001-metatrader5-downloader/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
# Option 1: Single project (DEFAULT)
src/
├── data_providers/
│   ├── __init__.py
│   └── mt5_provider.py
├── models/
│   ├── __init__.py
│   └── historical_data.py
├── services/
│   ├── __init__.py
│   └── downloader_service.py
└── main.py

tests/
├── integration/
│   └── test_downloader_service.py
└── unit/
    └── test_mt5_provider.py
```

**Structure Decision**: A single project structure is chosen for simplicity. The `data_providers` directory will contain modules for each data source, allowing for easy extension.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
|           |            |                                     |