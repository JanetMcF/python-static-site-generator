import re
from collections.abc import Mapping
from yaml import load, FullLoader


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def __init__(self, metadata, content):
        self.metadata = metadata
        self.data["content"] = content

    @classmethod
    def load(cls, string):
        (_, fm, content) = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if 'type' in self.data:
            return self.data["type"]
        else:
            return None

    @type.setter
    def type(self, type):
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for (key, value) in self.data.items():
            if key != "content":
                data[key] = value

        return str(data)

