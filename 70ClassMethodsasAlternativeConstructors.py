class Employee:
    def __init__(self, name, salary):
        # 1. Normal Constructor: Ise name aur salary alag-alag chahiye hote hain
        self.name = name 
        self.salary = salary

    # =========================================================================
    # ALTERNATIVE CONSTRUCTOR (Ek naya tarika object banane ka)
    # =========================================================================
    @classmethod
    def fromStr(cls, string):
        # Yeh method ek single string "John-12000" ko pakadta hai,
        # use "-" se do tukdon mein todta hai (split) aur 'cls' (Employee Class) ko bhej deta hai.
        # string.split("-")[0] ban gaya "John"
        # int(string.split("-")[1]) ban gaya 12000
        return cls(string.split("-")[0], int(string.split("-")[1]))


# =========================================================================
# RUN KARKE DEKHTE HAIN
# =========================================================================

# Tarika A: Normal tarika (Do alag-alag arguments diye)
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)  

print("-" * 40)

# Tarika B: Alternative tarika (Poori ek lambi string bhej di!)
string = "John-12000"
e2 = Employee.fromStr(string) # Jadu: fromStr ne andar hi andar 'e2 = Employee("John", 12000)' chala diya!

print(e2.name)   
print(e2.salary)  
