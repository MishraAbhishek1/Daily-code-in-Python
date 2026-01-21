# thread with class
import threading
import time

class WorkerThread(threading.Thread):
    
    # here i make a funtion
    def run(self):
        time.sleep(12)
        print("Thread runinig using class")

t = WorkerThread()
t.start()