# Data Model: BCB Time Series Downloader

## Entities

### BCB Time Series

Represents a single time series from the Banco Central do Brasil (BCB).

**Fields**:

*   **Date**: The date of the data point (e.g., `YYYY-MM-DD`).
*   **Value**: The numerical value of the time series for that date.

**Validation Rules**:

*   The `Date` field must be a valid date.
*   The `Value` field must be a numerical type.
