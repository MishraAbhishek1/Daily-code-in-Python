# Multithreading program

import threading
import time

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")
    
start_time = time.time()

t1 = threading.Thread(target=task, args=("First Work", ))
t2 = threading.Thread(target=task, args=("Second Work", ))
t3 = threading.Thread(target=task, args=("Third Work", ))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = time.time()
print()