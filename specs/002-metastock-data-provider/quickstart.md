# Quickstart: Metastock Data Provider

**Date**: 2025-11-01

## Configuration

1.  Open the `config.yaml` file in the root directory of the project.
2.  Add or update the `metastock_data_path` key with the absolute path to your Metastock data folder.

    ```yaml
    metastock_data_path: "C:\\Users\\YourUser\\Documents\\MetastockData"
    ```

## Usage

The Metastock data provider will be automatically used by the `DownloaderService` when the `provider` is set to `metastock` in the `tickers.csv` file.

To use the provider directly in your code:

```python
from src.data_providers.metastock_provider import MetastockProvider

# The provider is initialized with the path from config.yaml
provider = MetastockProvider()

# Get historical data for a ticker
try:
    data = provider.get_historical_data("AAPL")
    print(data)
except Exception as e:
    print(f"An error occurred: {e}")
```

