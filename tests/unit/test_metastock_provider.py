import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.data_providers.metastock_provider import MetastockProvider
from src.models.historical_data import HistoricalData
from datetime import datetime

class TestMetastockProvider(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='metastock_data_path: /path/to/data')
    @patch('yaml.safe_load')
    def setUp(self, mock_yaml_safe_load, mock_open):
        mock_yaml_safe_load.return_value = {'metastock_data_path': '/path/to/data'}
        self.provider = MetastockProvider()

    @patch('src.data_providers.metastock_provider.metastock_read')
    def test_get_data_success(self, mock_metastock_read):
        expected_df = pd.DataFrame({
            'date': [datetime(2025, 1, 1)],
            'open': [100],
            'high': [101],
            'low': [99],
            'close': [100],
            'volume': [1000]
        })
        mock_metastock_read.return_value = expected_df
        data = self.provider.get_data('AAPL', datetime(2025, 1, 1), datetime(2025, 1, 2))
        self.assertEqual(len(data), 1)
        self.assertIsInstance(data[0], HistoricalData)

    @patch('src.data_providers.metastock_provider.metastock_read', side_effect=Exception("Ticker not found"))
    def test_get_data_ticker_not_found(self, mock_metastock_read):
        with self.assertRaises(Exception) as context:
            self.provider.get_data('INVALID', datetime(2025, 1, 1), datetime(2025, 1, 2))
        self.assertIn("Could not load data for ticker INVALID", str(context.exception))

    @patch('src.data_providers.metastock_provider.metastock_read', side_effect=Exception("Corrupted file"))
    def test_get_data_corrupted_file(self, mock_metastock_read):
        with self.assertRaises(Exception) as context:
            self.provider.get_data('CORRUPT', datetime(2025, 1, 1), datetime(2025, 1, 2))
        self.assertIn("Could not load data for ticker CORRUPT", str(context.exception))

if __name__ == '__main__':
    unittest.main()
