#Unit Tests for the get_all_office_hours
# write unit tests with output for the function get)all_course_office_hours
import unittest
from datetime import datetime
from your_module import TeachingAssistant, get_all_course_office_hours

@dataclass
class TestGetAllCourseOfficeHours(unittest.TestCase):
    def setUp(self):
        # Define some test data
        self.course1 = Course("Course1", TeachingAssistant("TA1", "Location1", "9:00 AM"))
        self.course2 = Course("Course2", TeachingAssistant("TA2", "Location2", "10:00 AM"))
        self.course3 = Course("Course3", TeachingAssistant("TA3", "Location3", "11:00 AM"))

        self.courses = [self.course1, self.course2, self.course3]
        

