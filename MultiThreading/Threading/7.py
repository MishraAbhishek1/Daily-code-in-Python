# here we make a multiple therading  ecample

import threading
import time

def worker(num):
    time.sleep(1)
    print(f"worker {num} done")

thread_store = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    thread_store.append(t)
    t.start()
    
for t in thread_store:
    t.join()

print("All workers finished")