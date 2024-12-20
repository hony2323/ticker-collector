from src.base.collectors.http_collector import HTTPCollector
from src.base.collectors.socket_collector import SocketCollector
from src.base.manager.collector_manager import CollectorManager

def main():
    # Instantiate collectors
    http_collector = HTTPCollector()
    socket_collector = SocketCollector()

    # Manage and start collectors
    manager = CollectorManager(collectors=[http_collector, socket_collector])
    manager.start_collectors()

    print("Stopping collectors...")
    manager.stop_collectors()

if __name__ == "__main__":
    main()
