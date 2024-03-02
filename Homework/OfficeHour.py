from dataclasses import dataclass

@dataclass
class TeachingAssistant:
    name: str
    location: str
    time: str
    
def get_office_hour(ken_schedule):
    '''get all the office hours from the ken_schedule as a list'''
    office_hours = []
    for office_hour in ken_schedule:
        office_hours.append(office_hour.name, office_hour.location, office_hour.time)
    return office_hours