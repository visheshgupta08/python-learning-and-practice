# ==========================================================
# CONCEPT: finally block hamesha chalega, chahe error aaye ya na aaye, 
# aur chahe function ke andar se value RETURN hi kyun na ho rahi ho!
# ==========================================================

def func1(): 
    try: 
        l = [1, 3, 5, 7] # List mein index 0, 1, 2, 3 hain
        i = int(input("Enter the index: ")) 
        print(l[i]) 
        
        # Agar code sahi chala, toh yeh return hone se PEHLE finally block ko chalayega
        return 1 
        
    except: 
        print("Some error occured") 
        
        # Agar error aayi, toh yeh return hone se PEHLE bhi finally block chalega
        return 0 
        
    finally: 
        # Yeh line HAR HAAL MEIN chalegi! 
        # Python function se bahaar nikalne (return karne) se pehle isko run karta hai.
        print("I am always executed") 

    # AGAR AAP FINALLY KI JAGAH YAHAN NORMAL PRINT LIKHTE:
    # print("I am always executed") 
    # Toh woh kabhi chalta hi nahi, kyunki return ke baad normal code block block ho jata hai!

# Function ko call kiya aur uski return value (1 ya 0) ko x mein save kiya
x = func1() 
print("Function ne return kiya:", x)
