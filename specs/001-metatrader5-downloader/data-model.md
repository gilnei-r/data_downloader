# Data Model: Metatrader5 Data Downloader

## Entities

### Ticker

Represents a financial instrument to be downloaded.

**Fields**:

- `symbol`: string - The ticker symbol (e.g., 'AAPL').
- `provider`: string - The data provider to use (e.g., 'metatrader5').

### HistoricalData

Represents the downloaded historical data for a ticker.

**Fields**:

- `date`: datetime - The date of the data point.
- `open`: float - The opening price.
- `high`: float - The highest price.
- `low`: float - The lowest price.
- `close`: float - The closing price.
