marks =int(input("enter marks:"))
attendance = int(input("enter:"))
project_status = input()
if marks>=60 and attendance>=75:
    if project_status =="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
