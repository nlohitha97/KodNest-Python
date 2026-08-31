class Employee:
    # Add the constructor
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    # ADd the constructor and display_profile()
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language
        
    def display_profile(self):
        print(f'Employee : {self.name}')
        print(f'Language : {self.language}')

name = input().strip()
language = input().strip()
# Create a developer objected and display the profile
dev = Developer(name,language)
dev.display_profile()