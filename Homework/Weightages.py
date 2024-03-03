from dataclasses import dataclass

@dataclass
class Weightages:
    '''The following dataclass docuents all the weightages for the course. The weightages are as follows:'''
    homework: float = 0.20
    exam: float = 0.40
    lab: float = 0.30
    participation: float = 0.10

