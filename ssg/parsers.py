import shutil
from typing import List
from pathlib import Path


class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):
        if self.extensions.__contains__(extension):
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: Path, source: Path, dest: Path):
            raise NotImplementedError

    @classmethod
    def read(cls, path):
        with open(path, 'r') as file:
            file.read()

    @classmethod
    def write(cls, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    @classmethod
    def copy(cls, path, source, dest):
        shutil.copy2(path, dest / source.path)


class ResourceParser(Parser):

    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        pass

    def copy(self, path, source, dest):
        pass