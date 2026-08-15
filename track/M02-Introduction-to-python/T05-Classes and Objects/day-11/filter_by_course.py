# Create the StudentProfile class
#Create the PlacementManager
# REad the student details
# Filter and display the marching students

class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.st_lst = []

    def add_student_profile(self, student_profile):
        self.st_lst.append(student_profile)

    def filter_by_course(self, course):
        matches = []
        for st in self.st_lst:
            if st.course.lower() == course.lower():   # case-insensitive comparison
                matches.append(st)
        return matches


profile = PlacementManager()
n = int(input())
for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    s = StudentProfile(student_id, name, course)
    profile.add_student_profile(s)

re_course = input().strip()
res = profile.filter_by_course(re_course)

if len(res) == 0:
    print(f"No students found for course: {re_course}")
else:
    for student in res:
        print(student)