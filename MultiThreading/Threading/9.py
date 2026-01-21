# here i make a simple thread

import threading
import time

def worker():
    print("Worker thread starting \n")

t = threading.Thread(target=worker)
t.start()

# t.join()
print("Main thread finished")

