# ==========================================
# TAREEQA 1: NORMAL IMPORT
# ==========================================
import math 
# Poore math module ko import kiya. Iske methods ko use karne ke liye 'math.' lagana padega
result = math.sqrt(9) 
print(result) 


# ==========================================
# TAREEQA 2: SPECIFIC IMPORT (from keyword)
# ==========================================
from math import sqrt, pi 
# Isse sirf 'sqrt' aur 'pi' bahaar aaye hain. Ab 'math.' likhne ki zaroorat nahi hai
result = sqrt(9) * pi 
print(result) 


# ==========================================
# TAREEQA 3: IMPORT EVERYTHING (from ... import *)
# ==========================================
from math import * 
# '*' ka matlab hai math ke SARE functions ek saath bina 'math.' ke use karne ke liye le aao
# NOTE: Is tareeqe ko bad habit mana jata hai, kyunki isse variable names takra sakte hain
result = sqrt(9) * pi 
print(result) 


# ==========================================
# TAREEQA 4: NICKNAME DENA (as keyword)
# ==========================================
from math import sqrt as s, pi 
# Humne 'sqrt' ka naam chhota karke 's' rakh diya (Alias bana diya)
result = s(9) * pi 
print(result) 


# ==========================================
# TAREEQA 5: POORE MODULE KO NICKNAME DENA
# ==========================================
import math as math_builtin_python 
# Poore math module ka ek bada-sa nickname rakh diya
result = math_builtin_python.sqrt(9) * math_builtin_python.pi 
print(result) 


# ==========================================
# 6. DIR() FUNCTION & SPECIAL CONSTANTS
# ==========================================
import math 
# dir() function math module ke andar jitne bhi functions aur variables hain, unki list dikhata hai
print(dir(math)) 

# math.nan ka matlab hota hai 'Not a Number'. Yeh ek special float value hoti hai math mein
print(math.nan, type(math.nan))

# PART 6: APNI BANAYI HUI FILE SE FUNCTION YA VARIABLE IMPORT KARNA
# =========================================================================

# MAAN LO AAPNE USI FOLDER MEIN EK FILE BANAYI HAI JISKA NAAM 'harry_file.py' HAI
# Aur usme aapne ek variable 'msg' aur ek function 'welcome()' likha hua hai:
# msg = "Hello from Harry Sir's Video!"
# def welcome(): print("Welcome to Video 44!")

# Toh aap use apni main file mein aise import karke bina dare chalayenge:
"""
from harry_file import msg, welcome

print(msg)      # Output: Hello from Harry Sir's Video!
welcome()       # Output: Welcome to Video 44!
"""

# Note: Maine ise comment mein isliye rakha hai taaki agar 'harry_file.py' 
# aapke folder mein na bhi ho, toh bhi code crash na kare aur baki upar ka chalta rahe!

#💡 Ek Important Interivew Question:
"""Aksar pucha jata hai ki from math import * kyun use nahi karna chahiye? Iska jawaab yeh hai ki
  agar aapne apne code mein pehle se ek function banaya hai def sqrt():, aur aapne niche import * kar diya,
  toh math ka sqrt aapke wale function ko mita (overwrite) dega,
  jisse code kharab ho jayega. Isliye specific import (from math import sqrt) ko hi best mana jata hai."""