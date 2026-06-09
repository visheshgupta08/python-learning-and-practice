Marks = [12, 43, 45, 62, 54, 65, 97] 

# --- PURANA TAREEQA ---
# index = 0 
# for mark in Marks: 
#     print(mark) 
#     if(index==3): 
#         print("Harry, awesome!") 
#     index += 1 # Isme baar-baar index ko badhana padta tha manually


# ==========================================================
# CASE 1: DEFAULT ENUMERATE (Index 0 se shuru hota hai)
# ==========================================================
print("--- Case 1: Start from Index 0 ---")

# enumerate(Marks) automatic pehle index dega (index mein) aur fir value (mark mein)
for index, mark in enumerate(Marks): 
    print(index, mark) #yaha sirf bracket mai agar mark likhenge toh bss itna hoga ki output main index nahi aayegi likhi hui
    # Jab index ki value 3 hogi (yaani list ka 4th element '62')
    if(index==3): 
        print("Harry, awesome!") 


# ==========================================================
# CASE 2: CUSTOM START ENUMERATE (Index 1 se shuru hota hai)
# ==========================================================
print("\n--- Case 2: Start from Index 1 ---")

# start=1 likhne se ginti 0 ke bajaye 1 se shuru hogi (lekin actual data wahi rahega)
for index, mark in enumerate(Marks, start=1): 
    print(index, mark) 
    # Ab ginti 1 se shuru hui hai, toh jab index 3 hoga (yaani list ka 3rd element '45')
    if(index==3): 
        print("Harry, awesome!")
