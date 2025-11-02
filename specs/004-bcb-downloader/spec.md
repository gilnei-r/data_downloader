# Feature Specification: BCB Time Series Downloader

**Feature Branch**: `004-bcb-downloader`  
**Created**: 2025-11-02  
**Status**: Draft  
**Input**: User description: "now add a new module that downloads time series data from Banco Central Brasileiro (BCB) and saves the data in data folder as .csv file. The time series code will be in ticker.csv with provider "BCB". Use bcb_time_series_example.py as an example for implementing the new mudule. The data must be chunked in order to be downloaded from BCB."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Download BCB Time Series Data (Priority: P1)

As a user, I want to download time series data from the Banco Central do Brasil (BCB) for tickers specified in the `tickers.csv` file.

**Why this priority**: This is the core functionality of the feature.

**Independent Test**: This can be tested by running the downloader and verifying that the correct data is downloaded and saved for a BCB ticker.

**Acceptance Scenarios**:

1. **Given** a ticker in `tickers.csv` with the provider "BCB", **When** the downloader is executed, **Then** the system downloads the corresponding time series data from BCB.
2. **Given** the data has been downloaded, **When** the process completes, **Then** the data is saved as a `.csv` file in the `data` folder.
3. **Given** a time series that is very large, **When** the data is being downloaded, **Then** it is downloaded in manageable chunks to prevent timeouts or memory issues.

### Edge Cases

- What happens when the BCB API is unavailable?
- How does the system handle invalid or non-existent BCB ticker codes?
- What happens if the `tickers.csv` file is missing or malformed?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a module to download time series data from the Banco Central do Brasil (BCB).
- **FR-002**: The system MUST read the `tickers.csv` file to identify which time series to download, based on the "BCB" provider.
- **FR-003**: The system MUST save the downloaded time series data into a `.csv` file within the `data` directory.
- **FR-004**: The system MUST implement a chunking mechanism to download large datasets from BCB without errors.
- **FR-005**: The implementation SHOULD follow the patterns and style of the `bcb_time_series_example.py` file as a reference.
- **FR-007**: The output CSV file MUST contain `Date` and `Value` columns.
- **FR-008**: If a download for a single ticker fails, the system MUST log the error and continue processing other tickers.
- **FR-009**: If a `.csv` file for a ticker already exists, the system MUST overwrite it with the newly downloaded data.
- **FR-010**: The system MUST fetch the entire historical data for each time series (from the earliest available date to the current date).
- **FR-006**: The filename for the saved data MUST follow the format `{ticker}_BCB.csv`.

### Key Entities *(include if feature involves data)*

- **BCB Time Series**: Represents a single time series from the BCB. It contains a series of data points, each with a date and a corresponding value.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The system can successfully download and save a complete time series from BCB for a valid ticker.
- **SC-002**: The system can successfully download and save a large time series from BCB, demonstrating the chunking mechanism works as expected.
- **SC-003**: The data in the downloaded `.csv` file accurately matches the data available from the BCB for the corresponding ticker and date range.

## Clarifications

### Session 2025-11-02

- Q: Should the filename convention be corrected to use a "BCB" suffix for clarity and consistency? → A: Yes, `{ticker}_BCB.csv`.
- Q: What specific columns should be included in the output CSV file for each time series? → A: `Date, Value`.
- Q: How should the system behave if the download of time series data for a *single* ticker fails (e.g., due to an invalid ticker code, API error for that specific ticker)? → A: Continue processing other tickers (log the error).
- Q: If a `.csv` file for a specific ticker already exists in the `data` folder, how should the system handle the new download? → A: Overwrite the existing file with the new data.
- Q: Should the downloader fetch the entire history for each time series, or should there be an option to specify a start and/or end date for the download? → A: Fetch entire history (from the earliest available date to the current date).