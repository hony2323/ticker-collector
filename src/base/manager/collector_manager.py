import asyncio

class CollectorManager:
    def __init__(self, collectors):
        """
        :param collectors: List of collector instances
        """
        self.collectors = collectors
        self.tasks = []

    async def start_collectors(self):
        """Start each collector asynchronously."""
        for collector in self.collectors:
            task = asyncio.create_task(self._collector_wrapper(collector))
            self.tasks.append(task)
            print(f"Started collector: {collector.__class__.__name__}")

    async def _collector_wrapper(self, collector):
        """Wrap the collector's run method to handle errors gracefully."""
        while True:
            try:
                await collector.run()
            except Exception as e:
                print(f"Collector {collector.__class__.__name__} encountered an error: {e}")
                await collector.retry()

    async def stop_collectors(self):
        """Stop all collector tasks gracefully."""
        for collector in self.collectors:
            await collector.dispose()
        await asyncio.gather(*self.tasks, return_exceptions=True)
        print("All collectors have been stopped.")
