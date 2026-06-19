class Math: 
    def __init__(self, num): 
        self.num = num 
        
    def addtonum(self, n): 
        # Yeh ek normal method hai, ise self (object ka data) chahiye
        self.num = self.num + n 
        
    # STATIC METHOD (Bina self waala function)
    # Iske upar @staticmethod likha hai. Iska matlab hai is function ko 
    # chalne ke liye class ke kisi variable (self) ki koi zaroorat nahi hai.
    # Yeh ek ekdum independent utility function hai!
    @staticmethod 
    def add(a, b): 
        return a + b 

a = Math(5) 
print(a.num)       # Output: 5

a.addtonum(6) 
print(a.num)       # Output: 11 (5 + 6)

# RIGHT WAY: Static method ko direct Class ke naam se call karte hain
print(Math.add(7, 2))  # Output: 9

# print(add(7,2)) 
# ERROR: Python bolega "Bhai 'add' kya hai? Mujhe nahi pata!" Kyunki 'Math.' nahi lagaya.


''' Short Summary (Yaad rakhne ke liye):Static Method ek aisa mehmaan hai jo class ke ghar
 mein rehta zaroor hai, par use class ke baki members (self) se koi matlab nahi hota.
   Ise aap bina koi object banaye, direct ClassName.method_name() karke chala sakte hain.'''