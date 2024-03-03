from Course import Course
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
    '''Create a table with all of the assignments and their due dates'''
    df = pd.DataFrame({'Assignment Name': [assignment.name for assignment in assignment_list],
                       'Due Date': [assignment.due_date for assignment in assignment_list]})
    return df

def add_office_hours_to_table(office_hours: list[str], df: pd.DataFrame) -> pd.DataFrame:
    '''Add another row to the table with the office hours'''
    office_hours_df = pd.DataFrame({'Office Hours': office_hours})
    return pd.concat([df, office_hours_df]) #fix 




