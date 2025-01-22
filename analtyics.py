import tkinter as tk
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Database connection details
DB_HOST = "localhost"
DB_USER = "root"  # Change if needed
DB_PASSWORD = ""  # Add password if set
DB_NAME = "sms"  # Your database name

# Function to fetch and analyze student data
def get_gender_counts():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT gender FROM students_data")  # Modify table name if needed
        rows = cursor.fetchall()
        conn.close()

        # Count male and female students manually
        male_count = sum(1 for row in rows if row[0].lower() == 'm')
        female_count = sum(1 for row in rows if row[0].lower() == 'f')

        return male_count, female_count

    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None, None

# Function to display pie chart
def pie_chart():
    window = tk.Tk()
    window.title("Genders")
    window.geometry("1650x1000")
    window.config(bg="Light Blue")
    
    male, female = get_gender_counts()
    if male is None or female is None:
        return

    # Data for pie chart
    labels = ['Male', 'Female']
    counts = [male, female]
    colors = ['#66b3ff', '#ff9999']

    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title('Male vs Female Students')

    canvas = FigureCanvasTkAgg(fig,master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    

# Create Tkinter window







   



