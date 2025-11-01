"""Module for the HistoricalData model."""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class HistoricalData:
    """Dataclass for historical data."""
    date: datetime
    open: float
    high: float
    low: float
    close: float
