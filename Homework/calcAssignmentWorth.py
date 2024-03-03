from Course import Course
from updateTotalPoint import update_total_point

def calculate_final_percent(schedule: list[Course]) -> list[Course]:
    for course in update_total_point(schedule):
        if course.enrolled_status:
            for assignment in course.assignments:
                if assignment.types.lower() == "homework":
                    assignment.final_grade_value = assignment.point / course.total_point.total_homework * course.weights.homework
                if assignment.types.lower() == "lab":
                    assignment.final_grade_value = assignment.point / course.total_point.total_lab * course.weights.lab
                if assignment.types.lower() == "exam":
                    assignment.final_grade_value = assignment.point / course.total_point.total_exam * course.weights.exam
                if assignment.types.lower() == "participation":
                    assignment.final_grade_value = assignment.point / course.total_point.total_participation * course.weights.participation
    return schedule