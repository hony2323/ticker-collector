import json
import os
from datetime import datetime

import aiofiles

from src.core.interfaces import Submitter
from asyncio import Lock


class JSONLinesFileWriter(Submitter):
    def __init__(self, base_path):
        """
        :param base_path: Base directory where files will be saved.
        """
        self.base_path = base_path
        self.lock = Lock()  # To ensure asynchronous safety
        print(f"JSONLinesFileWriter initialized with base path: {self.base_path}")

    def _get_file_path(self, exchange_name, timestamp):
        """
        Generate the file path based on exchange name and date.
        :param exchange_name: Name of the exchange (e.g., OKX).
        :param timestamp: Unix timestamp of the data.
        :return: Full file path for the data file.
        """
        print(f"Generating file path for exchange: {exchange_name}, timestamp: {timestamp}")
        day = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d_%H00")
        dir_path = os.path.join(self.base_path, exchange_name, day)
        os.makedirs(dir_path, exist_ok=True)  # Ensure the directory exists
        file_path = os.path.join(dir_path, f"data.jsonl")
        print(f"File path generated: {file_path}")
        return file_path

    async def submit(self, data):
        """
        Append a single parsed record to the JSON Lines file.
        :param data: A dictionary representing the parsed record.
        """
        print(f"Submitting data: {data}")
        exchange_name = data["exchange"]
        timestamp = data["timestamp"]
        file_path = self._get_file_path(exchange_name, timestamp)

        async with self.lock:  # Asynchronously acquire the lock
            try:
                print(f"Acquired lock for file: {file_path}")
                async with aiofiles.open(file_path, 'a', encoding='utf-8') as file:
                    await file.write(json.dumps(data) + '\n')
                print(f"Successfully wrote data to file: {file_path}")
            except Exception as e:
                print(f"Error writing to file: {e}")

    async def read_all(self, exchange_name, day):
        """
        Read all records from the JSON Lines file for a specific exchange and day.
        :param exchange_name: Name of the exchange.
        :param day: Date in the format YYYY-MM-DD.
        :return: A list of dictionaries.
        """
        file_path = os.path.join(self.base_path, exchange_name, day, "data.jsonl")
        print(f"Reading all data from file: {file_path}")

        async with self.lock:
            try:
                async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
                    records = [json.loads(line) async for line in file]
                    print(f"Successfully read {len(records)} records from file: {file_path}")
                    return records
            except FileNotFoundError:
                print(f"File not found: {file_path}")
                return []
            except Exception as e:
                print(f"Error reading from file: {e}")
                return []
