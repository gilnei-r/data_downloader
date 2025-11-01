# Feature Specification: Metatrader5 Data Downloader

**Feature Branch**: `001-metatrader5-downloader`
**Created**: 2025-11-01
**Status**: Draft
**Input**: User description: "Create a code that download stocks data from Metatrader5. This is the first data provider that will be implemented. The code shall be prepared for addition of new data providers later. The data file must be saved in data folder and must contain a sufix indicating the source of the data."

## Clarifications

### Session 2025-11-01

- Q: How should the application behave when it fails to download data for a specific ticker? → A: Retry: Attempt to download the data again a specified number of times before skipping.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Download Metatrader5 Data (Priority: P1)

As a user, I want to download historical stock data from Metatrader5 for a list of tickers, so that I can use it for analysis.

**Why this priority**: This is the core functionality of the feature.

**Independent Test**: The feature can be tested by running the downloader with a list of tickers and verifying that the data is downloaded correctly.

**Acceptance Scenarios**:

1. **Given** a list of valid tickers, **When** the downloader is run, **Then** the system downloads the historical data for each ticker and saves it to a CSV file in the `data` folder.
2. **Given** a list of tickers containing an invalid ticker, **When** the downloader is run, **Then** the system attempts to download the data for the invalid ticker a specified number of times, logs an error, and continues with the valid tickers.

---

### User Story 2 - Modular Design (Priority: P2)

As a developer, I want the downloader to be modular, so that I can easily add new data providers in the future.

**Why this priority**: This is important for the long-term maintainability and extensibility of the application.

**Independent Test**: The modularity can be tested by adding a new data provider and verifying that it can be integrated with the existing system with minimal changes.

**Acceptance Scenarios**:

1. **Given** a new data provider implementation, **When** it is added to the system, **Then** the downloader can use it to download data without requiring changes to the core application logic.

---

### Edge Cases

- What happens when the Metatrader5 API is unavailable?
- How does the system handle rate limiting?
- What happens if the ticker list is empty?
- How many times should the system retry a failed download?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST download historical stock data from Metatrader5.
- **FR-002**: The system MUST accept a list of tickers to download.
- **FR-003**: The system MUST save the downloaded data into a `data` folder.
- **FR-004**: Each downloaded file MUST have a suffix indicating the data source (e.g., `_mt5`).
- **FR-005**: The system MUST be designed in a modular way to allow for the addition of new data providers.
- **FR-006**: The downloaded data MUST be in CSV format.
- **FR-007**: The CSV file MUST contain the following columns: `Data`, `Open`, `Close`, `High`, `Low`.
- **FR-008**: The data MUST be adjusted for dividends and splits.
- **FR-009**: If a download for a specific ticker fails, the system MUST retry the download a configurable number of times.
- **FR-010**: If the download for a ticker fails after all retry attempts, the system MUST log an error and continue to the next ticker.

### Key Entities *(include if feature involves data)*

- **Ticker**: Represents a financial instrument to be downloaded. Contains the symbol of the instrument.
- **HistoricalData**: Represents the downloaded historical data for a ticker. Contains the date, open, high, low, and close prices.

### Assumptions

- The user has a running instance of Metatrader5.
- The user has the necessary credentials to connect to the Metatrader5 terminal.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The system can successfully download data for 99% of valid tickers from Metatrader5.
- **SC-002**: The downloaded data is correctly formatted in CSV files with the specified columns and matches the source data from Metatrader5.
- **SC-003**: A new data provider can be added by implementing a single new module, with no more than 10 lines of code changed in the core application.