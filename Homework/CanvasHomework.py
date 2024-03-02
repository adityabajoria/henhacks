#Program without API
from Courses import Course
from Assignments import Assignment

# load the environment 
de.load_dotenv()

# get the API key
api_key = os.getenv(input("Enter your API key: "))
