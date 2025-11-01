# Tasks: Metatrader5 Data Downloader

**Input**: Design documents from `/specs/001-metatrader5-downloader/`

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project structure per implementation plan in `src/` and `tests/`
- [X] T002 Create `requirements.txt` with `MetaTrader5` and `pandas`

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T003 Implement logging setup in `src/main.py`
- [X] T004 Implement configuration management for Metatrader5 credentials in `src/main.py`

---

## Phase 3: User Story 1 - Download Metatrader5 Data (Priority: P1) 🎯 MVP

**Goal**: Download historical stock data from Metatrader5 for a list of tickers.

**Independent Test**: Run the downloader with a list of tickers and verify that the data is downloaded correctly.

### Tests for User Story 1

- [X] T005 [P] [US1] Create unit tests for `mt5_provider` in `tests/unit/test_mt5_provider.py`
- [X] T006 [P] [US1] Create integration tests for `downloader_service` in `tests/integration/test_downloader_service.py`

### Implementation for User Story 1

- [X] T007 [P] [US1] Create `HistoricalData` model in `src/models/historical_data.py`
- [X] T008 [US1] Implement `mt5_provider` in `src/data_providers/mt5_provider.py`
- [X] T009 [US1] Implement `downloader_service` in `src/services/downloader_service.py`
- [X] T010 [US1] Implement `main.py` to read tickers from `tickers.csv` and run the downloader

---

## Phase 4: User Story 2 - Modular Design (Priority: P2)

**Goal**: Refactor the downloader to be modular and easily support new data providers.

**Independent Test**: Add a new data provider and verify that it can be integrated with the existing system with minimal changes.

### Implementation for User Story 2

- [X] T011 [US2] Refactor `downloader_service` to use a provider factory pattern in `src/services/downloader_service.py`
- [X] T012 [US2] Create a base provider class in `src/data_providers/__init__.py`

---

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T013 [P] Add docstrings to all functions and classes
- [X] T014 [P] Code cleanup and refactoring

---

## Dependencies & Execution Order

- **Phase 1** must be completed before **Phase 2**.
- **Phase 2** must be completed before **Phase 3**.
- **Phase 3** is the MVP.
- **Phase 4** can be done after **Phase 3**.
- **Phase 5** can be done at any time after **Phase 3**.

## Parallel Opportunities

- Within Phase 3, tests can be written in parallel with the implementation.
- Within Phase 5, documentation and code cleanup can be done in parallel.
