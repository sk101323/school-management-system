import tkinter as tk
from screen import root, main_page
from student_record import show_student_record

    



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

    edit_student_grades = tk.Button(table_frame, text="Edit Student Grades")
    edit_student_grades.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


    back_button = tk.Button(root, text="back", command=teacher_action)
    back_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Configure the columns and rows to expand proportionally
    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_rowconfigure(1, weight=1)