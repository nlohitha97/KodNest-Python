class JobDescription:
    def __init__(self,job_id,company,role):
        self.job_id = job_id
        self.company = company
        self.role = role
    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"
class PlacementManager:
    def __init__(self):
        self.job_descriptions=[]
    def add_job_description(self,job_description):
        self.job_descriptions.append(job_description)
    def find_job_by_id(self,job_id):
        for job in self.job_descriptions:
            if job.job_id == job_id:
                return job
    # Search for and return the matching object
    # Return None if non match is found
        return None
manager = PlacementManager()
n= int(input())
for _ in range(n):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    job = JobDescription(job_id,company,role)
    manager.add_job_description(job)
required_id = int(input())
result = manager.find_job_by_id(required_id)
if result is not None:
    print(result)
else:
    print(f"Job Description with ID {required_id} not found")