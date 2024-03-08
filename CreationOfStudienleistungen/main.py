from typing import LiteralString
import numpy as np
import re
from openpyxl import Workbook
from openpyxl.styles import Font

def generate_report(input_rows: list[str], user_seperator) -> list:
    formatted_names = []
    error_report = []
    for row in input_rows:
        names_list = row.split(user_seperator)
        names_list = [item for item in names_list if bool(item)]
        for name in names_list:
            ls = name.split(' ')
            ls = [item.strip() for item in ls]
            ls = [item for item in ls if bool(item)]
            if (len(ls) == 3):
                first_name, last_name, mat_num = ls
                mat_num = re.search(r'\d+', mat_num).group()
                arr = np.array([mat_num, last_name, first_name])
                formatted_names.append(arr)
            elif(len(ls) == 2):
                first_name, last_name = ls
                arr = np.array(["???", last_name, first_name])
                formatted_names.append(arr)
            else: 
                error_report.append(' '.join(ls) + '\n')
    if (len(error_report) > 0):
        with open("error report.txt", 'w', encoding='utf-8') as output_file:
            # Write rows to the output file
            for row in error_report:
                output_file.write(row)
    return formatted_names

def import_data(user_input: str) -> list[str]:
    with open(user_input + ".txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def save_to_xlsx(content: list, name: str) -> None:
    wb = Workbook()
    ws = wb.active
    
    bold_font = Font(bold=True)
    ws.append(["Mat.Nr.", "Name", "Vorname"])
    for cell in ws[1]:
        cell.font = bold_font
        
    for row in content: 
        ws.append(row.tolist())
    excel_file_name = name + '.xlsx'
    wb.save(excel_file_name)

# Generate and print the report
user_input = input("Please enter the path and file name for the input: ")
user_path = input("Please enter the path and file name for the output: ")
user_seperator = input("Please enter the seperator (default: ','): ") or ','
data = import_data(user_input)
output_report = generate_report(data, user_seperator)
save_to_xlsx(output_report, user_path)