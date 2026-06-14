# Hamari asli list
l = [1, 2, 4, 6, 4, 3] 

# =========================================================================
# 1. MAP (Har ek element par ek function apply karna)
# =========================================================================
# Formula: map(function, iterable)

# --- PURANA TAREEQA  ---
# def cube(x): 
#    return x*x*x
# newl = []
# for item in l: 
#     newl.append(cube(item))
# Isme 4-5 lines lagti thi aur extra empty list banani padti thi.

# SMART TAREEQA: map() ne list ke har ek number ka cube nikala, 
# aur list() ne use wapas ek nayi list mein convert kar diya.
newl = list(map(lambda x : x*x*x, l)) 
print("Map ka result (Cubes):", newl) 


# =========================================================================
# 2. FILTER (Sirf wahi elements rakhna jo condition pass karein)
# =========================================================================
# Formula: filter(function, iterable)

# Yeh function True return karega agar number 2 se bada hai
def filter_function(a): 
    return a > 2 

# filter() ne list ke saare elements par condition check ki. 
# Jo numbers 2 se bade the (4, 6, 4, 3), sirf unka naya set bana kar list mein daal diya.
newnewl = list(filter(filter_function, l)) 
print("Filter ka result (Numbers > 2):", newnewl) 


# =========================================================================
# 3. REDUCE (Puri list ko jodkar ya process karke ek SINGLE VALUE banana)
# =========================================================================
# NOTE: reduce() Python mein direct nahi milta, iske liye 'functools' module se import karna padta hai
from functools import reduce 

numbers = [1, 2, 3, 4, 5] 

# reduce() kaise kaam karta hai:
# Step A: Pehle 1 aur 2 ko joda -> 3
# Step B: Phir us 3 mein agla number 3 joda -> 6
# Step C: Phir 6 mein agla number 4 joda -> 10
# Step D: Phir 10 mein aakhri number 5 joda -> 15 (Final Answer)
sum = reduce(lambda x,y : x+y , numbers) 
print("Reduce ka result (Total Sum):", sum) 


'''Short Summary (Yaad rakhne ke liye):
map(): List ka size SAME rehta hai, par andar ki values badal jaati hain (jaise sabka cube ho gaya).
filter(): List ka size CHHOTA ho jata hai, par andar ki values wahi rehti hain (sirf condition pass karne wale bachte hain).
reduce(): Poori list gayab hokar sirf EK SINGLE VALUE ban jaati hai (jaise total sum).'''