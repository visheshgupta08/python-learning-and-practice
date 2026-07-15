from functools import lru_cache
import time

# JADU 1: Function ke upar lru_cache ka jacket (decorator) pehna diya.
# maxsize=None ka matlab hai: "Bhai computer, jitne bhi inputs aayein, sabka answer dimaag mein save rakhna."
@lru_cache(maxsize=None)
def fx(n):
    # Yeh line dikhane ke liye hai ki function bohot bada aur bhaari kaam kar raha hai (5 second lagenge)
    time.sleep(5)
    return n * 5


# =========================================================================
# ROUND 1: NAYE INPUTS (Pehli baar chal rahe hain - Time lagega)
# =========================================================================

# Pehli baar fx(20) chala: 5 second ka wait karega, answer aayega 100
print(fx(20))
print("done for 20")

# Pehli baar fx(2) chala: Fir se 5 second ka wait karega, answer aayega 10
print(fx(2))
print("done for 2")

# Pehli baar fx(6) chala: Fir se 5 second ka wait karega, answer aayega 30
print(fx(6))
print("done for 6")

# =========================================================================
# ROUND 2: SAM MEIN JADU (Purane inputs dobara aaye - Instant Output!)
# =========================================================================

# fx(20) dobara aaya: Computer dimaag se sochega, "Arey, iska answer toh 100 tha!" 
# Yeh 'time.sleep(5)' ko chalaega hi nahi, 0 seconds mein 100 print kar dega!
print(fx(20))
print("done for 20")

# fx(2) dobara aaya: Instant 10 print ho jayega bina kisi rukawat ke!
print(fx(2))
print("done for 2")

# fx(6) dobara aaya: Instant 30 print ho jayega!
print(fx(6))
print("done for 6")

# fx(61) ek naya input hai: Iska answer cache mein nahi hai, 
# isliye yeh fir se 5 second ka time lega aur answer 305 dega.
print(fx(61))
print("done for 61")




'''LRU Cache Ka Full Form Kya Hai? (Interview / LPU Viva Question)
Teacher hamesha puxhenge ki is LRU ka kya matlab hai?
Jawaab: LRU ka matlab hota hai Least Recently Used. Yeh ek aisi algorithm hai jo 
dimaag ke us hisse ki tarah kaam karti hai jo sabse purani aur fuzool baaton ko bhool 
jata hai aur jo baatein baar-baar kaam aa rahi hain, unhe sabse upar yaad rakhta hai.'''