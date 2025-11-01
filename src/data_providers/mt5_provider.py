"""Module for the Metatrader5 data provider."""
import MetaTrader5 as mt5
from datetime import datetime
from typing import List
from src.models.historical_data import HistoricalData
from src.data_providers import BaseProvider

class MT5Provider(BaseProvider):
    """Metatrader5 data provider."""
    def __init__(self, login, password, server):
        """Initializes the MT5Provider.

        Args:
            login: The Metatrader5 login.
            password: The Metatrader5 password.
            server: The Metatrader5 server.
        """
        self.login = login
        self.password = password
        self.server = server

    def connect(self):
        """Connects to Metatrader5."""
        if not mt5.initialize(login=self.login, password=self.password, server=self.server):
            print(f"initialize() failed, error code = {mt5.last_error()}")
            return False
        return True

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
                )
            )
        return data
