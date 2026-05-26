fruit = "mango"
# len() function string ki total lambai (count) batata hai
mangolen = len(fruit)
print(mangolen)

# 0 se shuru hoga par 4th index wala character nahi lega (0,1,2,3 lega)
# print(fruit[0:4])

# 1 se shuru karega aur 3 tak jayega (1,2,3 lega)
# print(fruit[1:4])

# Agar start khali choda hai toh Python ise 0 se shuru maanta hai
# print(fruit[:5])

# Negative Slicing: Iska matlab hai [0 : len(fruit)-3] i.e. [0 : 2]
# print(fruit[0:-3])

# Yeh upar wale code ka hi lamba tarika hai, same result aayega
# print(fruit[:len(fruit)-3])

# Isme empty output aayega kyunki start index (-1 i.e. 4) end index (2) se bada hai
print(fruit[-1:len(fruit)-3])

# Iska matlab hai [len(fruit)-3 : len(fruit)-1] i.e. [2 : 4]
# Index 2 aur 3 print honge (Output: 'ng')
print(fruit[-3:-1])

#Harry Sir Ki Special Tip:
#Jab bhi negative slicing (-) dekho, toh bas usme len(fruit) add kar do.
#Example: fruit[-3:-1] ban jayega fruit[5-3 : 5-1], yaani fruit[2:4].

# quick quiz :
nm = "harry"
print(nm[-4:-2]) 
# answer = ar 