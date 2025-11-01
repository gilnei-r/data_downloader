"""Module for the DownloaderService."""
import os
import pandas as pd
from datetime import datetime
from typing import Dict, Type
from src.data_providers import BaseProvider

class DownloaderService:
    """Service to download data from different providers."""
    def __init__(self, provider_factory: Dict[str, Type[BaseProvider]]):
        """Initializes the DownloaderService.

        Args:
            provider_factory: A dictionary mapping provider names to provider classes.
        """
        self.provider_factory = provider_factory
        self.providers = {}

    def get_provider(self, provider_name: str, **kwargs) -> BaseProvider:
        """Gets a provider instance.

        Args:
            provider_name: The name of the provider.
            **kwargs: Keyword arguments to pass to the provider constructor.

        Returns:
            A provider instance.
        """
        if provider_name not in self.providers:
            self.providers[provider_name] = self.provider_factory[provider_name](**kwargs)
        return self.providers[provider_name]

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

            provider = self.get_provider(provider_name, login=int(os.getenv('MT5_LOGIN')), password=os.getenv('MT5_PASSWORD'), server=os.getenv('MT5_SERVER'))

            if not provider.connect():
                continue

            data = provider.get_data(ticker, from_date, to_date)
            if data:
                df = pd.DataFrame(data)
                file_path = os.path.join(data_dir, f'{ticker}_{provider_name}.csv')
                df.to_csv(file_path, index=False)
                print(f"Data for {ticker} saved to {file_path}")

            provider.disconnect()
