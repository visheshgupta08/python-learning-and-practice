# User se pehla number input liya 
# i = int(input("enter the number: "))

# Jab tak user 38 ya usse chota number dalega, yeh loop chalta rahega
while(i<=38):
 # Loop ke andar dobara input le rahe hain taaki i ki value update ho sake
 i = int(input("enter the number: "))   
 print(i)

# Jaise hi user 38 se bada number dalega, loop toot jayega aur yeh line chalegi
print("done with the loop")


count=5 
# Decrementing While Loop: Yeh loop ulta chal raha hai (5 se 1 tak)
while(count>0):
 print(count)
 count=count-1 # Har baar count ki value 1 kam ho rahi hai
# Else block tab chalta hai jab while ki condition poori tarah galat (False) ho jati hai
else:
 print("i am inside else")


# --- DO-WHILE LOOP IN PYTHON ---
# Python mein 'do-while' keyword nahi hota. Harry sir ne bataya tha ki 
# isko chalane ke liye hum 'while True' aur 'break' ka use karte hain.


# Harry Sir Ki Special Trick (Do-While Loop):
#Kyunki Python mein direct do {} while() nahi hota, isiliye hum use aise likhte hain taaki
#code kam se kam ek baar zaroor chale
while True:
    # Loop body (Yeh pehle ek baar zaroor chalegi)
    i = int(input("Enter number: "))
    print(i)
    
    # Condition check jo decide karegi ki loop todna hai ya nahi
    if not (i <= 38):
        break