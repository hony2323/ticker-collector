from src.core.interfaces import Parser


class GenericParser(Parser):
    def parse(self, raw_data):
        # Normalize raw data to a standard format
        parsed_data = []
        for ticker, details in raw_data.items():
            parsed_data.append({
                "ticker": ticker,
                "price": float(details["price"]),
                "volume": float(details["volume"])
            })
        return parsed_data
