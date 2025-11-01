"""Unit tests for the DownloaderService."""
import os
import shutil
import pandas as pd
from datetime import datetime
from unittest.mock import MagicMock, patch
from src.services.downloader_service import DownloaderService


class TestDownloaderService:
    """Test suite for the DownloaderService."""

    def setup_method(self):
        """Set up the test environment."""
        self.provider_factory = {
            'mock_provider': MagicMock()
        }
        self.downloader = DownloaderService(self.provider_factory)
        self.test_output_dir = 'test_output'

    def teardown_method(self):
        """Tear down the test environment."""
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_download_data_creates_output_directory(self):
        """Test that download_data creates the output directory if it doesn't exist."""
        # Arrange
        tickers_df = pd.DataFrame({'symbol': ['TEST'], 'provider': ['mock_provider']})
        from_date = datetime(2023, 1, 1)
        to_date = datetime(2023, 1, 2)

        # Act
        with patch.dict(os.environ, {'MT5_LOGIN': '12345', 'MT5_PASSWORD': 'password', 'MT5_SERVER': 'server'}):
            self.downloader.download_data(tickers_df, from_date, to_date, data_dir=self.test_output_dir)

        # Assert
        assert os.path.exists(self.test_output_dir)

    def test_download_data_saves_data_to_specified_directory(self):
        """Test that download_data saves the data to the specified directory."""
        # Arrange
        tickers_df = pd.DataFrame({'symbol': ['TEST'], 'provider': ['mock_provider']})
        from_date = datetime(2023, 1, 1)
        to_date = datetime(2023, 1, 2)
        mock_provider_instance = self.provider_factory['mock_provider'].return_value
        mock_provider_instance.connect.return_value = True
        mock_provider_instance.get_data.return_value = [{'date': datetime(2023, 1, 1), 'open': 1, 'high': 2, 'low': 0, 'close': 1.5}]

        # Act
        with patch.dict(os.environ, {'MT5_LOGIN': '12345', 'MT5_PASSWORD': 'password', 'MT5_SERVER': 'server'}):
            self.downloader.download_data(tickers_df, from_date, to_date, data_dir=self.test_output_dir)

        # Assert
        expected_file_path = os.path.join(self.test_output_dir, 'TEST_mock_provider.csv')
        assert os.path.exists(expected_file_path)
        # cleanup
        os.remove(expected_file_path)
