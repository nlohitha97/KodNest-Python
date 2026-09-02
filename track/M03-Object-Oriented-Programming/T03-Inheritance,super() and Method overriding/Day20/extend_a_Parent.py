class Profile:
    def __init__(self,name):
        self.name = name
    def summary(self):
        return f"Name: {self.name}"

class StudentProfile(Profile):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
        
        #Override summary() here
    def summary(self):
        return f"{super().summary()} \ngit Course: {self.course}"
name=input().strip()
course = input().strip()
#Create object and display summary
student = StudentProfile(name,course)
print(student.summary())