# ==========================================
# PART 1: FACTORIAL USING RECURSION
# ==========================================

# Math logic: 
# factorial(5) = 5 * 4 * 3 * 2 * 1
# Formula: factorial(n) = n * factorial(n-1)

def factorial(n):
    # Base Case: Agar n ki value 0 ya 1 hai, toh factorial 1 hota hai
    if(n==0 or n==1):
        return 1
    # Recursive Case: n ko multiply karo usse ek chhote number ke factorial se
    else:
        return n*factorial(n-1)

# Function ko call kiya aur 5 ka factorial print karwaya (Ans: 120)
print("Factorial of 5 is:", factorial(5)) 

# --- Computer ke andar factorial(5) aise tootega ---
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120


# ==========================================
# PART 2: FIBONACCI SEQUENCE (QUICK QUIZ)
# ==========================================

# Logic: Pichle do numbers ko jodkar agla number banta hai
# f(0) = 0, f(1) = 1
# Formula: f(n) = f(n-1) + f(n-2)
# Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def f(n):
    # Base Case 1: Agar 0th term chahiye toh 0 return karo
    if(n==0):
        return 0
    # Base Case 2: Agar 1st term chahiye toh 1 return karo
    elif(n==1):
        return 1
    # Recursive Case: Pichle do terms ko plus (add) karo
    else:
        return f(n-1)+f(n-2)

# Hamein jitne numbers chahiye series mein, woh yahan set kiye
Terms = 10 
print(f"Fibonacci series {Terms} terms tak:")

# Ek-ek karke saare numbers ko ek hi line mein print karne ke liye loop lagaya
for i in range(Terms):
    # end=" " lagaya taaki naye line par na jaye, bas ek space aaye
    print(f(i), end=" ")



# practice

# 1. write a recursive function to calculate the sum of first n natural numbers 


def cal_sum(n):
    total = n*(n+1)/2
    print(total)

cal_sum(5)