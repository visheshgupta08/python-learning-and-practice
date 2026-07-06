# =========================================================================
# STEP 1: BASE CLASS (Dada Ji Class)
# =========================================================================
class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

# =========================================================================
# STEP 2: DERIVED CLASS 1 (Papa Class - Jo Dada Ji se bani hai)
# =========================================================================
class Dog(Animal):
    def __init__(self, name, breed):
        
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

# =========================================================================
# STEP 3: DERIVED CLASS 2 (Pota Class - Jo Papa Class se bani hai)
# =========================================================================
# MULTILEVEL INHERITANCE: GoldenRetriever ne Dog ko inherit kiya.
# Iske paas Dog ke saath-saath Animal ke bhi saare features automatic aa gaye!
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

# Sabse aakhri (Pota) class ka object banaya
o = GoldenRetriever("Tommy", "Golden")
o.show_details()    
print(GoldenRetriever.mro())