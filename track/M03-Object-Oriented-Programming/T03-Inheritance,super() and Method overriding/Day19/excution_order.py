class Employee:
    def __init__(self,name):
        self.name = name
class Developer(Employee):
    # Add the child constructor
    def __init__(self,name):
        print("Developer constructor started")
        super().__init__(name)
        print("Developer constructor ended")

name = input().strip()

# Create the object and dispaly the name
dev  = Developer(name)
print(f"Developer: {dev.name}")
