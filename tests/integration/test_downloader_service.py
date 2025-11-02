import unittest
import os
import pandas as pd
from unittest.mock import patch
from src.services.downloader_service import DownloaderService

class TestDownloaderService(unittest.TestCase):
    def test_instantiate_service(self):
        # Arrange
        downloader = DownloaderService()

        # Assert
        self.assertIsInstance(downloader, DownloaderService)

    @patch('src.data_providers.bcb_provider.BCBProvider.download_data')
    def test_download_data_for_bcb_provider(self, mock_download_data):
        # Arrange
        mock_df = pd.DataFrame({
            'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'Value': [10, 20, 30]
        })
        mock_download_data.return_value = mock_df

        tickers_data = {
            'symbol': ['123'],
            'provider': ['BCB']
        }
        tickers_df = pd.DataFrame(tickers_data)

        downloader = DownloaderService()
        data_dir = 'test_data'
        expected_file_path = os.path.join(data_dir, '123_BCB.csv')

        # Act
        downloader.download_data(tickers_df, None, None, data_dir=data_dir)

        # Assert
        self.assertTrue(os.path.exists(expected_file_path))

        # Clean up
        os.remove(expected_file_path)
        os.rmdir(data_dir)

if __name__ == '__main__':
    unittest.main()