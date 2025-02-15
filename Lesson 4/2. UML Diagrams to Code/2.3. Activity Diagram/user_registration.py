class Registration:
	# Method to register a user
	def register_user(self, username, password):
		if self.validate_input(username, password):
			self.create_account(username, password)
			print("Account created successfully.")
		else:
			print("Invalid input. Registration failed.")

	# Method to validate user input
	def validate_input(self, username, password):
		# Simple validation logic (e.g., check non-empty fields)
		return username and len(password) >= 8

	# Method to create a user account
	def create_account(self, username, password):
		# Simulate account creation (in a real application, this might involve database interaction)
		print(f"Creating account for {username}")


# Main function to demonstrate registration
if __name__ == "__main__":
	registration = Registration()
	registration.register_user("Marie", "whUtTh3si6m4_???")