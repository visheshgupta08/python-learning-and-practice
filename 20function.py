# 'def' keyword se hum apna khud ka function banate hain
# Is function ka kaam hai do numbers ka mean nikalna aur print karna
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

# Yeh function check karega ki kaunsa number bada hai
def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater")

# 'pass' ka matlab hai "abhi isse khali chhod do"
# Agar aap function ki body khali chhodoge toh error aayega, isliye 'pass' likhte hain
def islesser(a,b):
    pass

# Variables define kiye
a = 9
b = 8 
# Function ko 'call' kiya: Ab function ke andar 'a' aur 'b' ki values chali jayengi
isGreater(a,b)
calculateGmean(a,b)

c = 8
d = 7
# Fayda: Humein dobara if-else ya calculation likhne ki zaroorat nahi padi
isGreater(c,d)
calculateGmean(c,d)