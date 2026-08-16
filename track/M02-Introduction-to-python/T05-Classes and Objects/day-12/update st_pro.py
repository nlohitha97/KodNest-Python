class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self,new_experience):
        self.new_experience = new_experience

    def add_skill(self,new_skill):
        self.new_sklll = new_skill
    
name = input().strip()
experience = int(input())
skills = input().split()
new_experience =  int(input())
new_skill = input().strip()

# Create one StudentProfile object
s1 = StudentProfile(name,experience,skills)

# Update the Student's experience
s1.experience = new_experience

# Add the new_skill 
s1.skills.append(new_skill)

# Print the update profile
print(f"Name: {s1.name}\nExperience in Years: {s1.experience}\nSkills: {', '.join(s1.skills)}")