# Example code for Dictionary Data Structure in Python

# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Computer Science"]
}

# Accessing values using keys
print("Name:", student["name"])  # Output: John Doe
print("Age:", student["age"])    # Output: 21

# Adding a new key-value pair
student["grade"] = "A"
print("Updated student dictionary:", student)

# Updating an existing key-value pair
student["age"] = 22
print("Updated age:", student["age"])  # Output: 22

# Removing a key-value pair using pop()
removed_course = student.pop("courses")
print("Removed courses:", removed_course)  # Output: ['Math', 'Computer Science']
print("Dictionary after removing courses:", student)

# Checking if a key exists in the dictionary
if "name" in student:
    print("Name is present in the dictionary")

# Iterating through the dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Getting the length of the dictionary
print("Number of key-value pairs:", len(student))  # Output: 3
