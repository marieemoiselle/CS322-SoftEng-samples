# Base class (Person)
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Method to show details
	def show_details(self):
		print(f"Name: {self.name}, Age: {self.age}")


# Subclass (Student) extending Person
class Student(Person):
	def __init__(self, name, age, student_id):
		super().__init__(name, age)
		self.student_id = student_id

	# Method specific to Student
	def study(self):
		print(f"{self.name} is studying.")


# Subclass (Instructor) extending Person
class Instructor(Person):
	def __init__(self, name, age, subject):
		super().__init__(name, age)
		self.subject = subject

	# Method specific to instructor
	def teach(self):
		print(f"{self.name} is teaching {self.subject}.")


# Main code to demonstrate usage
if __name__ == "__main__":
	student = Student("Theo Jang", 30, "S12345")
	instructor = Instructor("Fatima Marie", 28, "Software Engineering")

	student.show_details()
	student.study()

	instructor.show_details()
	instructor.teach()