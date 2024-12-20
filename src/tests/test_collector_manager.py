import unittest
from unittest.mock import MagicMock
from src.base.collectors.http_collector import HTTPCollector
from src.base.manager.collector_manager import CollectorManager
import time

class TestCollectorManager(unittest.TestCase):
    def test_start_and_stop_collectors(self):
        # Mock collector
        mock_collector = MagicMock()
        mock_collector.run = MagicMock(side_effect=lambda: time.sleep(1))  # Simulate work

        # Create manager
        manager = CollectorManager(collectors=[mock_collector])

        # Start collectors
        manager.start_collectors()
        self.assertEqual(len(manager.threads), 1)
        self.assertTrue(manager.threads[0].is_alive())

        # Stop collectors
        manager.stop_collectors()

        # Validate threads are no longer alive
        self.assertFalse(manager.threads[0].is_alive())
        print("Test passed: Threads stopped gracefully.")

if __name__ == "__main__":
    unittest.main()
