# Hierarchical inheritance
# =========================================================================
# PARENT CLASS (Papa Class)
# =========================================================================
class Parent:
    def house(self):
        print("Papa ka apna ek Sundar Ghar hai! ")

# =========================================================================
# CHILD CLASS 1 (Pehla Beta - Isne Parent ko inherit kiya)
# =========================================================================
class Son(Parent):
    def son_car(self):
        print("Bete ke paas apni Sports Car hai! ")

# =========================================================================
# CHILD CLASS 2 (Doosri Beti - Isne bhi Parent ko hi inherit kiya)
# =========================================================================
class Daughter(Parent):
    def daughter_bike(self):
        print("Beti ke paas apni Electric Scooty hai! ")

s = Son()
s.house()     
s.son_car()   

d = Daughter()
d.house()           
d.daughter_bike()   
# Note: 's.daughter_bike()' nahi chal sakta, kyunki bhai-behan ka data alag hai!



# Hybrid inheritance
# =========================================================================
# STEP 1: CLASS A (Sabse Upar - Base Class)
# =========================================================================
class School:
    def school_info(self):
        print("Welcome to LPU School! ")

# =========================================================================
# STEP 2: CLASS B & C (Hierarchical Setup - Dono School se bane hain)
# =========================================================================
class Teacher(School):
    def teacher_role(self):
        print("Teacher: Main Python padhata hoon.")

class Student(School):
    def student_role(self):
        print("Student: Main LPU Engage se Python seekh raha hoon.")

# =========================================================================
# STEP 3: CLASS D (Multiple Inheritance Setup - Jo B aur C dono se bani hai)
# =========================================================================
# HYBRID INHERITANCE: Yeh class Teacher aur Student dono se bani hai, 
# aur Teacher-Student khud School se bane hain! Poora mix ho gaya.
class TA(Teacher, Student):
    def ta_role(self):
        print("TA (Teaching Assistant): Main copy check karta hoon aur khud padhta bhi hoon! 📑")


obj = TA()

# Jadu: Ek hi object se hum chain ki kisi bhi class ka function chala sakte hain!
obj.school_info()   # School Class ka function chala (Dada ji)
obj.teacher_role()  # Teacher Class ka function chala (Parent 1)
obj.student_role()  # Student Class ka function chala (Parent 2)
obj.ta_role()       # TA Class ka apna function chala (Child)

print(TA.mro())