class StudentProfile:
    def __init__(self,student_id,name,course,score=0.0,skills = None,is_placed = False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills=[] if skills is None else list(skills)
        self.is_placed = is_placed
    
    def __str__(self):
        skills_text = (",".join(self.skills) if self.skills else "Not added")
        placement_status = ("Placed" if self.is_placed else "Not placed")
        return(f"Student ID:{self.student_id}\n"
                f"Student name:{self.name}\n"
                f"Course: {self.course}\n"
                f"Score:{self.course}\n"
                f"Skilld:{skills_text}\n"
                f"placement status:{placement_status}")

s = StudentProfile(101,"lohi","AIML",80.0,["PYTHON"],True)
print(s)

            