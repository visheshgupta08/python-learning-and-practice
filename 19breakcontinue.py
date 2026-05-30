# --- BREAK STATEMENT ---
# Range(12) matlab loop 0 se 11 tak chalne wala tha
for i in range (12):
    # Break ka matlab hai: "Bas ab bohot ho gaya, loop se bahar nikal jao"
    if(i==10):
        break # Jaise hi i=10 hoga, loop wahin khatam ho jayega
    print("5 X", i+1, "=", 5* (i+1))

print("loop ko chodkar nikal gya")


# --- CONTINUE STATEMENT ---
for i in range (12):
    # Continue ka matlab hai: "Is wale round ko chodo aur agle round par jao"
    if(i==10):
        print("skip the iteration")
        continue # i=10 ke liye neeche wala print nahi chalega, sidha i=11 par jump karega
    print("5 X", i, "=", 5* i) 


# --- BREAK IN WHILE LOOP (DO-WHILE STYLE) ---
i = 0 
# While True ka matlab hai 'Infinite Loop' jo kabhi khatam nahi hoga
while True:
    print(i)
    i=i+1
    # Lekin humne andar ek condition laga di ki jaise hi i, 100 ka multiple hoga...
    if(i%100==0):
        break # ...waise hi break karke loop ko rok do