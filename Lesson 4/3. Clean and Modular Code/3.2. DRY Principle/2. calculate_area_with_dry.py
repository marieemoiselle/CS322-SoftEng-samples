# Function to calculate the area of any shape
def calculate_area(shape, dimensions):
	if shape == "rectangle":
		return dimensions["length"] * dimensions["width"]
	if shape == "circle":
		return 3.14 * dimensions["radius"] ** 2
	if shape == "square":
		return dimensions["side"] * dimensions["side"]

# Main function
if __name__ == "__main__":
	rectangle = {"length": 7, "width": 13}
	circle = {"radius": 8}
	square = {"side": 6}

	print(f'Rectangle: {calculate_area("rectangle", rectangle)}')
	print(f'Circle: {calculate_area("circle", circle)}')
	print(f'Square: {calculate_area("square", square)}')