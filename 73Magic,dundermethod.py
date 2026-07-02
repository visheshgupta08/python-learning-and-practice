class Employee:
    def __init__(self, name):
        self.name = name

    # =========================================================================
    # 1. __LEN__ DUNDER METHOD
    # =========================================================================
    # Jadu: Jab aap bahar 'len(e)' likhenge, toh yeh waala function automatic chalega.
    # Aapne bilkul loop lagakar length nikali hai, par iska simple tarika 'return len(self.name)' bhi hota hai!
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i 
    
    # =========================================================================
    # 2. __STR__ DUNDER METHOD
    # =========================================================================
    # Jadu: Jab aap kisi object ko 'print(e)' ya 'str(e)' karte hain, toh Python 
    # use ek saaf-suthra aur sundar text format (user-friendly string) mein dikhane ke liye ise chalata hai.
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    # =========================================================================
    # 3. __REPR__ DUNDER METHOD
    # =========================================================================
    # Jadu: Yeh developers ke liye hota hai code debug karne ke liye. Agar '__str__' 
    # nahi likha hota, toh 'print(e)' karne par yahi '__repr__' chalta hai jo batata hai ki object bana kaise hai.
    def __repr__(self):
        return f"Employee('{self.name}') "

    # =========================================================================
    # 4. __CALL__ DUNDER METHOD
    # =========================================================================
    # Sabse Bada Jadu: Kisi object ko direct FUNCTION ki tarah chalane ki azaadi deta hai!
    # Yaani aap direct 'e()' likh sakte hain aur yeh function background mein trigger ho jayega.
    def __call__(self):
        print("Hey I am good")




e = Employee("Harry")

# __str__ chala rahe hain 
print(str(e)) 
print(repr(e)) 

# __call__ chala rahe hain -> Object ke aage direct brackets () lagaye!
e() 


'''__str__ aur __repr__ mein kya farq hai? (Interview Question)
Harry sir jab yeh video khatam karenge, toh yeh sawaal aapke samne zaroori aayega:
__str__ (String): Yeh End-User (Aam janta) ke liye hota hai taaki unhe screen par ek aasan aur pyara sa message dikhe.
__repr__ (Representation): Yeh Developers ke liye hota hai taaki unhe pata chal sake ki is object ko dubara recreate 
kaise karna hai (Jaise Employee('Harry')).'''


''' Short Summary (Yaad rakhne ke liye):
Dunder (Double Underscore) methods ko Magic Methods isliye kehte hain kyunki inko alag se dot . lagakar call nahi karna
 padta. Yeh Python ke built-in behaviors (jaise len(), print(), ya ()) par automatic back-end mein trigger ho jaate hain.'''