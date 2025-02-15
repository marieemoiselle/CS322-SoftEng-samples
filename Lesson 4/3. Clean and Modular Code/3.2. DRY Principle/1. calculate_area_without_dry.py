# Function to calculate the Rectangle Area
def calculate_rectangle_area(length, width):
	return length * width

# Function to calculate the Circle's area
def calculate_circle_area(radius):
	return 3.14 * radius ** 2

# Function to calculate the Square's area
def calculate_square_area(side):
	return side * side

# Main function
if __name__ == "__main__":
	print(calculate_rectangle_area(7, 13))
	print(calculate_circle_area(8))
	print(calculate_square_area(6))