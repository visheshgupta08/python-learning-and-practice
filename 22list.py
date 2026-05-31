# List mein alag-alag types ka data (numbers, text, boolean) save kar sakte hain
marks = [3,5,6,"harry",True]
print(marks)
print(type(marks))

# Positive Indexing: 0 se shuru hoti hai
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) # Yeh error dega kyunki index 5 exist nahi karta

# Negative Indexing: Isme peeche se count hota hai (-1 se)
# print(marks[-3])  
# print(marks[len(marks)-3]) # Lamba tarika: total length se minus karna
# print(marks[5-3])  
# print(marks[2]) # Teeno ka matlab index 2 hi hai (Output: 6)

# 'in' keyword check karta hai ki kya koi cheez list ke andar hai ya nahi
# Yahan "6" ek string hai aur list mein number 6 hai, isiliye 'no' aayega
if "6" in marks:
    print("yes")
else:
    print("no")

# 'in' keyword strings ke sath bhi kaam karta hai (substring check karne ke liye)
if "ha" in "harry":
    print("yes")

print(marks)
# Slicing: Index 1 se lekar index 3 tak print karega (-1 shamil nahi hoga)
print(marks[1:-1])
# Slicing with step: Index 1 se 3 tak chalega aur har 2 step baad uthayega
print(marks[1:4:2])

# --- LIST COMPREHENSION (Short tarike se list banana) ---
# 0 se 9 tak ke saare numbers ka square (i*i) karke list bana dega
lst= [i*i for i in range (10)]
print(lst)

# Isme condition bhi laga di: Sirf Even numbers (jo 2 se divide ho) unka hi square karega
lst=[i*i for i in range(10) if i%2==0]
print(lst)
 

#  Harry Sir Ki Ek Importat Interview Tip:
""" Aapne code mein check kiya if "6" in marks:. Yaad rakhiye, Python mein 6 (integer)
 aur "6" (string) dono bilkul alag hain. Isiliye aapka code isme no print karega.
   Agar aap bina quotes ke if 6 in marks: likhte, toh output yes aata."""


#Question : WAP to ask the user to enter names of their 3 favorite movies and store them in a list .

a = input("enter 1st favorite movie:")
b = input("enter 2nd favorite movie:")
c = input("enter 3rd favorite movie:")

movies = [a,b,c]
print(movies)


#Question: wap to check if a list contains a palindrome of elements . (Hint = use copy() method)

list = [1,2,3,2,1]
list2 = list.copy()
list2.reverse()

if(list2==list):
    print("list is palindrome")
else:
    print("list is not palindrome")
