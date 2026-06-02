#exercise = Kaun Banega Crorepati
questions = [ 
    ["what is the capital of india?","A.UP","B.Delhi","C.Chennai","D.gujrat","B",1000], 
    ["who is called the god of cricket?","A.MS Dhoni","B.Virat Kohli","C.sachin Tendulkar","D.Rohit Sharma", "C",5000], 
    ["Who is the first pm of india?","A.jahawar lal nehru","B.Narendra Modi","C. Rajendra Prasad","D.Indra gandhi","A",10000]
]

print("==============================================")
print("     WELCOME TO KAUN BANEGA CROREPATI!        ")
print("==============================================")
print("Rules: Har sahi jawab par paise milenge.")
print("Agar jawab nahi pata, toh 'Q' daba kar QUIT karein.\n")
print("so lets start the game")
print("pehla swal aapki computer screen pr")

money=0

for q in questions:
    print(q[0])     
    print(q[1])   
    print(q[2])      
    print(q[3])      
    print(q[4])      
    
    e= input("Apna jawab dalein (A/B/C/D) ya QUIT karne ke liye 'Q' dalein: ")
    
    if(e.upper() == "Q"):
        print("\nAapne game beech mein hi chhodne ka faisla kiya.")
        break   
        
    if(e.upper() == q[5]):
        print("sahi javab") 
        money = money + q[6]  
        print(f"aapne jite h rs {q[6]}") 
        print("congratulations")
    else:
        print("galat javab ,game khatam") 
        break   

print(f"ghar le jane wali rashi: Rs.{money}")
print("Thank you for playing KBC!")


# KBC Game ki Nested List: Isme sawal, options, sahi jawab (index 5) aur prize (index 6) hain
# Shuruat mein total prize money 0 set ki hai
# Loop ek-ek karke questions list se poori sub-list 'q' mein nikalega
# User se input lekar use 'e' variable mein save kiya
# e.upper() se agar user small 'q' dale toh bhi wo capital 'Q' ban kar match ho jaye
# f-string se actual prize money show ho rahi hai