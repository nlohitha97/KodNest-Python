from abc import ABC, abstractmethod

class SkillAnalyzer(ABC):
    def __init__(self,student_skills,required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)
    def get_matched_skills(self):
        return self.student_skills & self.required_skills
    @abstractmethod
    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        # Return mtach-score result
        matched = self.get_matched_skills()
        score = (len(matched)/len(self.required_skills)) * 100
        return f"Match Score: {score:.2f}%"
    
class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        # Return missing - skills result
        missing = self.required_skills -  self.student_skills
        if len(missing) == 0:
            return "Missing Skills: None"
        return f"Missing Skills: {', '.join(sorted(missing))}"

def run_analyzers(analyzers):
    # PRocess every analyzer using ohnr loop
    for i in analyzers:
        print(i.analyze()) 
student_skills = input().split()
required_skills = input().split()

# Create analyzer objects, store them in one list and run them
m = MatchScoreCalculator(student_skills,required_skills)
d = MissingSkillDetector(student_skills,required_skills)
a = [m,d]
run_analyzers(a)


    