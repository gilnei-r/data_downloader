# Quickstart: Yahoo Finance Data Downloader

## To use the Yahoo Finance data downloader:

1.  **Add tickers to `tickers.csv`:**

    Open the `tickers.csv` file and add the tickers you want to download from Yahoo Finance. Make sure to set the `provider` column to `YF` for these tickers.

    Example:

    ```csv
    ticker,provider
    PETR4,mt5
    VALE3,mt5
    MSFT,YF
    GOOG,YF
    ```

2.  **Run the application:**

    Execute the main application. The downloader service will automatically pick up the new tickers and download the data from Yahoo Finance.

3.  **Check the `data` directory:**

    The downloaded data will be saved in the `data` directory with the `_YF.csv` suffix (e.g., `MSFT_YF.csv`).
