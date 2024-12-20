import unittest
from unittest.mock import MagicMock, patch
from src.base.collectors.http_collector import HTTPCollector
from src.base.orchestrator.data_pipeline import DataPipeline

class TestHTTPCollector(unittest.TestCase):
    @patch("requests.get")
    def test_run_with_pipeline(self, mock_get):
        # Mock the HTTP response
        mock_response = MagicMock()
        mock_response.json.return_value = {"BTC": {"price": 45000, "volume": 1200}}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Mock the pipeline
        mock_pipeline = MagicMock()

        # Create the HTTPCollector
        collector = HTTPCollector(
            url="https://api.example.com/data",
            interval=1,
            pipeline=mock_pipeline
        )

        # Run the collector (simulate one iteration)
        with patch("time.sleep", return_value=None):
            collector.run()

        # Verify the pipeline was executed
        mock_pipeline.execute.assert_called_once_with({"BTC": {"price": 45000, "volume": 1200}})

    def test_dispose(self):
        collector = HTTPCollector(url="https://api.example.com/data")
        collector.dispose()
        self.assertFalse(collector.running)

if __name__ == "__main__":
    unittest.main()
