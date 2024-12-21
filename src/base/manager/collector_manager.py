import asyncio

class CollectorManager:
    def __init__(self, collectors):
        """
        :param collectors: List of collector instances
        """
        self.collectors = collectors
        self.tasks = []

    async def start_collectors(self):
        """Start all collectors and wait for them indefinitely."""
        for collector in self.collectors:
            task = asyncio.create_task(self._collector_wrapper(collector))
            self.tasks.append(task)
            print(f"Started collector: {collector.__class__.__name__}")
        # Wait for all tasks to complete (this blocks until all collectors are stopped)
        await asyncio.gather(*self.tasks)

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
        # Cancel running tasks
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)
        print("All collectors have been stopped.")
