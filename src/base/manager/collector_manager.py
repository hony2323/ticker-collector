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

    def stop_collectors(self):
        """Stop all collector threads."""
        for thread in self.threads:
            if thread.is_alive():
                print(f"Stopping thread: {thread.name}")
                # Ensure the thread completes its current task
                thread.join()
        print("All collectors have been stopped.")
