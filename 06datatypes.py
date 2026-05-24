a=16
print(a)

# 'b' ek string variable hai kyunki isme text "harry" hai
b = "harry"
print(b)

# 'a1' ek integer (number) hai
a1 = 2 
# Do numbers ko add kar rahe hain
print(a+a1)

# 'c' Boolean type hai, isme sirf True ya False hota hai
c = True 

# complex() se imaginary numbers bante hain (jaise 8 + 2j)
d = complex(8,2)

# type() function batata hai ki variable kis tarah ka data save kar raha hai
print("the type of a is ", type(a))
print("the type of b is ", type(b))
print("the type of c is ", type(c))

# Python integer aur complex number ko bhi add kar sakta hai
print(a+d)

# List: Isme multiple items (numbers, strings, even doosri list) aa sakte hain. 
# Yeh square brackets [] mein hoti hai aur change (mutable) ho sakti hai.
list1= [ 8,2.3 , [4,3] , ["apple", "banana"] ]
print(list1)

# Tuple: Yaad rakhiye, Tuple hamesha round brackets () mein hota hai. 
# Harry sir ne bataya tha ki Tuple change nahi ho sakta (immutable).
tuple1 = ( 8,2.3 , (4,3) , ("apple", "banana") ) # Yahan () aayenge
print(tuple1)

# Dictionary: Yeh 'Key-Value' pair hai (jaise real dictionary mein word aur meaning hota hai)
dict1 = {"name": "sakshi", "age":20 , "canvote": True }
print(dict1)