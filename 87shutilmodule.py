import shutil
import os

backup = "C:/Users/kcs/3D Objects/web development"

# LINE 1: Normal Copy-Paste (Data copy hoga, metadata nahi)
# shutil.copy("myfile.txt", "myfile2.txt")

# LINE 2: VIP Copy-Paste (Data + exact Date/Time metadata sab copy hoga)
# shutil.copy2("myfile.txt", "myfile2.txt")

# LINE 3: Poore folder ka backup banana (Isme hamara 'backup' folder use hota hai)
# shutil.copytree(backup, "mytutorial")

# LINE 4: Cut-Paste karna (File ya folder ko permanent shift karna)
# shutil.move(backup+"/.txt", "file.txt")

# LINE 5: POORA FOLDER PERMANENT DELETE (Recycle bin mein nahi jayega!)
# shutil.rmtree("mytutorial")

# LINE 6: SINGLE FILE PERMANENT DELETE (Sirf ek file udane ke liye 'os' ka use)
# os.remove("file.txt")
