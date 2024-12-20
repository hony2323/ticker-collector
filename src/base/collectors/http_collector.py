import aiohttp
import asyncio

class HTTPCollector:
    def __init__(self, url, auth=None, headers=None, interval=5, pipeline=None):
        self.url = url
        self.auth = auth
        self.headers = headers or {}
        self.interval = interval
        self.pipeline = pipeline
        self.running = True

    async def run(self):
        """Fetch data and pass it to the pipeline asynchronously."""
        while self.running:
            try:
                async with aiohttp.ClientSession(auth=self.auth, headers=self.headers) as session:
                    async with session.get(self.url) as response:
                        response.raise_for_status()
                        data = await response.json()
                        if self.pipeline:
                            await self.pipeline._execute(data)
                await asyncio.sleep(self.interval)
            except Exception as e:
                print(f"HTTPCollector encountered an error: {e}")

    async def dispose(self):
        """Stop the collector loop."""
        self.running = False

    async def retry(self):
        """Handle retry logic asynchronously."""
        print("Retrying HTTPCollector...")
        await asyncio.sleep(2)
