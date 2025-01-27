from screen import root
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import mysql.connector 




def insert_students_data():
    """Insert teacher data into the database."""
    # Retrieve values from entry fields
    sname = sname_entry.get()
    sroll_no = roll_entry.get()
    sclass = class_entry.get()
    gender = gender_entry.get()
    scontact_no = contactno_entry.get()
    

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="sms"  # Replace with your database name
        )
        
        cursor = conn.cursor()
        
        # Create an SQL query to insert the data into the teacher table
        query = """
        INSERT INTO students_data (sname,sroll_no, sclass, gender,scontact_no)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (sname,sroll_no,sclass, gender,scontact_no)
        
        cursor.execute(query, values)
        conn.commit()
        
        messagebox.showinfo("Success", "Students record inserted successfully!")
        
        conn.close()  # Close the connection
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

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

    from main import admin_interface
    
    tk.Button(root, text="Edit Record", command=edit_students_record).pack(pady=10)
    tk.Button(root, text="Back", command=admin_interface).pack(pady=10)

# ---------------- edit teacher record--------------------
def edit_students_record():
    for widget in root.winfo_children():
        widget.destroy()

    sname = tk.Label(root, text="Enter students name:")
    sname.pack(pady=10)

    # Add an entry box
    global sname_entry
    sname_entry = tk.Entry(root, width=30)
    sname_entry.pack(pady=10)

    sroll_no = tk.Label(root, text="Enter Roll No:")
    sroll_no.pack(pady=10)

    # Add an entry box
    global roll_entry
    roll_entry = tk.Entry(root, width=30)
    roll_entry.pack(pady=10)

    sclass = tk.Label(root, text="Enter Class:")
    sclass.pack(pady=10)

    # Add an entry box
    global class_entry
    class_entry = tk.Entry(root, width=30)
    class_entry.pack(pady=10)

    sgender = tk.Label(root, text="Enter Gender")
    sgender.pack(pady=10)

    # Add an entry box
    global gender_entry
    gender_entry = tk.Entry(root, width=30)
    gender_entry.pack(pady=10)

    scontact = tk.Label(root, text="Enter Contact no")
    scontact.pack(pady=10)

    # Add an entry box
    global contactno_entry
    contactno_entry = tk.Entry(root, width=30)
    contactno_entry.pack(pady=10)


    # Add "Save" button to insert data into the database
    save_button = tk.Button(root, text="Save Students Data", command=insert_students_data)
    save_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=show_student_record)
    back_button.pack(pady=10)
