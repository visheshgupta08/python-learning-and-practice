# 1. Sets duplicate values ko remove kar deta hai (Unique elements rakhta hai)
# Aur iska koi order nahi hota (unordered), yaani elements aage-piche ho sakte hain
s = {2, 4, 2, 6} 
# Output mein sirf {2, 4, 6} aayega, kyunki '2' do baar tha toh duplicate hat gaya
print(s) 

# 2. Set mein alag-alag data types (String, Int, Boolean, Float) ek saath aa sakte hain
info = {"Carla", 19, False, 5.9, 19} 
# Yahan bhi '19' do baar hai, toh output mein ek hi baar '19' dikhega
print(info) 

# 3. KHALI (EMPTY) SET BANANE KA RULES:
# Agar aap sirf {} likhenge, toh Python use Dictionary samajh lega
# Harry = {} -> Isse type dictionary aayega set nahi

# Isliye khali set banane ke liye set() function ka use karte hain:
Harry = set() 
# Yeh 'set' class print karega (<class 'set'>)
print(type(Harry)) 

# 4. LOOP IN SET:
# Set ke saare elements ko ek-ek karke print karne ke liye loop chalaya
for value in info: 
    # Yaad rahe: Elements ka order fix nahi hota, toh kisi bhi sequence mein print ho sakte hain
    print(value)
