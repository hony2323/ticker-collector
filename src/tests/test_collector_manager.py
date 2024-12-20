import unittest
from src.base.collectors.http_collector import HTTPCollector
from src.base.manager.collector_manager import CollectorManager

class TestCollectorManager(unittest.TestCase):
    def test_start_collectors(self):
        http_collector = HTTPCollector()
        manager = CollectorManager(collectors=[http_collector])

        # Start collectors
        manager.start_collectors()

        # Check that at least one thread is running
        self.assertGreater(len(manager.threads), 0)
