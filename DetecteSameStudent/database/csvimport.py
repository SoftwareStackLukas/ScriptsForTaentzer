from database.importer import Importer
from database.student import Student
from os import listdir
from os.path import isfile, join
import csv

class CSV_IMPORTER(Importer):
    """An Importer for data from a csv file"""
    def __init__(self, url_path, has_header, seperator):
        super().__init__(url_path)
        self.has_header = has_header
        self.seperator = seperator

    def import_students(self) -> []:
        onlyfiles = self.load_all_files()
        result: [] = []
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

    def load_all_files(self):
        try:
            onlyfiles = [f for f in listdir(self.url_path) if isfile(join(self.url_path, f))]
            onlyfiles = [f for f in onlyfiles if f.endswith(".csv")]
        except Exception as e:
            print("Error: " + e)
        return onlyfiles

#importing = CSV_IMPORTER("D:\_GitHub_Projects\ScriptsForTaentzer\DetecteSameStudent\csvfiles", False, ",")
#importing = CSV_IMPORTER("csvfiles", False, ",")
#cprint(importing.import_students()[0])
