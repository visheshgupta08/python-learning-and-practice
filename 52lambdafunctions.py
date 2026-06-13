# --- PURANA TAREEQA  ---
# def doubleL:
#     return x*2 # Isme 2-3 lines lagti thi function banane mein

# =========================================================================
# 1. LAMBDA FUNCTIONS (Single Line Functions)
# =========================================================================
# Formula: lambda arguments: expression

# 1 argument wala lambda function (X ko 2 se multiply karega)
double = lambda x: x*2 

# 1 argument wala lambda function (X ka cube nikalega)
cube = lambda x: x*x*x 

# 2 arguments wala lambda function (X aur Y ka average nikalega)
avg = lambda x,y: (x+y)/2 

# Inhe normal function ki tarah hi call karte hain:
print("Double of 5 is:", double(5)) # Output: 10
print("Cube of 5 is:", cube(5))     # Output: 125
print("Average of 5 and 3 is:", avg(5,3)) # Output: 4.0


# =========================================================================
# 2. HIGHER-ORDER FUNCTION (Function ke andar function pass karna)
# =========================================================================

# Yeh ek normal function hai jo ek function (fx) aur ek value (value) input leta hai
def appl(fx, value): 
    # Yeh fx wale function ko chala kar usme 6 plus kar deta hai
    return 6 + fx(value) 

# Case A: Humne 'cube' function ko as an argument pass kiya
# Calculation: 6 + cube(2) -> 6 + (2*2*2) -> 6 + 8 = 14
print("Using cube function in appl:", appl(cube, 2)) 

# Case B: Humne direct ek anonyomous lambda function pass kar diya on-the-fly!
# Calculation: 6 + (2*2) -> 6 + 4 = 10
print("Using direct lambda in appl:", appl(lambda x: x*2 , 2))



''' Interview Tip:Lambda functions ka use hum tabhi karte hain jab humein kisi chhotey kaam 
ke liye sirf ek line ka function banana ho, jise humein poore code mein baar-baar use
 nahi karna (jaise appl() ke andar direct pass karna). Agar bada logic ho, toh hamesha 
 normal def wala function hi use karna chahiye.'''