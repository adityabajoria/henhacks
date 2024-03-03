# this file is going to indicate the website's structure, displaying the framework of the website
# for the website, we are going to be using NICEGUI, which is a simple GUI framework for Python. 

from nicegui import ui
from Course import ken_schedule
from Course import Assignment
from Course import Course
from DateFormat import Date
#from Main import grab_all_assignment
#from Course import grab_course_names

# create a main function that uses nicegui to display only the title as "Updated Canvas Interface" and the body as "Welcome to the updated Canvas Interface"
# in the ui.body, we are going to display the welcome message to the user. I want to implement the code for get_assignments and get_office_hours in the body of the website interface. 
# I want to display the assignments and the office hours of the courses in the body of the website interface.

'''display the main interface of the website along with the title and the body'''
assignments = grab_all_assignment(ken_schedule)
courses = grab_course_names(ken_schedule)


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
    
    
    