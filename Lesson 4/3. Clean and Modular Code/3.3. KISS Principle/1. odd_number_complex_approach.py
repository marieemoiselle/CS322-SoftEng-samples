# Complex Approach of a function to check if a number is odd
def is_even(number):
	if number % 2 != 0:
		return True
	else:
		return False

# Main function
if __name__ == "__main__":
	print(is_even(18))
	print(is_even(27))