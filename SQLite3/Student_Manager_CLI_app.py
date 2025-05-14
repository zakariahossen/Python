import sqlite3  # Import the sqlite3 module for database operations

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

# Function to create the 'students' table
def create_table():
    """
    Creates the 'students' table in the database if it doesn't already exist.
    The table has three columns:
    - id: Integer, primary key, auto-incremented (unique identifier for each student)
    - name: Text, not null (stores the student's name)
    - age: Integer, not null (stores the student's age)
    """
    cursor.execute("create table if not exists students (id integer primary key autoincrement, name text not null, age integer not null)")
    conn.commit()  # Save the changes to the database

# Function to add a new student to the 'students' table
def add_students():
    """
    Prompts the user to enter the student's name and age,
    and then inserts this data as a new record into the 'students' table.
    """
    name = input("Name: ")  # Get the student's name from user input
    age = input("Age: ")    # Get the student's age from user input
    cursor.execute("insert into students (name,age) values (?,?)", (name, age))  # Insert the data into the table
    conn.commit()  # Save the changes to the database
    print("New student has successfully added.")  # Display a success message

# Function to view all students in the 'students' table
def view_students():
    """
    Retrieves all records from the 'students' table and prints them to the console.
    Each record represents a student's information (id, name, age).
    """
    cursor.execute("select * from students")  # Select all data from the 'students' table
    result = cursor.fetchall()  # Fetch all the rows returned by the query
    for row in result:
        print(row)  # Print each row (student record)

# Function to update a student's age in the 'students' table
def update_student():
    """
    Prompts the user to enter the ID of the student whose age needs to be updated,
    and then prompts for the new age.  It then updates the corresponding record
    in the 'students' table.
    """
    student_id = int(input("Enter the ID you want to update: "))  # Get the ID of the student to update
    new_age = int(input("Inter the new age: "))  # Get the new age from the user
    cursor.execute("update students set age = ? where id = ?", (new_age, student_id))  # Update the student's age
    conn.commit()  # Save the changes to the database
    print("Successfully updated")  # Display a success message

# Function to delete a student from the 'students' table
def delete_students():
    """
    Prompts the user to enter the ID of the student to delete,
    and then deletes the corresponding record from the 'students' table.
    """
    student_id = int(input("Enter the ID you want to delete: "))  # Get the ID of the student to delete
    cursor.execute("delete from students where id = ?", (student_id,))  # Delete the student record
    conn.commit()  # Save the changes to the database
    print("successfully deleted.")  # Display a success message

# Create the 'students' table (if it doesn't exist)
create_table()

# Main loop to display the menu and handle user input
while True:
    print("\n📚 Student Manager")
    print("1. ছাত্র যোগ করুন")  # Add student
    print("2. ছাত্রদের তালিকা দেখুন")  # View students
    print("3. ছাত্র আপডেট করুন")  # Update student
    print("4. ছাত্র ডিলিট করুন")  # Delete student
    print("5. অ্যাপ বন্ধ করুন")  # Exit the application
    choice = input("আপনার পছন্দ দিন: ")  # Get the user's choice

    if choice == '1':
        add_students()  # Call the add_students function
    elif choice == '2':
        view_students()  # Call the view_students function
    elif choice == '3':
        update_student()  # Call the update_student function
    elif choice == '4':
        delete_students()  # Call the delete_students function
    elif choice == '5':
        print("👋 বিদায়! ধন্যবাদ অ্যাপ ব্যবহারের জন্য।")  # Exit message
        break  # Exit the loop
    else:
        print("⚠️ ভুল অপশন। আবার চেষ্টা করুন।")  # Error message for invalid input
