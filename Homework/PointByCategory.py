#import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    total_homework: int
    total_lab: int
    total_exam: int
    total_participation: int

# find the percent change of the points, the formula is assignment point / (assignment_point + total_point) * 100
def find_percentage_per_weightage(ken_grade: Point, ken_weightage: Point) -> Point:
    '''find the percent change of the points'''
    total_point = (ken_grade.total_homework + ken_grade.total_lab + ken_grade.total_exam + ken_grade.total_participation) # using grade weightages
    ken_grade.total_homework = (ken_grade.total_homework / total_point) * ken_weightage.total_homework
    ken_grade.total_lab = (ken_grade.total_lab / total_point) * ken_weightage.total_lab
    ken_grade.total_exam = (ken_grade.total_exam / total_point) * ken_weightage.total_exam
    ken_grade.total_participation = (ken_grade.total_participation / total_point) * ken_weightage.total_participation
    return ken_grade

