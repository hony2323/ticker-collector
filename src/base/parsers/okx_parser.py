import datetime

from src.base.parsers.schemes import validate_and_deserialize
from src.core.interfaces import Parser


class OKXParser(Parser):
    def __init__(self, exchange_name="OKX"):
        self.exchange_name = exchange_name

    def parse(self, raw_data):
        try:
            # Extract the relevant data
            ticker_data = raw_data["data"][0]

            # Normalize to the standard format
            parsed_data = {
                "timestamp": datetime.datetime.utcfromtimestamp(int(ticker_data["ts"]) / 1000).isoformat(),
                "exchange": self.exchange_name,
                "instrument_id": ticker_data["instId"],
                "price": float(ticker_data["last"]),
                "best_bid": float(ticker_data["bidPx"]),
                "best_ask": float(ticker_data["askPx"]),
                "24h_volume": float(ticker_data["vol24h"])
            }

            # Validate against the schema
            return validate_and_deserialize(parsed_data)
        except (KeyError, ValueError, IndexError) as e:
            raise ValueError(f"Failed to parse raw data: {e}")
