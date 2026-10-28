from threading import current_thread
import threading
import time

balance=1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:
        current_balance = balance
        time.sleep(0.1)
        balance=current_balance
        print(f"Thread name={current_thread().name}, Balance after withdrawal: {balance}")

t1=threading.Thread(target=withdraw,args=(500,))
t2=threading.Thread(target=withdraw,args=(300,))
#start Threading
t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:",balance)



# from threading import current_thread
# import threading
# import time

# balance=1000
#lock=threading.Lock()
# def withdraw(amount):
#     global balance
#     #with lock: in kodnest app
#     lock.acquire()
#     try:
#         current_balance = balance
#         time.sleep(0.1)
#         balance=current_balance
#     finally:
#         lock.release()
# t1=threading.Thread(target=withdraw,args=(500,))
# t2=threading.Thread(target=withdraw,args=(300,))
# #start Threading
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Final Balance:",balance)