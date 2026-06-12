# =========================================================================
# PART 1: READLINE METHOD (Ek-ek line karke padhna aur split karna)
# =========================================================================

f = open('myfile.txt', 'r') 
i = 0 

# Infinite loop chalaya taaki jab tak file mein lines hain, tab tak padhte rahein
while True: 
    i = i+1 
    line = f.readline() # File se ek single line uthayi
    
    # BREAK CONDITION: Agar file khatam ho gayi aur koi line nahi bachi, toh loop se bahar nikal jao
    if not line: 
        break 
        
    # LOGIC: line.split(",") se string alag-alag ho jayegi. Jaise "50,60,70" ban jayega ['50', '60', '70']
    # int() ka use karke unhe numbers mein badla taaki calculation (jaise m1*2) kar sakein
    m1 = int(line.split(",")[0]) # Pehla number (Maths)
    m2 = int(line.split(",")[1]) # Dusra number (SST)
    m3 = int(line.split(",")[2]) # Teesra number (Art)
    
    # Har student ke marks print kiye 2 se multiply karke
    print(f"Marks of student {i} in Maths is {m1*2} ") 
    print(f"Marks of student {i} in SST is {m2*2} ") 
    print(f"Marks of student {i} in art is {m3*2} ") 
    print("Asli line thi:", line) 

f.close() # File close karna achhi aadat hai


# =========================================================================
# PART 2: WRITELINES METHOD (Ek saath bohot saari lines likhna)
# =========================================================================

# 'myfile2.txt' ko write mode mein khola (naye data ke liye)
f = open('myfile2.txt', 'w') 

# Ek list banayi jisme har line ke aakhri mein '\n' lagaya taaki naye line par print ho
lines = ['line1\n', 'line2\n', 'line3\n'] 

# writelines() poori list ko ek hi baar mein file ke andar alag-alag lines mein save kar deta hai
f.writelines(lines) 
f.close()

