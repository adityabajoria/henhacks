from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    due_date: Date
    point: int
    types: str
    
# create a function get_assignment_due_date that takes in ken_schedule and returns a list of the course with the earliest due date. 
# sort the assignments and the course with the due date. the final result will be to print out the course with the earliest 
# due date in order in the form of a list. 
def get_all_assignment_due_date(ken_schedule):
    '''get the course with the earliest due date'''
    assignments = []
    for assignment in ken_schedule:
        assignments.append(assignment.name, assignment.due_date)
    assignments.sort(key=lambda x: x[1])
    return assignments

