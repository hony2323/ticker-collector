import asyncio
from src.base.collectors.http_collector import HTTPCollector
from src.base.collectors.okx_collector import OKXCollector
from src.base.orchestrator.data_pipeline import DataPipeline
from src.base.manager.collector_manager import CollectorManager
from src.base.parsers.generic_parser import GenericParser
from src.base.parsers.okx_parser import OKXParser
from src.base.submitters.local_storage_submitter import LocalStorageSubmitter


async def main():
    # Create parser and submitter
    parser = GenericParser()
    okx_parser = OKXParser()
    submitter = LocalStorageSubmitter()

    # Create pipeline
    pipeline = DataPipeline(
        parser=parser,
        submitter=submitter,
    )

    okx_pipeline = DataPipeline(
        parser=okx_parser,
        submitter=submitter,
    )

    # Instantiate collectors with the pipeline
    http_collector = HTTPCollector(
        url="https://api.example.com/data",
        interval=1,
        pipeline=pipeline
    )

    okx_collector = OKXCollector(
        inst_id="BTC-USD-SWAP",
        flag="0",
        interval=1,
        pipeline=okx_pipeline
    )

    # Create and start the manager
    # manager = CollectorManager(collectors=[http_collector, okx_collector])
    manager = CollectorManager(collectors=[okx_collector])
    await manager.start_collectors()

    # Let collectors run for a while
    await asyncio.sleep(10)

    # Stop collectors
    await manager.stop_collectors()


if __name__ == "__main__":
    asyncio.run(main())
