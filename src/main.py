import asyncio
from src.base.collectors.http_collector import HTTPCollector
from src.base.orchestrator.data_pipeline import DataPipeline
from src.base.manager.collector_manager import CollectorManager

async def main():
    # Create a pipeline
    pipeline = DataPipeline(
        collector=None,
        parser=None,  # Mock parser
        submitter=None,  # Mock submitter
    )

    # Instantiate collectors
    http_collector = HTTPCollector(
        url="https://api.example.com/data", pipeline=pipeline
    )

    # Manage and start collectors
    manager = CollectorManager(collectors=[http_collector])
    await manager.start_collectors()

    # Simulate running for a while
    await asyncio.sleep(10)

    # Stop collectors
    await manager.stop_collectors()

if __name__ == "__main__":
    asyncio.run(main())
