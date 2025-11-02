"""Module for the HistoricalData model."""
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class HistoricalData:
    """Dataclass for historical data."""
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    def to_dict(self):
        return asdict(self)
