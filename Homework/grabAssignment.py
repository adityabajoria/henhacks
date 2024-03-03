from Course import Course
from Assignment import Assignment

def grab_all_assignment(schedule: list[Course]) -> list[Assignment]:
    """
    This function grab all assignments from the entire schedule, excluding
    any course that are withdrawn, completed, or unenrolled status.
    """
    assignment_list = []
    for course in schedule:
        if course.enrolled_status:
            for assignment in course.assignments:
                assignment_list.append(assignment)
    return assignment_list