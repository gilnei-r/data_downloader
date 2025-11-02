import unittest
from unittest.mock import patch
import pandas as pd
from datetime import datetime
from src.data_providers.bcb_provider import BCBProvider

class TestBCBProvider(unittest.TestCase):
    @patch('src.data_providers.bcb_provider.sgs.get')
    def test_get_data(self, mock_sgs_get):
        # Arrange
        mock_df = pd.DataFrame({
            '123': [10, 11, 12]
        }, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))
        mock_sgs_get.return_value = mock_df

        provider = BCBProvider()
        ticker = '123'
        from_date = datetime(2023, 1, 1)
        to_date = datetime(2023, 1, 3)

        # Act
        result_df = provider.get_data(ticker, from_date, to_date)

        # Assert
        self.assertIsInstance(result_df, pd.DataFrame)
        self.assertListEqual(list(result_df.columns), ['Date', 'Value', 'cumulative_factor'])
        self.assertEqual(len(result_df), 3)
        self.assertAlmostEqual(result_df['cumulative_factor'].iloc[-1], 1.2)

if __name__ == '__main__':
    unittest.main()