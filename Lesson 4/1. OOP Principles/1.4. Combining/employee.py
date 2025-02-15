class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	# Getter for salary
	def get_salary(self):
		return self.salary

	# Setter for salary
	def set_salary(self, salary):
		self.salary = salary

	# Get details
	def get_details(self):
		return f"Name: {self.name}, Salary: {self.salary}"

	# Calculate bonus (To be overridden by subclasses)
	def calculate_bonus(self):
		return 0.10 * self.salary

class Manager(Employee):
	def calculate_bonus(self):
		return 0.20 * self.get_salary()

class Developer(Employee):
	def calculate_bonus(self):
		return 0.15 * self.get_salary()

# Main code
if __name__ == "__main__":
	employee1 = Manager("Kazuha", 8000)
	employee2 = Developer("Heiji", 7000)

	print(f"{employee1.get_details()}, Bonus: {employee1.calculate_bonus()}")
	print(f"{employee2.get_details()}, Bonus: {employee2.calculate_bonus()}")