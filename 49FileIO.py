# =========================================================================
# PART 1: READING A FILE (File se data padhna)
# =========================================================================
# Humne 'myfile.txt' ko sirf padhne ke liye 'r' (Read) mode mein khola
# (Yaad rahe: Yeh file pehle se folder mein honi chahiye, nahi toh error aayega)

f = open('myfile.txt', 'r') 
text = f.read()             # f.read() ne poora data nikal kar 'text' mein daal diya
print(text)                 # Data ko screen par print kiya
f.close()                   # Kaam khatam, toh file ko manually close kiya


# =========================================================================
# PART 2: WRITING A FILE (Naya data likhna - OVERWRITE KHATRA)
# =========================================================================
# 'w' mode file mein naya data likhta hai. 
# AGAR FILE PEHLE SE HAI, TOH YEH USKA PURANA SAARA DATA MITA (DELETE) DEGA!
f = open('myfile.txt', 'w') 
f.write('Hello, world!')    # Ab file mein purana jo bhi tha sab gayab, sirf 'Hello, world!' bacha
f.close() 


# =========================================================================
# PART 3: APPENDING A FILE (Purane data ke niche naya data jodna - SAFE)
# =========================================================================
# 'a' (Append) mode sabse safe hai. Yeh purane data ko chhedta nahi, uske thik aage se likhta hai
f = open('myfile.txt', 'a') 
f.write('Hello, world!')    # Ab file mein ho jayega: 'Hello, world!Hello, world!'
f.close() 


# =========================================================================
# PART 4: THE SMART WAY - WITH STATEMENT (Automatic Close)
# =========================================================================
# Yeh sabse professional tareeqa hai. Isme alag se 'f.close()' likhne ki jhanjhat nahi hoti.
# Jaise hi is block se code bahaar nikalta hai, Python file ko khud hi close kar deta hai.

with open('myfile.txt', 'a') as f: 
    f.write("Hey I am inside with") # Yeh text bhi file ke aakhri mein bina purana delete kiye jud jayega
