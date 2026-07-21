def report_header(fun):
    def wrapper(*args, **kwargs):
        print("="*40)
        print("Student Report")
        print("="*40)
        fun(*args, **kwargs)
        print("="*40)
    return wrapper

class Report:
    college_name = "ABC College"
    def __init__(self, name, rool_no,marks, city):
        self.name = name
        self.rool_no = rool_no
        self.marks = marks
        self.city = city
    @classmethod
    def change_college_name(cls , new_name):
        cls.college_name = new_name
    def __str__(self):
        return f"Name: {self.name}\nRool No: {self.rool_no}\nCity: {self.city}\nCollege Name: {self.college_name}"
    @report_header
    def display_report(self):
        print(f"Name: {Report.college_name}")
        print(self)
        if self.marks >= 40:
            print("Result:PASS")
        else:
            print("Result:FAIL")

student1 = Report("Rahul",101,85,"Pune")
student1.display_report()

print()

Report.change_college_name("XYZ COLLEGE")
student1 = Report("Priya",95,75,"Pune")
student1.display_report()
"""
OUTPUT:-
========================================
Student Report
========================================
Name: ABC College
Name: Rahul
Rool No: 101
City: Pune
College Name: ABC College
Result:PASS
========================================

========================================
Student Report
========================================
Name: XYZ COLLEGE
Name: Priya
Rool No: 95
City: Pune
College Name: XYZ COLLEGE
Result:PASS
========================================
"""