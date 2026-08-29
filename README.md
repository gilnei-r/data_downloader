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

The `tickers.csv` file specifies which data provider to use for each ticker. The `provider` column in `tickers.csv` should contain the name of the desired provider. The file uses the semicolon (`;`) as the delimiter.

**`tickers.csv` example:**

```csv
symbol;provider
PETR4;mt5
AAPL;metastock
BBDC4.SA;YF
12-CDI;BCB
```

## Output Data

The downloaded data is saved as CSV files inside the directory configured by `output_directory` in `config.yaml` (default: `data`). The directory is created automatically if it does not exist. All output CSV files use the semicolon (`;`) as the column separator.

Each ticker produces **one CSV file per ticker**, named using the **base ticker name** (the exchange suffix and provider suffix are removed):

- `BBDC4.SA` (Yahoo) → `data/BBDC4.csv`
- `PETR4` (MetaTrader 5) → `data/PETR4.csv`
- `12-CDI` (BCB) → `data/12-CDI.csv`

> **Note:** because the file name is the bare ticker name (without provider suffix), two different providers downloading the same ticker would write to the same file. If a file already exists, it is overwritten with the newly downloaded data.

## Error Handling

If a download fails for a **single ticker** (e.g. the ticker is not found in the Metastock database, a network error, an invalid symbol, etc.), the application **logs an error and continues processing the next ticker** — it does not abort the whole run.

### MetaTrader 5 (mt5)

- **Description**: Downloads historical data from the MetaTrader 5 platform.
- **Configuration**: See "MetaTrader 5 Connection" section above.

### Metastock (metastock)

- **Description**: Reads historical data from local Metastock data files.
- **Configuration**: The `metastock_data_path` in `config.yaml` must point to the root directory of your Metastock data.

### Yahoo Finance (YF)

- **Description**: Downloads historical data from Yahoo Finance.
- **Configuration**: No specific configuration is required.