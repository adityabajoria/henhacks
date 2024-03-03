#import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    total_homework: int
    total_lab: int
    total_exam: int
    total_participation: int
    

# create a function that gets the course with the earliest due date
