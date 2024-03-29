from dataclasses import dataclass
from DateFormat import Date

@dataclass
class Assignment:
    name: str
    due_date: Date
    point: int
    types: str
    final_grade_value: float


