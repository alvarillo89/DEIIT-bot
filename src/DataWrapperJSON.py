import json

class DataWrapperJSON:
    def load_subject(self, path):
        with open(path, 'r') as f:
            self.subjects = json.load(f)