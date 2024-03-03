from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    course: str
    due_date: Date
    point: int
    types: str
    
def get_assignment_due_date(ken_schedule):
    '''get the course with the earliest due date'''
    assignments = []
    for assignment in ken_schedule:
        assignments.append(assignment)
    assignments.sort(key=lambda x: x.due_date) # sorts the assignments by due date
    return assignments

