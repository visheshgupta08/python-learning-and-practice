# =========================================================================
# PART 1: METHODS KE SAATH SUPER() KA USE (Function Overriding)
# =========================================================================
class ParentClass:
    def parent_method(self):
        print("This is the parent method1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry2")
        # JADU 1: super() ne Papa Class ke asli 'parent_method' ko call kiya
        super().parent_method()
        
    def child_method(self):
        print("This is the child method.2")
        # JADU 2: Yahan se bhi hum direct Papa Class ke function ko chala sakte hain
        super().parent_method()

child_object = ChildClass()

# Execution Step A: child_method chala
child_object.child_method()

print("-" * 40)

# Execution Step B: parent_method chala (Overridden waala)
child_object.parent_method()

# =========================================================================
# PART 2: CONSTRUCTORS KE SAATH SUPER() KA USE (Real World Use-case)
# =========================================================================
class Employee:
    def __init__(self, name, id):
        # Base setup jo har employee ke liye common hai
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        # JADU 3: Code ki bachat! Humne Employee ke constructor ko super() se 
        # aawaz lagayi aur name-id pass kar diya. Usne automatic variables set kar diye.
        super().__init__(name, id)
        # Programmer ka apna naya extra variable
        self.lang = lang 

# Objects banaye
rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")

# Print karke check kiya data sahi set hua ya nahi
print(harry.name) 
print(harry.id)  
print(harry.lang)  
