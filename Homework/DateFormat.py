from dataclasses import dataclass

@dataclass
class Date:
    month: int
    day: int
    year: int
    
def date_value(date:Date) -> int:
    """
    31 given for month to ensure 1-31 has less value than 2-1
    405 given for year to ensure 12-31-2023 has less value than 1-1-2024
    """
    return date.year * 405 + date.month * 31 + date.day