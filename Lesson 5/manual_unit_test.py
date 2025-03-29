# Function to calculate area
def calculate_area(length, width):
	if length < 0 or width < 0:
		return "Invalid input"
	return length * width

# Unit Test Cases
test_cases = [
	{"input": {"length": 5, "width": 10}, "expected": 50},
	{"input": {"length": 0, "width": 10}, "expected": 0},
	{"input": {"length": -5, "width": 10}, "expected": "Invalid input"}
]

# Running test cases
for test_case in test_cases:
	result = calculate_area(test_case["input"]["length"], test_case["input"]["width"])
	if result == test_case["expected"]:
		print("Test Passed")
	else:
		print(f"Test Failed: Expected {test_case['expected']}, Got {result}")