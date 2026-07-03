class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        # Base Area: Kisi bhi 4-side shape ka length * width
        return self.x * self.y
    

# =========================================================================
# METHOD OVERRIDING (Purane function ko naya jadu dena)
# =========================================================================
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # JADU 1: Shape class ke constructor ko aawaz lagayi.
        # x ban gaya radius, y ban gaya radius!
        super().__init__(radius, radius)

    # OVERRIDING: Shape class ke paas apna 'area' function pehle se tha.
    # Par Circle ne kaha: "Bhai mera area nikalne ka tarika alag hai (Pi * r^2)."
    # Isliye Circle ne Papa class ke function ko daba diya (Override kar diya)!
    def area(self):
        # JADU 2: super().area() ne chalaya (radius * radius)
        # Aur bahar usme 3.14 (Pi) se guna (multiply) kar diya!
        return 3.14 * super().area()
    

# Agar niche diye comments ko kholenge toh:
# rec = Shape(3,5)
# print(rec.area()) # Output aayega: 15 (3 * 5)

c = Circle(5)

# Jadu Check: Jab hum 'c.area()' chalayenge, toh Shape wala area nahi chalega, 
# balki Circle wala upgraded 'area' chalega!
print(c.area()) 



'''Short Summary:
Method Overriding ka matlab hota hai: "Child class ke andar ek aisa function banana jiska
 naam aur arguments ekdum Parent class ke function jaise hon." Iska use tab hota hai jab 
 Child class ko Papa class wale function ka naam toh chahiye, par uske andar ka kaam
   (logic) badalna ho.'''