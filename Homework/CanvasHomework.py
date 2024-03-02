#Program without API
import requests
import json
import os
import dotenv as de
from Course import Course
from Assignment import Assignment

# load the environment 
de.load_dotenv()

# get the API key
api_key = os.getenv(input("Enter your API key: "))
