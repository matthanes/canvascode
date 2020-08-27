import csv, json
from datetime import datetime
# Import the Canvas class
from canvasapi import Canvas


# Canvas API URL
API_URL = "https://yourinstitution.instructure.com/"
# Canvas API key
API_KEY = "Token Goes Here"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#Fill out this stuff below:
course_number = 'Canvas Course Number Goes Here'
publish = True

#Don't change the stuff below
course = canvas.get_course(course_number)

csvdates = 'dates.csv'

with open(csvdates, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    next(csvReader) #skips the header row
    
    for row in csvReader:
        new_assignment = course.create_assignment({
            'name': row[0],
            'submission_types': ['online_upload'],
            'points_possible': row[1],
            'due_at': datetime.strptime(row[2], '%m/%d/%Y %H %p'),
            'unlock_at': datetime.strptime(row[3], '%m/%d/%Y %H %p'),
            'lock_at': datetime.strptime(row[4], '%m/%d/%Y %H %p'),
            'description': row[5],
            'published': publish
        })
        print(row[0])
