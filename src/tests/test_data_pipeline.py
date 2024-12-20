import unittest
from unittest.mock import MagicMock
from src.base.orchestrator.data_pipeline import DataPipeline

class TestDataPipeline(unittest.TestCase):
    def test_execute(self):
        # Mock components
        mock_parser = MagicMock()
        mock_parser.parse.return_value = {"parsed": "data"}

        mock_submitter = MagicMock()

        # Create the pipeline
        pipeline = DataPipeline(
            collector=None,  # Collector is unused directly in the pipeline
            parser=mock_parser,
            submitter=mock_submitter
        )

        # Execute the pipeline
        raw_data = {"BTC": {"price": 45000, "volume": 1200}}
        pipeline.execute(raw_data)

        # Verify parser and submitter calls
        mock_parser.parse.assert_called_once_with(raw_data)
        mock_submitter.submit.assert_called_once_with({"parsed": "data"})

if __name__ == "__main__":
    unittest.main()
