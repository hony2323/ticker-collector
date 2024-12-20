import threading

class CollectorManager:
    def __init__(self, collectors):
        """
        :param collectors: List of collector instances
        """
        self.collectors = collectors
        self.threads = []

    def start_collectors(self):
        """Start each collector in a separate thread."""
        for collector in self.collectors:
            thread = threading.Thread(target=collector.run)
            thread.daemon = True  # Ensure threads exit when the main program exits
            thread.start()
            self.threads.append(thread)
            print(f"Started collector: {collector.__class__.__name__}")
