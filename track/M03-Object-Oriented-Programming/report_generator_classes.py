from abc import ABC,abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class StudentReport(ReportGenerator):
    def generate_report(self):
        # write code
        return f"Generating Student Report"
    
class PlacementReport(ReportGenerator):
    def generate_report(self):
        #write code
        return f"Generating Placement Report"

class AttendanceReport(ReportGenerator):
    def generate_report(self):
        #write code
        return f"Generating Attendance Report"
def create_report(report_type):
    if report_type=="student":
        return StudentReport()
    if report_type=="placement":
        return PlacementReport()
    return AttendanceReport()

n = int(input())
reports=[]

for _ in range(n):
    report_type = input().strip()
    reports.append(create_report(report_type))

for report in reports:
    print(report.generate_report())