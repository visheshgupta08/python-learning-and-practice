# Dictionary mein data 'key:value' ke pairs (jode) mein hota hai
info = {'name':'Karan', 'age': 19, 'eligible':True} 
print(info) 

# ==========================================
# 1. VALUES ACCESS KARNE KE TAREEQE
# ==========================================

# Tareeqa A: Agar 'name' key nahi mili toh yeh ERROR (Crash) dega
print(info['name']) 

# Tareeqa B: Agar 'name' key nahi mili toh yeh 'None' dega, crash nahi karega (Safe hai)
print(info.get('name')) 

# ==========================================
# 2. KEYS AUR LOOPING
# ==========================================

# info.keys() se saari keys ki list mil jati hai dict_keys(['name', 'age', 'eligible'])
print(info.keys()) 

# Saari keys par ek-ek karke loop chalaya
for key in info.keys(): 
    # Har key ki value ko print kar rahe hain
    print(info[key]) 

# ==========================================
# 3. ITEMS (KEY-VALUE PAIRS) AUR F-STRING LOOP
# ==========================================

# info.items() se key aur value dono ka joda milta hai dict_items([('name', 'Karan'), ...])
print(info.items()) 

# Loop mein 'key' aur 'value' dono ko ek saath bahaar nikal rahe hain
for key, value in info.items(): 
    # f-string ka use karke ek sundar message print kiya
    print(f"The Value corresponding to the key {key} is {value}")
