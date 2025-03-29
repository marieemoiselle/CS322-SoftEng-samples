# Function to calculate area
def calculate_area(length, width):
	if length < 0 or width < 0:
		return "Invalid input"
	return length * width

test_cases = [
    # Normal Cases
    {"input": {"length": 5, "width": 10}, "expected": 50},
    {"input": {"length": 3, "width": 7}, "expected": 21},
    
    # Edge Cases
    {"input": {"length": 0, "width": 10}, "expected": 0},  # Zero
    {"input": {"length": 2.5, "width": 4}, "expected": 10.0},  # Decimals
    {"input": {"length": 1e6, "width": 1e6}, "expected": "Warning: Area is extremely large, double-check inputs"},  # Huge
    
    # Error Cases
    {"input": {"length": -5, "width": 10}, "expected": "Error: Length and width cannot be negative"},
    {"input": {"length": "ten", "width": 5}, "expected": "Error: Length and width must be numbers"},
    {"input": {"length": None, "width": 8}, "expected": "Error: Length and width must be numbers"},
]

for test_case in test_cases:
    length = test_case["input"]["length"]
    width = test_case["input"]["width"]
    result = calculate_area(length, width)
    
    if result == test_case["expected"]:
        print(f"PASS: {length} x {width} -> {result}")
    else:
        print(f"FAIL: {length} x {width} -> Expected '{test_case['expected']}', Got '{result}'")