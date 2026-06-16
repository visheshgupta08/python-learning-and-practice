# =========================================================================
# STEP 1: CLASS DEFINITION WITH CONSTRUCTOR
# =========================================================================
class Person : 
    # __init__ ek special method hai jise CONSTRUCTOR kehte hain.
    # Ise alag se call nahi karna padta, jaise hi naya object banta hai, 
    # yeh AUTOMATICALLY apne aap chal jata hai!
    def __init__(self, n, o): 
        print("Hey I am a person") 
        # Jo values (n, o) bahar se aayengi, unhe self.name aur self.occ mein save kar liya
        self.name = n 
        self.occ = o 
        
    # Normal Method (Function)
    def info(self): 
        print(f"{self.name} is a {self.occ}") 


# =========================================================================
# STEP 2: OBJECTS CREATION (Yahan automatic constructor chalega!)
# =========================================================================

# Jaise hi 'a = Person(...)' likha, back-end mein automatic __init__ chala.
# n ban gaya "Harry" aur o ban gya "Developer". Screen par "Hey I am a person" print ho jayega.
a = Person ("Harry", "Developer") 

# isi tarah 'b' ke liye bhi automatic constructor chala.
b = Person ("Divya", "HR") 


# =========================================================================
# STEP 3: METHODS CALL (Data use karna)
# =========================================================================
# Ab info() ko call kiya data print karne ke liye
a.info() # Output: Harry is a Developer
b.info() # Output: Divya is a HR



'''Revision ke liye Short Note (Interview Question):
Aksar pucha jata hai ki Constructor kya hota hai?
Jawaab: __init__ Python ka built-in constructor hai. Iska kaam hota hai object banate hi 
variables ke andar values ko initialize (set) karna [stem-calculative-problem-solving].
Ise humein manually call nahi karna padta, yeh object = ClassName() likhte hi automatic 
back-end mein chal jata hai.'''