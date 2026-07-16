import asyncio
import time

# STEP 1: 'async def' se ek upgraded function banaya
async def function1():
    print("Function 1 shuru hua... ")
    # time.sleep() ki jagah asyncio.sleep() use hota hai taaki computer baaki kaam kar sake
    await asyncio.sleep(5)  
    print("Function 1 KHATAM ho gaya! ")
    return "Result 1"

async def function2():
    print("Function 2 shuru hua... ")
    await asyncio.sleep(3)  
    print("Function 2 KHATAM ho gaya! ")
    return "Result 2"

async def function3():
    print("Function 3 shuru hua... ")
    await asyncio.sleep(1)  
    print("Function 3 KHATAM ho gaya! ")
    return "Result 3"

# STEP 2: Main core function jahan sab ek sath chalenge
async def main():
    start_time = time.time()
    
    # ASLI JADU: asyncio.gather saare functions ko ek sath parallel chala deta hai
    # Jaise hi function 1 wait karega, computer automatic function 2 aur 3 ko chalu kar dega!
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    
    # L ke andar teeno functions ke returns ek list ban kar bachaate hain
    print(f"\nSaare results mil gaye: {L}")
    
    end_time = time.time()
    print(f"Poora program chalne mein kul samay laga: {end_time - start_time} seconds")

# STEP 3: AsyncIO engine ko chalu karne ka standard tarika
asyncio.run(main())


'''asyncio.gather(): Jab aapko bohot saare functions ko ek sath group mein chala kar
 unke saare results ek single list mein chahiye hon [local].
 
 asyncio.create_task(): Jab aapko kisi specific function ko background mein azaad
   chhod dena ho, taaki aap apna baaki bacha hua code chala sakein aur baad mein jab 
   zaroorat pade tab us task ka result await se pakad sakein [local].Aapka'''