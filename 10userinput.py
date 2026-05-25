# input() hamesha user se text (string) leta hai
a = input("enter your first name: ")
print("my name is ", a )

# Yaad rakhiye: x aur y yahan strings ki tarah save honge
x = input("enter first number: ")
y = input("enter second number:")

# Yahan 'String Concatenation' hoga (agar x=5 aur y=2 hai, toh answer 52 aayega)
print(x+y) 

# Yahan 'Typecasting' ho rahi hai: String ko Integer mein badal kar add kar rahe hain
# Isse sahi maths wala answer aayega (agar x=5 aur y=2 hai, toh answer 7 aayega)
print(int(x)+int(y))

#Agar hum chahe toh input lete waqt hi usse int mein badal sakte ho aise:
#x = int(input("Enter number: ")) Isse humko baar-baar int(x) nahi likhna padega.


# homework
x= input("enter first number: ")
y= input("enter second number:")
print(int(x)-int(y))
print(int(x)*int(y))
print(int(x)/int(y))
#isme agr ye tino -,*,/ bina integar opreation ke lagaye toh usme error aata hai jbki plus main nahi aata 