import time
from src.core.interfaces import ExchangeCollector


class HTTPCollector(ExchangeCollector):

    def run(self):
        """Run an operational loop for HTTP requests."""
        while True:
            # Simulated HTTP request fetching ticker data
            print("HTTPCollector fetching data...")
            data = {"BTCUSDT": {"price": "27000", "volume": "1000"}}
            print(f"HTTPCollector received data: {data}")
            time.sleep(5)  # Simulate periodic HTTP polling

    def dispose(self):
        pass

    def retry(self):
        pass
