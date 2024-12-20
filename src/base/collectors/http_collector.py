import requests
import time
from src.core.interfaces import ExchangeCollector

class HTTPCollector(ExchangeCollector):
    def __init__(self, url, auth=None, headers=None, interval=5, pipeline=None):
        """
        :param url: API endpoint to fetch data from
        :param auth: Authentication information (e.g., token or basic auth tuple)
        :param headers: Additional headers for the HTTP request
        :param interval: Time interval (in seconds) between requests
        :param pipeline: An instance of DataPipeline
        """
        self.url = url
        self.auth = auth
        self.headers = headers or {}
        self.interval = interval
        self.pipeline = pipeline
        self.running = True

    def run(self):
        """Fetch data and pass it to the pipeline."""
        while self.running:
            try:
                response = requests.get(self.url, auth=self.auth, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                if self.pipeline:
                    self.pipeline.execute(data)
                time.sleep(self.interval)
            except requests.RequestException as e:
                print(f"HTTPCollector encountered an error: {e}")

    def dispose(self):
        """Stop the collector loop."""
        self.running = False

    def retry(self):
        """Handle retry logic if needed."""
        print("Retrying HTTPCollector...")
        time.sleep(2)
