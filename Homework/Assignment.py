from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    due_date: Date
    point: int
    types: str
    
def get_assignment_due_date(ken_schedule):
    '''get the course with the earliest due date'''
    assignments = []
    for assignment in ken_schedule:
        assignments.append(assignment.name, assignment.due_date, assignment.point, assignment.types)
    assignments.sort(key=lambda x: x.due_date) # sorts the assignments by due date
    return assignments

