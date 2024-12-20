from abc import ABC, abstractmethod

class ExchangeCollector(ABC):
    @abstractmethod
    def run(self):
        """Run the collector's operational loop."""
        pass

class Parser(ABC):
    @abstractmethod
    def parse(self, raw_data):
        """Normalize raw ticker data into a standard format."""
        pass

class Submitter(ABC):
    @abstractmethod
    def submit(self, data):
        """Submit parsed data to a destination."""
        pass

class Orchestrator(ABC):
    @abstractmethod
    def execute(self):
        """Coordinate the collection, parsing, and submission of data."""
        pass
