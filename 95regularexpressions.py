import re  # Built-in Regular Expressions module ko import kiya

text = """
Cyclone Dumazile was a strong tropical cyclone in the south-west Indian Ocean that 
affected Madagascar and Réunion in early March 2018. It formed on March 2, 
from a low-pressure area that had tracked near Madagascar. 
Dumazile originated from a low-pressure area that was first monitored by the Joint 
Typhoon Warning Center on 27 February.
Harry bhai ki website hai codewithharry.com aur unki email id@gmail.com hai.
Rohan das ka number hai 9876543210 aur unka pin code 400001 hai.
"""

# =========================================================================
# DEMO 1: re.search() — (Sirf pehla match dhoondhna)
# =========================================================================

# Hum ek simple word 'Madagascar' dhoondh rahe hain
pattern1 = r"Madagascar"
match = re.search(pattern1, text)

if match:
    # match.span() batata hai ki wo word kis character index se shuru aur khatam hua
    print(match.span()) 
else:
    print("Match nahi mila! ")

print("\n" + "-"*50 + "\n")


# =========================================================================
# DEMO 2: re.finditer() — (Saare matches line se nikalna)
# =========================================================================

# TASK A: Capital Letter se shuru hone waale saare words dhoondhna
# [A-Z] = Pehla letter bada ho | [a-z]+ = Uske baad chote letters aate rahein
pattern2 = r"[A-Z][a-z]+"
matches2 = re.finditer(pattern2, text)

for m in matches2:
    print(m.group())  # m.group() se asli dhoondha hua word bahar nikalta hai


# TASK B: Saare Numbers (Digits) dhoondhna (Jaise Phone number ya Pin code)
# \d = Kisi bhi number (0-9) ko pakadne waala code
pattern3 = r"\d+"
matches3 = re.finditer(pattern3, text)

for m in matches3:
    print(f"Number mila: {m.group()} | Rasta (Span): {m.span()}")
