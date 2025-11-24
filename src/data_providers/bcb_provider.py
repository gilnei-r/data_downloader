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
            
            all_data = []
            current_date = from_date
            chunk_num = 0
            while current_date <= to_date:
                chunk_num += 1
                chunk_end_date = current_date + pd.DateOffset(days=365)
                if chunk_end_date > to_date:
                    chunk_end_date = to_date
                
                df_chunk = sgs.get({ticker: int(ticker)}, start=current_date.strftime('%Y-%m-%d'), end=chunk_end_date.strftime('%Y-%m-%d'))
                if not df_chunk.empty:
                    all_data.append(df_chunk)
                
                current_date = chunk_end_date + pd.DateOffset(days=1)

            if not all_data:
                logging.warning(f"No data found for ticker {ticker}")
                return None

            df = pd.concat(all_data)
            df = df.reset_index()
            # Remove duplicates that can occur at chunk boundaries (e.g., monthly data on Jan 1)
            df = df.drop_duplicates(subset=['Date'], keep='first')
            # The Date column already exists from reset_index(), ticker column needs to be renamed to Value
            df.rename(columns={ticker: 'Value'}, inplace=True)
            df['cumulative_factor'] = (1 + df['Value'] / 100).cumprod()
            logging.info(f"Successfully downloaded {len(df)} records for ticker {ticker}.")
            return df
        except Exception as e:
            logging.error(f"Error downloading data for ticker {ticker}: {e}")
            return None