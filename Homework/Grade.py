from dataclasses import dataclass

@dataclass
class GradeCategory:
    homework: int
    exam: int
    lab: int
    participation: int
