from Course import ken_schedule, Course
from Assignment import Assignment
import pandas as pd


def grab_all_assignment(schedule: list[Course]) -> list[Assignment]:
    assignment_list = []
    for course in schedule:
        for assignment in course.assignments:
            assignment_list.append(assignment)
    return assignment_list

# i want to create a table with all of the assignments and their due dates
def create_table(assignment_list: list[Assignment]) -> pd.DataFrame:
    '''create a table with all of the assignments and their due dates'''
    assignment_name = []
    due_date = []
    for assignment in assignment_list:
        assignment_name.append(assignment.name)
        due_date.append(assignment.due_date)
    df = pd.DataFrame({'Assignment Name': assignment_name, 'Due Date': due_date})
    return df

# i want to add to this function that adds another row to the table with the get_all_office_hours to the table e
def add_office_hours_to_table(office_hours: list[str], df: pd.DataFrame) -> pd.DataFrame:
    '''add another row to the table with the get_all_office_hours to the table'''
    df['Office Hours'] = office_hours
    return df



