import mysql.connector


def insert_teacher_data():
    from main import edit_record
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



