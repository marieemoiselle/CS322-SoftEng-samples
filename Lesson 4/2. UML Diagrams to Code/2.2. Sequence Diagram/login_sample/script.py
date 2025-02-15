from database_service import DatabaseService
from login_service import LoginService

# Main function to demonstrate interaction
if __name__ == "__main__":
	db_service = DatabaseService()
	login_service = LoginService(db_service)

	username = "Marie"
	password = "whUtTh3si6m4_???"
	is_authenticated = login_service.authenticate_user(username, password)

	if is_authenticated:
		print(f"User {username} authenticated successfully.")
	else:
		print(f"Authentication failed for user {username}.")
