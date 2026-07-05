class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

# =========================================================================
# 1. DOG CLASS (Single Inheritance)
# =========================================================================
class Dog(Animal):
    def __init__(self, name, breed):
        # Parent class ke constructor ko call kiya
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Tommy", "Doberman")
print(f"Dog Name: {d.name}, Breed: {d.breed}, Species: {d.species}")
d.make_sound() 

print("-" * 40)

a = Animal("Sheru", "Lion")
a.make_sound() 

print("-" * 40)



# Quick Quiz --> Implement a cat class by using the animal class.add some methods specific to cat

class Cat(Animal): 
    def __init__(self, name, food):
        Animal.__init__(self, name, species="Cat")
        self.food = food  

    # Cat ka apna naya specific method (Jo sirf Cat ke paas hoga)
    def favourite_food(self):
        print(f"{self.name} ko khaane mein '{self.food}' bohot pasand hai! ")

    # Method Overriding: Animal ke purane sound ko badal diya
    def make_sound(self):
        print("Meow~")

 
c = Cat("Lucy", "Milk & Fish")
print(f"Cat Name: {c.name}, Species: {c.species}")
c.make_sound()        
c.favourite_food()    
