from nicegui import ui

# Functions to use for the arrangement of data
class Time:
    hours: int=0 # (0-23)
    minutes: int=0 # (0-59)

    def __init__(self, hours, minutes) -> None:
        self.hours = hours % 24
        self.minutes = minutes % 60

class Course:
    name: str="Course Name"
    totalPoints: float=0.0

    def __init__(self, name, totalPoints) -> None:
        self.name = name
        self.totalPoints = totalPoints

class Date:
    month: int=1
    day: int=1
    year: int=2024
    time: Time=Time(23, 59)

    def __init__(self, month, day, year, time) -> None:
        self.month = month
        self.day = day
        self.year = year
        self.time = time

class Assignment:
    name: str = "Assignment Name"
    course: str = "Course Name"
    due: Date = Date(1, 1, 2024, (23, 59))
    points: float = 0.0

    def __init__(self, name, course, due, points) -> None:
        self.name = name
        self.course = course
        self.due = due
        self.points = points
    
# Sample assignments in an array
assignments = [
    Assignment("Math Homework", "MATH241", Date(3, 4, 2024, Time(23, 59)), 5.0),
    Assignment("English Homework", "ENG110", Date(3, 6, 2024, Time(23, 59)), 5.0),
    Assignment("Essay", "EDUC414", Date(3, 12, 2024, Time(23, 59)), 125.0),
    Assignment("Diction Homework", "MUSC172", Date(3, 4, 2024, Time(11, 35)), 5.0),
    Assignment("Past Due Math Homework", "MATH241", Date(2, 29, 2024, Time(23, 59)), 15.0)
]

courses = [
    Course("MATH241", 200.0),
    Course("MUSC172", 350.0),
    Course("ENG110", 125.0),
    Course("EDUC414", 750.0),
]


#
def dueDateToString(date: Date):
    return str(date.month) + "/" + str((date.day) if date.day >= 10 else "0" + str(date.day)) + "/" + str(date.year)


#
def sortByDueDate(dates):
    pass


#Gives the fractional value of the impact an assignment has on the total grade. 
#If course name doesn't match anything in 'courses', the function will return -1.0.
def getAssignmentImpact(a:Assignment):
    for course in courses:
        if a.course == course.name:
            #                             |
            #Print statement for testing  |
            #                             v
            #print(str(a.points) + " / " + str(course.totalPoints) + " = " + str(a.points / course.totalPoints))
            return a.points / course.totalPoints
    else: return -1.0

#Takes the assignment impact and turns it into a percentage to the nearest hundredth.
#If course name doesn't match anything in 'courses', the function will return an empty string.
def getImpactString(a:Assignment):
    impact:float = getAssignmentImpact(a)
    
    if impact == -1.0: return ""
    else: return str(impact*100)[:4] + "%"



ui.markdown("# Assignments <br /> --- <br />")



with ui.column().classes("w-full"):
    for i in assignments:
        ui.html("""
        <div class="assignment" style="font-size:24px; padding:20px; background-color: #ddd;">
            <strong>
            """ + i.name + """
            </strong> -- <em style="font-size:20px;">(""" + i.course + """)</em>
            <strong style="">""" + getImpactString(i) + """</strong>
            <figcaption style="text-align:left; font-size:18px"> Due 
            """ + dueDateToString(i.due) + """
            </figcaption>
        </div>
        """).style("width: 40%; margin: auto;")

ui.run()
