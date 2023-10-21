from database.csvimport import CSV_IMPORTER
from database.students_database import StudentDatabase
import os

from rich import print
from rich.panel import Panel

instructions = """
1.) The structure of the CSV file shall be: name, username, email
2.) It can contain or not the header. This can be specified via the console.
3.) You can compare multiple .csv files for redundant data.
4.) Please, provide the whole path to the folder in which all .csv files are stored.
5.) This is just a demo version and can be extended in future.
"""

panel = Panel.fit(instructions, title="Attention! Please, consider the following rules", border_style="blue")
print(panel)

while True:
    #Add a selector for csv, pdf etc.
    try:
        src = input("Src folder: ")
        user_input = input("Has Header (y/n): ").strip().lower()
        has_header = {"y": True, "n": False}.get(user_input, False)
        seperator = input("Seperator: ")
        db = StudentDatabase()
        importer = CSV_IMPORTER(src, has_header, seperator)
        db.import_database(importer)
        output = db.find_duplicated_students()  # Assuming this returns a list of objects
        output.sort(key=lambda student: (student.name, student.username))  # Assuming 'name' is the attribute to sort by
       
        if len(output) >= 1:
            BASE_PATH = src + "\\output_folder\\"
            if not os.path.exists(BASE_PATH):
                os.makedirs(BASE_PATH)
            # Specify the file path where you want to write the output       
            OUTPUT_FILE_PATH = BASE_PATH + "output.txt"
            if os.path.exists(OUTPUT_FILE_PATH):
                user_input_overwrite = input("File already exists. Shall it be overwriten (y/n)?: ").strip().lower()
                shall_overwrite = {"y": True, "n": False}.get(user_input_overwrite, False)
                if not shall_overwrite:
                    i = 0
                    POSITION = -4
                    TEMP = OUTPUT_FILE_PATH
                    while True:
                        #Check if -3 is correct or rather -4
                        if os.path.exists(TEMP[:POSITION] + str(i) + TEMP[POSITION:]):
                            i = i + 1
                        else:
                            break
                    OUTPUT_FILE_PATH = TEMP[:POSITION] + str(i) + TEMP[POSITION:]
                                
            # Open the file in write mode and write the output
            with open(OUTPUT_FILE_PATH, "w") as output_file:
                output_file.write("Name, Username, Email\n")
                for student in output:
                    output_file.write(f"{student.name} - {student.username} - {student.email}\n")
            print("Output has been written to", OUTPUT_FILE_PATH)
        else: 
            print("No duplicates found.")
        if input("Exit (y/n)?: ") == "y":
            break
    except Exception as e:
        if input("An error occured. Want to try again (y/n): ") == "n":
            print("Close application based of: " + str(e))
            break
        print("Avoid following mistake: " + str(e))
