# this file is going to indicate the website's structure, displaying the framework of the website
# for the website, we are going to be using NICEGUI, which is a simple GUI framework for Python. 

from nicegui import ui
from Course import ken_schedule

# create a main function that uses nicegui to display only the title as "Updated Canvas Interface" and the body as "Welcome to the updated Canvas Interface"
# in the ui.body, we are going to display the welcome message to the user. I want to implement the code for get_assignments and get_office_hours in the body of the website interface. 
# I want to display the assignments and the office hours of the courses in the body of the website interface.
def main():
    '''display the main interface of the website along with the title and the body'''
    
    
    