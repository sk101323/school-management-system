import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("School Management System")
root.geometry("500x500")


root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
root.grid_rowconfigure(5, weight=1)  # Allow row 3 to expand
root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
root.grid_columnconfigure(9, weight=1)  # Allow column 5 to expand



def main_page():
    # Clear all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Add the Admin and Teacher buttons back to the main page
    button1 = tk.Button(root, text="Admin", bg="blue", width=12, command=admin_action, fg="white")
    button1.grid(row=0, column=2)

    button2 = tk.Button(root, text="Teacher", bg="red", width=12, command=teacher_action, fg="white")
    button2.grid(row=1, column=2)




def admin_action():
    
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
    submit_button = tk.Button(root, text="Submit", command=admin_interface)
    submit_button.pack(pady=10)


    back_button = tk.Button(root, text = "back" , command=main_page)
    back_button.pack(pady=10)




def admin_interface():
    
    for widget in root.winfo_children():
        widget.destroy()
    

     # Create a frame to hold the buttons and make the layout easier
    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)
    
    # Create buttons with lambda functions to show information
    show_teacher_record = tk.Button(button_frame, text="Show Teacher Record", command=lambda: messagebox.showinfo("Info", "Teacher Record"))
    show_teacher_record.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    show_student_record = tk.Button(button_frame, text="Show Student Record", command=lambda: messagebox.showinfo("Info", "Student Record"))
    show_student_record.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    show_time_table = tk.Button(button_frame, text="Show Time Table", command=lambda: messagebox.showinfo("Info", "Time Table"))
    show_time_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    show_analytics = tk.Button(button_frame, text="Show Analytics", command=lambda: messagebox.showinfo("Info", "Analytics"))
    show_analytics.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    back_button = tk.Button(root, text = "back" , command=admin_action)
    back_button.pack(pady=10)

    # Configure the columns and rows to expand proportionally
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_rowconfigure(1, weight=1)

def teacher_action():
    # Use the same root window and clear it
    for widget in root.winfo_children():
        widget.destroy()
    
    # Add content for the Teacher section
    label_teacher = tk.Label(root, text="Welcome, Teacher!")
    label_teacher.pack(pady=10)
    
    back_button = tk.Button(root, text = "back" , command=main_page)
    back_button.pack(pady=10)


# Buttons in the main window
button1 = tk.Button(root, text="Admin", bg="blue", width=12, command=admin_action, fg="white")
button1.grid(row=0, column=2)

button2 = tk.Button(root, text="Teacher", bg="red", width=12, command=teacher_action, fg="white")
button2.grid(row=1, column=2)


root.mainloop()
