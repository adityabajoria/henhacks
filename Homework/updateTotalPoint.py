from Course import Course

def update_total_point(schedule: list[Course]) -> list[Course]:
    """
    This function update total point as assignments are added.
    Total point is then used to calculate the percentage of final grade
    that one assignment hold.
    """
    for course in schedule:
        for assignment in course.assignments:
            if assignment.types.lower() == "homework":
                course.total_point.total_homework += assignment.point
            if assignment.types.lower() == "lab":
                course.total_point.total_lab += assignment.point
            if assignment.types.lower() == "exam":
                course.total_point.total_exam += assignment.point
            if assignment.types.lower() == "participation":
                course.total_point.total_participation += assignment.point
    return schedule