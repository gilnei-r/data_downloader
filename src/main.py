"""Main module for the data downloader application."""
import logging
import os
from datetime import datetime
from dotenv import load_dotenv
import yaml
import pandas as pd

from src.data_providers.mt5_provider import MT5Provider
from src.services.downloader_service import DownloaderService

load_dotenv()

# Load configuration from config.yaml
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Application started.")

    # Get settings from config
    start_date_str = config['start_date']
    end_date_str = config['end_date']
    output_dir = config['output_directory']
    tickers_file = config['tickers_file']

    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # Load tickers from CSV
    tickers_df = pd.read_csv(tickers_file)

    # Initialize DownloaderService with a factory for MT5Provider
    provider_factory = {'metatrader5': MT5Provider}
    downloader = DownloaderService(provider_factory)

    # Download data
    downloader.download_data(tickers_df, start_date, end_date, data_dir=output_dir)

    logging.info("Application finished.")

if __name__ == "__main__":
    main()
