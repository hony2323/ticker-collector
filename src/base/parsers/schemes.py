import json

from marshmallow import Schema, fields, post_load, ValidationError


class StandardOutputSchema(Schema):
    timestamp = fields.Float(required=True) # Unix timestamp
    exchange = fields.Str(required=True)  # Name of the exchange
    instrument_id = fields.Str(required=True)  # Trading pair or instrument ID
    price = fields.Float(required=True)  # Last traded price
    best_bid = fields.Float(required=True)  # Highest buy price
    best_ask = fields.Float(required=True)  # Lowest sell price
    volume_24h = fields.Float(required=True, data_key="24h_volume")  # 24-hour trading volume

    @post_load
    def make_standard_output(self, data, **kwargs):
        return StandardOutput(**data)


class StandardOutput:
    def __init__(self, timestamp, exchange, instrument_id, price, best_bid, best_ask, volume_24h):
        self.timestamp = timestamp
        self.exchange = exchange
        self.instrument_id = instrument_id
        self.price = price
        self.best_bid = best_bid
        self.best_ask = best_ask
        self.volume_24h = volume_24h

    def __repr__(self):
        return (
            f"StandardOutput(timestamp={self.timestamp}, exchange={self.exchange}, "
            f"instrument_id={self.instrument_id}, price={self.price}, "
            f"best_bid={self.best_bid}, best_ask={self.best_ask}, volume_24h={self.volume_24h})"
        )

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "exchange": self.exchange,
            "instrument_id": self.instrument_id,
            "price": self.price,
            "best_bid": self.best_bid,
            "best_ask": self.best_ask,
            "24h_volume": self.volume_24h
        }

    def to_json(self):
        return json.dumps(self.to_dict())


# Utility function to validate and deserialize parser output

def validate_and_deserialize(data):
    schema = StandardOutputSchema()
    try:
        return schema.load(data)
    except ValidationError as e:
        print(f"Validation Error: {e.messages}")
        raise
