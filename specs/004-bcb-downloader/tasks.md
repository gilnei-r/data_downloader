# Tasks: BCB Time Series Downloader

**Branch**: `004-bcb-downloader` | **Date**: 2025-11-02 | **Spec**: [link](./spec.md)

## Phase 1: Setup

- [X] T001 Install `python-bcb` library using pip: `pip install python-bcb`

## Phase 2: Foundational Tasks

- [X] T002 Create the file `src/data_providers/bcb_provider.py`

## Phase 3: User Story 1 - Download BCB Time Series Data

- [X] T003 [US1] Implement the `BCBProvider` class in `src/data_providers/bcb_provider.py` to download data from BCB.
- [X] T004 [US1] Modify `src/services/downloader_service.py` to read tickers from `tickers.csv` and identify tickers with "BCB" as the provider.
- [X] T005 [US1] In `src/services/downloader_service.py`, call the `BCBProvider` to download the data for the identified BCB tickers.
- [X] T006 [US1] In `src/services/downloader_service.py`, save the downloaded data to a `.csv` file with the format `{ticker}_BCB.csv` in the `data` folder.

## Phase 4: Testing

- [X] T007 Create the file `tests/unit/test_bcb_provider.py`
- [X] T008 [P] Add unit tests for the `BCBProvider` class in `tests/unit/test_bcb_provider.py`.
- [X] T009 [P] Add integration tests to `tests/integration/test_downloader_service.py` to verify the end-to-end download process for BCB data.

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T010 Add error handling in `src/data_providers/bcb_provider.py` to gracefully handle API connection failures and invalid ticker codes.
- [X] T011 Implement logging in `src/data_providers/bcb_provider.py` and `src/services/downloader_service.py` to provide insights into the download process.

## Dependencies

- **User Story 1** is the only user story and has no dependencies on other stories.

## Parallel Execution

- Tasks T008 and T009 can be worked on in parallel after the initial implementation of the `BCBProvider` is complete.

## Implementation Strategy

The implementation will follow an MVP-first approach, focusing on delivering the core functionality of downloading and saving BCB time series data as defined in User Story 1. Subsequent phases will add testing and polish to ensure the feature is robust and maintainable.
