# code ko chalane se pehle check karlein ki folder mein 'myfile.txt' hai aur usme kuch text likha hai
# Maan lijiye 'myfile.txt' mein likha hai: "CodeWithHarry is awesome"

with open('myfile.txt', 'r') as f: 
    print(type(f)) # Yeh batayega ki 'f' kis class ka object hai (<class '_io.TextIOWrapper'>)
    
    # f.seek(10) ka matlab hai cursor ko seedhe kooda kar 10th character (byte) par bhej do
    f.seek(10) 
    
    # f.tell() se pucha ki suee (cursor) kahan khada hai? Yeh 10 return karega
    print(f"Cursor abhi is position par hai: {f.tell()}") 
    
    # f.read(5) ka matlab hai ki jahan cursor khada hai (10th byte), wahan se sirf AGLE 5 CHARACTERS padho
    data = f.read(5) 
    print("Agle 5 characters hain:", data) 


# =========================================================================
# TRUNCATE METHOD (File ka size chhota karna)
# =========================================================================


with open('myfile2.txt', 'w') as f: 
    f.write('Hello World!') # File mein 'Hello World!' (12 bytes) likha gaya
    
    # f.truncate(5) ka matlab hai: "Bhai file ke sirf PEHLE 5 CHARACTERS rakho, baaki sab kaat kar phek do!"
    f.truncate(5) 

with open('myfile2.txt', 'r') as f: 
    # Ab screen par sirf 'Hello' dikhega, kyunki ' World!' truncate (kat) ho chuka hai
    print("Truncate ke baad file mein bacha:", f.read())
