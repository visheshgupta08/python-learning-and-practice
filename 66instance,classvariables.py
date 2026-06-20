class Employee: 
    # CLASS VARIABLES (Pure school ka common board)
    companyName = "Apple" 
    noOfEmployees = 0 
    
    def __init__(self, name): 
        # INSTANCE VARIABLES (Har employee ki apni personal notebook)
        self.name = name 
        self.raise_amount = 0.02 
        # Naya object bante hi common board par employees ki ginti +1 kar di
        Employee.noOfEmployees += 1 
        
    def showDetails(self): 
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}") 


# OBJECT 1: HARRY (emp1)
emp1 = Employee("Harry") 

# Harry ne apni personal notebook mein raise_amount badal kar 0.3 kar liya
emp1.raise_amount = 0.3 

# SABSE BADA TWIST: emp1.companyName likhne se CLASS VARIABLE nahi badla!
# Harry ne apni notebook mein ek naya personal variable 'companyName' bana liya hai.
emp1.companyName = "Apple India" 

emp1.showDetails()

# CLASS VARIABLE CHANGED (Board par naam badla)
# Humne main board par company ka naam badal kar "Google" kar diya
Employee.companyName = "Google" 
print(Employee.companyName) 

# OBJECT 2: ROHAN (emp2)
emp2 = Employee("Rohan") 

# Rohan ne bhi apni personal notebook mein companyName badal kar "Nestle" likh liya
emp2.companyName = "Nestle" 

emp2.showDetails()


'''Revision ke liye Ek Chota Rule:Python ka Rule: Jab aap object.variable_name = "Kuch bhi"
 likhte hain, toh Python hamesha us object ki personal notebook (Instance) mein naya
   variable bana deta hai, woh kabhi bhi main board (Class variable) ko hath nahi lagata!
     Main board ko chhedne ke liye hamesha ClassName.variable_name likhna padta hai.'''
