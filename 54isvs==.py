# =========================================================================
# CONCEPT: 
# '==' (Equality) check karta hai ki kya dono variables ki VALUE same hai.
# 'is' (Identity) check karta hai ki kya dono variables ka MEMORY LOCATION same hai.
# =========================================================================

# -------------------------------------------------------------------------
# CASE 1: LISTS KE SAATH (Mutable Objects)
# -------------------------------------------------------------------------


a = [1, 2, 3]
b = [1, 2, 3]

# '==' True dega kyunki dono lists ke andar ka data (value) ekdum same hai
print(a == b)  # Output: True

# 'is' False dega kyunki Python memory mein do alag-alag lists (bhi) banata hai.
# Dono ka memory address (id) alag hai.
print(a is b)  # Output: False

# id() function se memory address check kar sakte hain:
print(f"a ki memory id: {id(a)}")
print(f"b ki memory id: {id(b)}")


# -------------------------------------------------------------------------
# CASE 2: STRINGS & INTEGERS KE SAATH (Immutable Objects - Python Smartness)
# -------------------------------------------------------------------------


x = "Harry"
y = "Harry"

# Value toh same hai hi, toh '==' True dega
print(x == y)  # Output: True

# Yahan 'is' bhi True dega! 
# Kyunki strings immutable (na badalne wali) hoti hain, Python memory bachane ke liye 
# naya dabba nahi banata, dono variables ko ek hi memory location par point karwa deta hai.
print(x is y)  # Output: True


# -------------------------------------------------------------------------
# CASE 3: NONE KE SAATH (Hamesha 'is' use hota hai)
# -------------------------------------------------------------------------


c = None

# Jab bhi code mein 'None' check karna ho, toh professional coders hamesha 'is' use karte hain:
if c is None:
    print("c ki value kuch nahi (None) hai")


'''Revision ke liye ek line ka rule:
== = Kya dono ke kapde/shakal (data) ek jaise hain?
is = Kya dono ek hi insaan (memory space) hain?'''