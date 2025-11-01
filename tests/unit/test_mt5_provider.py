import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.data_providers.mt5_provider import MT5Provider

class TestMT5Provider(unittest.TestCase):
    @patch('src.data_providers.mt5_provider.mt5')
    def test_get_data_success(self, mock_mt5):
        # Arrange
        mock_rates = [
            {'time': 1672531200, 'open': 150.0, 'high': 152.0, 'low': 149.0, 'close': 151.0},
            {'time': 1672617600, 'open': 151.0, 'high': 153.0, 'low': 150.0, 'close': 152.0},
        ]
        mock_mt5.copy_rates_range.return_value = mock_rates

        provider = MT5Provider(12345, 'password', 'server')

        # Act
        data = provider.get_data('AAPL', datetime(2023, 1, 1), datetime(2023, 1, 2))

        # Assert
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0].open, 150.0)
        self.assertEqual(data[1].close, 152.0)

    @patch('src.data_providers.mt5_provider.mt5')
    def test_get_data_no_rates(self, mock_mt5):
        # Arrange
        mock_mt5.copy_rates_range.return_value = None

        provider = MT5Provider(12345, 'password', 'server')

        # Act
        data = provider.get_data('AAPL', datetime(2023, 1, 1), datetime(2023, 1, 2))

        # Assert
        self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()
