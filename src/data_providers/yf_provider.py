
import yfinance as yf
from datetime import datetime
from typing import List
import pandas as pd
from src.models.historical_data import HistoricalData
from src.data_providers import BaseProvider

class YFProvider(BaseProvider):
    """Yahoo Finance provider."""

    def connect(self) -> bool:
        """Connects to Yahoo Finance."""
        return True

    def disconnect(self):
        """Disconnects from Yahoo Finance."""
        pass

    def get_data(self, symbol: str, from_date: datetime, to_date: datetime) -> List[HistoricalData]:
        """Gets historical data for a symbol.

        Args:
            symbol: The ticker symbol.
            from_date: The start date for the data.
            to_date: The end date for the data.

        Returns:
            A list of HistoricalData objects.
        """
        for i in range(3): # 3 retries
            try:
                ticker = yf.Ticker(symbol)
                data_df = ticker.history(start=from_date, end=to_date)
                
                if data_df.empty:
                    print(f"No data found for {symbol}")
                    return []

                data = []
                for index, row in data_df.iterrows():
                    data.append(
                        HistoricalData(
                            date=index.date(),
                            open=row['Open'],
                            high=row['High'],
                            low=row['Low'],
                            close=row['Close'],
                            volume=row['Volume']
                        )
                    )
                return data
            except Exception as e:
                print(f"Error downloading data for {symbol}: {e}. Retry {i+1}/3")
        
        print(f"Failed to download data for {symbol} after 3 retries.")
        return []
