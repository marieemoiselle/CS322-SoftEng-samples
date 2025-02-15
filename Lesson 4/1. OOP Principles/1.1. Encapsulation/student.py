class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute (encapsulated)
        self.__grade = grade  # Private attribute (encapsulated)

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age with validation
    def set_age(self, age):
        if 5 <= age <= 40:  # Valid age range
            self.__age = age
        else:
            print("Invalid age. Please enter a valid age between 5 and 40.")

    # Getter method for grade
    def get_grade(self):
        return self.__grade

    # Setter method for grade with validation
    def set_grade(self, grade):
        if grade in ["A", "B", "C", "D", "F"]:
            self.__grade = grade
        else:
            print("Invalid grade. Please enter a valid grade (A, B, C, D, or F).")

# Creating a Student object
student1 = Student("Ai Haibara", 17, "A")

# Accessing student details
print("Student Name:", student1.name)
print("Student Age:", student1.get_age())
print("Student Grade:", student1.get_grade())

# Trying to set invalid age
student1.set_age(150)  # This will show an error message

# Updating student grade
student1.set_grade("A")
print("Updated Grade:", student1.get_grade())

# Attempting direct access to private attributes (will raise an error)
# print(student1.__age)  # AttributeError
# print(student1.__grade)  # AttributeError