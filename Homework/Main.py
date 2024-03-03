from Course import Course, ken_schedule
from calcAssignmentWorth import calculate_final_percent
from grabAssignment import grab_all_assignment
from sortAssignment import sort_assignment
from taList import office_hour_list

print(sort_assignment(grab_all_assignment(calculate_final_percent(ken_schedule))))
print(office_hour_list(ken_schedule))