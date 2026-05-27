# User se age input le kar use pehle hi integer mein badal diya
a= int(input("enter your age:")) 
print("your age is:", a )

# Conditional operators jo True ya False (Boolean) return karte hain
# > , < , >= , <= , == , !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# Simple If-Else: Agar condition True hui toh if chalega, nahi toh else chalega
if(a>18):
    print("you can drive")
else:
    print("you cannot drive") 


appleprice= 210 
budget = 200 
# Budget check karne ke liye ek aur simple if-else example
if(appleprice <= budget ):
    print("alexa, add 1 kg apples to the cart.")
else:
    print("alexa, do not add apples to the cart.")


num= int(input("enter the value of num:"))
# Elif Ladder: Jab aapke paas check karne ke liye bohot saari conditions hon
if(num<0):
    print("number is negative.")
elif(num==0):
    print("number is zero . ")
elif(num==999):
    print("numer is special.") # Note: Agar user 999 dalega toh pehle 'num>0' check nahi ho raha, seedhe yahan match ho jayega
else:
    print("number is positive.")



num= 18
# Nested If-Else: Jab ek condition sach hone ke baad andar ek aur condition check karni ho
if(num<0):
    print("number is negative.")
elif(num>0):
    # Agar number positive hai, toh ab andar wali conditions check hongi
    if(num<=10):
        print("number is between 1-10")
    # 'and' operator tab use hota hai jab dono baatein sach honi zaroori hon
    elif(num>10 and num <= 20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero . ")

    #Ek Choti Si Baat (Logical Bug):
    """Aapne teesre block mein elif(num==999) likha hai. Agar user 999 enter karega, toh
    Python pehle hi num<0 aur num==0 check karke fail hoga, fir num==999 match ho jayega
    aur "numer is special." print karega. Ye bilkul sahi chalega!"""
    """ Lekin agar aapne num==999 ko else ke baad rakha hota ya kisi galat order mein, toh logic
    bigad jata. Harry sir kehte hain ki conditions ka order hamesha dhyan se rakhna chahiye."""