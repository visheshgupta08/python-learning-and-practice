# =========================================================================
# VIDEO 43: VIRTUAL ENVIRONMENT IN PYTHON ( NOTES)
# =========================================================================


# Virtual Environment koi Python code nahi hai, yeh computer ke terminal ki setting hai.
# Iska kaam hai: "Har ek project ke liye Python ka ek alag, saaf-suthra dabba banana".
# Taaki ek project ke packages (modules) doosre project ke packages se na takrayein.

# DESI EXAMPLE: Maan lo aapko ek purana project chalana hai jisme pandas ka purana 
# version chahiye, aur ek naya project chalana hai jisme pandas ka naya version chahiye.
# Virtual Environment laptop ke andar do alag khufiya kamre bana dega taaki dono versions chal sakein.


# =========================================================================
# TERMINAL COMMANDS GUIDE ( Revision ke liye hamesha kaam aayega)
# =========================================================================

"""
1. NAYA ENVIRONMENT (KAMRA) BANANE KE LIYE:
-------------------------------------------
Terminal mein ye command likhte hain (Isse folder mein 'myenv' naam ka folder ban jayega):

python -m venv myenv


2. US KAMRE KE ANDAR GHUSNA (ACTIVATE KARNA):
--------------------------------------------
Ise chalate hi terminal ke aage (myenv) likha aa jayega, matlab ab aap safe zone mein hain.

- Windows (PowerShell/CMD) par:   myenv\Scripts\activate
- Mac / Linux par:                source myenv/bin/activate


3. US KAMRE SE BAHAR NIKALNA (DEACTIVATE KARNA):
------------------------------------------------
Jab aapka kaam khatam ho jaye aur normal laptop ke system par wapas aana ho:

deactivate


4. PACKAGES KI LIST SAVE KARNA (pip freeze):
---------------------------------------------
Maan lo aapne is environment mein 5 alag packages install kiye. Unki list ek 
text file mein save karne ke liye (taaki aapka dost bhi wahi install kar sake):

pip freeze > requirements.txt


5. DOST KE COMPUTER PAR SARE PACKAGES EK SAATH INSTALL KARNA:
--------------------------------------------------------------
Aapka dost sirf us text file se saare packages ek second mein install kar sakta hai:

pip install -r requirements.txt
"""

# =========================================================================
# PROGRAM RUN CHECK
# =========================================================================
if __name__ == "__main__":
    print("Rule 1: Isme koi Python code khud se nahi likhna hota.")
    print("Rule 2: Roz-roz basic programs ke liye ise chalane ki zaroorat nahi hai.")
    print("Rule 3: Sirf bade projects ya data science mein packages manage karne ke kaam aata hai.")
   