from src.core.interfaces import Submitter


class LocalStorageSubmitter(Submitter):
    def submit(self, data):
        # Simulate submission to local file
        print(f"Submitting data: {data}")
        return True
