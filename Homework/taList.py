from Course import Course
from OfficeHour import extract_ta_info
from calcAssignmentWorth import calculate_final_percent
from grabAssignment import grab_all_assignment
from sortAssignment import sort_assignment

def office_hour_list(schedule: list[Course]) -> list[tuple]:
    """
    Take in a schedule and extract all the info of TAs for sorted
    assignment list.
    """
    sorted_assignment = sort_assignment(grab_all_assignment(calculate_final_percent(schedule)))
    assignment_tas = []
    sorted_ta_list = []
    for assignment in sorted_assignment:
        for course in schedule:
            if assignment in course.assignments:
                assignment_tas = course.office_hour
        sorted_ta_list.append(extract_ta_info(assignment_tas))
        assignment_ta = []
    return sorted_ta_list