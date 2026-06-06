# Do alag-alag employees ki ID aur unke scores ki dictionary
ep1 = {122:45 , 123:89, 567:69, 670:69} 
ep2 = {222:67 , 566:90} 

# ==========================================
# 1. UPDATE METHOD (Dono ko jodne ke liye)
# ==========================================
# ep2 ka saara data uthakar ep1 ke andar daal dega
ep1.update(ep2) 
print("After Update ep1:", ep1) 


# ==========================================
# 2. CLEAR METHOD (Sab saaf karne ke liye)
# ==========================================
ep1 = {122:45 , 123:89, 567:69, 670:69} 
# CRITICAL FIX: clear() ke andar kuch nahi likhte! Yeh akela hi poori dict khali kar deta hai
ep1.clear() 
print("After Clear ep1:", ep1) # Output aayega: {} (Khali dabba)


# ==========================================
# 3. POPITEM METHOD (Aakhri element hatane ke liye)
# ==========================================
ep1 = {122:45 , 123:89, 567:69, 670:69} 
# Yeh dictionary ke sabse LAST wale key-value pair (670:69) ko nikal phekega
ep1.popitem() 
print("After Popitem ep1:", ep1) 


# 4. POP METHOD (Kisi specific key ko hatane ke liye)
ep1 = {122:45 , 123:89, 567:69, 670:69}
# Mujhe key '123' ko hatana hai, toh uska naam likhenge
ep1.pop(123) 
print("After Pop(123) ep1:", ep1)


# 5. DEL KEYWORD (Kisi ek item ya poori dict ko udane ke liye)
ep1 = {122:45 , 123:89, 567:69, 670:69}
# Yeh specific key '122' ko poori tarah delete kar dega
del ep1[122]
print("After del ep1[122]:", ep1)

# Note: Agar aap 'del ep1' likhenge, toh poori dictionary memory se gayab ho jayegi!


# 6. DICTIONARY MEIN NAYA DATA JODNA YA BADALNA
ep1 = {122:45 , 123:89}
# Agar key pehle se NAHI hai, toh NAYI KEY jud jayegi
ep1[999] = 100 
# Agar key pehle se HAI, toh uski VALUE BADAL (update) jayegi
ep1[122] = 50 
print("After Manual Changes ep1:", ep1)


