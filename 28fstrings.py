# Purana tarika (String Formatting): Indexing ka use karke placeholders {0}, {1} lagaye hain
letter = "Hey my name is {1} and I am from {0} "
Country = "India"
name = "Vishesh"

# print(letter.format(name,Country))

# format() ke andar pehla item Country (index 0) hai aur doosra name (index 1) hai
print(letter.format(Country,name))

# Naya aur modern tarika (f-string): String ke aage 'f' lagao aur variables ko seedha {} mein likho
print(f"Hey my name is {name} and I am from {Country} ")

# Agar aapko terminal par sach mein {name} hi print karwana ho (variable ki value nahi), 
# toh hum double curly brackets {{}} ka use karte hain
print(f"we use f-strings like this: Hey my name is {{name}} and I am from {{Country}} ")

price = 49.09999
# Float formatting: :.2f ka matlab hai point ke baad sirf 2 numbers tak round-off karo (i.e. 49.10)
txt= f"for only{price:.2f}dollars! "
print(txt)

# Yahan .format() ki zaroorat nahi hai kyunki txt pehle hi f-string se ban chuka hai
# print(txt.format()) 

# f-string ke andar aap maths calculation bhi kar sakte ho. 
# 2*30 ka result 60 aayega aur type hamesha 'str' (string) hi rahega
print(type(f"{2*30}"))