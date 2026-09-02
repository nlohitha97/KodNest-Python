class StudnetProfile:
    def show_profile(self):
        pass
class FresherStudent(StudnetProfile):
    def __init__(self,n,gy):
        self.n = n
        self.gy = gy
    def show_profile(self):
        #write code
        return f"{self.n} - Fresher - Graduation Yera: {self.gy}"

class ExperiencedStudent(StudnetProfile):
    def __init__(self,name,ey):
        self.name = name
        self.ey =ey
    def show_profile(self):
        #write code
        return f"{self.name} - Experienced - Experience in Years: {self.ey} years"


fresher_name = input()
graduatin_year =int(input())
experienced_name = input()
experience_in_years = int(input())

#Create the two objects
f1=FresherStudent(fresher_name,graduatin_year)
f2=ExperiencedStudent(experienced_name,experience_in_years)
# Store both objects in one list
st = [f1,f2]
#Process the list using one loop
for i in st:
    print(i.show_profile())
      