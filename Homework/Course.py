from dataclasses import dataclass
from Assignment import Assignment
from DateFormat import Date
from PointByCategory import Point
from Weight import Weightages
from OfficeHour import TeachingAssistant

@dataclass
class Course:
    name: str
    professor: str
    enrolled_status: bool
    assignments: list[Assignment]
    office_hour: list[TeachingAssistant]
    weights: Weightages
    total_point: Point

#COURSE DATA
#Preferably we could have use CanvasAPI to pull all the data needed below. 
#However, the process was complex so we only build the model of the program itself.
ken_schedule = [Course("ECON101", "Dr. Bender", True, [Assignment("Equilibrium", Date(3,5,2024), 20, "Homework", 0.0), 
                                         Assignment("Summative Exam 1", Date(4,11,2024), 150, "Exam", 0.0), 
                                         Assignment("Market and Supply", Date(3,29,2024), 50, "Participation", 0.0)], 
                                         [TeachingAssistant("Bilal Raza", "Purnell 229", "4PM - 6PM")], Weightages(0.20, 0.50, 0.0, 0.30),
                                         Point(300,200,100,50)),
                Course("CHEM112", "Dr. Collison", True, [Assignment("Gen Chem 1", Date(3,25,2024), 45, "Homework", 0.0),
                                         Assignment("Gen Chem 2", Date(3,26,2024), 55, "Lab", 0.0), 
                                         Assignment("Gen Chem 3", Date(3,27,2024), 65, "Exam", 0.0)], 
                                         [TeachingAssistant("Dr. Shara Compton", "Brown 207", "1PM-2PM")], Weightages(0.30, 0.40, 0.20, 0.10),
                                         Point(300,200,100,50)),
                Course("CHEM120", "Dr. Beebe", True, [Assignment("Statistic 1", Date(4,1,2024), 45, "Homework", 0.0),
                                         Assignment("Calibration Curve", Date(3,30,2024), 55, "Homework", 0.0), 
                                         Assignment("Analytical Method", Date(4,5,2024), 65, "Exam", 0.0)], 
                                         [TeachingAssistant("Connor Balickie", "CRC", "12:30PM-1:30PM"),
                                          TeachingAssistant("Jerimiah Epting", "CRC", "2:30PM-3:30PM")], Weightages(0.15, 0.40, 0.20, 0.25),
                                         Point(300,200,100,50)),
                Course("HONR292", "Dr. Chajes", True, [Assignment("Preclass Question", Date(3,31,2024), 10, "Participation", 0.0),
                                         Assignment("Essay Proposal", Date(4,3,2024), 85, "Homework", 0.0), 
                                         Assignment("Ted Talk", Date(4,20,2024), 30, "Exam", 0.0)], 
                                         [TeachingAssistant("Dr. Michael Chajes", "S College Ave 186", "10AM - 11AM")], Weightages(0.40, 0.30, 0.0, 0.30),
                                         Point(300,200,100,50)),
                Course("ENTR163", "Dr. Gasiorowski", True, [Assignment("100 Uses of Rubber Band", Date(3,5,2024), 50, "Homework", 0.0),
                                         Assignment("Curiousity List", Date(3,5,2024), 50, "Participation", 0.0)], 
                                         [TeachingAssistant("Dr. Laura", "VDC", "MWF 10-11AM")], Weightages(0.50, 0.0, 0.0, 0.50),
                                         Point(300,200,100,50)),
                Course("CISC181", "Dr. Bart", True, [Assignment("Homework 5", Date(3,8,2024), 45, "Homework", 0.0),
                                         Assignment("Dr. Bart secret assignment", Date(3,15,2024), 1000, "Exam", 0.0)], 
                                         [TeachingAssistant("Faith Lowell", "Smith 202", "9-10AM")], Weightages(0.20, 0.45, 0.20, 0.15),
                                         Point(300,200,100,50)),
                Course("HIST102", "Prof Haidinger", True, [Assignment("Midterm Essay", Date(3,16,2024), 75, "Exam", 0.0),
                                         Assignment("Quiz 2", Date(3,4,2024), 100, "Exam", 0.0)], 
                                         [], Weightages(0.25, 0.60, 0.0, 0.15),
                                         Point(300,200,100,50)),
                Course("UNIV101", "Dr. Genova", False, [], [], Weightages(0.0, 0.0, 0.0, 0.0), Point(0,0,0,0)),
                Course("CISC108", "Dr. Bart", False, [], [], Weightages(0.30, 0.40, 0.20, 0.10), Point(0,0,0,0)),
                Course("CHEM164", "Dr. Genova", False, [Assignment("Fake assignment", Date(3,3,2024), 100, "Homework", 0.0)], [], 
                       Weightages(0.0, 0.0, 0.0, 0.0), Point(0,0,0,0))]