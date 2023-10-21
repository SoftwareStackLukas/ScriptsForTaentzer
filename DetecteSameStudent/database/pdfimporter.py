from database.importer import Importer
from database.student import Student

class CSV_IMPORTER(Importer):
    """An Importer for data from a csv file"""
    def __init__(self, url_path: str, has_header: bool, seperator: str):
        super().__init__(url_path)
        self.has_header: bool = has_header
        self.seperator: str = seperator
        self.FILE_FORMAT: str = ".pdf"

    def import_students(self) -> list[Student]:
        onlyfiles: list[str] = self.load_all_files(self.FILE_FORMAT)
        result: list[Student] = []
        if len(onlyfiles) != 0:
            for file in onlyfiles:
                file_path = self.url_path + "/" + file
                #Introduce here the reading from the pdf. 
        return result
    
    def load_all_files(self, file_format: str) -> list[str]:
        return super().load_all_files(file_format)


