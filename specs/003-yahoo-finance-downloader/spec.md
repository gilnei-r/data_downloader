# Feature Specification: Yahoo Finance Data Downloader

**Feature Branch**: `003-yahoo-finance-downloader`  
**Created**: 2025-11-02  
**Status**: Draft  
**Input**: User description: "Now create a new module for downloading data from yahoo finance. Use tickers.csv to read the tickers that are assigned to the provider "YF". Save the donloaded data using the same format as in data\PETR4_mt5.csv using the suffix _YF."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Download data from Yahoo Finance (Priority: P1)

As a user, I want to download historical financial data from Yahoo Finance for tickers specified in `tickers.csv` under the "YF" provider. The downloaded data should be saved in a format consistent with existing data files.

**Why this priority**: This is the core functionality of the feature.

**Independent Test**: Can be fully tested by running the downloader and verifying the output files.

**Acceptance Scenarios**:

1. **Given** the `tickers.csv` file contains tickers assigned to the "YF" provider, **When** the downloader is executed, **Then** CSV files for each "YF" ticker are created in the `data` directory.
2. **Given** a file is downloaded, **When** I open it, **Then** the columns are `Date,Open,High,Low,Close,Volume`.

### Edge Cases


## Clarifications

### Session 2025-11-02

- Q: What happens when the `tickers.csv` file is missing or empty? → A: Log an error and exit gracefully.
- Q: What is the desired behavior when a ticker from `tickers.csv` is not found on Yahoo Finance? → A: Log a warning for the specific ticker and continue with the next one.
- Q: How should the system handle network errors during the download process for a ticker? → A: Retry the download for the failed ticker a few times before giving up.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST read the `tickers.csv` file to identify tickers to be downloaded.
- **FR-002**: The system MUST filter tickers for the provider "YF".
- **FR-003**: The system MUST download historical data for each identified ticker from Yahoo Finance.
- **FR-004**: The system MUST save the downloaded data into a CSV file in the `data/` directory.
- **FR-005**: The filename for the saved data MUST follow the format `{ticker}_YF.csv`.
- **FR-006**: The saved CSV file MUST have the following columns in order: `Date,Open,High,Low,Close,Volume`.
- **FR-007**: The system MUST log an error and exit gracefully if `tickers.csv` is missing or empty.
- **FR-008**: The system MUST save adjusted data in the output csv file.
- **FR-009**: The system MUST log a warning and continue to the next ticker if a ticker is not found on Yahoo Finance.
- **FR-010**: The system MUST retry downloading data for a ticker a few times in case of network errors before giving up and logging an error.

### Functional Requirements

- **FR-001**: The system MUST read the `tickers.csv` file to identify tickers to be downloaded.
- **FR-002**: The system MUST filter tickers for the provider "YF".
- **FR-003**: The system MUST download historical data for each identified ticker from Yahoo Finance.
- **FR-004**: The system MUST save the downloaded data into a CSV file in the `data/` directory.
- **FR-005**: The filename for the saved data MUST follow the format `{ticker}_YF.csv`.
- **FR-006**: The saved CSV file MUST have the following columns in order: `Date,Open,High,Low,Close,Volume`.
- **FR-007**: The system MUST log an error and exit gracefully if `tickers.csv` is missing or empty.
- **FR-008**: The system MUST save adjusted data in the output csv file.
- **FR-009**: The system MUST log a warning and continue to the next ticker if a ticker is not found on Yahoo Finance.

### Functional Requirements

- **FR-001**: The system MUST read the `tickers.csv` file to identify tickers to be downloaded.
- **FR-002**: The system MUST filter tickers for the provider "YF".
- **FR-003**: The system MUST download historical data for each identified ticker from Yahoo Finance.
- **FR-004**: The system MUST save the downloaded data into a CSV file in the `data/` directory.
- **FR-005**: The filename for the saved data MUST follow the format `{ticker}_YF.csv`.
- **FR-006**: The saved CSV file MUST have the following columns in order: `Date,Open,High,Low,Close,Volume`.
- **FR-007**: The system MUST log an error and exit gracefully if `tickers.csv` is missing or empty.
- **FR-008**: The system MUST save adjusted data in the output csv file.

### Functional Requirements

- **FR-001**: The system MUST read the `tickers.csv` file to identify tickers to be downloaded.
- **FR-002**: The system MUST filter tickers for the provider "YF".
- **FR-003**: The system MUST download historical data for each identified ticker from Yahoo Finance.
- **FR-004**: The system MUST save the downloaded data into a CSV file in the `data/` directory.
- **FR-005**: The filename for the saved data MUST follow the format `{ticker}_YF.csv`.
- **FR-006**: The saved CSV file MUST have the following columns in order: `Date,Open,High,Low,Close,Volume`.
- **FR-007**: The system MUST save adjusted data in the output csv file.

### Key Entities *(include if feature involves data)*

- **Ticker**: Represents a financial instrument to be downloaded. It has a `ticker` symbol and a `provider`.
- **Historical Data**: Represents the downloaded data for a ticker. It includes `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All tickers assigned to the "YF" provider in `tickers.csv` have a corresponding `_YF.csv` file in the `data` directory after the process runs.
- **SC-002**: The generated CSV files can be successfully parsed and have the correct header and data structure, matching the format of `data\PETR4_mt5.csv`.