# ==========================================
# PART 1: MULTIPLICATION TABLE WITH TRY-EXCEPT
# ==========================================

a = (input("enter no. :")) 
print(f"Multiplication table of {a} is :")

# try block ke andar hum woh code likhte hain jisme lagta hai ki ERROR AA SAKTI HAI
try: 
    for i in range(1,11):
        # Agar user number ki jagah 'Harry' likh de, toh int(a) line par error aayegi
        print(f"{int(a)} x {i} = {int(a)*i}")

# Agar try ke andar koi bhi error aayi, toh program crash nahi hoga, seedhe yahan aayega
except Exception as e : 
    # Yeh line print karegi ki ASLI ERROR KYA THI (jaise ValueError)
    print("Kuch gadbad hui:", e) 

# Yeh lines hamesha chalengi, chahe error aaye ya na aaye (Kyunki humne exception handle kar li hai)
print("some imp lines of code") 
print ("End of program")


# ==========================================
# PART 2: SPECIFIC EXCEPTIONS (ValueError & IndexError)
# ==========================================

try: 
    num = int(input("enter number:")) 
    a = [5, 3] # Is list mein sirf 2 items hain, index 0 aur 1
    print(a[num]) 

# Agar user integer ke alawa kuch aur daale (jaise 'abc'), toh yeh block chalega
except ValueError: 
    print("number entered is not an integer ") 

# Agar user aisa index daale jo list mein nahi hai (jaise 5 ya -3), toh yeh block chalega
except IndexError: 
    print("Index error")
