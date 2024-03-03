from Course import ken_schedule, Course
from Assignment import Assignment


def grab_all_assignment(schedule: list[Course]) -> list[Assignment]:
    assignment_list = []
    for course in schedule:
        for assignment in course.assignments:
            assignment_list.append(assignment)
    return assignment_list



