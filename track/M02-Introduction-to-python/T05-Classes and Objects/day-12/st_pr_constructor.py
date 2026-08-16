class StudentProfile:
    def __init__(self,student_id,name,course,experience,skills):
        # Store all received values as instance attribute
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills
student_id = int(input())
name= input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

#Create one StudentProfile object
sp = StudentProfile(student_id,name,course,experience,skills)
# Print the data stored in the objects
print(f"Studnet ID: {sp.student_id}\n Name: {sp.name}\n Course: {sp.course}\n Experience in Years: {sp.experience}\n Skills: {", ".join(sp.skills)}")