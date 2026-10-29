import threading
import time
lock = threading.Lock()
def student(name):
    while True:
        if lock.acquire(blocking = False):
            try:
                print(name, "got snacks")
            finally:
                lock.release()
            time.sleep(0.1)
        else:
            print(name, "is waiting for snacks")

t1 = threading.Thread(target=student, args=("Student A",),daemon =True)
t2 = threading.Thread(target=student, args=("Student B",), daemon=True)

t1.start()
t2.start()

time.sleep(2)
print("Exam break is Over")