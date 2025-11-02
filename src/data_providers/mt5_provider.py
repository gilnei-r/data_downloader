"""Module for the Metatrader5 data provider."""
import MetaTrader5 as mt5
from datetime import datetime
from typing import List
from src.models.historical_data import HistoricalData
from src.data_providers import BaseProvider

class MT5Provider(BaseProvider):
    """MetaTrader 5 provider."""

    def __init__(self, login: int = None, password: str = None, server: str = None):
        """Initializes the MT5Provider.

        Args:
            login: The login account number.
            password: The password.
            server: The server name.
        """
        self.login = login
        self.password = password
        self.server = server

    def connect(self) -> bool:
        """Connects to MetaTrader 5."""
        if self.login and self.password and self.server:
            return mt5.initialize(
                login=self.login, password=self.password, server=self.server
            )
        return mt5.initialize()

    def disconnect(self):
        """Disconnects from Metatrader5."""
        mt5.shutdown()

    def get_data(self, symbol: str, from_date: datetime, to_date: datetime) -> List[HistoricalData]:
        """Gets historical data for a symbol.

        Args:
            symbol: The ticker symbol.
            from_date: The start date for the data.
            to_date: The end date for the data.

        Returns:
            A list of HistoricalData objects.
        """
        rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_D1, from_date, to_date)
        if rates is None:
            print(f"No rates found for {symbol}, error code = {mt5.last_error()}")
            return []

        data = []
        for rate in rates:
            data.append(
                HistoricalData(
                    date=datetime.fromtimestamp(rate['time']),
                    open=rate['open'],
                    high=rate['high'],
                    low=rate['low'],
                    close=rate['close'],
                    volume=rate['tick_volume']
                )
            )
        return data
