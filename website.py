from nicegui import ui

# Functions to use for the arrangement of data
class Time:
    hours: int=0
    minutes: int=0

    def __init__(self, hours, minutes) -> None:
        self.hours = hours
        self.minutes = minutes

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

    def __init__(self, name, course, due) -> None:
        self.name = name
        self.course = course
        self.due = due
    
# Sample assignments in an array
assignments = [
    Assignment("Math Homework", "MATH241", Date(3, 4, 2024, Time(23, 59))),
    Assignment("English Homework", "ENG110", Date(3, 6, 2024, Time(23, 59))),
    Assignment("Essay", "EDUC414", Date(3, 12, 2024, Time(23, 59))),
    Assignment("Diction Homework", "MUSC172", Date(3, 4, 2024, Time(11, 35))),
    Assignment("Past Due Math Homework", "MATH241", Date(2, 29, 2024, Time(23, 59))),
]

def dueDateToString(date: Date):
    return str(date.month) + "/" + str((date.day) if date.day >= 10 else "0" + str(date.day)) + "/" + str(date.year)

ui.markdown("# Assignments <br /> --- <br />")

for i in assignments:
    with ui.column():
        ui.html("""
        <div style="font-size:24px; padding:20px; background-color: #ddd;">
            <strong>
            """ + i.name + """
            </strong> -- <em style="font-size:20px;">(""" + i.course + """)</em>
            <figcaption style="text-align:left; font-size:18px"> Due 
            """ + dueDateToString(i.due) + """
            </figcaption>
        </div>
        """)

ui.run()
