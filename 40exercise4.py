#Write a python program to transalate a message into secret code language . use the rules below to transalte normal english into secret code language . 

#Coding 
#if the words contains atleast three characters , remove the first letter and append it at the end 
# now append three random characters at the starting and the end
# else:
#    simply reverse the string


#Decoding
#if the words contains less than 3 characters , revrese it 
# else :
#    remove 3 randome characters from start and the end , now remove the last letter and append it to the beginning .





st = input("Enter message: ")
words = st.split(" ")


coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding == "1") else False

# Naye words ko store karne ke liye ek khali list
new_words = []

# Loop chalaya taaki har ek word par alag-alag kaam ho sake
for word in words:
    
    
    # PART 1: CODING 
    
    if(coding):
      
        if(len(word) >= 3):
            r1 = "abc" 
            r2 = "xyz" 
            
            st_new = r1 + word[1:] + word[0] + r2
            new_words.append(st_new)
        else:
            
            new_words.append(word[::-1])    #Reverse 
            
    
    # PART 2: DECODING 
    
    else:
        
        if(len(word) < 3):
           
            new_words.append(word[::-1])
        else:
            strip_word = word[3:-3]
            
            
            # strip_word[-1] matlab last letter, aur strip_word[:-1] matlab baaki ka word
            st_new = strip_word[-1] + strip_word[:-1]
            new_words.append(st_new)

# Saare badle hue words ko space dekar firse ek line mein jod diya
print("Result:", " ".join(new_words))


#random module se :
# # Step 1: Random characters generate karne ke liye modules import kiye
# import random
# import string

# # User se poora sentence input liya
# st = input("Enter message: ")
# words = st.split(" ")

# # User se pucho ki use Coding karni hai ya Decoding
# coding = input("1 for Coding or 0 for Decoding: ")
# coding = True if (coding == "1") else False

# # Naye words ko store karne ke liye ek khali list
# new_words = []

# # Loop chalaya taaki har ek word par alag-alag kaam ho sake
# for word in words:
    
#     # ------------------------------------------
#     # PART 1: CODING (Secret Code Banana)
#     # ------------------------------------------
#     if(coding):
#         if(len(word) >= 3):
#             # FIXED LOGIC: Ab har baar alag 'a' se 'z' ke beech ke 3 random letters milenge
#             # string.ascii_lowercase ka matlab hai 'abcdefghijklmnopqrstuvwxyz'
#             # random.choices() unme se 3 random letters nikalega aur ''.join() unhe jod dega
#             r1 = "".join(random.choices(string.ascii_lowercase, k=3))
#             r2 = "".join(random.choices(string.ascii_lowercase, k=3))
            
#             # Aapka wahi perfect logic (Pehla letter peeche + random letters)
#             st_new = r1 + word[1:] + word[0] + r2
#             new_words.append(st_new)
#         else:
#             # 3 se chhota hai toh reverse
#             new_words.append(word[::-1])
            
#     # ------------------------------------------
#     # PART 2: DECODING (Asli Message Wapas Lana)
#     # ------------------------------------------
#     else:
#         if(len(word) < 3):
#             # 3 se chhota hai toh firse reverse
#             new_words.append(word[::-1])
#         else:
#             # FIXED REASONING: Kyunki coding ke waqt 3 letters jode the, toh hum bina dare
#             # hamesha shuruat aur aakhri ke 3-3 letters cut kar denge (Slicing se)
#             strip_word = word[3:-3]
            
#             # Last letter ko uthakar sabse aage laga diya
#             st_new = strip_word[-1] + strip_word[:-1]
#             new_words.append(st_new)

# # Saare badle hue words ko space dekar firse ek line mein jod diya
# print("Result:", " ".join(new_words))

