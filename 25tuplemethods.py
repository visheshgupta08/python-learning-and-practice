countries = ("spain","italy","india","england","germany")

# Hack: Tuple ko pehle list mein badla taaki isme badlav (change) kiya ja sake
temp = list(countries)

temp.append("russia")          # List banne ke baad append() se naya desh joda
        

# pop(3) se index 3 wala element (england) list se delete ho jayega
temp.pop(3)

# Index 2 par jo "india" tha use badal kar "finland" kar diya
temp[2]="finland"

# Badlav karne ke baad wapas list ko tuple mein convert kar diya
countries= tuple(temp)
print(countries)


countries=("pakistan","afganistan","bangladesh","shrilanka")
countries2=("vietnam","india","china")
# Do alag-alag tuples ko '+' operator se jod kar ek naya bada tuple bana diya
southeastasia = countries+countries2
print(southeastasia)

tuple1=(0,1,2,3,2,3,1,3,2,3)
# count() ginta hai ki element '3' is tuple mein total kitni baar aaya hai
res= tuple1.count(3)
print("count of 3 in tuple1 is:", res)

# res= tuple1.index(3) # Pehli baar 3 kis index par hai wo batata (index 3 deta)
# res= tuple1.index(311) # Error dega kyunki 311 tuple mein nahi hai

res = len(tuple1) # Tuple ki total lambai (elements ka count) batayega

# index(element, start, end): Index 4 se lekar index 8 ke beech mein 
# dhoondega ki '3' sabse pehle kis position par aaya hai
res= tuple1.index(3,4,8)
print("index of 3 in tuple1 is:", res)