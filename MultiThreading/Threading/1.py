# # today we satart a  new topic : therading 
# seriously threading is very important in python why we use a threading 
# generally we discuss the threading in operation ystem  and same purpose we use threading in real
# life application threading is very important liek therading is  useful in webserver
# like apache server use threading to handle multiple request at a same time
# in video rendering also we use threading to render multiple part

import threading
import time

def task(name):
    print(f'Task {name} starting')
    time.sleep(2)
    print(f"Task {name} completed")
    
t1 = threading.Thread(target=task, args=('A',))
t2 = threading.Thread(target=task, args=('B',))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks Completed")