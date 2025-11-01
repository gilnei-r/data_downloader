# Quickstart: Metatrader5 Data Downloader

## Prerequisites

- Python 3.11
- A running instance of Metatrader5
- Metatrader5 credentials configured as environment variables:
  - `MT5_LOGIN`
  - `MT5_PASSWORD`
  - `MT5_SERVER`

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Create a `tickers.csv` file in the root directory with the following format:

    ```csv
    symbol,provider
    AAPL,metatrader5
    GOOG,metatrader5
    ```

2.  Run the application:
    ```bash
    python src/main.py
    ```

3.  The downloaded data will be saved in the `data` directory.
