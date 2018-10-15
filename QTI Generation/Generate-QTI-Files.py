#!/usr/bin/python

import csv, requests, time, json, urllib
from pprint import pprint


#############################
###### EDIT THIS STUFF ######
#############################

API_URL = 'https://yourinstitution.instructure.com/api/v1/'
API_KEY = 'Your token here'
quizzes_csv = 'quizIDs.csv' # name of file storing course and quiz IDs
log_file = 'download_links.csv'

payload = {}
header = {'Authorization' : 'Bearer ' + API_KEY}

##############################################################################
## ONLY update the code below if you are experimenting with other API calls ##
##############################################################################

def main():	

	
	payload={'export_type':'qti'}
	
	l = open(log_file, 'w+') # creates a new csv file and overwrites the existing
	l.close()
	
	w = csv.writer(open(log_file,"wb")) #opens the csv file for recording download links
	w.writerow(['course_id','qti_download_link','filename']) #adds headers to the CSV file

	
	with open(quizzes_csv, 'rU') as csvFile:
		csvReader = csv.reader(csvFile, delimiter = ',')

		for row in csvReader:
			try:
				url = API_URL + 'courses/%s/content_exports' %(row[0])
				pprint(url)
				r = requests.post(url, headers = header, data = payload)
				j = json.loads(r.text)
				pprint(j['progress_url'])
			except requests.exceptions.RequestException as e:
				print e
			
			try:
				r2 = requests.get(j['progress_url'],headers = header, data = {})
				j2 = json.loads(r2.text)
				pprint(j2['workflow_state'])
			
			except requests.exceptions.RequestException as e2:
				print e2
				
			while j2['workflow_state'] != 'completed':
				r2 = requests.get(j['progress_url'],headers = header, data = {})
				j2 = json.loads(r2.text)
				pprint(j2['workflow_state'])
				time.sleep(1)
			
			new_url = url + '/' + str(j['id'])
			pprint(new_url)
			r3 = requests.get(new_url,headers = header, data = {})
			j3 = json.loads(r3.text)
			pprint(j3['attachment']['url'])
			
			w.writerow([str(j3['course_id']),j3['attachment']['url'],j3['attachment']['filename']])
				
if __name__ == "__main__": main()

