import pyttsx3  # Text-to-Speech library

# 1. Jin dosto ko shoutout dena hai unki list
names = ["Harry", "Rohan", "Rahul", "Shivani", "Divya"]

# 2. Speak engine ko chalu kiya
engine = pyttsx3.init()

# Upgrade A: Bolne ki speed set karna (Default 200 hoti hai, 150 ekdum natural lagti hai)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150) 

# Upgrade B: Awaaz badalna (0 = Male/David, 1 = Female/Zira)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 likhne se Female voice set ho jayegi!

long_speech = ""
for name in names:
    long_speech += f"Shoutout to {name}" 
    
    # Computer ko bola ki ye message apni awaaz mein bolo
engine.say(long_speech)

# 4. Sab kuch line se sunane ke liye engine ko block kiya
engine.runAndWait()
