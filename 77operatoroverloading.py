class Vector:
    def __init__(self, i, j, k):
        # Constructor: Jo bhi values bahar se aayengi unhe i, j, k mein save kar liya
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        # Magic Method: Jab bhi object ko print karenge, ye automatic text format return karega
        return f"{self.i}i + {self.j}j + {self.k}k"

    # =========================================================================
    # OPERATOR OVERLOADING (`+` sign ko naya jadu sikhana)
    # =========================================================================
    def __add__(self, x):
        # self = pehla object (v1) | x = doosra object (v2) जो '+' ke right side hai.
        # Rule: v1 ke 'i' ko v2 ke 'i' se jodo, aur waise hi j aur k ko bhi jodo!
        # End mein ek naya Vector object banakar return kar diya.
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


v1 = Vector(3, 5, 6)
print(v1)  # (Yahan back-end mein __str__ chala)

v2 = Vector(1, 2, 9)
print(v2)  

# ASLI JADU: Do custom objects ke beech direct '+' lagaya!
# Jaise hi computer ne '+' dekha, usne chupchaap upar waale '__add__' function ko chala diya.
print(v1 + v2)  

# Check kar rahe hain ki '+' hone ke baad jo naya jor aaya, uska type kya hai
print(type(v1 + v2))  
