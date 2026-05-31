# Default Arguments: Agar hum value nahi denge, toh a=9 aur b=1 use hoga
def average(a=9,b=1):
    print("the average is ", (a+b)/2)

# Yahan a=4 aur b=6 ho jayega (defaults override ho jayenge)
average(4,6)
# Keyword Argument: Humne bataya ki 9 sirf 'b' ke liye hai, 'a' default (9) hi rahega
average(b=9)

# fname required hai (dena hi padega), mname aur lname default hain
def name(fname , mname="jhon", lname="whatson"):
    print("hello,",fname, mname,lname)

# Teeno values manually di hain toh defaults use nahi honge
name("any","agarwal","jain")

# *numbers (Arbitrary Arguments): Yeh saari values ko ek 'Tuple' mein band kar leta hai
# Isse aap kitne bhi numbers pass kar sakte ho (5, 10, ya 100)
def average (*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # return ka matlab hai function ab yeh value wapas bhej raha hai
    return sum/len(numbers)

# Iska result return ho raha hai, agar output dekhna hai toh print(average(5,6,7,1)) karna hoga
average(5,6,7,1)

# **name (Keyword Arbitrary Arguments): Yeh values ko 'Dictionary' mein band kar leta hai
def name(**name):
    # Dictionary se value nikalne ke liye keys (fname, mname) ka use kiya
    print("hello",name["fname"],name["mname"], name["lname"])

# Yahan humne key-value pairs pass kiye hain
name(mname="buchanan", lname="barnes", fname= "james")


#Harry Sir Ka Special Concept:
#*args (Tuple): Jab aapko nahi pata ki user kitne numbers dega.
#**kwargs (Dictionary): Jab aapko data 'key-value' pairs mein bhejna ho.
"""return vs print: print sirf console par dikhata hai, lekin return us value ko
variable mein save karne ke liye wapas bhejta hai (Jaise: res = average(5,6))."""