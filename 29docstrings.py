def square(n):
    '''Takes in a number n, returns the square of n'''
    # Docstring hamesha function ki body ke pehle line mein triple quotes (''' ya """) ke andar aati hai
    # Yeh batati hai ki yeh function kya kaam karta hai
    print(n**2)

# Function ko call kiya, output 25 aayega
square(5)

# __doc__ attribute ka use karke hum kisi bhi function ki docstring ko print kar sakte hain
# Agar aap iski jagah normal comment (#) likhte, toh wo yahan print nahi hota
print(square.__doc__)

# 'import this' ek Easter Egg hai Python mein. 
# Ise run karne par Tim Peters ka likha hua "The Zen of Python" print hota hai, 
# jo batata hai ki acha Python code kaise likhein (jaise: Beautiful is better than ugly).
import this

# =====================================================================
# 📚 PEP 8 NOTES: Python Code Likhne Ki Official Rulebook/Guidelines
# =====================================================================
# 1. Indentation: Hamesha 4 spaces ka use karein (Tab ki jagah).
# 2. Line Length: Ek line max 79 characters tak hi lambi honi chahiye.
# 3. Naming Style: Functions aur variables ke naam small letters mein 
#    undescore (_) ke sath hone chahiye (e.g., user_answer).
# 4. Clean Code: Code ko saaf aur readable rakhna hi PEP 8 ka maksad hai.
# =====================================================================