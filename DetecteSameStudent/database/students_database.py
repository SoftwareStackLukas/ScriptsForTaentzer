"""Stores all students"""
from database.utilis.detector import return_duplicated_students
from database.student import Student

class StudentDatabase:
    """Class representing a database of students"""
    def __init__(self, src_folder) -> None:
        self.students = []
        self.src_folder = src_folder

    def add_student(self, name, username, email) -> None:
        """Adds a student to the database. 
        If the same student is already contained a redunent entry will be attached"""
        student = Student(name, username, email)
        self.students.append(student)

    def import_database(self, importer) -> None:
        """Imports all students. Dependend on the importer. 
        However, the importer shall return a list of Students"""
        raw_data = importer.import_students()
        for row in raw_data:
            self.students.append(row)

    def find_student_by_username(self, target_username) -> Student:
        """Finds a student by the username"""
        for student in self.students:
            if student.username == target_username:
                return student
        return None

    def list_all_students(self) -> list:
        """Simple getter"""
        for student in self.students:
            print(student) #--> make it pretty
        return self.students

    def find_duplicated_students(self) -> list:
        """Returns all duplicated students"""
        return return_duplicated_students(self.students)
