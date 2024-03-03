# this file is going to indicate the website's structure, displaying the framework of the website
# for the website, we are going to be using NICEGUI, which is a simple GUI framework for Python. 

import nicegui as ui
from Course import ken_schedule
from random import randint

# create a main function that uses nicegui to display only the title as "Updated Canvas Interface" and the body as "Welcome to the updated Canvas Interface"
def main():
    '''display the title and body of the updated canvas interface'''
    ui.title('Updated Canvas Interface')
    ui.body('Welcome to the updated Canvas Interface')
    ui.run()