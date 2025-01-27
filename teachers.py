import tkinter as tk
from tkinter import ttk, messagebox
from screen import root, main_page
from student_record import show_student_record
import mysql.connector



def students_fetch_data():
    
    """Fetch data from the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="sms"  # Replace with your database name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students_data")  # Replace with your table name
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return []
 #---------------------------------------




def show_student_record():
    for widget in root.winfo_children():
        widget.destroy()
      
    
    tk.Label(root, text="Students Records", font=("Arial", 14), bg="Light Blue").pack(pady=10)
    columns = ("sname",'sroll_no', "sclass",'gender','scontact_no')
    table = ttk.Treeview(root, columns=columns, show="headings", height=15)
    
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)
    table.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Populate Table
    data = students_fetch_data()
    for record in data:
        table.insert("", "end", values=record)


    #tk.Button(root, text="Edit Record", command=edit_students_record).pack(pady=10)
    back_button1= tk.Button(root, text="Back", command=teacher_interface)
    back_button1.pack(pady=10)

    

try:
    db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="sms"
       )
    cursor = db.cursor()
except mysql.connector.Error as err:
     print("Error: Could not connect to database.", err)
     exit()

# SQL functions
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to the MySQL database (local host)
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="sms"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print("Error: Could not connect to database.", err)
    exit()

# SQL functions
def fetch_grade(student_id):
    try:
        cursor.execute("SELECT students_name, subject_name, grade FROM students_grade WHERE id = %s", (student_id,))
        result = cursor.fetchone()
        return result if result else None
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch grade: {e}")


def update_grade(student_id, subject_name, new_grade):
    try:
        cursor.execute("UPDATE students_grade SET grade = %s WHERE id = %s AND subject_name = %s", (new_grade, student_id, subject_name))
        db.commit()
        return cursor.rowcount > 0
    except Exception as e:
        messagebox.showerror("Error", f"Could not update grade: {e}")
        return False


def add_new_student(student_name, subject_name, grade):
    try:
        cursor.execute("INSERT INTO students_grade (students_name, subject_name, grade) VALUES (%s, %s, %s)", (student_name, subject_name, grade))
        db.commit()
        return cursor.lastrowid  # Return the auto-generated student ID
    except Exception as e:
        messagebox.showerror("Error", f"Could not add new student: {e}")
        return None

# Tkinter interface
def view_grade():
    student_id = entry_student_id.get()

    if not student_id:
        messagebox.showwarning("Input Error", "Please enter a student ID.")
        return

    result = fetch_grade(student_id)
    if result is not None:
        student_name, subject_name, grade = result
        label_result.config(
            text=f"Student Name: {student_name}\nSubject: {subject_name}\nGrade: {grade}"
        )
    else:
        label_result.config(text=f"No record found for Student ID {student_id}.")


def edit_grade():
    student_id = entry_student_id.get()
    subject_name = entry_subject_name.get()
    new_grade = entry_new_grade.get()

    if not student_id or not subject_name or not new_grade:
        messagebox.showwarning("Input Error", "Please enter Student ID, Subject Name, and New Grade.")
        return

    if update_grade(student_id, subject_name, new_grade):
        messagebox.showinfo("Success", f"Grade updated for Student ID {student_id} and Subject {subject_name}.")
        label_result.config(text="")
    else:
        messagebox.showerror("Error", f"Failed to update grade for Student ID {student_id} and Subject {subject_name}.")


def add_grade():
    student_name = entry_student_name.get()
    subject_name = entry_subject_name.get()
    grade = entry_new_grade.get()

    if not student_name or not subject_name or not grade:
        messagebox.showwarning("Input Error", "Please enter Student Name, Subject Name, and Grade.")
        return

    new_id = add_new_student(student_name, subject_name, grade)
    if new_id:
        messagebox.showinfo("Success", f"New student added with ID {new_id}.")
        label_result.config(text=f"New Student ID: {new_id}\nName: {student_name}\nSubject: {subject_name}\nGrade: {grade}")
    else:
        messagebox.showerror("Error", "Failed to add new student.")


def grades():
    global entry_student_id,entry_new_grade,label_result, entry_student_name, entry_subject_name
    for widget in root.winfo_children():
        widget.destroy()

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    
    # Labels and Entry Widgets
    label_student_id = tk.Label(root, text="Student ID:")
    label_student_id.grid(row=0, column=0, padx=1, pady=1)

    entry_student_id = tk.Entry(root)
    entry_student_id.grid(row=0, column=1, padx=1, pady=1)

    student_name = tk.Label(root, text="Student Name:")
    student_name.grid(row=1, column=0, padx=10, pady=10)

    entry_student_name = tk.Entry(root)
    entry_student_name.grid(row=1, column=1, padx=10, pady=10)

    
    subject_name = tk.Label(root, text="Subject Name:")
    subject_name.grid(row=2, column=0, padx=10, pady=10)

    entry_subject_name = tk.Entry(root)
    entry_subject_name.grid(row=2, column=1, padx=10, pady=10)

    label_new_grade = tk.Label(root, text="New Grade:")
    label_new_grade.grid(row=3, column=0, padx=10, pady=10)



    entry_new_grade = tk.Entry(root)
    entry_new_grade.grid(row=3, column=1, padx=10, pady=10)

    button_add = tk.Button(root, text="Add New Student", command=add_grade)
    button_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


    
    # Buttons
    button_view = tk.Button(root, text="View Grade", command=view_grade)
    button_view.grid(row=5, column=0, padx=10, pady=10)

    button_edit = tk.Button(root, text="Edit Grade", command=edit_grade)
    button_edit.grid(row=5, column=1, padx=10, pady=10)

    # Result Label
    label_result = tk.Label(root, text="", fg="blue")
    label_result.grid(row=4, column=0, columnspan=2, pady=10)

    # Run the Tkinter loop

def add_grade():
    student_name = entry_student_name.get()
    subject_name = entry_subject_name.get()
    grade = entry_new_grade.get()

    if not student_name or not grade:
        messagebox.showwarning("Input Error", "Please enter both Student Name and Grade.")
        return

    new_id = add_new_student(student_name,subject_name, grade)
    if new_id:
        messagebox.showinfo("Success", f"New student added with ID {new_id}.")
        label_result.config(text=f"New Student ID: {new_id}\nName: {student_name}\nGrade: {grade}")
    else:
        messagebox.showerror("Error", "Failed to add new student.")



# Main Tkinter window

# Close the database connection


    



def teacher_action():
    
    
    for widget in root.winfo_children():
        widget.destroy()
    
    # Add a label
    label1 = tk.Label(root, text="Enter user name:")
    label1.pack(pady=10)

    # Add an entry box
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    # Add a label
    label2 = tk.Label(root, text="Enter Password:")
    label2.pack(pady=10)

    # Add an entry box
    entry = tk.Entry(root, width=30,show="*")
    entry.pack(pady=10)

    # Add a submit button
    submit_button = tk.Button(root, text="Submit", command=teacher_interface)
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="back", command=main_page)
    back_button.pack(pady=10)





def teacher_interface():
    for widget in root.winfo_children():
        widget.destroy() 
    

    root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    root.grid_rowconfigure(5, weight=1)  # Allow row 3 to expand
    root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    root.grid_columnconfigure(9, weight=1)  # Allow column 5 to expand


    table_frame = tk.Frame(root, bg="lightblue")
    table_frame.grid(row=0, column=0, pady=10)
    
    

     # Create a frame to hold the buttons and make the layout easier
    # button_frame = tk.Frame(root)
    # button_frame.pack(expand=True)
    # Create buttons with lambda functions to show information 
    show_self_record1 = tk.Button(table_frame, text="Show Teacher Record")
    show_self_record1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    show_student_record1 = tk.Button(table_frame, text="Show Student Record", command=show_student_record)
    show_student_record1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    show_time_table = tk.Button(table_frame, text="Show Time Table" )
    show_time_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    student_grades = tk.Button(table_frame, text="Student Grades", command= grades)
    student_grades.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    back_button = tk.Button(root, text="back", command=teacher_action)
    back_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Configure the columns and rows to expand proportionally
    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_rowconfigure(1, weight=1)