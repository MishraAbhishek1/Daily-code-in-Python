# 🔰 LEVEL 1: BASIC THREADING
# 1️⃣ Thread kya hota hai?

# Thread = execution ka independent flow
# Same program, same memory

# 2️⃣ First threading program (BASIC)

import threading
import time

def task():
    time.sleep(2)
    print("Task Finished")
    
t = threading.Thread(target=task)
t.start()

print("Main program continues")