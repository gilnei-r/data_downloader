import unittest
from unittest.mock import MagicMock
import pandas as pd
import os
from datetime import datetime
from src.services.downloader_service import DownloaderService
from src.models.historical_data import HistoricalData

class TestDownloaderService(unittest.TestCase):
    def test_download_data(self):
        # Arrange
        mock_provider = MagicMock()
        mock_provider.connect.return_value = True
        mock_provider.get_data.return_value = [
            HistoricalData(datetime(2023, 1, 1), 150.0, 152.0, 149.0, 151.0),
            HistoricalData(datetime(2023, 1, 2), 151.0, 153.0, 150.0, 152.0),
        ]

        downloader = DownloaderService(mock_provider)
        tickers = ['PETR4', 'VALE3'] 
        tickers_df = pd.DataFrame({'symbol': tickers, 'provider': ['metatrader5'] * len(tickers)})
        data_dir = 'test_data'

        # Act
        downloader.download_data(tickers, datetime(2023, 1, 1), datetime(2023, 1, 2), data_dir)

        # Assert
        self.assertTrue(os.path.exists(data_dir))
        for ticker in tickers:
            file_path = os.path.join(data_dir, f'{ticker}_mt5.csv')
            self.assertTrue(os.path.exists(file_path))
            df = pd.read_csv(file_path)
            self.assertEqual(len(df), 2)

        # Clean up
        for ticker in tickers:
            os.remove(os.path.join(data_dir, f'{ticker}_mt5.csv'))
        os.rmdir(data_dir)

if __name__ == '__main__':
    unittest.main()
