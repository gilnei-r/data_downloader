"""Main module for the data downloader application."""
import argparse
import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from src.data_providers.mt5_provider import MT5Provider
from src.services.downloader_service import DownloaderService
import pandas as pd

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    """Main function to run the data downloader."""
    parser = argparse.ArgumentParser(description='Data downloader application.')
    parser.add_argument('--output-dir', type=str, default='data', help='The output directory for the downloaded data.')
    args = parser.parse_args()

    logging.info('Application started.')

    provider_factory = {
        'metatrader5': MT5Provider,
    }

    tickers_df = pd.read_csv('tickers.csv')

    downloader = DownloaderService(provider_factory)

    # Download data for the last 365 days
    to_date = datetime.now()
    from_date = datetime(to_date.year - 1, to_date.month, to_date.day)

    downloader.download_data(tickers_df, from_date, to_date, data_dir=args.output_dir)

    logging.info('Application finished.')
