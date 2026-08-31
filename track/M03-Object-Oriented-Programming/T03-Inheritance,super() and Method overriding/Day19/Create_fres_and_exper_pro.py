class StudentProfile:
    # Add the constructir and disply_profile()
    def __init__(self,name):
        self.name = name
    def display_profile(self,category):
       print(f"{category}:{self.name}")

class FresherStudent(StudentProfile):
    pass
class ExperiencedStudent(StudentProfile):
    pass

fresher_name = input().strip()
experienced_name = input().strip()
# Create both objects and display their profiles
fresher = FresherStudent(fresher_name)
fresher.display_profile("Fresher")
experienced = ExperiencedStudent(experienced_name)
experienced.display_profile("Experienced")