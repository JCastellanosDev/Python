class pokedex:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print("\n" + (self.name + " ") * 2 + "!")

    def display_details(self):
        print("Entry: " + str(self.entry))
        print("Name: " + self.name)
        print("Types: " + ", ".join(self.types))
        print("Description: " + self.description)
        print("Caught: " + str(self.is_caught))   

pokemon1 = pokedex(1, "Bulbasaur", ["Grass", "Poison"], "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.", True)
pokemon2 = pokedex(4, "Charmander", ["Fire"], "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.", False)
pokemon3 = pokedex(7, "Squirtle", ["Water"], "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.", True)

pokemon1.speak()
pokemon1.display_details()
pokemon2.speak()
pokemon2.display_details()
pokemon3.speak()
pokemon3.display_details()