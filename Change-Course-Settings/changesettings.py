#!/usr/bin/python

import csv, requests, time, json
from pprint import pprint

#############################
###### EDIT THIS STUFF ######
#############################

access_token = 'YOUR ACCESS TOKEN HERE' # your access token
courses_csv = 'courselist.csv' # name of file storing course numbers, each course number should be on its own line. No header row.
log_file = 'log.txt' # a log file for logging all the things.
baseUrl = 'https://institutionurl.instructure.com' # change to domain of your Canvas account
header = {'Authorization' : 'Bearer ' + access_token}
payload = {}

##############################################################################
## ONLY update the code below if you are experimenting with other API calls ##
##############################################################################

def main():

    # add time stamp to log file
    log_time = str(time.asctime(time.localtime(time.time())))
    write_to_log(log_time)   

    # do the update
    update_course()
    
    # add time stamp to log file
    log_time = str(time.asctime(time.localtime(time.time())))
    write_to_log(log_time)   
    write_to_log("\nDONE\n")
   

def update_course():

    with open(courses_csv, 'rU') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ',')

        for row in csvReader:
             course_id = row[0]
             url = baseUrl + '/api/v1/courses/%s/settings?hide_final_grades=true&hide_distribution_graphs=true' %(course_id)
             write_to_log(url)
             r = requests.put(url, headers = header, data = payload)


def write_to_log(message):

       with open(log_file, 'a') as log:
              log.write(message + "\n")
              pprint(message)



if __name__ == "__main__": main()
