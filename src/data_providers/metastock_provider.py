import pandas as pd
import yaml
import logging
from datetime import datetime
from metastock2pd import metastock_read
from src.models.historical_data import HistoricalData

logging.basicConfig(level=logging.INFO)

class MetastockProvider:
    def __init__(self):
        try:
            logging.info("Initializing MetastockProvider")
            with open('config.yaml', 'r') as f:
                config = yaml.safe_load(f)
                self.data_path = config['metastock_data_path']
            logging.info("MetastockProvider initialized successfully")
        except FileNotFoundError:
            logging.error("Config file not found")
            raise Exception("Config file not found")
        except KeyError:
            logging.error("metastock_data_path not found in config file")
            raise Exception("metastock_data_path not found in config file")

    def get_data(self, ticker: str, from_date: datetime, to_date: datetime) -> list[HistoricalData]:
        logging.info(f"Getting historical data for {ticker}")
        try:
            df = metastock_read(self.data_path, ticker)
            df = df[(df['date'] >= from_date) & (df['date'] <= to_date)]
            
            data = []
            for _, row in df.iterrows():
                data.append(HistoricalData(
                    date=row['date'],
                    open=row['open'],
                    high=row['high'],
                    low=row['low'],
                    close=row['close'],
                    volume=row['volume']
                ))
            
            logging.info(f"Successfully loaded data for {ticker}")
            return data
        except Exception as e:
            logging.error(f"Could not load data for ticker {ticker}: {e}")
            raise Exception(f"Could not load data for ticker {ticker}: {e}")
