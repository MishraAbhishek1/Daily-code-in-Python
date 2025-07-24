# Synchronous Function mean line by line exute simply we say first task completed and then other task is completed >
import time

def first_task():
    print("first Task is Start")
    time.sleep(2)
    print("First Task is completed")

def second_task():
    print("Second Task is Started")
    time.sleep(2)
    print("Second Task is completed")

first_task(), second_task()   