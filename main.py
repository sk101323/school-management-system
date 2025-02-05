import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import mysql.connector
from PIL import Image
from io import BytesIO
from PIL import Image, ImageTk
import analtyics
import os
import teachers
from screen import root,main_page
from student_record import show_student_record

image_id= None
#-------------------connection of database-----------------------
def insert_teacher_data():
    """Insert teacher data into the database."""
    # Retrieve values from entry fields
    teacher_name = name_entry.get()
    contact_no = contact_entry.get()
    email = email_entry.get()
    class_name = class_entry.get()
    subject = subject_entry.get()
    username = user_nameentry.get()
    password = passowrd_entry.get()

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
        INSERT INTO teacher (Name, Contact_no, Email_address, Class, Subject, tuser_name, tpassword)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (teacher_name, contact_no, email, class_name, subject, username, password)
        
        cursor.execute(query, values)
        conn.commit()
        
        messagebox.showinfo("Success", "Teacher record inserted successfully!")
        
        conn.close()  # Close the connection
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def fetch_data():
    """Fetch data from the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your host
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="sms"  # Replace with your database name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teacher")  # Replace with your table name
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return []

#---------------------------------------------------------------------

def get_image_from_database(image_name):
    """
    Fetch the image from the database based on the image name.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",             # Replace with your MySQL username
            password="",             # Replace with your MySQL password
            database="sms"         # Database name
        )
        cursor = connection.cursor()

        # Since we only have one column, adjust the query accordingly
        query = "SELECT image FROM school_images WHERE image = %s"
        cursor.execute(query, (image_name,))
        image_data = cursor.fetchone()

        if image_data:
            return image_data[0]
        else:
            return None

    except mysql.connector.Error as error:
        print(f"Error fetching image: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def display_image(image_id):
    for widget in root.winfo_children():
        widget.destroy()
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="sms"  # Replace with your database name
        )
        cursor = connection.cursor()

        # Query to fetch the image path based on image_id
        query = "SELECT image FROM school_images WHERE id = %s"
        cursor.execute(query, (image_id,))
        result = cursor.fetchone()

        if result:
            image = result[0]
            print(f"Image path fetched: {image}")  # Debugging: Print the image path

            # Check if the file exists
            if os.path.exists(image):
                # Open and display the image
                display_image_window(image)
            else:
                messagebox.showerror("Error", f"Image file does not exist: {image}")
        else:
            messagebox.showerror("Error", f"No image found with ID {image_id}!")

    except mysql.connector.Error as error:
        print(f"Error fetching image from database: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    #tk.Button(root, text="Back", command=admin_interface).pack(pady=10)

def display_image_window(image):
    try:
        # Create a window to display the image
        img = Image.open(image)  # Open the image
        img = img.resize((400, 400))  # Resize for display, if needed

        # Convert the image to a Tkinter-compatible format
        img_tk = ImageTk.PhotoImage(img)

        # Add the image to a Tkinter label and pack it into the window
        label = tk.Label(root, image=img_tk)
        #label.image = img_tk  # Keep a reference to avoid garbage collection
        label.pack()

    except Exception as e:
        messagebox.showerror("Error", f"Could not open the image: {e}")



#----------------------------------------------------------------
def save_image_to_database():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    if not file_path:
        print("No image selected.")
        return

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="sms"  # Replace with your database name
        )
        

        # Commit the deletion
        connection.commit()
        cursor = connection.cursor()


        # Insert the image file path into the database
        query = "INSERT INTO school_images (image) VALUES (%s)" 
        cursor.execute(query, (file_path,))
        connection.commit()


    except mysql.connector.Error as error:
        print(f"Error saving image to the database: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

#-------------------------------------------------------------------------------




# -------------------------------------------------------------------------------



# ----------------------teacher record button in admin interface----------------------
def show_teacher_record():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Teacher Records", font=("Arial", 14), bg="Light Blue").pack(pady=10)
    columns = ("ID", "Name", "Contact_no", "Email_Address", "Class", "Subject","tuser_name","tpassword")
    table = ttk.Treeview(root, columns=columns, show="headings", height=15)
    
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=100)
    table.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Populate Table
    data = fetch_data()
    for record in data:
        table.insert("", "end", values=record)

    tk.Button(root, text="Edit Record", command=edit_record).pack(pady=10)
    tk.Button(root, text="Back", command=admin_interface).pack(pady=10)

# ---------------- edit teacher record--------------------
def edit_record():
    for widget in root.winfo_children():
        widget.destroy()

    tname = tk.Label(root, text="Enter Teacher name:")
    tname.pack(pady=10)

    # Add an entry box
    global name_entry
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=10)

    tcontact_no = tk.Label(root, text="Enter Contact No:")
    tcontact_no.pack(pady=10)

    # Add an entry box
    global contact_entry
    contact_entry = tk.Entry(root, width=30)
    contact_entry.pack(pady=10)

    temail = tk.Label(root, text="Enter Email:")
    temail.pack(pady=10)

    # Add an entry box
    global email_entry
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=10)

    tclass = tk.Label(root, text="Enter Class Name:")
    tclass.pack(pady=10)

    # Add an entry box
    global class_entry
    class_entry = tk.Entry(root, width=30)
    class_entry.pack(pady=10)

    tsubject = tk.Label(root, text="Enter Subject name:")
    tsubject.pack(pady=10)

    # Add an entry box
    global subject_entry
    subject_entry = tk.Entry(root, width=30)
    subject_entry.pack(pady=10)

    tusername = tk.Label(root, text="Enter user name:")
    tusername.pack(pady=10)

    # Add an entry box
    global user_nameentry
    user_nameentry = tk.Entry(root, width=30)
    user_nameentry.pack(pady=10)

    tpassowrd = tk.Label(root, text="Enter password:")
    tpassowrd.pack(pady=10)

    # Add an entry box
    global passowrd_entry
    passowrd_entry = tk.Entry(root, width=30)
    passowrd_entry.pack(pady=10)

    # Add "Save" button to insert data into the database
    save_button = tk.Button(root, text="Save Teacher Data", command=insert_teacher_data)
    save_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=admin_interface)
    back_button.pack(pady=10)


# ----------------------Show admin buttons---------------------
def admin_interface():
    
    
    for widget in root.winfo_children():
        widget.destroy()
    

     # Create a frame to hold the buttons and make the layout easier
    button_frame = tk.Frame(root, bg="lightblue")
    button_frame.grid(row=0, column=0, pady=10)

    # Create buttons with lambda functions to show information 
    show_teacher_record1 = tk.Button(button_frame, text="Show Teacher Record",command=show_teacher_record)
    show_teacher_record1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    tshow_student_record = tk.Button(button_frame, text="Show Student Record", command=show_student_record)
    tshow_student_record.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    show_time_table = tk.Button(button_frame, text="Show Time Table", command=lambda: display_image(1))
    show_time_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    save_time_table = tk.Button(button_frame, text="Time Table Save", command=save_image_to_database)
    save_time_table.grid(row=3,column=0, padx=10, pady=10, sticky="nsew")

    show_analytics = tk.Button(button_frame, text="Show Analytics", command=analtyics.pie_chart)
    show_analytics.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    back_button = tk.Button(root, text="back", command=admin_action)
    back_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Configure the columns and rows to expand proportionally
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)
    button_frame.grid_rowconfigure(1, weight=1)


# ------------------admin credentials page-------------------
def admin_action():
    
    for widget in root.winfo_children():
        widget.destroy()  
    
    # Add a label
    label1 = tk.Label(root, text="Enter user name:")
    label1.grid(row=0, column=1)

    # Add an entry box
    entry = tk.Entry(root, width=30)
    entry.grid(row=0, column=2)

    # Add a label
    label2 = tk.Label(root, text="Enter Password:")
    label2.grid(row=1, column=1)

    # Add an entry box
    entry = tk.Entry(root, width=30,show="*")
    entry.grid(row=1, column=2)

    # Add a submit button
    submit_button = tk.Button(root, text="Submit", command=admin_interface)
    submit_button.grid(row=3, column=1)

    back_button = tk.Button(root, text="back", command=main_page)
    back_button.grid(row=3, column=2)


    
    root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
    root.grid_rowconfigure(5, weight=1)  # Allow row 3 to expand
    root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    root.grid_columnconfigure(9, weight=1)  # Allow column 5 to expand














# -----------------------------------------teachers function-----------------





root.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
root.grid_rowconfigure(5, weight=1)  # Allow row 3 to expand
root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
root.grid_columnconfigure(9, weight=1)  # Allow column 5 to expand


# table_frame = tk.Frame(root, bg="lightblue")
# table_frame.grid(row=0, column=0, pady=10)

 
button1 = tk.Button(root, text="Admin", bg="blue", width=12, command=admin_action, fg="white").grid(row=0, column=2)
button2 = tk.Button(root, text="Teacher", bg="red", width=12, command=teachers.teacher_action, fg="white").grid(row=1, column=2)



root.mainloop()