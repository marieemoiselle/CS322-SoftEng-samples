class BankAccount:
	def __init__(self, initial_balance):
		self.balance = initial_balance

	# Getter for balance
	def get_balance(self):
		return self.balance

	# Method to deposit
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
		else:
			print("Invalid deposit amount.")

	# Method to withdraw
	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
		else:
			print("Insufficient funds.")


def main():
	# Create a BankAccount object with an initial balance of 500
	account = BankAccount(500)

	# Display the initial balance
	print("Initial Balance:", account.get_balance())

	# Deposit 200 into the account
	account.deposit(200)
	print("Balance after deposit:", account.get_balance())

	# Attempt to withdraw 100 from the account
	account.withdraw(100)
	print("Balance after withdrawal:", account.get_balance())

	# Attempt to withdraw 700, which exceeds the current balance
	account.withdraw(700)  # Should print "Insufficient funds."

	# Attempt to deposit a negative amount
	account.deposit(-50)  # Should print "Invalid deposit amount."

	# Display the final balance
	print("Final Balance:", account.get_balance())


if __name__ == "__main__":
	main()
