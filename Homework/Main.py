from Course import Course
from Assignment import Assignment
import pandas as pd


def grab_all_assignment(ken_schedule: list[Course]) -> list[Assignment]:
    assignment_list = []
    for course in ken_schedule:
        for assignment in course.assignments:
            assignment_list.append(assignment)
    return assignment_list




