"""Module for the DownloaderService."""
import os
import csv
import re
import pandas as pd
from datetime import datetime
import logging
from src.data_providers.mt5_provider import MT5Provider
from src.data_providers.metastock_provider import MetastockProvider
from src.data_providers.yf_provider import YFProvider
from src.data_providers.bcb_provider import BCBProvider
from src.models.historical_data import HistoricalData


def _base_ticker_name(ticker):
    """Returns the base ticker name without exchange suffix (e.g. 'BBDC4.SA' -> 'BBDC4')."""
    return str(ticker).split('.')[0]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DownloaderService:
    """Service to download data from different providers."""
    def __init__(self, providers=None):
        """Initializes the DownloaderService."""
        if providers is None:
            self.providers = {
                'mt5': MT5Provider,
                'metastock': MetastockProvider,
                'YF': YFProvider,
                'BCB': BCBProvider
            }
        else:
            self.providers = providers

    @staticmethod
    def _write_log_row(log_path, ticker, provider, status, message):
        """Appends one row to the per-run CSV download log."""
        is_new = not os.path.exists(log_path)
        with open(log_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            if is_new:
                writer.writerow(['timestamp', 'ticker', 'provider', 'status', 'message'])
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                ticker, provider, status, message,
            ])

    def download_data(
        self, tickers_df: pd.DataFrame, from_date: datetime, to_date: datetime, data_dir: str = 'data'
    ):
        """Downloads data for a list of tickers.

        Args:
            tickers_df: A DataFrame with ticker symbols and provider names.
            from_date: The start date for the data download.
            to_date: The end date for the data download.
            data_dir: The directory to save the data to.
        """
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        log_path = os.path.join(data_dir, f"download_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

        for _, row in tickers_df.iterrows():
            ticker = row['symbol']
            provider_name = row['provider']

            if provider_name not in self.providers:
                logging.warning(f"Provider {provider_name} not supported.")
                self._write_log_row(log_path, ticker, provider_name, 'failure', f'Provider {provider_name} not supported.')
                continue

            provider = None
            try:
                logging.info(f"Downloading data for {ticker} using provider {provider_name}.")
                provider = self.providers[provider_name]()

                if provider_name == 'mt5':
                    if not provider.connect():
                        # If connection fails, try with credentials from environment variables
                        login = os.getenv('MT5_LOGIN')
                        password = os.getenv('MT5_PASSWORD')
                        server = os.getenv('MT5_SERVER')
                        if login and password and server:
                            provider = self.providers[provider_name](login=int(login), password=password, server=server)
                            if not provider.connect():
                                logging.error(f"Failed to connect to MT5 with credentials for {ticker}.")
                                self._write_log_row(log_path, ticker, provider_name, 'failure', 'Failed to connect to MT5 with credentials.')
                                continue
                        else:
                            logging.error(f"Failed to connect to MT5 for {ticker}.")
                            self._write_log_row(log_path, ticker, provider_name, 'failure', 'Failed to connect to MT5.')
                            continue

                if provider_name == 'BCB':
                    bcb_ticker = re.match(r'\d+', str(ticker))
                    if bcb_ticker:
                        data = provider.get_data(bcb_ticker.group(0), from_date, to_date)
                    else:
                        logging.warning(f"Invalid BCB ticker format for {ticker}. Skipping.")
                        self._write_log_row(log_path, ticker, provider_name, 'failure', 'Invalid BCB ticker format.')
                        continue
                else:
                    data = provider.get_data(ticker, from_date, to_date)

                if data is not None and ((isinstance(data, pd.DataFrame) and not data.empty) or (isinstance(data, list) and data)):
                    if isinstance(data, list) and all(isinstance(d, HistoricalData) for d in data):
                        df = pd.DataFrame([d.to_dict() for d in data])
                        if provider_name == 'mt5':
                            df['date'] = df['date'].dt.date
                    elif isinstance(data, pd.DataFrame):
                        df = data
                    else:
                        logging.warning(f"Unsupported data type returned from provider {provider_name}")
                        self._write_log_row(log_path, ticker, provider_name, 'failure', f'Unsupported data type returned from provider {provider_name}.')
                        continue

                    if not df.empty:
                        file_path = os.path.join(data_dir, f'{_base_ticker_name(ticker)}.csv')
                        df.to_csv(file_path, index=False, sep=';')
                        logging.info(f"Data for {ticker} saved to {file_path}")
                        self._write_log_row(log_path, ticker, provider_name, 'success', f'Data saved to {file_path}')
                else:
                    logging.warning(f"No data downloaded for {ticker}.")
                    self._write_log_row(log_path, ticker, provider_name, 'failure', 'No data downloaded.')
            except Exception as e:
                logging.error(f"Failed to download data for {ticker} using provider {provider_name}: {e}")
                self._write_log_row(log_path, ticker, provider_name, 'failure', f'Failed to download data: {e}')
                continue
            finally:
                if hasattr(provider, 'disconnect'):
                    provider.disconnect()