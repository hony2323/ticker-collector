from src.base.collectors.http_collector import HTTPCollector
from src.base.collectors.socket_collector import SocketCollector
from src.base.manager.collector_manager import CollectorManager

# Instantiate collectors
http_collector = HTTPCollector()
socket_collector = SocketCollector()

# Manage and start collectors
manager = CollectorManager(collectors=[http_collector, socket_collector])
manager.start_collectors()

# Keep the main thread alive to allow collectors to run
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
