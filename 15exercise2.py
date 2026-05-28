# exercise : Good Morning 
import time 
timestamp= time.strftime('%H,%M,%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
minute= int(time.strftime('%M'))
print(minute)
second= int(time.strftime('%S'))
print(second)



if(hour>=5 and hour<12):
    print("good morning, sir!")
elif(hour>=12 and hour<17 ):
    print("good afternoon, sir!")
elif(hour>=17 and hour<22):
    print("good evening, sir!")
else:
    print("good night, sir!")

# strftime se humne pure time ka ek string format le liya (HH,MM,SS)
# Sirf Hour (ghanta) nikala aur use int mein badla taaki condition check ho sake