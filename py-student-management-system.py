# Import required modules
import mysql.connector as mysql
from prettytable import PrettyTable

# Create connection
conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = ""
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        class VARCHAR(20),
        roll_no VARCHAR(20) UNIQUE,
        marks INT
    )
""")
conn.commit()

# Functions
def add_student(name, class_name, roll_no, marks):
    sql = "INSERT INTO students (name, class, roll_no, marks)" \
            "VALUES (%s, %s, %s, %s)"
    val = (name, class_name, roll_no, marks)
    cursor.execute(sql, val)
    conn.commit()
    print("Student added successfully!")
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    table = PrettyTable(["ID","Name","Class","Roll No","Marks"])
    for row in records:
        table.add_row(row)
    print(table)
def search_student(roll_no):
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    record = cursor.fetchone()
    if record:
        table = PrettyTable(["ID","Name","Class","Roll No","Marks"])
        table.add_row(record)
        print(table)
    else:
        print("Student not found!")
def update_student(roll_no, name, class_name, marks):
    sql = "UPDATE students SET name=%s, class=%s, marks=%s WHERE roll_no=%s"
    val = (name, class_name, marks, roll_no)
    cursor.execute(sql,val)
    conn.commit()
    print("Student record updated!")
def delete_student(roll_no):
    cursor.execute("DELETE FROM students WHERE roll_no=%s",(roll_no,))
    conn.commit()
    print("Student record deleted!")

# Menu Driven Program
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        name = input("Enter Name: ")
        class_name = input("Enter Class: ")
        roll_no = input("Enter Roll No: ")
        marks = int(input("Enter New Marks: "))
        add_student(name, class_name, roll_no, marks)
    elif choice == '2':
        view_students()
    elif choice == '3':
        roll_no = input("Enter Roll No to search: ")
        search_student(roll_no)
    elif choice == '4':
        roll_no = input("Enter Roll No to update: ")
        name = input("Enter New Name: ")
        class_name = input("Enter New Class: ")
        marks = int(input("Enter New Marks: "))
        update_student(roll_no,name,class_name,marks)
    elif choice == '5':
        roll_no = input("Enter Roll No to delete: ")
        delete_student(roll_no)
    elif choice == '6':
        print("Exiting program... Goodbye!")
        cursor.close()
        conn.close()
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")