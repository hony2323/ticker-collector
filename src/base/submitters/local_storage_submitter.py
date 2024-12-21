import json

import aiofiles

from src.core.interfaces import Submitter
from asyncio import Lock


class LocalStorageSubmitter(Submitter):
    def submit(self, data):
        # Simulate submission to local file
        print(f"Submitting data: {data}")
        return True


class JSONLinesFileWriter(Submitter):
    def __init__(self, file_path):
        """
        :param file_path: Path to the JSON Lines file.
        """
        self.file_path = file_path
        self.lock = Lock()  # To ensure asynchronous safety

    async def submit(self, data):
        """
        Append a single parsed record to the JSON Lines file.
        :param data: A dictionary representing the parsed record.
        """
        async with self.lock:  # Asynchronously acquire the lock
            try:
                async with aiofiles.open(self.file_path, 'a', encoding='utf-8') as file:
                    await file.write(json.dumps(data) + '\n')
            except Exception as e:
                print(f"Error writing to file: {e}")

    async def read_all(self):
        """
        Read all records from the JSON Lines file.
        :return: A list of dictionaries.
        """
        async with self.lock:
            try:
                async with aiofiles.open(self.file_path, 'r', encoding='utf-8') as file:
                    return [json.loads(line) async for line in file]
            except FileNotFoundError:
                print("File not found.")
                return []
            except Exception as e:
                print(f"Error reading from file: {e}")
                return []
