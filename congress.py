import os
import json
import requests

congress_token = 'JxDNj3v4p1OAcaEy5UeOljJljyCWtUKcNkKDXYVp'

url = f'https://api.congress.gov/v3/committee-report/118/hrpt?api_key={congress_token}'

r = requests.get(url)

results = r.json()
print(results['reports'][0]['url'])