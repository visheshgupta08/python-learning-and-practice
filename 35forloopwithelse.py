# ==========================================
# CONCEPT: Loop ke saath else tabhi chalega 
# jab loop POORA KHATAM hoga bina kisi break ke!
# ==========================================

# Case 1: Loop poora 0 se 4 tak chala, koi break nahi mila
for i in range(5):
    print(i)
else:
    # Loop poora khatam hua, isliye yeh line PRINT HOGI
    print("sorry no i") 

# ------------------------------------------

# Case 2: Loop khali list par hai, yaani 1 baar bhi nahi chala
for i in []:
    print(i)
else:
    # Loop khatam mana jayega (chahe chala hi na ho), isliye yeh line BHI PRINT HOGI
    print("sorry no i") 

# ------------------------------------------

# Case 3: Loop ke andar BREAK lag gaya
for i in range(6):
    print(i)
    if(i==4):
        break # Loop beech mein hi toot gaya!
else:
    # Loop poora nahi chal paya break ki wajah se, isliye yeh line PRINT NAHI HOGI!
    print("sorry no i") 

# ------------------------------------------

# Case 4: While loop ke saath else
i = 0
while i<7:
    print(i)
    i=i+1
    # if i==4:
    #  break  # Abhi yeh comment hai, toh loop poora chalega
else:
    # While condition False (i=7) hone par loop normal khatam hua, toh yeh PRINT HOGI
    print("Sorry no i ") 

# ------------------------------------------

# Case 5: String Formatting aur Loop
for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    # Loop normal khatam hua, toh else block chalega
    print("else block in loop ")

# Yeh toh loop ke bahar hai, toh yeh hamesha hi chalega
print("Out of loop")


#Ek Line ka Golden Rule yaad rakhna:
#"Agar loop BREAK hua, toh else NAHI chalega. Agar loop BINAY BREAK ke khatam hua, toh else CHALEGA."
