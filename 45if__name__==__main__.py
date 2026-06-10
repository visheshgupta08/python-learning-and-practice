# PART 1: MAIN CODE & TESTING (Yeh asli file ka kaam karegi)


def welcome():
    print("Welcome to CodeWithHarry Python Course! ")

def add_numbers(a, b):
    return a + b

# -------------------------------------------------------------------------
# THE SECURITY GUARD: if __name__ == "__main__"
# -------------------------------------------------------------------------
# Iske andar hum wahi code likhte hain jo humein sirf is file ko DIRECT chala kar 
# test karna ho. Hum nahi chahte ki koi is file ko import kare toh yeh automatic chal jaye.

if __name__ == "__main__":
    print("--- TESTING MODE ACTIVE (Sirf is file ko direct chalane par dikhega) ---")
    
    welcome()
    result = add_numbers(10, 20)
    print(f"Testing Add Function: 10 + 20 = {result}")
    
    # Is file ko direct run karne par computer kahega ki __name__ ki value '__main__' hai
    print(f"Khufiya variable __name__ ki value hai: {__name__}")


# =========================================================================
# PART 2: IMPORT CONCEPT (Sirf samajhne ke liye comment mein)
# =========================================================================

# Agar aap is file ka naam 'harry.py' rakhte hain aur kisi doosri file mein 
# jaakar 'import harry' likhte hain...

"""
import harry

# Jaise hi hum 'import harry' karenge, upar PART 1 ke guard wale 
# block ke andar ka TESTING wala code AUTOMATIC NAHI CHALEGA! Kyunki guard ne use rok diya.
# Kyunki ab is file ke liye __name__ ki value '__main__' nahi rahi, balki 'harry' ban gayi.

# Ab hum apni marzi se harry ke functions ko jab chahein call kar sakte hain:
harry.welcome()

res = harry.add_numbers(5, 5)
print("Main file mein addition ka result:", res)
"""
