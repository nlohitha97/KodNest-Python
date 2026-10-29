import threading
import time

required_skills = [skill.strip() for skill in input().split(",")]
n=int(input())
students=[]

for _ in range(n):
    name = input().strip()
    skills = [skill.strip() for skill in input().split(",")]
    students.append((name,skills))

shared = {"results":{},"eligible":0}
lock = threading.Lock()

def match_student(name,skills):
    time.sleep(0.01)
    match_count=0
    for skill in required_skills:
        if skill in skills:
            match_count+=1
    if match_count>=2:
        status="Eligible"
    else:
        status ="Not Eligible"

    with lock:
        shared["results"][name]=(match_count,status)
        if status == "Eligible":
            shared["eligible"]+=1


threads =[]
for name,skills in students:
    t = threading.Thread(target=match_student,args=(name,skills))
    t.start()

for t in threads:
    t.join()
