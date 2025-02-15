class Animal:
	def say_hello(self):
		print("Generic animal says hello")

class Capybara(Animal):
	def say_hello(self):
		print("Capybara says hello")

class Hedgehog(Animal):
	def say_hello(self):
		print("Hedgehog says hello")

def main():
	# Create a generic Animal object and call say_hello
	generic_animal = Animal()
	generic_animal.say_hello()  # Should print "Generic animal says hello"

	# Create a Capybara object and call say_hello
	capybara = Capybara()
	capybara.say_hello()  # Should print "Capybara says hello"

	# Create a Hedgehog object and call say_hello
	hedgehog = Hedgehog()
	hedgehog.say_hello()  # Should print "Hedgehog says hello"

if __name__ == "__main__":
	main()
