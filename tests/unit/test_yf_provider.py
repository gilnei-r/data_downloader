
import unittest
from unittest.mock import patch, MagicMock
from src.data_providers.yf_provider import YFProvider
from src.models.historical_data import HistoricalData
from datetime import datetime
import pandas as pd

class TestYFProvider(unittest.TestCase):

    @patch('yfinance.Ticker')
    def test_get_data_success(self, mock_ticker):
        # Arrange
        mock_df = pd.DataFrame({
            'Open': [100], 'High': [110], 'Low': [90], 'Close': [105], 'Volume': [1000]
        }, index=pd.to_datetime([datetime(2024, 1, 1)]))
        mock_ticker.return_value.history.return_value = mock_df

        provider = YFProvider()
        
        # Act
        data = provider.get_data('AAPL', datetime(2024, 1, 1), datetime(2024, 1, 2))

        # Assert
        self.assertEqual(len(data), 1)
        self.assertIsInstance(data[0], HistoricalData)
        self.assertEqual(data[0].open, 100)

    @patch('yfinance.Ticker')
    def test_get_data_no_data(self, mock_ticker):
        # Arrange
        mock_ticker.return_value.history.return_value = pd.DataFrame()

        provider = YFProvider()

        # Act
        data = provider.get_data('AAPL', datetime(2024, 1, 1), datetime(2024, 1, 2))

        # Assert
        self.assertEqual(len(data), 0)

    @patch('yfinance.Ticker')
    def test_get_data_exception(self, mock_ticker):
        # Arrange
        mock_ticker.side_effect = Exception("Test Exception")

        provider = YFProvider()

        # Act
        data = provider.get_data('AAPL', datetime(2024, 1, 1), datetime(2024, 1, 2))

        # Assert
        self.assertEqual(len(data), 0)
        # Check if retry logic was called 3 times
        self.assertEqual(mock_ticker.call_count, 3)

if __name__ == '__main__':
    unittest.main()
