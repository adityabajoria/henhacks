from dataclasses import dataclass
from Assignment import Assignment
from OfficeHour import TeachingAssistant
from Grade import GradeCategory
from DateFormat import Date
from PointByCategory import Point

@dataclass
class Course:
    name: str
    enrolled_status: bool
    assignments: list[Assignment]
    office_hour: list[TeachingAssistant]
    grade: GradeCategory
    total_point: Point

#If somehow CanvasAPI can give all these input, it would be nice
ken_schedule = [Course("ECON101", True, [Assignment("Equilibrium", Date(3,5,2024), 20, "Homework"), 
                                         Assignment("Summative Exam 1", Date(4,11,2024), 150, "Exam"), 
                                         Assignment("Market and Supply", Date(3,29,2024), 50, "Participation")], 
                                         [TeachingAssistant("Bilal Raza", "Purnell 229", "4PM - 6PM")], GradeCategory(20,50,0,30)),
                Course("CHEM112", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("CHEM120", True, [Assignment("Statistic 1", Date(4,1,2024), 45, "Homework"),
                                         Assignment("Calibration Curve", Date(3,30,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(4,5,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("HONR292", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("ENTR163", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("CISC181", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("HIST102", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("UNIV101", False, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("CISC108", False, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10)),
                Course("CHEM164", False, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework"),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab"), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam")], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], GradeCategory(30,40,20,10))]