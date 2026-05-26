# Simple variables jisme names (strings) save hain
name = "harry" 
friend = "rohan"
anotherfriend = "lovish"

# Triple quotes (''' या """) tab use karte hain jab message multiple lines mein ho
apple = '''he said,
hi harry 
hey i am good 
"i want to eat an apple '''

# String Concatenation: + sign se strings ko jodna
print("hello,"+name )

# Indexing: String ke kisi bhi character ko uske number (0 se shuru) se nikalna
print(name[0]) # 'h' aayega
print(name[1])
print(name[2])
print(name[3])
print(name[4]) # 'y' aayega
# print(name[5]) # Yeh error dega kyunki 'harry' mein sirf 0 se 4 tak index hain

print("lets use a for loop\n")

# For Loop: Yeh apple string ke ek-ek character (chahe wo space ho ya new line) par jayega
# Aur use 'character' variable mein daal kar print karega
for character in apple:
    print(character)

#Yaad Rakhne Wali Baat: #Indexing 0 se shuru hoti hai: Pehla letter 0, doosra 1, aur aise hi aage
#For Loop on String: String par loop chalane ka matlab hai uske har ek akshar (letter) se milna.