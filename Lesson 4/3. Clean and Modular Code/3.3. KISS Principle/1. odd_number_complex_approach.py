# Complex Approach of a function to check if a number is odd
def is_odd(number):
	if number % 2 != 0:
		return True
	else:
		return False

# Main function
if __name__ == "__main__":
	print(is_odd(18))
	print(is_odd(27))