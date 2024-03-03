from Course import Course
from Assignment import Assignment
from Course import ken_schedule


def grab_all_assignment(schedule: "list[Course]") -> "list[Assignment]":
    assignment_list = []
    for course in ken_schedule:
        for assignment in course.assignments:
            assignment_list.append(assignment)
    return assignment_list




