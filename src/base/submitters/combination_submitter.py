import asyncio

from src.core.interfaces import Submitter


class CombinationSubmitter(Submitter):
    def __init__(self, submitters):
        """
        :param submitters: A list of Submitter instances.
        """
        self.submitters = submitters
        print(f"CombinationSubmitter initialized with {len(self.submitters)} submitters.")

    async def submit(self, data):
        """
        Submit data to all provided submitters concurrently.
        :param data: A dictionary representing the parsed record.
        """
        print("Submitting data to all submitters.")
        await asyncio.gather(*(submitter.submit(data) for submitter in self.submitters))
        print("Submission completed for all submitters.")
