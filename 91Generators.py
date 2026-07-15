def my_generator():
    # Loop chalaya 0 se 4 tak ke liye
    for i in range(5):
        # ASLI JADU: 'return' ki jagah 'yield' ka use kiya!
        # return function ko turant khatam kar deta hai, 
        # par yield value dekar function ko wahin PAUSE (rok) deta hai!
        yield i

# Function ko call karne par ye direct run nahi hota, 
# balki ek Generator Object bana kar deta hai.
gen = my_generator()

# -------------------------------------------------------------------------
# TARIKA A: NEXT() KA USE KARNA (Comments se samajhein)
# -------------------------------------------------------------------------
# Agar mai in comments ko kholenge toh:
# print(next(gen))  # Output: 0 (Pehli value mili aur function ruk gaya)
# print(next(gen))  # Output: 1 (Agli value mili)
# print(next(gen))  # Output: 2 (Teesri value mili)

# IMPORTANT POINT: Agar aapne upar 3 baar next() chala diya, 
# toh neeche waala loop bachi hui values (3 aur 4) se hi shuru hoga!


# -------------------------------------------------------------------------
# TARIKA B: FOR LOOP KA USE KARNA (Bina crash hue saari values nikalna)
# -------------------------------------------------------------------------
# Loop automatic background mein 'next()' ko tab tak chalta hai 
# jab tak generator ki saari values khatam nahi ho jaatin.
for j in gen:
    print(j)



''' Generators ka Asli fayda kya hai? (Interview / LPU Viva Question)
Teacher hamesha puchenge ki "Jab hamare paas normal list ya range() loop tha,
 toh Generators ki kya zaroorat padi?
 
"Jawaab (Memory ki bachat): Maan lijiye aapko 1 Crore numbers par loop chalana hai. 
Agar aap list banayenge, toh computer ki poori RAM ek jhatke mein full ho jayega aur 
laptop hang ho jayega. Lekin Generator ek sath saare 1 Crore numbers memory mein save 
nahi karta! Yeh "On-the-fly" (Jab mangoge tabhi naya number banayega)kaam karta hai. 
Is wajah se memory 0 MB use hoti hai aur program super-fast chalta hai!'''