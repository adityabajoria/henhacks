from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    due_date: Date
    point: int
    types: str
    
def find_assignment(ken_schedule, course_name):
    '''find all the assignments for a given course'''
    assignments = []
    for course in ken_schedule:
        if course.name == course_name:
            for assignment in course.assignments:
                assignments.append(assignment.name)
    return assignments