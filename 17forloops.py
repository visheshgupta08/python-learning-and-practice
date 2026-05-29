name = "Abhishek"
# String loop: Ek ek karke 'name' ke saare letters 'i' variable mein aayenge
for i in name:
    print(i)
    # Loop ke andar if condition: Jab letter 'b' aayega, tabhi yeh special message print hoga
    if(i=="b"):
        print("this is something special!")

colors = ["red","green","blue", "yellow"]
# Nested Loop Example: Pehla loop ek-ek karke rang (color) uthayega
for color in colors:
    print(color)
    # Andar wala loop us rang ke ek-ek letter (i) ko print karega
    for i in color:
        print(i)

# range(5) matlab 0 se lekar 4 tak chalega (total 5 baar)
# k+1 karne se ginti 0 ki jagah 1 se shuru hokar 5 tak dikhegi
for k in range(5):
    print(k+1)

# range(1, 100) matlab ginti 1 se shuru hogi aur 99 tak chalegi (100 shamil nahi hota)
for k in range(1,100):
    print(k)

# range(start, stop, step): 1 se shuru hoga, 12 se pehle rukega, aur har baar 3-3 ka gap (step) lega
# Output aayega: 1, 4, 7, 10
for k in range (1,12,3):
    print(k)