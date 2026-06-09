# a = 38000 
# b = 35 

# # ==========================================================
# # 1. NESTED SHORT-HAND IF-ELSE (Ek hi line mein 3 conditions)
# # ==========================================================
# # Isko left se right padhte hain:
# # Pehle check hoga: Kya a > b hai? Agar HAAN, toh print("A") chalega aur code ruk jayega.
# # Agar NAHI, toh else ke baad waali condition check hogi: if (a == b) -> print("=") else print("B")

# print("A") if a>b else print("=") if (a==b) else print("B")


# # ==========================================================
# # 2. VARIABLE MEIN VALUE SET KARNA SHORT-HAND SE
# # ==========================================================
# # Agar a > b hai, toh c ki value 9 hogi. Nahi toh c ki value 0 hogi.
# c = 9 if a>b else 0 

# # Kyunki a ki value 38000 hai aur b ki 35, toh a>b TRUE hai, isliye c = 9 print hoga
# print(c)


import keyword  # 1. पहले 'keyword' नाम के मॉड्यूल को इम्पोर्ट करें
print(keyword.kwlist)  # 2. kwlist की मदद से सारे कीवर्ड्स की लिस्ट प्रिंट करें

