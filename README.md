# Data Downloader

This project is a Python application for downloading historical financial data from various platforms.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/gilnei-r/data_downloader.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd data_downloader
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    pip install metastock2pd  # For Metastock data provider
    ```

## Usage

To run the application, execute the following command from the root of the project:

```bash
python -m src.main
```

## Configuration

The application's settings are managed through a `config.yaml` file located in the root of the project. This file defines parameters such as start and end dates for data download, the output directory, and the path to the tickers file.

**`config.yaml` example:**

```yaml
start_date: 2023-01-01
end_date: 2023-01-02
output_directory: data
tickers_file: tickers.csv
metastock_data_path: C:\Path\To\Your\Metastock\Data # Required for Metastock provider
```

### MetaTrader 5 Connection

The application connects to the MetaTrader 5 terminal in two ways:

1.  **Without credentials:** If the MetaTrader 5 terminal is already running and logged in, the application will connect to it automatically.
2.  **With credentials:** If the application cannot connect to a running terminal, it will try to log in using the credentials provided in a `.env` file.

To use the credential-based login, create a `.env` file in the root of the project with the following content, replacing the values with your own credentials:

```
MT5_LOGIN=your_login
MT5_PASSWORD=your_password
MT5_SERVER=your_server
```

## Data Providers

The `tickers.csv` file specifies which data provider to use for each ticker. The `provider` column in `tickers.csv` should contain the name of the desired provider.

**`tickers.csv` example:**

```csv
symbol,provider
PETR4,mt5
AAPL,metastock
```

### MetaTrader 5 (mt5)

- **Description**: Downloads historical data from the MetaTrader 5 platform.
- **Configuration**: See "MetaTrader 5 Connection" section above.

### Metastock (metastock)

- **Description**: Reads historical data from local Metastock data files.
- **Configuration**: The `metastock_data_path` in `config.yaml` must point to the root directory of your Metastock data.

### Yahoo Finance (YF)

- **Description**: Downloads historical data from Yahoo Finance.
- **Configuration**: No specific configuration is required.