import threading
lock1 = threading.Lock() #PEN
lock2 = threading.Lock() #BOOK

def student_a():
    lock1.acquire()
    print("Student A acquired Pen")

    lock2.acquire()
    print("Stundent A acquired BOOK")

    lock2.release()
    lock1.release()

def student_b():
    lock2.acquire()
    print("Student B acquired BOOK")

    lock1.acquire()
    print("Student B aquired Pen")

    lock1.release()
    lock2.release()

t1 = threading.Thread(target = student_a)
t2 = threading.Thread(target = student_b)

t1.start()
t2.start()

t1.join()
t2.join()