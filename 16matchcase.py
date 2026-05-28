x= int(input("enter the value of x:")) 
# match keyword batata hai ki hum 'x' variable ki value ko check kar rahe hain
match x:
    # Agar user ne 0 input kiya toh yeh chalega
    case 0:
        print("x is zero")
        
    # Agar user ne 4 input kiya toh yeh chalega
    case 4:
        print("x is four")
        
    # case _ ka matlab default hai, lekin 'if' lagane se yeh sirf tabhi chalega jab x 90 nahi hoga
    # Agar user 80 dalega, toh wo 90 nahi hai, isiliye yahi case chal jayega aur neeche wala check hi nahi hoga!
    case _ if x!=90:
        print(x, "is not 90")
        
    # Yeh case tabhi chalega jab upar ke saare cases fail ho jayein AUR x 80 na ho
    case _ if x!=80:
        print(x, "is not 80")
        
    # Yeh bilkul aakhri default case hai (jaise else hota hai). Jab kuch bhi match nahi karega tab yeh chalega.
    case _:
        print(x)