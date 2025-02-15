class Shape:
	def calculate_area(self):
		print("Area calculation is not defined")

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		area = 3.14 * self.radius * self.radius
		print(f"Area of Circle: {area}")

class Rectangle(Shape):
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		area = self.length * self.width
		print(f"Area of Rectangle: {area}")

def main():
	# Create a generic Shape object
	generic_shape = Shape()
	generic_shape.calculate_area()  # Should print "Area calculation is not defined"

	# Create a Circle object with radius 5
	circle = Circle(5)
	circle.calculate_area()  # Should print the area of the circle

	# Create a Rectangle object with length 4 and width 6
	rectangle = Rectangle(4, 6)
	rectangle.calculate_area()  # Should print the area of the rectangle

if __name__ == "__main__":
	main()
