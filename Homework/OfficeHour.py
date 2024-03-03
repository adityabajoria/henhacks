from dataclasses import dataclass
from Course import Course

@dataclass
class TeachingAssistant:
    name: str
    location: str
    time: str

"""
def get_all_course_office_hours(ken_course: list[Course]) -> list[str]:
    '''get all the course with the office hours'''
    office_hours = []
    for course in ken_course:
        office_hours.append(f"{course.name} : + {course.office_hours.name} at {course.office_hours.location} with a time slot of {date_value(course.office_hours.time)}")
    return office_hours
"""