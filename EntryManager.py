import os
from resources import Entry


class EntryManager:
    entries: list[Entry]
    data_path: str

    def __init__(self, data_path):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for value in self.entries:
            value.save(self.data_path)

    def load(self):
        file_names = os.listdir(self.data_path)
        for file_name in file_names:
            if file_name.endswith(".json"):
                file_path = os.path.join(self.data_path, file_name)
                entry = Entry.load(file_path)
                self.entries.append(entry)


grocery_list = Entry("Grocery List")