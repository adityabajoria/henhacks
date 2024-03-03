# this file is going to indicate the website's structure, displaying the framework of the website
# for the website, we are going to be using NICEGUI, which is a simple GUI framework for Python. 

from nicegui import ui
from Course import ken_schedule
from Main import compile_homeworks, compile_tas, combined_compiles

'''display the main interface of the website along with the title and the body'''
assignments = combined_compiles(compile_homeworks(ken_schedule), compile_tas(ken_schedule))



ui.markdown("# Assignments <br /> --- <br />").style("text-align:center; width: 40%; margin: auto;")



with ui.column().classes("w-full"):
    for i in assignments:
        ui.html("""
        <div class="assignment" style="font-size:24px; position: relative; padding:20px; background-color: #ddd;">
            <strong>
            """ + i + """
            </strong><em style="font-size:20px;"></em>
            <div style="position: absolute; right: 0; top:0; padding:20px; text-align: center;"><p><strong style="padding: 0; font-size: 24px;">""" + """</strong></p><p style="font-size: 50%;"></p></div>
            <figcaption style="text-align:left; font-size:18px">
            </figcaption>
        </div>
        """).style("width: 40%; margin: auto;")

ui.run()