# Function to simulate user login
def login(username, password):
	if username == "marie" and password == "whUtth3si6m4???":
		return "Login successful"
	return "Invalid credentials"

# valid username = marie
# password = whUtth3si6m4???

# Function to test user login
def test_user_login():
	# Test Case 1: Valid credentials
	input_data = {"username": "marie", "password": "whUtth3si6m4???"}
	result = login(input_data["username"], input_data["password"])
	if result == "Login successful":
		print("Test Case 1 Passed")
	else:
		print(f"Test Case 1 Failed: {result}")

	# Test Case 2: Invalid credentials
	input_data = {"username": "marie", "password": "incorrectPassword"}
	result = login(input_data["username"], input_data["password"])
	if result == "Invalid credentials":
		print("Test Case 2 Passed")
	else:
		print(f"Test Case 2 Failed: {result}")

# Running the tests
if __name__ == "__main__":
	test_user_login()