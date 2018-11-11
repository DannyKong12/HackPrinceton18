import requests
import json
import time
import os
from tqdm import tqdm



data = {}

with open('repos.json', 'r') as f:
    j = json.load(f)
    data['size'] = j['size']
    repos = []
    for i in tqdm(range(data['size'])):
        url = j['repos'][i]
        r = requests.get(url, auth=('dannykong12', os.environ['OAUTH'])).text
        repos += [r]

    data['repos'] = repos
    with open('repos1.json', 'w') as of:
        json.dump(data, of)

