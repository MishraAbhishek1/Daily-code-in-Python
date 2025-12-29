import threading

def greet():
    print("Hello form thread")
    
t1 = threading.Thread(target=greet)
t1.start()
t1.join()

print("Main thread end")