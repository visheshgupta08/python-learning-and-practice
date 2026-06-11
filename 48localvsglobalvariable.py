# =========================================================================
# CASE 1: BINA GLOBAL KEYWORD KE (Ghar ka AC vs Gali ki Street Light)
# =========================================================================
print("--- Case 1: Without global keyword ---")

x = 4 # Yeh GLOBAL x hai (Sabse bahar banyaya hai)
print(x) # Output: 4

def Hello():
    x = 5 # Yeh LOCAL x hai (Sirf is function ke andar ke liye banya hai)
    y = 1 # Yeh LOCAL y hai (Bahar ka koi bhi aadmi ise use nahi kar sakta)
    print(f"the local x is {x}") # Yeh local x (5) ko uthayega
    print("hello harry")

# Yeh abhi function ke BAHAR hai, toh yeh bahar wale asli GLOBAL x (4) ko hi print karega
print(f"the global x is {x}") 

Hello() # Function call hua, toh andar ka print chala (local x is 5)

# Function chalne ke BAAD bhi bahar wala GLOBAL x abhi bhi 4 hi rahega, badla nahi!
print(f"the global x is {x}") 

# print(y) # <-- AGAR YEH UNCOMMENT KIYA TOH ERROR AAYEGA! Kyunki y sirf Hello() ke andar bacha hai


# =========================================================================
# CASE 2: GLOBAL KEYWORD KE SAATH (Gali ki light ka switch andar le aana)
# =========================================================================
print("\n--- Case 2: With global keyword ---")

x = 10 # Naya GLOBAL x set kiya

def Hello_with_global():
    global x # Python ko chillakar bola: "Bhai, hum bahar wale asli x ko badalna chahte hain!"
    x = 5    # Ab isne local dabba nahi banaya, balki bahar wale asli x ko 10 se badal kar 5 kar diya
    y = 5    # Yeh abhi bhi LOCAL y hai
    print("Local y inside function:", y)

Hello_with_global() # Function chala, aur isne asli x ki value badal di

#Ab function ke bahar jab hum x print karenge, toh output 10 nahi balki 5 aayega!
print("Global x after function call:", x) 

# print(y) # <-- Yahan bhi error aayega, kyunki y local hai aur function ke sath khatam ho gaya
