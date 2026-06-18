# STEP 1: PARENT CLASS (Papa Class / Base Class)

class Employee: 
    def __init__(self, name, id): 
        self.name = name 
        self.id = id 
        
    def showDetails(self): 
        print(f"The name of Employee: {self.id} is {self.name}") 


# STEP 2: CHILD CLASS (Beta Class / Derived Class)
# Programmer ke aage bracket mein (Employee) likhne se, Employee ke 
# # saare functions aur variables automatic Programmer ke paas aa gaye!
class Programmer(Employee): 
    def showLanguage(self): 
        print("The default language is Python ") 


# STEP 3: OBJECTS CREATION AND USE

# 1. Normal Employee ka object banaya
e1 = Employee("Rohan Das", 400) 
e1.showDetails() 

# 2. Programmer ka object banaya (Iske paas Employee ke saare features hain)
e2 = Programmer("Harry", 4100) 

# Programmer class mein 'showDetails' function nahi likha tha, 
# fir bhi hum use call kar pa rahe hain kyunki usne apne Papa (Employee) se inherit kiya hai!
e2.showDetails() 

# Programmer ka apna khud ka special function
e2.showLanguage() 