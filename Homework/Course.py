from dataclasses import dataclass
from Assignment import Assignment
from OfficeHour import TeachingAssistant
from Grade import GradeCategory

@dataclass
class Course:
    name: str
    enrolled_status: bool
    assignments: list[Assignment]
    office_hour: list[TeachingAssistant]
    grade: list[GradeCategory]