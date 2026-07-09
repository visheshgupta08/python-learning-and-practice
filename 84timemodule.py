import time  # Built-in module ko import kiya (Ise pip install nahi karna padta)

# =========================================================================
# DEMO 1: time.sleep() aur time.strftime()
# =========================================================================

# Local time ko achhe format mein (%H: Hour, %M: Minute, %S: Second) print kiya
ab_ka_time = time.strftime("%H:%M:%S")
print(f"Shuruat ka time: {ab_ka_time}")

# Ab Python 2 seconds ke liye break le raha hai..
time.sleep(2)  # Computer agli line par jaane se pehle 2 second rukega

ab_ka_time_new = time.strftime("%H:%M:%S")
print(f"Break ke baad ka time: {ab_ka_time_new}\n")


# =========================================================================
# DEMO 2: time.time() se speed check karna (Stopwatch Logic)
# =========================================================================

start = time.time()  # T1: Loop chalne se pehle ka stopwatch time (seconds mein)

i = 0
while i < 500000:
    i += 1

end = time.time()    # T2: Loop khatam hone ke baad ka stopwatch time

# (End - Start) karne se pata chal jata hai ki beech mein kitne seconds beete
print(f"While loop ko 5 lakh tak chalne mein {end - start} seconds lage! ")



'''Quick Summary (Hamesha yaad rakhne ke liye):
time.time(): Code ki speed check karne ke liye stopwatch ka kaam karta hai.
time.sleep(n): Program ko n seconds ke liye pause karne ke kaam aata hai.
time.strftime(): Date aur Time ko sundar string format mein badal kar dikhata hai.'''
