from database.importer import Importer
from database.student import Student
import csv

class CSV_IMPORTER(Importer):
    """An Importer for data from a csv file"""
    def __init__(self, url_path: str, has_header: bool, seperator: str):
        super().__init__(url_path)
        self.has_header: bool = has_header
        self.seperator: str = seperator
        self.FILE_FORMAT: str = ".csv"

    def import_students(self) -> list[Student]:
        onlyfiles: list[str] = self.load_all_files(self.FILE_FORMAT)
        result: list[Student] = []
        if len(onlyfiles) != 0:
            for file in onlyfiles:
                file_path = self.url_path + "/" + file
                try:
                    with open(file_path, 'r') as open_file:
                        csv_reader = csv.reader(open_file, delimiter=self.seperator)
                        if self.has_header:
                            next(csv_reader, None)  # Skip the header row
                        for row in csv_reader:
                            name, username, email = row #Change here the order of imported students
                            student = Student(name, username, email)
                            result.append(student)
                except csv.Error as e:
                    print(f"CSV Error: {e}")
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        return result

    def load_all_files(self, file_format) -> list[str]:
        return super().load_all_files(file_format)
