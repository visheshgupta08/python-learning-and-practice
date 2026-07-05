class Employee:
    def __init__(self, name):
        self.name = name 
        
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance 

    def show(self):
        print(f"The dance is {self.dance}")


# =========================================================================
# MULTIPLE INHERITANCE (Ek child ke do parents!)
# =========================================================================
# Jadu: DancerEmployee ke bracket mein (Employee, Dancer) likha hai.
# Iska matlab is ek akeli child class ke paas dono parents ki taqat aa gayi!
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name



o = DancerEmployee("Kathak", "Shivani")

print(o.name)  
print(o.dance)  
# =========================================================================
# SABSE BADA TWIST: o.show() karne par kaun sa show() chalega?
# =========================================================================
# Employee ke paas bhi show() hai, aur Dancer ke paas bhi show() hai.
# Kyunki humne upar definition mein 'Employee' ka naam PEHLE likha hai: (Employee, Dancer),
# isiliye Python pehle 'Employee' wale show() ko chalayega!
o.show()  


# =========================================================================
# MRO (Method Resolution Order) CHECK
# =========================================================================
# mro() function computer ki poori planning (order) nikal kar dikhata hai 
# ki agar koi function dhoondhna hai, toh Python kis raste se jayega.
print(DancerEmployee.mro())

