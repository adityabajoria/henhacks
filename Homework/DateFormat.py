from dataclasses import dataclass

@dataclass
class Date:
    month: int
    day: int
    year: int
    
# Helper Function (Used in Homework/Assignment.py)
def find_date(date):
    date = date.split('/')
    return Date(int(date[0]), int(date[1]), int(date[2]))