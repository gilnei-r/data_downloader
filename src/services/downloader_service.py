"""Module for the DownloaderService."""
import os
import pandas as pd
from datetime import datetime
from src.data_providers.mt5_provider import MT5Provider
from src.data_providers.metastock_provider import MetastockProvider
from src.models.historical_data import HistoricalData

class DownloaderService:
    """Service to download data from different providers."""
    def __init__(self, providers=None):
        """Initializes the DownloaderService."""
        if providers is None:
            self.providers = {
                'mt5': MT5Provider,
                'metastock': MetastockProvider
            }
        else:
            self.providers = providers

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

        for _, row in tickers_df.iterrows():
            ticker = row['symbol']
            provider_name = row['provider']

            if provider_name not in self.providers:
                print(f"Provider {provider_name} not supported.")
                continue

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
                            continue
                    else:
                        continue

            data = provider.get_data(ticker, from_date, to_date)
            
            if data:
                if isinstance(data, list) and all(isinstance(d, HistoricalData) for d in data):
                    df = pd.DataFrame([d.to_dict() for d in data])
                elif isinstance(data, pd.DataFrame):
                    df = data
                else:
                    print(f"Unsupported data type returned from provider {provider_name}")
                    continue

                if not df.empty:
                    file_path = os.path.join(data_dir, f'{ticker}_{provider_name}.csv')
                    df.to_csv(file_path, index=False)
                    print(f"Data for {ticker} saved to {file_path}")

            if hasattr(provider, 'disconnect'):
                provider.disconnect()
