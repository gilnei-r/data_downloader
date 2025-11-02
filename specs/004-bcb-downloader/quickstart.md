# Quickstart: BCB Time Series Downloader

## Prerequisites

*   Python 3.11
*   pip

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/gilnei-r/data_downloader.git
    cd data_downloader
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Add the tickers you want to download to the `tickers.csv` file. Make sure the `provider` column is set to `BCB` for the new tickers.

    Example `tickers.csv`:
    ```csv
    ticker,provider
    12,BCB
    433,BCB
    ```

2.  Run the main application:
    ```bash
    python src/main.py
    ```

3.  The downloaded data will be saved as `.csv` files in the `data` folder (e.g., `12_BCB.csv`, `433_BCB.csv`).
