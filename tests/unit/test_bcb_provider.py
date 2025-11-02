import unittest
from unittest.mock import patch
import pandas as pd
from src.data_providers.bcb_provider import BCBProvider

class TestBCBProvider(unittest.TestCase):
    @patch('src.data_providers.bcb_provider.sgs.get')
    def test_download_data(self, mock_sgs_get):
        # Arrange
        mock_df = pd.DataFrame({
            '123': [10, 20, 30]
        }, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))
        mock_sgs_get.return_value = mock_df

        provider = BCBProvider()
        ticker = '123'

        # Act
        result_df = provider.download_data(ticker)

        # Assert
        self.assertIsInstance(result_df, pd.DataFrame)
        self.assertListEqual(list(result_df.columns), ['Date', 'Value'])
        self.assertEqual(len(result_df), 3)

if __name__ == '__main__':
    unittest.main()
