import requests
import urllib
import json
import pprint
printer = pprint.PrettyPrinter(indent=4)

GLASSDOOR_PARTNER_ID = '34802'
GLASSDOOR_KEY = 'isx6oLLCxUQ'
USERIP = '72.182.6.193'
USERAGENT = 'Bruce Garro User Agent'
FORMAT = 'json'

BASE_PARAMETERS = {
	't.p': GLASSDOOR_PARTNER_ID,
	't.k': GLASSDOOR_KEY,
	'userip': USERIP,
	'useragent': USERAGENT,
	'v': '1',
	'action': 'jobs-prog',
	'countryId': '1',
	'format': FORMAT
}

JOB_PROGRESS_API_ENDPOINT = (
	"http://api.glassdoor.com/api/api.htm"
)

JOB_TITLES = [
	# 'Senior Full Stack Engineer',
	'Full Stack Developer',
	# 'Software Engineer',
	# 'Web Engineer',
	# 'Research Associate',
	# 'Business Development Intern',
]

def fetch_job_title_data(job_title):
	params = dict(BASE_PARAMETERS.items() + {'jobTitle': job_title}.items())
	headers = {
		'User-Agent': USERAGENT,
		'From': 'brucegarro@gmail.com'
	}
	request = requests.get(JOB_PROGRESS_API_ENDPOINT, params=params, headers=headers)
	return request.json()

def fetch_jobs_data():
	jobs_data = []
	for job_title in JOB_TITLES:
		jobs_data.append(fetch_job_title_data(job_title))
	return jobs_data

if __name__=="__main__":
	jobs_data = fetch_jobs_data()

	FILE_PATH = "/home/bruce/repos/roadmap/bruces_jobs.json"
	# with open(FILE_PATH, 'w+') as f:
	# 	f.seek(0)
	# 	f.write(json.dumps(jobs_data))
	# 	f.truncate()
	print printer.pprint(jobs_data)