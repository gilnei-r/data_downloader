import os
import shutil
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch
import pandas as pd
from src.services.downloader_service import DownloaderService
from src.models.historical_data import HistoricalData

class TestDownloaderService(unittest.TestCase):
    """Unit tests for the DownloaderService."""

    def setUp(self):
        """Set up the test environment."""
        self.mock_provider = MagicMock()
        self.downloader = DownloaderService(providers={'mt5': lambda: self.mock_provider})
        self.test_data_dir = 'test_data'
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)

    def tearDown(self):
        """Tear down the test environment."""
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)

    def test_download_data_creates_output_directory(self):
        """Test that download_data creates the output directory if it doesn't exist."""
        shutil.rmtree(self.test_data_dir)
        tickers_df = pd.DataFrame({'symbol': ['TICKER'], 'provider': ['mt5']})
        self.downloader.download_data(tickers_df, datetime(2023, 1, 1), datetime(2023, 1, 2), self.test_data_dir)
        self.assertTrue(os.path.exists(self.test_data_dir))

    def test_download_data_saves_data_to_specified_directory(self):
        """Test that download_data saves data to the specified directory."""
        self.mock_provider.connect.return_value = True
        self.mock_provider.get_data.return_value = [
            HistoricalData(datetime(2023, 1, 1), 1, 2, 0, 1.5, 1000)
        ]
        
        tickers_df = pd.DataFrame({'symbol': ['TICKER'], 'provider': ['mt5']})
        self.downloader.download_data(tickers_df, datetime(2023, 1, 1), datetime(2023, 1, 2), self.test_data_dir)
        
        expected_file_path = os.path.join(self.test_data_dir, 'TICKER.csv')
        self.assertTrue(os.path.exists(expected_file_path))

    def test_download_data_continues_when_provider_raises_exception(self):
        """Test that download_data logs the error and continues to the next ticker when a provider raises an exception."""
        self.mock_provider.connect.return_value = True
        # First ticker raises an exception (e.g. ticker not found in Metastock),
        # second ticker returns valid data.
        self.mock_provider.get_data.side_effect = [
            Exception("Ticker NOTFOUND not found in Metastock data"),
            [HistoricalData(datetime(2023, 1, 1), 1, 2, 0, 1.5, 1000)]
        ]

        tickers_df = pd.DataFrame({'symbol': ['BADTICKER', 'GOODTICKER'], 'provider': ['mt5', 'mt5']})
        with self.assertLogs(level='ERROR') as logs:
            self.downloader.download_data(
                tickers_df, datetime(2023, 1, 1), datetime(2023, 1, 2), self.test_data_dir
            )

        # The failure must be logged and must not abort the whole loop.
        self.assertTrue(any('BADTICKER' in message for message in logs.output))
        # The second ticker must still have been processed and saved.
        expected_file_path = os.path.join(self.test_data_dir, 'GOODTICKER.csv')
        self.assertTrue(os.path.exists(expected_file_path))

    def test_download_data_uses_base_ticker_name(self):
        """Test that the saved file uses the base ticker name without exchange suffix."""
        self.mock_provider.connect.return_value = True
        self.mock_provider.get_data.return_value = [
            HistoricalData(datetime(2023, 1, 1), 1, 2, 0, 1.5, 1000)
        ]

        tickers_df = pd.DataFrame({'symbol': ['BBDC4.SA'], 'provider': ['mt5']})
        self.downloader.download_data(tickers_df, datetime(2023, 1, 1), datetime(2023, 1, 2), self.test_data_dir)

        expected_file_path = os.path.join(self.test_data_dir, 'BBDC4.csv')
        self.assertTrue(os.path.exists(expected_file_path))
