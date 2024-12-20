import asyncio

class DataPipeline:
    def __init__(self, collector, parser, submitter):
        """
        :param collector: An instance of ExchangeCollector
        :param parser: An instance of Parser
        :param submitter: An instance of Submitter
        """
        self.collector = collector
        self.parser = parser
        self.submitter = submitter

    async def _execute(self, raw_data):
        """
        Process the raw data through the pipeline asynchronously.
        :param raw_data: Raw data fetched by the collector
        """
        try:
            parsed_data = self.parser.parse(raw_data)
            await asyncio.to_thread(self.submitter.submit, parsed_data)
        except Exception as e:
            print(f"Pipeline execution error: {e}")

    def execute(self, raw_data):
        """
        Public method to run the asynchronous pipeline execution non-blocking.
        :param raw_data: Raw data fetched by the collector
        """
        asyncio.create_task(self._execute(raw_data))  # Fire-and-forget
