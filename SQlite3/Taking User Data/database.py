import sqlite3  # Importing the SQLite3 module to work with databases

# Connecting to (or creating) the database file named 'users.db'
conn = sqlite3.connect('users.db')

# Creating a cursor object to execute SQL commands
cursor = conn.cursor()

# Creating a table named 'users' if it doesn't already exist
# The table has 3 columns: id, name, and email
cursor.execute('''
    CREATE TABLE IF NOT EXISTS  users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT,  
    email TEXT  
    )
''')  # Auto-incremented unique ID for each user, # User's name, # User's email

conn.commit()  # Saving changes to the database

# --- Getting input from users ---
user_data = {}  # Dictionary to store name-email pairs temporarily

# Loop to collect multiple users' data
while True:
    name = input("আপনার নাম দিন (বের হতে চাইলে Exit লিখুন) :  ")
    if name.lower() == 'exit':  # যদি ইউজার Exit লেখে, লুপ থেমে যাবে
        break
    email = input("আপনার ইমেইল দিনঃ ")
    user_data[name] = email  # Save the data in the dictionary


# Function to insert collected data into the database
def add_to_db(data_dict):
    for name, email in data_dict.items():  # Looping through each name-email pair
        cursor.execute("INSERT INTO users (name,email) VALUES (?,?)", (name, email))
    conn.commit()  # Committing changes to the database


# Calling the function to save data
add_to_db(user_data)
print("All emails have been saved successfully ✔️")


# Function to display all data from the database
def show_all():
    cursor.execute("SELECT * FROM users")  # Fetching all records
    rows = cursor.fetchall()  # Getting all rows as a list
    for row in rows:
        print(row)  # Displaying each row (id, name, email)


# Calling the function to show saved users
show_all()
