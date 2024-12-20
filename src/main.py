import asyncio
from src.base.collectors.http_collector import HTTPCollector
from src.base.orchestrator.data_pipeline import DataPipeline
from src.base.manager.collector_manager import CollectorManager
from src.base.parsers.generic_parser import GenericParser
from src.base.submitters.local_storage_submitter import LocalStorageSubmitter


async def main():
    # Create parser and submitter
    parser = GenericParser()
    submitter = LocalStorageSubmitter()

    # Create pipeline
    pipeline = DataPipeline(
        collector=None,  # Collector doesn't directly interact with the pipeline here
        parser=parser,
        submitter=submitter,
    )

    # Instantiate collectors with the pipeline
    http_collector = HTTPCollector(
        url="https://api.example.com/data",
        interval=1,
        pipeline=pipeline
    )

    # Create and start the manager
    manager = CollectorManager(collectors=[http_collector])
    await manager.start_collectors()

    # Let collectors run for a while
    await asyncio.sleep(10)

    # Stop collectors
    await manager.stop_collectors()

if __name__ == "__main__":
    asyncio.run(main())
