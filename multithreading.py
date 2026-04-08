#without multithreading
#
# import time
#
# def task():
#     for i in range(5):
#         print("Task running!!")
#         time.sleep(1)
# task()
# task()

#with multithreading

import threading
import time

def task():
    for i in range(5):
        print("Task running")
        time.sleep(1)
t1 =         threading.Thread(target=task)
t2 =  threading.Thread(target=task)

t1.start()
t2.start()
t1.join()
t2.join()
