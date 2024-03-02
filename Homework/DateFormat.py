from dataclasses import dataclass

@dataclass
class Date:
    month: int
    day: int
    year: int
    

# Helper function to determine which date is earlier or later
def date_value(month: int, day: int, year: int) -> int:
    """
    31 given for month to ensure 1-31 has less value than 2-1
    405 given for year to ensure 12-31-2023 has less value than 1-1-2024
    """
    return year * 405 + month * 31 + day