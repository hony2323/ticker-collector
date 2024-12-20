import asyncio
import time
from src.core.interfaces import ExchangeCollector
import okx.MarketData as MarketData

class OKXCollector(ExchangeCollector):
    def __init__(self, inst_id, flag="0", interval=5, pipeline=None):
        self.inst_id = inst_id
        self.flag = flag
        self.interval = interval
        self.pipeline = pipeline
        self.running = True
        self.market_data_api = MarketData.MarketAPI(flag=self.flag)

    async def run(self):
        """Fetch data and pass it to the pipeline asynchronously."""
        while self.running:
            try:
                result = self.market_data_api.get_ticker(instId=self.inst_id)
                if self.pipeline:
                    self.pipeline.execute(result)  # Non-blocking now
                await asyncio.sleep(self.interval)
            except Exception as e:
                print(f"OKXCollector encountered an error: {e}")

    async def dispose(self):
        """Stop the collector loop."""
        self.running = False

    async def retry(self):
        """Handle retry logic asynchronously."""
        print("Retrying OKXCollector...")
        await asyncio.sleep(2)
