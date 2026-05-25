# 'a' aur 'b' yahan strings hain kyunki wo quotes "" mein hain
a="1"
b="2"

# Explicit Typecasting: Humne manually int() use karke string ko number banaya 
# taaki unhe joda (add kiya) ja sake, varna wo "12" print kar dete
print(int(a)+int(b)) 

# Implicit Typecasting: Python khud se chhote data type (int) ko 
# bade data type (float) mein convert kar deta hai taaki koi data loss na ho
c=1.9 # Float (decimal wala number)
d=8   # Integer (poora number)

# Yahan Python ne 'd' ko khud 8.0 maan liya aur result decimal mein diya
print(c+d)