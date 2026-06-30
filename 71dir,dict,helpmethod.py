# =========================================================================
# PART 1: DIR() AUR DUNDER METHODS CHK KARNA
# =========================================================================
x = (1, 2, 3) # 'x' ek tuple hai

# DIR() KA JADU: Yeh is tuple ke andar chupe hue saare methods aur 
# functions ki ek bohot badi list print kar dega jo Python ne ise diye hain.
print(dir(x)) 

# __add__ DUNDER METHOD: Jab aap do tuples ko '+' karte hain, toh back-end 
# mein yahi '__add__' function chalta hai. Is line se screen par is function ka 
# memory address ya detail print ho jayegi (Kahega: 'builtin_function_or_method').
print(x.__add__)


# =========================================================================
# PART 2: __DICT__ KA JADU (Kundali nikalna)
# =========================================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)

# __DICT__ KA JADU: Yeh kisi bhi object ke saare variables aur unki values ko 
# ek DICTIONARY format {'key': 'value'} mein convert karke screen par dikha deta hai.
print(p.__dict__) 
# Output aayega: {'name': 'John', 'age': 30, 'version': 1}


# =========================================================================
# PART 3: HELP() FUNCTION (Official Documentation)
# =========================================================================
# HELP() KA JADU: Yeh Python ka official help desk hai. Ise chalane par 
# screen par 'Person' class ki poori manual book (documentation) khul jayegi—
# jaise isme kaun sa constructor hai, kaun se methods hain, sab kuch detail mein!
print(help(Person))
