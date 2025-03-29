# Function to simulate opening a page
def open_page(url):
	print(f"Navigating to: {url}")

# Function to simulate entering text in a field
def enter_text(field, text):
	print(f"Entering text '{text}' in field '{field}'")

# Function to simulate clicking a button
def click_button(button):
	print(f"Clicking the '{button}' button")

# Function to simulate getting the page title
def get_page_title():
	return "Dashboard"  # Simulating a successful login

# Test function for login
def test_login():
	# Step 1: Navigate to the login page
	open_page("http://example.com/login")

	# Step 2: Enter valid credentials
	enter_text("usernameField", "testUser")
	enter_text("passwordField", "password123")

	# Step 3: Click the login button
	click_button("loginButton")

	# Step 4: Verify the result
	if get_page_title() == "Dashboard":
		print("Test Passed")
	else:
		print("Test Failed")

# Running the test
if __name__ == "__main__":
	test_login()