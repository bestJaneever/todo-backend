import os
import json


def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(indentation + str(value))


def entry_from_json(dictionary):
    result = Entry(title=dictionary["title"])
    for sub_entry in dictionary.get('entries', []):
        result.add_entry(entry_from_json(sub_entry))
    return result


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def recursive_json(self, entry):
        dictionary = {}
        dictionary["title"] = entry.title
        dictionary["entries"] = []
        for item in entry.entries:
            dictionary["entries"].append(self.recursive_json(item))
        return dictionary

    def json(self):
        return self.recursive_json(self)

    @classmethod
    def from_json(cls, value):
        result = cls(value["title"])
        for sub_value in value.get("entries", []):
            result.add_entry(cls.from_json(sub_value))
        return result

    def save(self, path):
        os.makedirs(path, exist_ok=True)
        f_path = os.path.join(path, f'{self.title}.json')
        content = self.json()
        with open(f_path, "w") as file:
            json.dump(content, file)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            content = json.load(file)
            obj = cls.from_json(content)
            return obj


entry_object1 = Entry("Object1")
entry_object1.add_entry(Entry("test1"))
entry_object1.add_entry((Entry("test2")))

entry_object1.save('/Users/Yauheniya_Hrebianko/Downloads')