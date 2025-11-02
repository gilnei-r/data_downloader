import unittest
from src.services.downloader_service import DownloaderService

class TestDownloaderService(unittest.TestCase):
    def test_instantiate_service(self):
        # Arrange
        downloader = DownloaderService()

        # Assert
        self.assertIsInstance(downloader, DownloaderService)

if __name__ == '__main__':
    unittest.main()
