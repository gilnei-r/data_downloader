from bcb import sgs
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BCBProvider:
    def get_data(self, ticker: str, from_date: datetime, to_date: datetime) -> pd.DataFrame:
        """
        Downloads time series data from BCB for a given ticker.

        Args:
            ticker (str): The ticker code for the time series.

        Returns:
            pd.DataFrame: A DataFrame with the time series data, with 'Date' and 'Value' columns.
        """
        try:
            logging.info(f"Downloading data for ticker {ticker} from BCB.")
            df = sgs.get({ticker: ticker}, start=from_date.strftime('%Y-%m-%d'), end=to_date.strftime('%Y-%m-%d'))
            if df.empty:
                logging.warning(f"No data found for ticker {ticker}")
                return None
            df = df.reset_index()
            df.rename(columns={'index': 'Date', ticker: 'Value'}, inplace=True)
            df['cumulative_factor'] = (1 + df['Value'].pct_change()).cumprod().fillna(1)
            logging.info(f"Successfully downloaded data for ticker {ticker}.")
            return df
        except Exception as e:
            logging.error(f"Error downloading data for ticker {ticker}: {e}")
            return None