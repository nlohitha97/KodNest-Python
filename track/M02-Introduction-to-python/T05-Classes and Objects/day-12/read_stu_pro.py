class StudentProfile:
    def __init__(self,student_id,name,course,experience,skills):
        self.studnet_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills  = skills

    def __str__(self):
        # Return the complete formated profile
        return (f"Stuent ID: {self.studnet_id}\nName: {self.name}\nCourse: {self.course}\nExperience in Years: {self.experience}\nSkills: {", ".join(self.skills)}")

student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
s = StudentProfile(student_id,name,course,experience,skills)

# Display the onject usong print(student)
print("STUDENT PROFILE")
print(s)