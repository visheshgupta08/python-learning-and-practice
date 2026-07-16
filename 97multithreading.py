import threading  # Built-in Multithreading module ko import kiya
import time       # Time napne aur sleep lagane ke liye
from concurrent.futures import ThreadPoolExecutor   # Modern thread factory manager
# STEP 1: Ek normal function banaya jo internet se download hone ka drama (simulate) karega
def func(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)  # Yeh thread ko thodi der ke liye pause kar dega
    return seconds
def main():
    # Stopwatch shuru kari
    time1 = time.perf_counter()

    # =========================================================================
    # PURANA TARIKA: SEQUENTIAL (Bina threads ke ek ke baad ek chalna)
    # =========================================================================
    # Agar hum neeche wale normal tarike se chalayenge, toh kul 4 + 2 + 1 = 7 seconds lagenge.
    # func(4)
    # func(2)
    # func(1)


    # =========================================================================
    # NAYA TARIKA: MULTITHREADING (Parallel background workers)
    # =========================================================================
    
    # 1. Teen alag-alag Threads taiyar kiye aur unhe unka kaam (target aur arguments) bataya
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    # 2. START JADU: Teeno threads ko ek sath background mein parallel shuru kar diya!
    # Is line par aate ही teeno functions ek hi samay par apna kaam shuru kar denge.
    t1.start()
    t2.start()
    t3.start()

    # 3. JOIN JADU: Main program ko bola ki jab tak ye teeno apna kaam complete karke 
    # wapas nahi aa jaate, tab tak tum rukoge aur aage ka stopwatch calculation nahi karoge.
    t1.join()
    t2.join()
    t3.join()

    # Stopwatch band kari
    time2 = time.perf_counter()
    
    print(time2 - time1)

# =========================================================================
# MODERN TARIKA: THREADPOOL EXECUTOR (Automatic Paltan)
# =========================================================================
def poolingDemo():
    # 'with' lagane se threads apna kaam khatam karke automatic clean (close) ho jaate hain
    with ThreadPoolExecutor() as executor:
        
        # --- SUBMIT TARIKA (Comments se samajhein) ---
        # future1 = executor.submit(func, 3) # Background thread mein phenk diya
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result()) # .result() lagane se join() ki tarah wait hota hai aur answer milta hai
        # print(future2.result())
        # print(future3.result())
        
        # --- MAP TARIKA (Pro Coder Style) ---
        l = [3, 5, 1, 2] # Inputs ki ek list banayi
        
        # JADU: executor.map ne ek jhatke mein list ke saare numbers [3, 5, 1, 2] 
        # ke liye alag-alag background threads chalu kar diye parallel mein!
        results = executor.map(func, l)
        
       # Loop lagakar saare threads ke return answers ko line se print kiya
        for result in results:
            print(result)


# --- FUNCTION CALL ---
# Abhi aapne sirf poolingDemo() ko call kiya hai, isliye sirf niche wala pool chalega.
poolingDemo()
