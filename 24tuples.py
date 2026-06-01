# Tuple ko round brackets () mein likhte hain. Isme bhi alag-alag data types aa sakte hain.
tup= (1,2,76,342,32,"green",True)

# Agar aap isko un-comment karoge toh error aayega kyunki tuple change nahi ho sakta (immutable hai)
#tup[0]=90

print(type(tup),tup)

# len() function tuple ke andar ke total elements ki ginti batata hai
print(len(tup))

# Positive Indexing: Pehla element (index 0) print karega
print(tup[0])

# Negative Indexing: Bilkul aakhiri element (index -1) print karega
print(tup[-1])

# Index 2 (yaani teesra element) print karega
print(tup[2])

# print(tup[34]) # Yeh error dega kyunki index 34 is tuple mein hai hi nahi (IndexError)

# 'in' keyword se hum check kar rahe hain ki kya 342 is tuple mein maujood hai
if 342 in tup:
    print("yes 342 is present in this tuple ")

# Tuple Slicing: Index 1 se lekar 3 tak ke elements ka ek naya tuple bana dega (4 shamil nahi hoga)
tup2 = tup[1:4]
print(tup2)


# Harry Sir Ki Ek Pro Tip:

'''Agar aapko kabhi ek akele element ka tuple banana ho, toh hamesha uske aage ek comma , lagana zaroori hai.
Jaise: tup1 = (5,) -> Yeh tuple hai. 'Agar aap sirf tup1 = (5) likhoge, toh Python use normal Integer samajhlega, tuple nahi!'''