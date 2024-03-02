from dataclasses import dataclass

@dataclass
class TeachingAssistant:
    name: str
    location: str
    time: str
    
# create a function takes in ken_course and returns a list of the course with their office hours. make sure to return the course with the office hours, 
# use the helper function (find_date) to get the time of the office hours. 
def get_all_course_office_hours(ken_course):
    '''get all the course with the office hours'''
    office_hours = []
    for course in ken_course:
        office_hours.append(f"{course.name} : + {course.office_hours.name} at {course.office_hours.location} with a time slot of {date_value(course.office_hours.time)}")
    return office_hours

