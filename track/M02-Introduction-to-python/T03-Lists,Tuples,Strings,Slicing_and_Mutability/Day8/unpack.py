import functools
name = input()
course = input()
score = int(input())
#Create the tuple
student_record = (name,course,score)

#Unpack the tuple
n,c,s = student_record
print(f"Name:{n}")
print(f"Course:{c}")
print(f"Score:{s}")
