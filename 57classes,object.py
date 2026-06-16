# =========================================================================
# STEP 1: CLASS DEFINITION (Form ya Blueprint banana)
# =========================================================================
class Person: 
    # DEFAULT VALUES: Agar hum kisi object ke liye naam/kaam nahi batayenge, 
    # toh computer automatic ye default details utha lega (Jaise 'c' object ke case mein hoga)
    name = "Harry" 
    occupation = "Software Developer" 
    networth = 10 
    
    # METHDOD (Class ke andar banya hua function)
    # 'self' ka matlab hai "woh object jo is function ko abhi use kar raha hai"
    def info(self): 
        print(f"{self.name} is a {self.occupation}") 


# =========================================================================
# STEP 2: OBJECTS CREATION (Naye bande/instances banana)
# =========================================================================

# Humne 'Person' class se 3 alag-alag log (Objects) banaye
a = Person() 
b = Person() 
c = Person() # 'c' mein hum koi naya data nahi bharenge, ye default par chalega

# Object 'a' (Shubham) ne apna alag data bhara
a.name = "Shubham" 
a.occupation = "Accountant" 

# Object 'b' (Nitika) ne apna alag data bhara
b.name = "Nitika" 
b.occupation = "HR" 


# =========================================================================
# STEP 3: FUNCTION CALLS (Data use karna)
# =========================================================================

# 1. a.info() chalne par 'self' ban jayega 'a'. Output aayega: Shubham is a Accountant
a.info() 

# 2. b.info() chalne par 'self' ban jayega 'b'. Output aayega: Nitika is a HR
b.info() 

# 3. c.info() chalne par 'self' ban jayega 'c'. Kyunki c mein koi data nahi tha, 
# toh ye class ki automatic Default Values utha lega: Harry is a Software Developer
c.info()



'''Revision ke liye ek line ka rule:
self ka bas itna kaam hai ki woh computer ko batata hai ki Bhai abhi a ki baat ho rahi hai, ya b ki, ya c ki!'''