# here we without threading line by lone print no threading we use
print("A")
print("B")
print("C")

# here we see in output terminal all value print line by line first a is completed and then b is print
# ok no threadin we use no paralesim concept follow

# here we have a problem how work threading and problem raise 
# ❓ Problem kaha aayi?

import time

def download():
    time.sleep(5)
    print("Download Done")
    
download()
print("Next Tasks")