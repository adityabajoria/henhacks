# this file is going to indicate the website's structure, displaying the framework of the website
# for the website, we are going to be using NICEGUI, which is a simple GUI framework for Python. 

from nicegui import ui
from Course import ken_schedule
from Course import Assignment
from DateFormat import Date
from Main import grab_all_assignment
from Course import grab_course_names

'''display the main interface of the website along with the title and the body'''
assignments = grab_all_assignment(ken_schedule)
courses = grab_course_names(ken_schedule)


def dueDateToString(date: Date):
    return str(date.month) + "/" + str((date.day) if date.day >= 10 else "0" + str(date.day)) + "/" + str(date.year)


#
def sortByDueDate(dates):
    pass


#Gives the fractional value of the impact an assignment has on the total grade. 
def getAssignmentImpact(a:Assignment):
    return str(a.point)[:4] + "%"



ui.markdown("# Assignments <br /> --- <br />").style("text-align:center; width: 40%; margin: auto;")



with ui.column().classes("w-full"):
    for i in assignments:
        ui.html("""
        <div class="assignment" style="font-size:24px; position: relative; padding:20px; background-color: #ddd;">
            <strong>
            """ + i.name + """
            </strong> -- <em style="font-size:20px;">(""" + i.course + """)</em>
            <div style="position: absolute; right: 0; top:0; padding:20px; text-align: center;"><p><strong style="padding: 0; font-size: 24px;">""" + getAssignmentImpact(i) + """</strong></p><p style="font-size: 50%;">of final grade</p></div>
            <figcaption style="text-align:left; font-size:18px"> Due 
            """ + dueDateToString(i.due_date) + """
            </figcaption>
        </div>
        """).style("width: 40%; margin: auto;")

ui.run()