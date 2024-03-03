from Course import Course, ken_schedule
from calcAssignmentWorth import calculate_final_percent
from grabAssignment import grab_all_assignment
from sortAssignment import sort_assignment
from taList import office_hour_list

# print(sort_assignment(grab_all_assignment(calculate_final_percent(ken_schedule))))
# print(office_hour_list(ken_schedule))

def compile_homeworks(schedule: list[Course]) -> list[str]:
    sorted_assignment_list = sort_assignment(grab_all_assignment(calculate_final_percent(schedule)))
    compiled_text = []
    for assignment in sorted_assignment_list:
        text = (f"Assignment '{assignment.name}' is due on {assignment.due_date.month}"
                f"/{assignment.due_date.day}/{assignment.due_date.year}"
                f" and currently worths {round(assignment.final_grade_value*100,2)}% of the final grade.")
        compiled_text.append(text)
    return compiled_text

# print(compile_homeworks(ken_schedule))

def compile_tas(schedule: list[Course]) -> list[str]:
    sorted_ta_list = office_hour_list(schedule)
    compiled_text = []
    for ta in sorted_ta_list:
        phrase = ""
        if not ta:
            phrase = "None"
        elif len(ta) == 1:
            phrase = "".join(ta)
        elif len(ta) > 1:
            i = 0
            while i < len(ta):
                phrase += "".join(ta[i]) + ", "
                i += 1 
        if phrase.endswith(", "):
            phrase = phrase[:-2]
        text = (f"Help availables: {phrase}")
        compiled_text.append(text)
    return compiled_text

# print(compile_tas(ken_schedule))

def combined_compiles(assignments: list[str], tas: list[str]) -> list[str]:
    full_report = []
    i = 0
    while i < len(assignments):
        full_report.append(f"{assignments[i]} {tas[i]}")
        i += 1
    return full_report

# print(combined_compiles(compile_homeworks(ken_schedule), compile_tas(ken_schedule)))

def compile_to_string(report: list[str]) -> str:
    return "\n\n".join(report)

print(compile_to_string(combined_compiles(compile_homeworks(ken_schedule), compile_tas(ken_schedule))))
