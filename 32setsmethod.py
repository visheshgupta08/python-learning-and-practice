# ==========================================
# 1. UNION & UPDATE (Dono sets ko jodna)
# ==========================================
s1 = {1, 2, 5, 6} 
s2 = {3, 6, 7} 
# union() dono ko mila kar NAYA set banata hai, s1 aur s2 pehle jaise hi rehte hain
print(s1.union(s2)) 

# update() s2 ke saare elements ko uthakar s1 ke ANDAR hi daal deta hai
s1.update(s2)    
print(s1, s2) 

# ==========================================
# 2. INTERSECTION (Common elements nikalna)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# union() se firse dono sets mix hokar naya set bana
cities3 = cities.union(cities2)
print(cities3)

# intersection() dono sets mein jo COMMON (Tokyo, Madrid) hai, unka naya set banata hai
cities4 = cities.intersection(cities2)
print(cities4)

# intersection_update() common elements ko dhundkar seedhe 'cities' set ko badal deta hai
cities.intersection_update(cities2)
print(cities)

# ==========================================
# 3. SYMMETRIC DIFFERENCE (Jo common NAHI hain)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# Jo dono mein common hain (Tokyo, Madrid) unhe CHHODKAR baaki sab naye set mein aayenge
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# ==========================================
# 4. DIFFERENCE (Sirf pehle set ke unique elements)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Madrid"}
# cities mein se woh hata do jo cities2 mein bhi hain (Madrid hat jayega)
cities3 = cities.difference(cities2)
print(cities3)

# ==========================================
# 5. ISDISJOINT, ISSUPERSET, ISSUBSET (Check karne ke liye)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# isdisjoint(): Agar DONO mein ek bhi element common NAHI hai toh True, nahi toh False
cities3 = cities.isdisjoint(cities2)
print(cities3) 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
# issuperset(): Kya cities ke andar cities2 ke SARE elements hain? (Nahi hain -> False)
print(cities.issuperset(cities2)) 

cities3 = {"Seoul", "Madrid", "Kabul"}
# Kya cities ke andar cities3 ke SARE elements hain? (Nahi -> False)
print(cities.issuperset(cities3))
# issubset(): Kya cities3 ke SARE elements cities ke andar hain? (Nahi -> False)
print(cities.issubset(cities3))

# ==========================================
# 6. ADD & REMOVE / DISCARD (Elements badalna)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# add() se set mein naya element jud jata hai
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# remove() element ko hata deta hai. (Agar element na ho toh ERROR deta hai)
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# discard() bhi element hatata hai, par agar element NA HO toh ERROR NAHI deta (Safe hai)
cities.discard("Tokyo2") 
print(cities)

# ==========================================
# 7. POP, DEL, CLEAR (Khatam ya khali karna)
# ==========================================
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# pop() kisi bhi EK random element ko nikal deta hai (Kyunki set ka order fix nahi hota)
item = cities.pop()
print(cities)
print(item) # Kaunsa item bahaar nikla, woh dikhega

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del poore set variable ko hi memory se DELETE kar deta hai
del cities
# print(cities) # <-- IS LINE KO RUN KARNE SE ERROR AAYEGA! Kyunki cities ab bacha hi nahi.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# clear() set ke andar ke saare elements mita deta hai, par set (khali bartan) bacha rehta hai
cities.clear()
print(cities) # Output: set()

# ==========================================
# 8. CHECK IF ELEMENT EXISTS (In keyword)
# ==========================================
info = {"Carla", 19, False, 5.9}
# Check kar rahe hain ki "Carla" set ke andar maujood hai ya nahi
if "Carla" in info:
    print("Carla is Present.")
else:
    print("Carla is absent.")



