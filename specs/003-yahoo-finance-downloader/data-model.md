# Data Model: Yahoo Finance Data Downloader

## Entities

### Ticker

Represents a financial instrument to be downloaded.

**Fields**:

- `ticker`: string (e.g., "PETR4")
- `provider`: string (e.g., "YF")

### HistoricalData

Represents the downloaded data for a ticker.

**Fields**:

- `Date`: date
- `Open`: float
- `High`: float
- `Low`: float
- `Close`: float
- `Volume`: integer
