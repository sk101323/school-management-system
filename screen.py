import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk


# Buttons in the main window
root = tk.Tk()
root.title("School Management System")
root.geometry("1650x1000")
root.config(bg="Light Blue")

def main_page():
    
    # Clear all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    from main import admin_action
    from teachers import teacher_action    

    # Add the Admin and Teacher buttons back to the main page
    button1 = tk.Button(root, text="Admin", bg="blue", width=12, command=admin_action, fg="white")
    button1.grid(row=0, column=2)

    button2 = tk.Button(root, text="Teacher", bg="red", width=12, command=teacher_action, fg="white")
    button2.grid(row=1, column=2)


    
    root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    root.grid_rowconfigure(5, weight=1)  # Allow row 3 to expand
    root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    root.grid_columnconfigure(9, weight=1)  # Allow column 5 to expand

