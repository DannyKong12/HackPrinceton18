import requests
import json
import time
from tqdm import tqdm

rawdata = requests.get('https://api.github.com/search/issues?q=label:"help wanted"?page=1&per_page=100')

pages = int(rawdata.links['last']['url'][rawdata.links['last']['url'].rfind('page')+5:])

print(pages)

repos = []

for i in tqdm(range(pages)):
    r = requests.get('https://api.github.com/search/issues?q=label:"help wanted"?page='
    + str(i) + '&per_page=100').text
    j = json.loads(r)
    repos += [x['repository_url'] for x in j['items']]
    time.sleep(6000)

with open('repositories.json', 'wb') as f:
    json.dump(repos, f)
