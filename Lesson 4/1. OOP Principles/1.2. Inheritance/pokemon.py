# Generic/wild Pokemon
class Pokemon:
    def make_attack(self):
        print("A wild Pokemon appeared!")

# Pikachu as subclass of Pokemon
class Pikachu(Pokemon):
    def make_attack(self):
        print("Thunderbolt!")

# Charizard as subclass of Pokemon
class Charizard(Pokemon):
    def make_attack(self):
        print("Flamethrower!")

# Swampert as subclass of Pokemon
class Swampert(Pokemon):
    def make_attack(self):
        print("Hydro Pump!")

def main():
    wild_pokemon = Pokemon()
    wild_pokemon.make_attack()

    pikachu = Pikachu()
    pikachu.make_attack()

    charizard = Charizard()
    charizard.make_attack()

    swampert = Swampert()
    swampert.make_attack()

if __name__ == "__main__":
	main()