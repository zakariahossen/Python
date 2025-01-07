class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# অবজেক্ট তৈরি করা
student1 = Student("Zakaria", 16)
student1.display_info()
