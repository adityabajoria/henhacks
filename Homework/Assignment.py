from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    due_date: Date
    point: int
    weight: int
    
def get_assignment(ken_schedule):
    '''get all the  assignments from the ken_schedule as a list'''
    assignments = []
    for assignment in ken_schedule:
        assignments.append(assignment.name, assignment.due_date, assignment.point, assignment.weight)
    return assignments

for assignment in assignments:
    # if the assignment is due soon, print the assignment and print("The assignment is due soon!"), else print("The assignment is not due soon!")
    if assignment.due_date.year == 2024 and assignment.due_date.day <= 10:
        print(assignment.name, assignment.due_date, assignment.point, assignment.weight)
        print("The assignment is due soon!")
    else:
        print("Chill, you have plenty of time!")

