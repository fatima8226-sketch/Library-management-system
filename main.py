#------------------------------------IMPORTS-----------------------------------#
import csv
from tkinter import *
from datetime import *
from tkinter import messagebox
from tkinter import ttk

#------------------------------------WINDOW------------------------------------#
window = Tk()
window.title("Students who issued the book")
window.state('zoomed')

# Use a main frame to hold everything
main_frame = Frame(window, bg="#9ebbf5")
main_frame.pack(fill=BOTH, expand=True)

#------------------------------------TREEVIEW----------------------------------#
tree = ttk.Treeview(main_frame, columns=("ID","Title","Author","Name","Class","Section", "Date", "Due"), show="headings")
tree.heading("ID", text="Book ID")
tree.heading("Title", text="Book Title")
tree.heading("Author", text="Author")
tree.heading("Name", text="Student Name")
tree.heading("Class", text="Class")
tree.heading("Section", text="Section")
tree.heading("Date", text="Date Issued")
tree.heading("Due", text="Due Date")

tree.grid(row=8, column=0, columnspan=4, padx=10, pady=(20, 40), sticky="nsew")
main_frame.grid_rowconfigure(8, weight=3) 

tree.column("ID", width=50, anchor="center")
tree.column("Title", width=160, anchor="center")
tree.column("Author", width=80, anchor="center")
tree.column("Name", width=100, anchor="center")
tree.column("Class", width=50, anchor="center")
tree.column("Section", width=50, anchor="center")
tree.column("Date", width=80, anchor="center")
tree.column("Due", width=80, anchor="center")

# Make grid expandable
for i in range(9):
    main_frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    main_frame.grid_columnconfigure(j, weight=1)

#----------------------------------BOOKS DATA----------------------------------#
books = [
    {"id": "B001", "title": "Harry Potter and the Sorcerer’s Stone", "author": "J.K. Rowling"},
    {"id": "B002", "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": "B003", "title": "Alice’s Adventures in Wonderland", "author": "Lewis Carroll"},
    {"id": "B004", "title": "Charlie and the Chocolate Factory", "author": "Roald Dahl"},
    {"id": "B005", "title": "Matilda", "author": "Roald Dahl"},
    {"id": "B007", "title": "Peter Pan", "author": "J.M. Barrie"},
    {"id": "B010", "title": "The Hunger Games", "author": "Suzanne Collins"},
    {"id": "B011", "title": "Catching Fire", "author": "Suzanne Collins"},
    {"id": "B012", "title": "Mockingjay", "author": "Suzanne Collins"},
    {"id": "B014", "title": "Divergent", "author": "Veronica Roth"},
    {"id": "B015", "title": "Insurgent", "author": "Veronica Roth"},
    {"id": "B016", "title": "Allegiant", "author": "Veronica Roth"},
    {"id": "B019", "title": "Paper Towns", "author": "John Green"},
    {"id": "B020", "title": "The Book Thief", "author": "Markus Zusak"},
    {"id": "B021", "title": "Wonder", "author": "R.J. Palacio"},
    {"id": "B023", "title": "Heidi", "author": "Johanna Spyri"},
    {"id": "B024", "title": "Black Beauty", "author": "Anna Sewell"},
    {"id": "B027", "title": "The Secret Garden", "author": "Frances Hodgson Burnett"},
    {"id": "B028", "title": "Little Women", "author": "Louisa May Alcott"},
    {"id": "B029", "title": "The Jungle Book", "author": "Rudyard Kipling"}
]

for book in books:
    tree.insert("", "end", iid=book["id"], values=(
        book["id"],book["title"],book["author"]," ", " ", " "," "," "))

#-----------------------------LABELS AND ENTRIES------------------------------#
form_frame = Frame(main_frame, bg="#9ebbf5")
form_frame.grid(row=0, column=0, columnspan=4, pady=20)

Label(form_frame, text="Student's Name", font=("Georgia", 14), bg="#9ebbf5").grid(row=0, column=0, padx=20, pady=8)
name_entry = Entry(form_frame, width=20, font=("Georgia", 14))
name_entry.grid(row=0, column=1, pady=8)

Label(form_frame, text="Student's Class", font=("Georgia", 14), bg="#9ebbf5").grid(row=1, column=0, padx=20, pady=8)
class_entry = Entry(form_frame, width=20, font=("Georgia", 14))
class_entry.grid(row=1, column=1, pady=8)

Label(form_frame, text="Student's Section", font=("Georgia", 14), bg="#9ebbf5").grid(row=2, column=0, padx=20, pady=8)
section_entry = Entry(form_frame, width=20, font=("Georgia", 14))
section_entry.grid(row=2, column=1, pady=8)

Label(form_frame, text="Book ID", font=("Georgia", 14), bg="#9ebbf5").grid(row=3, column=0, pady=8)
issued_entry = Entry(form_frame, width=20, font=("Georgia", 14))
issued_entry.grid(row=3, column=1, pady=8)

Label(form_frame, text="Due Date", font=("Georgia", 14), bg="#9ebbf5").grid(row=4, column=0, padx=20, pady=8)
due_entry = Entry(form_frame, width=20, font=("Georgia", 14))
due_entry.grid(row=4, column=1, pady=8)

Label(form_frame, text="Search Entry", font=("Georgia", 14), bg="#9ebbf5").grid(row=5, column=0, padx=20, pady=8)
search_entry = Entry(form_frame, width=20, font=("Georgia", 14))
search_entry.grid(row=5, column=1, pady=8)

#----------------------------------FUNCTIONS-----------------------------------#
def add_entry():
    student_name = name_entry.get()
    student_class = class_entry.get()
    student_section = section_entry.get()
    book_id = issued_entry.get()
    due_date = due_entry.get()
    date_issued = datetime.now().strftime("%d-%m-%Y")

    for book in books:
        if book["id"] == book_id:
            if tree.exists(book_id):
                tree.item(book_id, values=(
                    book["id"],
                    book["title"],
                    book["author"],
                    student_name,
                    student_class,
                    student_section,
                    date_issued,
                    due_date
                ))
            with open("issued_books_data.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    book["id"],
                    book["title"],
                    book["author"],
                    student_name,
                    student_class,
                    student_section,
                    date_issued,
                    due_date
                ])
            messagebox.showinfo("Success", "Entry successfully added")
            break
    else:
        messagebox.showerror("Error", "Book ID not found! Please check again.")

    name_entry.delete(0, END)
    class_entry.delete(0, END)
    section_entry.delete(0, END)
    issued_entry.delete(0, END)
    due_entry.delete(0, END)
    search_entry.delete(0, END)

def search_entry_func():
    get_search_entry = search_entry.get().strip().lower()
    for row_id in tree.get_children():
        values = [str(v).lower() for v in tree.item(row_id)["values"]]
        if get_search_entry in values:
            tree.selection_set(row_id)
            tree.focus(row_id)
            tree.see(row_id)
            return
    messagebox.showinfo("Not Found", f"No match for {get_search_entry}")

def delete_entry():
    book_id = issued_entry.get().strip()
    if not book_id:
        messagebox.showerror("Error", "Enter a Book ID")
        return
    for book in books:
        if book["id"].lower() == book_id.lower():
            tree.item(book_id, values=(book["id"], book["title"], book["author"], "", "", "", "", ""))
            try:
                with open("issued_books_data.csv", "r") as f:
                    rows = list(csv.reader(f))
                with open("issued_books_data.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for row in rows:
                        if not (row and row[0].lower() == book_id.lower()):
                            writer.writerow(row)
            except FileNotFoundError:
                pass
            messagebox.showinfo("Success", f"Student info cleared for {book_id}")
            issued_entry.delete(0, END)
            return
    messagebox.showerror("Error", f"Book ID {book_id} not found")

def load_entries():
    try:
        with open("issued_books_data.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                book_id = row[0]
                if tree.exists(book_id):
                    tree.item(book_id, values=row)
    except FileNotFoundError:
        pass

def highlight_overdue():
    today = datetime.now().date()
    for row_id in tree.get_children():
        values = tree.item(row_id)["values"]
        due_date_str = str(values[7]).strip()
        try:
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
            if due_date < today:
                tree.item(row_id, tags=("overdue",))
            else:
                tree.item(row_id, tags=())
        except ValueError:
            continue
    tree.tag_configure("overdue", background="tomato")

#------------------------------------BUTTONS------------------------------------#
button_frame = Frame(main_frame, bg="#9ebbf5")
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

btn_style = {"height": 1, "width": 10, "font": ("Georgia", 13), "bg": "#4882f5", "fg": "white"}

add_entry_button = Button(button_frame, text="Add Entry", command=add_entry, **btn_style)
add_entry_button.grid(row=0, column=0, padx=10)

search_entry_button = Button(button_frame, text="Search Entry", command=search_entry_func, **btn_style)
search_entry_button.grid(row=0, column=1, padx=10)

delete_entry_button = Button(button_frame, text="Delete Entry", command=delete_entry, **btn_style)
delete_entry_button.grid(row=0, column=2, padx=10)

#------------------------------------RUN------------------------------------#
load_entries()
highlight_overdue()
window.mainloop()
