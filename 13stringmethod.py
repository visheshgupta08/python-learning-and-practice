 # Strings immutable hoti hain, inme koi change permanent nahi hota, naya result milta hai
a= "!!! Harry!!!! !!" 
print(len(a))
print(a)

# upper() saare letters ko CAPITAL kar deta hai
print(a.upper())

# lower() saare letters ko small kar deta hai
print(a.lower())

# rstrip() sirf right side se diye gaye character (!) ko hata deta hai
print(a.rstrip("!"))

# replace() purane shabd ko naye shabd se badal deta hai
print(a.replace("Harry","john"))

# split() space ke basis par string ke tukde karke ek List bana deta hai
print(a.split(" "))

blogheading= "introduction tO jS "
# capitalize() pehle letter ko capital karta hai aur baaki sabko small kar deta hai
print(blogheading.capitalize())

str1= "welcome to the console!!!" 
print(len(str1)) 

# center(50) string ke aage-piche spaces jod kar use 50 characters ke beech mein laata hai
print(len(str1.center(50)))

# count() batata hai ki koi word ya character string mein kitni baar aaya hai
print(a.count("Harry")) 

str1= "welcome to the console!!!" 
# endswith() check karta hai ki string "!!!" par khatam ho rahi hai ya nahi (True/False)
print(str1.endswith("!!!"))

str1= "welcome to the console!!!" 
# Index 4 se 10 ke beech check karega ki kya wo part "to" par end ho raha hai
print(str1.endswith("to", 4 , 10))

str1= "He's name is dan .He is an honest man."
# find() substring ko dhoondta hai, na milne par -1 deta hai (error nahi deta)
print(str1.find("ishh"))
# index() bhi dhoondta hai, par agar na mile toh sidha error throw karta hai
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
# isalnum() True deta hai agar string mein sirf A-Z, a-z, ya 0-9 ho (no spaces/symbols)
print(str1.isalnum())

str1="Welcome" 
# isalpha() True deta hai agar string mein sirf alphabets (letters) hon
print(str1.isalpha())

str1 = "hello world"
# islower() check karta hai ki kya saare letters small case mein hain
print(str1.islower())

str1= "We wish you a Merry Christmas\n"
# isprintable() False dega agar string mein \n ya \t jaise non-printable characters hon
print(str1.isprintable())

str1= "      "      #using Spacebar 
# isspace() True deta hai agar string mein sirf aur sirf spaces hon
print(str1.isspace())

str2= "    "  #using tab 
print(str2.isspace())

str1 = "World Health Organigation"
# istitle() True deta hai agar har word ka pehla letter Capital ho
print(str1.istitle()) 

str2= "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a interpreted language "
# startswith() check karta hai ki kya string "Python" se shuru ho rahi hai
print(str1.startswith("Python"))

str1 = "Python is a interpreted language "
# swapcase() badal deta hai: capital ko small aur small ko capital kar deta hai
print(str1.swapcase())

str1= "His name is Dan . Dan is an honest man ."
# title() har ek word ke pehle letter ko Capital bana deta hai
print(str1.title())
 

#   Interview Questions Waali Tip:
#Harry sir ne isme ek bohot important farq bataya hai jo interview mein pucha jata hai:
#find() agar text nahi dhoond paata toh -1 return karta hai (program chalta rehta hai).
#index() agar text nahi dhoond paata toh ValueError de deta hai (program ruk jata hai).