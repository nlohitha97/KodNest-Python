class JobDescription:
    def __init__(self,job_id,company,role,location,reqired_skills,is_active):
        self.job_id  = job_id
        self.company = company
        self.role = role
        self.location = location
        self.reqired_skills = reqired_skills
        self.is_active = is_active

    def __str__(self):
        # Convert the Boolean Value into in is_active to Active or Closed
        status = ("Active" if self.is_active else "Closed")
        # Return the complete formated job descriptions
        return(f"Job ID: {self.job_id}\nCompany: {self.company}\nRole: {self.role}\nLocation: {self.location}\nRequired Skills: {', '.join(self.reqired_skills)}\nActive: {status}")

job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
skills_input = input().strip()
status_input = input().strip()

required_skills = [skill.strip()
for skill in skills_input.split(",")
if skill.strip()]

is_active = status_input.lower()=='yes'

# Create one JOb description object
job = JobDescription(job_id,company,role,location,required_skills,is_active)

# Display the object using print(job)
print("JOB DESCRIPITON")
print(job)
