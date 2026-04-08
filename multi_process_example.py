from multiprocessing import  Process
import time
def task():
    for i in range(5):
        print("Task running success !1")
        time.sleep(1)
if __name__ == "__main__":
    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
