# User se 5 aur 9 ke beech ka koi number manga
a = int(input("Enter any value between 5 and 9: ")) 

# LOGIC: Agar user ne 5 se chhota ya 9 se bada number dala:
if (a < 5 or a > 9): 
    # 'raise' keyword ka use karke humne ZABARDASTI ek ValueError generate kar di
    # Aur uske andar apna custom message likh diya
    raise ValueError("Value should be between 5 and 9")

# Agar input sahi hai (jaise 6 ya 7), toh upar wala condition chalega hi nahi
# Aur program bina kisi error ke normal aage badh jayega
print(f"Bahut badhiya! Aapne sahi number dala: {a}")


#quick quiz 

# User se input le rahe hain (shuruat mein string hi rehne diya taaki 'quit' check kar sakein)
a = input("Enter any value between 5 and 9 or type 'quit': ") 

# Step 1: Pehle check karo ki kya user ne 'quit' likha hai
if a == "quit": 
    # Agar user ne 'quit' likha hai toh bina kisi error ke program yahin khatam ho jayega
    print("No error, program stopped.") 

# Step 2: Agar 'quit' nahi likha, toh baaki saare inputs is else block ke andar check honge
else: 
    try: 
        # String input ko integer (number) mein badalne ki koshish kar rahe hain
        num = int(a) 
        
        # Agar number 5 se chhota ya 9 se bada hai, toh zabardasti ValueError raise karo
        if num < 5 or num > 9: 
            raise ValueError("Value should be between 5 and 9") 
        # Agar number 5 aur 9 ke beech mein hai (matlab sahi number hai)
        else: 
            print(f"Success! You entered a valid number: {num}") 
            
    # Step 3: Agar int(a) karne par ValueError aayi (jaise user ne 'hello' likha ho) 
    except ValueError : 
       raise ValueError("Invalid input! You must enter a number or 'quit'")
