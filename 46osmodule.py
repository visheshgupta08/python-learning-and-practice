import os

# =========================================================================
# BLOCK 1: LOOP SE 100 FOLDERS EK SAATH BANANA
# =========================================================================
print("--- Block 1: Creating 100 Folders ---")
# Pehle check kiya ki 'data' naam ka main folder hai ya nahi, agar nahi hai toh banaya
if (not os.path.exists("data")):
    os.mkdir("data")

# Loop 0 se 99 tak chalega, aur Day1 se lekar Day100 tak ke folders bana dega
for i in range (0, 100):
    # Agar folder pehle se bana hai toh error se bachne ke liye check lagana achha hota hai
    if not os.path.exists(f"data/Day{i+1}"):
        os.mkdir(f"data/Day{i+1}")
print("100 Folders successfully ban gaye! 📁")


# =========================================================================
# BLOCK 2: 100 FOLDERS KA NAAM EK SAATH BADALNA (RENAME)
# =========================================================================
print("\n--- Block 2: Renaming 100 Folders ---")
# Yeh loop saare Day1...Day100 folders ka naam badal kar Tutorial1...Tutorial100 kar dega
for i in range (0, 100):
    # Pehle check kiya ki purana folder hai aur naya wala pehle se nahi bana hai
    if os.path.exists(f"data/Day{i+1}") and not os.path.exists(f"data/Tutorial{i+1}"):
        os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")
print("Saare folders ka naam badal kar 'Tutorial' ho gaya! 🔄")


# =========================================================================
# BLOCK 3: FOLDERS KI LIST DIKHANA (LISTDIR)
# =========================================================================
print("\n--- Block 3: Listing Folders ---")
# os.listdir("data") se 'data' folder ke andar ke saare folders ki ek LIST mil jayegi
folders = os.listdir("data")
print("Folders ki list:", folders)

# Loop chalakar ek-ek folder ka naam alag se print karwaya
for folder in folders:
    print("Folder name:", folder)
    


# =========================================================================
# BLOCK 4: CURRENT LOCATION BADALNA (GETCWD & CHDIR)
# =========================================================================
print("\n--- Block 4: Changing Directory ---")
# os.getcwd() batata hai ki aap abhi computer ke kis folder ke andar kaam kar rahe hain
print("Purani Location:", os.getcwd())

# os.chdir() se hum computer mein kisi doosre folder ke andar chale jaate hain
# CRITICAL NOTE: Agar aap Windows par hain, toh "/Users" chal jayega, par error se bachne ke liye 
# check lagana safe rehta hai:
if os.path.exists("/Users"):
    os.chdir("/Users")
    print("Nayi Location (Location badalne ke baad):", os.getcwd())
