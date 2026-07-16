import multiprocessing  # Built-in Multiprocessing module ko import kiya
import time

def heavy_calculation(number, task_name):
    print(f"Task '{task_name}' shuru hua CPU core par... ")
    
    # Ek heavy loop chalaya jo CPU ka dimaag choosega
    counter = 0
    for i in range(number):
        counter += 1
        
    print(f"Task '{task_name}' KHATAM ho gaya! ")

if __name__ == '__main__':
    start_time = time.time()
    
    # STEP 1: Do alag-alag PROCESSES (Azaad Workers) taiyar kiye
    # target = kaun sa function chalana hai | args = uske inputs
    p1 = multiprocessing.Process(target=heavy_calculation, args=[50, "Heavy Math 1"])
    p2 = multiprocessing.Process(target=heavy_calculation, args=[50, "Heavy Math 2"])
    
    # STEP 2: Dono processes ko ek sath parallel shuru kar diya!
    # Jadu: p1 aapke laptop ke Core 1 par chalega aur p2 Core 2 par chalega!
    p1.start()
    p2.start()
    
    # STEP 3: Main program ko bola ki dono ke khatam hone ka intezar karo
    p1.join()
    p2.join()
    
    end_time = time.time()
    print(f"\nDono heavy CPU tasks parallel mein khatam hue kul {end_time - start_time:.2f} seconds mein! ")
