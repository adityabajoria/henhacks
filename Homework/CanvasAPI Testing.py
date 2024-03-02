from canvasapi import Canvas
import warnings

from canvasapi.assignment import Assignment, AssignmentGroup
from canvasapi.account import Account
from canvasapi.account_calendar import AccountCalendar
from canvasapi.calendar_event import CalendarEvent
from canvasapi.course import Course, CourseNickname
from canvasapi.file import File 
from canvasapi.paginated_list import PaginatedList
#25~uStyd9XjukwNQdDz11N43MgDO9sVaK75YQE8F6jXSfkOF988aCuVW9McDFCjyF5c
#5861107 User ID

API_URL = "https://udel.instructure.com/"
API_KEY = "25~uStyd9XjukwNQdDz11N43MgDO9sVaK75YQE8F6jXSfkOF988aCuVW9McDFCjyF5c"

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(1761511)
user = canvas.get_user(5861107)
course_list = []
courses = user.get_courses() 
for course in courses[:18]:
    course_list.append(course) #Course is an instance of Dataclass Course.

#print(course_list)
    
assignments = course.get_assignments(bucket='ungraded')
assignment1 = course.get_assignment(12117845)
print(assignment1)
for assignment in assignments:
    print(assignment)

