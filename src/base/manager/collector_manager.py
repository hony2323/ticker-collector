import threading


class CollectorManager:
    def __init__(self, collectors):
        """
        :param collectors: List of collector instances
        """
        self.collectors = collectors
        self.threads = []

    def start_collectors(self):
        """Start each collector in a separate thread and wait for all threads to complete."""
        for collector in self.collectors:
            thread = threading.Thread(target=self._collector_wrapper, args=(collector,))
            thread.daemon = True  # Ensure threads exit when the main program exits
            thread.start()
            self.threads.append(thread)
            print(f"\nStarted collector: {collector.__class__.__name__}")

        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()
        print("All collectors have completed.")

    def _collector_wrapper(self, collector):
        """Wrap the collector's run method to handle crashes gracefully."""
        while True:
            try:
                collector.run()
            except Exception as e:
                print(f"Collector {collector.__class__.__name__} encountered an error: {e}")
                collector.retry()  # Retry mechanism for the collector

    def stop_collectors(self):
        """Call the dispose method for each collector."""
        for collector in self.collectors:
            collector.dispose()
        print("All collectors have been disposed.")
