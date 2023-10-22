from tkinter.ttk import Treeview
import requests
import tkinter as tk
from tkinter import (
    BOTTOM,
    CENTER,
    DISABLED,
    END,
    FLAT,
    NORMAL,
    RAISED,
    SUNKEN,
    TOP,
    WORD,
    Entry,
    Frame,
    IntVar,
    Label,
    OptionMenu,
    PhotoImage,
    Button,
    Radiobutton,
    StringVar,
    Text,
    Widget,
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()


APP_BG = "#26242f"
APP_TITLE = "Duplicated Student Detector"
APP_SIZE = "800x300"


def find_widget_by_id(widget_id, parent_frame):
    for child in parent_frame.winfo_children():
        if child.winfo_name() == widget_id:
            return child
    return None


def center_window(window: tk.Tk):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 4
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


URL = "http://api.forismatic.com/api/1.0/"
METHOD = "getQuote"
FORMAT_JSON = "json"
LANG = "en"

PARAMS = {
    "method": METHOD,
    "format": FORMAT_JSON,
    "lang": LANG
}

def search_quote() -> (str, str):
    while True:
        MAX: int = 5
        i: int = 1
        try:
            response = requests.get(URL, params=PARAMS)
            if response.status_code == 200:
                data = response.json()
                break
            else:
                raise requests.exceptions.RequestException("Not 200 Code")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            i = i + 1
            if i > MAX: return str(e), "Error occured"
    quote = data["quoteText"]
    author = data["quoteAuthor"]
    return quote, author

def organize_top(frame: Frame) -> None:
    quote, author = search_quote()
    
    # Create labels for quote and author
    quote_label = Label(frame, text="Quote:")
    quote_label.grid(row=0,column=0, **PADDING)

    # Create text box to display the quote
    quote_text = Text(frame, wrap=WORD, height=3)
    quote_text.insert(END, quote)
    quote_text.config(state=DISABLED)
    quote_text.grid(row=1,column=0, **PADDING)

    author_label = Label(frame, text="Author:")
    author_label.grid(row=0,column=1, **PADDING)

    # Create text box to display the author
    author_text = Text(frame, wrap=WORD, height=1)
    author_text.insert(END, author)
    author_text.config(state=DISABLED)
    author_text.grid(row=1,column=1, **PADDING)
    
    quote_text.config(width=max(40, len(quote) // 2))
    author_text.config(width=max(40, len(author) // 2))
    
    def reload_quote() -> None:
        new_quote, new_author = search_quote()
        quote_text.config(state=NORMAL)
        author_text.config(state=NORMAL)
        quote_text.delete(1.0, END)
        author_text.delete(1.0, END)
        quote_text.insert(END, new_quote)
        author_text.insert(END, new_author)
        quote_text.config(state=DISABLED)
        author_text.config(state=DISABLED)
        
    #Search for new quote
    btn_search_quote = tk.Button(frame, text="Search for New Quote", command=reload_quote)
    btn_search_quote.grid(row=2,column=0, columnspan=2)

    

def choose_dic(folder_path, frame) -> None:
    folder_path: Entry = find_widget_by_id("folder_path_entry", frame)
    folder_path.configure(state=NORMAL)
    text_to_set = "This is the text I want to set."
    folder_path.delete(0, tk.END)  # Clear any existing text
    folder_path.insert(0, text_to_set)  # Set the t
    folder_path.configure(state=DISABLED)


FILE_FORMAT_OPTIONS = [".csv", ".pdf"]
PADDING = {'padx': 5, 'pady': 5}

is_active_radio = False

def on_change_radio_has_header() -> None:
    global is_active_radio
    if is_active_radio:
        VAR_HAS_HEADER.set(1 - VAR_HAS_HEADER.get())
        is_active_radio = not is_active_radio
    else:
        is_active_radio = not is_active_radio

def on_file_format_changed(format: StringVar, frame: Frame) -> None:
    # Specify seperator if .csv-Type is selected
    if format.get() == FILE_FORMAT_OPTIONS[0]:
        seperator: Entry = Entry(frame, name="seperator")
        seperator.grid(row=1, column=1, **PADDING)
        global VAR_HAS_HEADER
        VAR_HAS_HEADER = IntVar()
        has_header = Radiobutton(frame, name="radiobutton_header1", text="Have the .csv files headers? ", variable=VAR_HAS_HEADER, value=1, command=on_change_radio_has_header)
        has_header.grid(row=1, column=2, **PADDING)
    else:
        seperator: Entry = find_widget_by_id("seperator", frame)
        has_header: Radiobutton = find_widget_by_id("radiobutton_header1", frame)
        if seperator != None and has_header != None:
            seperator.grid_remove()
            has_header.grid_remove()

def adjust_height_of_student_table(event):
    students_table.update_idletasks()
    students_table_height = students_table.bbox("all")[3] - students_table.bbox("all")[1]
    students_table.config(height=students_table_height)

    
def set_students_in_student_table(students: Treeview) -> None:
    print("Missing Impl.")

def organize_middle(frame: Frame) -> None:
    folder_path: Entry = Entry(frame, state=DISABLED, name="folder_path_entry")
    folder_path.grid(row=0, column=0)
    btn_set_folder = Button(
        frame, text="Choose Folder", command=lambda: choose_dic(folder_path, frame)
    )
    btn_set_folder.grid(row=0, column=1, **PADDING)
    # Starting Building the second row
    format = StringVar()
    format.set("Choose a format")
    format.trace("w", lambda *args: on_file_format_changed(format, frame))
    file_format_drop = OptionMenu(frame, format, *FILE_FORMAT_OPTIONS)
    file_format_drop.grid(row=1, column=0, **PADDING)
    #The start and restart btn
    btn_start: Button = Button(
        frame, name="btn_start", text="Start analyse", command=lambda: print("Dummy Value")
    )
    btn_restart: Button = Button(
        frame, name="btn_restart", text="Restart analyse", command=lambda: print("Dummy Value")
    )
    btn_start.grid(row=2, column=0, **PADDING)
    btn_restart.grid(row=2, column=1, **PADDING)
    #Building the table
    global students_table
    students_table = Treeview(frame, columns=("Name", "Username", "Email"), show="headings")
    students_table.heading("Name", text="Name")
    students_table.heading("Username", text="Username")
    students_table.heading("Email", text="Email")
    students_table.column("Name", width=100)
    students_table.column("Username", width=100)
    students_table.column("Email", width=200)

    # Insert sample data into the table
    data = [("John Doe", "johndoe", "johndoe@example.com"),
            ("Jane Smith", "janesmith", "janesmith@example.com")]

    for item in data:
        students_table.insert("", "end", values=item)
    students_table.grid(row=3, column=0, columnspan=3, **PADDING)
    students_table.bind("<Configure>", adjust_height_of_student_table)
    
    #Save btn
    btn_save: Button = Button(
        frame, text="Save", command=lambda: set_students_in_student_table(students_table)
    )
    btn_save.grid(row=4, column=0, columnspan=3, **PADDING)


def organize_bottom(frame: Frame) -> None:
    btn_close: Button = Button(
        frame, name="btn_close", text="Close the application", command=app.quit
    )
    btn_close.place(relx=.5, rely=.5,anchor= CENTER)


if __name__ == "__main__":
    app = App()
    app.title(APP_TITLE)
    app.geometry(APP_SIZE)
    app.config(bg=APP_BG)
    center_window(app)
    # Defining the frameing containers
    froot: Frame = Frame(app, bg=APP_BG)
    fhead: Frame = Frame(
        froot,
        bg=APP_BG,
        relief=RAISED,
        highlightthickness=0.5,
        highlightbackground="white",
    )
    fmiddle: Frame = Frame(
        froot,
        bg=APP_BG,
        relief=FLAT,
        highlightthickness=0.5,
        highlightbackground="white",
    )
    ffooter: Frame = Frame(
        froot,
        bg=APP_BG,
        relief=SUNKEN,
        highlightthickness=0.5,
        highlightbackground="white",
    )
    # Adding the needed elements to the frames
    organize_top(fhead)
    organize_middle(fmiddle)
    organize_bottom(ffooter)
    # Rendering the frames
    froot.pack(fill="both", expand=True)
    fhead.pack(fill="both", side=TOP) #, **PADDING
    fmiddle.pack(fill="both", expand=True)
    ffooter.pack(fill="both", side=BOTTOM, ipady=30)
    # Start the applcation
    app.mainloop()
