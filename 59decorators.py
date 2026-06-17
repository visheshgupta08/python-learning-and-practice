# =========================================================================
# STEP 1: DECORATOR FUNCTION (Upgrade karne wali machine)
# =========================================================================
def greet(fx): 
    # '*args' aur '**kwargs' ka matlab hai: "Bhai samne se koi bhi variable ya arguments 
    # aayein (chahe tuple ho ya dictionary), unhe chup-chaap pakad lo aur crash mat ho!"
    def mfx(*args, **kwargs): 
        print("Good Morning ") # Function chalne se PEHLE ka kaam
        
        # Asli function ko unhi arguments ke sath call kiya jo bahar se aaye the
        fx(*args, **kwargs) 
        
        print("Thanks for using this function \n") # Function chalne ke BAAD ka kaam
    return mfx 


# =========================================================================
# STEP 2: FUNCTIONS KO DECORATE KARNA (@ keyword se jacket pehnana)
# =========================================================================

# 1. hello() function ke paas koi argument nahi hai (0 arguments)
@greet 
def hello(): 
    print("Hello world ") 

# 2. add() function ke paas 2 arguments hain (a aur b)
@greet 
def add (a,b): 
    print(f"Addition result: {a+b}") 


# =========================================================================
# STEP 3: FUNCTION CALLS
# =========================================================================

# Normal call lag rahi hai, par back-end mein 'greet(hello)()' chal raha hai
hello() 

# Normal call lag rahi hai, par back-end mein 'greet(add)(1, 2)' chal raha hai
add(1, 2) 


'''Revision ke liye ek line ka rule:*args aur **kwargs lagane se aapka decorator ek "Universal Decorator" ban jata hai,
 yaani aap use kisi bhi function ke upar bina dare pehna sakte ho, chahe us function mein kitne bhi inputs/arguments 
 kyun na hon!'''