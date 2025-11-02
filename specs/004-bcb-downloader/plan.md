# Implementation Plan: BCB Time Series Downloader

**Branch**: `004-bcb-downloader` | **Date**: 2025-11-02 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/004-bcb-downloader/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature adds a new module to download time series data from the Banco Central do Brasil (BCB). The module will read tickers from `tickers.csv`, download the data in chunks, and save it as `.csv` files in the `data` folder. The implementation will be based on the existing project structure and conventions.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: pandas, python-bcb
**Storage**: Filesystem (CSV)
**Testing**: pytest
**Target Platform**: Command-line application (platform-independent)
**Project Type**: Single project
**Performance Goals**: N/A
**Constraints**: Must download data in chunks to handle large time series.
**Scale/Scope**: N/A

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

*   **Data Fetching**: The application must fetch financial data from specified APIs. (Pass)
*   **Data Storage**: Downloaded data must be stored locally in a structured and easily accessible format. All data must be saved in .csv files, one file for each ticker. (Pass)
*   **Configuration**: API keys and other settings must be managed externally from the code (e.g., via environment variables). (Pass - will be handled during implementation)
*   **Modular Design**: The code should be organized logically, with separate modules for each data source and for data storage. (Pass)
*   **Error Handling**: The application must gracefully handle common errors, such as API connection failures, invalid symbols, or rate limits. (Pass)
*   **Ticker Management**: The application shall use one .csv file for the list of tickers to download. In this file will be specified the data provider. (Pass)
*   **Data Format**: The .csv format for stocks data must be "Data, Open, Close, High, Low" and need to be adjusted for dividends, splits, etc. The data for other financial data must be saved in a specific format. (Pass)

## Project Structure

### Documentation (this feature)

```text
specs/004-bcb-downloader/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── data_providers/
│   ├── bcb_provider.py  # New file for this feature
│   └── ...
└── ...

tests/
├── unit/
│   ├── test_bcb_provider.py # New file for this feature
│   └── ...
└── ...
```

**Structure Decision**: The existing single project structure will be extended with a new `bcb_provider.py` module and corresponding unit tests.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
|           |            |                                     |