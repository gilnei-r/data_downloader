# Actionable Tasks: Metastock Data Provider

**Branch**: `002-metastock-data-provider` | **Spec**: `spec.md`

## Phase 1: Setup

- [X] T001 Install `metastock2pd` library using pip: `pip install metastock2pd`

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T002 Create the basic structure for the Metastock provider in `src/data_providers/metastock_provider.py`
- [X] T003 Create the test file with the basic structure in `tests/unit/test_metastock_provider.py`

## Phase 3: User Story 1 - Configure Metastock Data Path

**Goal**: As a data analyst, I want to specify the folder path of my local Metastock database in a configuration file, so that the application can locate and load the data.

**Independent Test**: Can be tested by creating a `config.yaml` file with a valid path and verifying that the application reads it without errors on startup.

- [X] T004 [US1] Implement configuration loading in `src/data_providers/metastock_provider.py` to read `metastock_data_path` from `config.yaml`.
- [X] T005 [US1] Add tests in `tests/unit/test_metastock_provider.py` for configuration loading, including success and failure cases (missing key, invalid path).

## Phase 4: User Story 2 - Load Historical Data from Metastock

**Goal**: As a data analyst, I want the application to read historical price data from the configured Metastock database, so that I can perform analysis and backtesting.

**Independent Test**: Can be tested by calling a function to get historical data for a specific ticker and verifying that the returned data matches the known data in the Metastock files.

- [X] T006 [US2] Implement the `get_historical_data` method in `src/data_providers/metastock_provider.py` to read data using the `metastock2pd` library.
- [X] T007 [US2] Add tests in `tests/unit/test_metastock_provider.py` for `get_historical_data`, covering success cases, ticker not found, and corrupted file scenarios.

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T008 Implement logging (info, warnings, errors) in `src/data_providers/metastock_provider.py`.
- [X] T009 Integrate the `MetastockProvider` into the `DownloaderService` in `src/services/downloader_service.py`.

## Dependencies

- User Story 2 is dependent on User Story 1.

## Parallel Execution

- Tasks within each user story phase can be worked on in parallel, but it's recommended to follow the order for clarity.
- The implementation of the provider (T006) and its tests (T007) can be developed in parallel.

## Implementation Strategy

The implementation will follow an MVP-first approach, starting with the foundational setup and then implementing each user story incrementally. This ensures that each completed phase delivers a testable and valuable piece of functionality.
