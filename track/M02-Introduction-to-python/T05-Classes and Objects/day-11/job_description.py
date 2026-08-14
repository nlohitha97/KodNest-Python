class JobDescription:
    def __init__(self,job_id,company,role,location="Remote",is_active =True):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active
    
    def str(self):
        status = "Active" if self.is_active else "Closed"

        return (f"{self.job_id} | " f"{self.company} | " f"{self.role} | " f"{self.location} | " f"{status}")

#Create job_one using keyword arguments
job_one = JobDescription(501,"TechNova","Python Developer","Bangalore",True)

# Create job_two using positional arguments
job_two = JobDescription(502,"CodeWorks","Java Developer","Hyderabad",True)

# create job_three using keyword and positional arguments
job_three = JobDescription(503,"CloudNine0","Support Engineer","Remote",False)

# store all three objects in the list
job_descriptions = [job_one,job_two,job_three]

# print every object using a for loop
for i in job_descriptions:
    print(i)