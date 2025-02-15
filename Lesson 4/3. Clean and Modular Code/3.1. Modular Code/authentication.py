# Authentication Module
class Authentication:
	@staticmethod
	def login(username, password):
		if Authentication.is_valid(username, password):
			return "Login successful"
		else:
			return "Invalid credentials"

	@staticmethod
	def logout(user):
		# End of user session
		return "Logout successful"

	@staticmethod
	def is_valid(username, password):
		# Simple validation function (demo only)
		return username == "marie" and password == "whUtTh3si6m4_???"


# UserManagement module
class UserManagement:
	@staticmethod
	def create_user(username, email):
		# Adding a new user to the database
		return "User created"

	@staticmethod
	def delete_user(user_id):
		# Removing a user from the database
		return "User deleted"

# Main application logic
if __name__ == "__main__":
	user = Authentication.login("marie", "whUtTh3si6m4_???")
	if user == "Login successful":
		result = UserManagement.create_user("newUser", "marie@qtqtqt.com")
		print(result)