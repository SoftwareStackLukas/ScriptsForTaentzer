"""Represents an Abstract interface for the importer"""
from abc import ABC, abstractmethod

class Importer(ABC):
    """Abstract class of an importer"""
    def __init__(self, url_path) -> None:
        self.url_path = url_path
        #pass

    @abstractmethod
    def import_students(self) -> list:
        """Abstract methods to import students. Shall return a list of students"""
        pass
