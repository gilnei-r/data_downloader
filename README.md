# Data Downloader

This project is a Python application for downloading historical financial data from the MetaTrader 5 platform.

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
```

Additionally, MetaTrader 5 credentials are required and should be configured via a `.env` file in the root of the project.

1.  Create a `.env` file in the root of the project.
2.  Add the following content to the `.env` file, replacing the values with your own credentials:

    ```
    MT5_LOGIN=your_login
    MT5_PASSWORD=your_password
    MT5_SERVER=your_server
    ```
