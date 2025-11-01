"""Module for data providers."""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.models.historical_data import HistoricalData

class BaseProvider(ABC):
    """Abstract base class for data providers."""
    @abstractmethod
    def connect(self):
        """Connects to the data provider."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnects from the data provider."""
        pass

    @abstractmethod
    def get_data(self, symbol: str, from_date: datetime, to_date: datetime) -> List[HistoricalData]:
        """Gets historical data for a symbol."""
        pass
