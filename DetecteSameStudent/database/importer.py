"""Represents an Abstract interface for the importer"""
from abc import ABC, abstractmethod
from os import listdir
from os.path import isfile, join

from database.student import Student

class Importer(ABC):
    """Abstract class of an importer"""
    def __init__(self, url_path: str) -> None:
        self.url_path = url_path

    @abstractmethod
    def import_students(self) -> list[Student]:
        """Abstract methods to import students. Shall return a list of students"""
        pass
    
    def load_all_files(self, file_format: str) -> list[str]:
        try:
            onlyfiles = [f for f in listdir(self.url_path) if isfile(join(self.url_path, f))]
            onlyfiles = [f for f in onlyfiles if f.endswith(file_format)]
        except Exception as e:
            print("Error: " + e)
        return onlyfiles
