# =========================================================================
# INTRODUCTION TO OBJECT ORIENTED PROGRAMMING (OOPs)
# =========================================================================

# OOPs koi naya code nahi hai, yeh code likhne ka ek smart tarika hai.
# 1. CLASS  = Khali Form (Sirf ek naksha ya blueprint hota hai).
# 2. OBJECT = Bhara hua asli form (Asli cheez jiske paas apna data hota hai).


# =========================================================================
# STEP 1: CLASS BANANA (Khali Admission Form)
# =========================================================================
# 'class' keyword se hum apna ek naya data type ya blueprint banate hain
class AdmissionForm:
    # 'pass' ka matlab hai abhi is form ke andar koi fixed function nahi hai, 
    # yeh bas ek khali dabba/blueprint hai.
    pass 


# =========================================================================
# STEP 2: OBJECTS BANANA (Bacchon ka asli bhara hua form)
# =========================================================================
if __name__ == "__main__":
   

    # 1. Karan ke liye ek naya object (khali form) banaya
    karan_ka_form = AdmissionForm()
    
    # Ab Karan ne apne form ke andar apna asli data bhara (Properties/Attributes)
    karan_ka_form.name = "Karan"
    karan_ka_form.age = 19
    karan_ka_form.course = "Python Masterclass"

    # 2. Harry sir ke liye ek alag naya object (khali form) banaya
    harry_sir_ka_form = AdmissionForm()
    
    # Harry sir ne apne form mein alag data bhara
    harry_sir_ka_form.name = "Harry Sir"
    harry_sir_ka_form.age = 28
    harry_sir_ka_form.course = "Advanced Programming"


# =========================================================================
# STEP 3: DATA USE KARNA
# =========================================================================
    # Ab hum dono bacchon ka data alag-alag access kar sakte hain:
    print(f"Student 1: {karan_ka_form.name} jo {karan_ka_form.age} saal ka hai, woh {karan_ka_form.course} seekh raha hai.")
    print(f"Student 2: {harry_sir_ka_form.name} jo {harry_sir_ka_form.age} saal ke hain, woh {harry_sir_ka_form.course} sikha rahe hain.")

    # Dono objects ka class same hai (AdmissionForm), par dono ka data ekdum ALAG hai!
