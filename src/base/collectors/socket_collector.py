import time
from src.core.interfaces import ExchangeCollector


class SocketCollector(ExchangeCollector):

    def run(self):
        """Run an operational loop for socket connections."""
        while True:
            # Simulate receiving ticker data over a socket
            print("SocketCollector receiving data...")
            data = {"ETHUSDT": {"price": "1800", "volume": "500"}}
            print(f"SocketCollector received data: {data}")
            time.sleep(2)  # Simulate receiving data over a socket

    def retry(self):
        pass

    def dispose(self):
        pass
