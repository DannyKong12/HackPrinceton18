import requests
import json
import os
# import time
import auth
import userFunc

os.environ['OAUTH'] = auth.auth

def convert_stored_repos():
    json_data = []
    print ("Hello World")
    with open('repos1.json', 'r') as f:
        data = json.load(f)

        for i in range(len(data["repos"])):
        # for i in range(1):
            index = json.loads(data["repos"][i])
            try:
                user = index["owner"]["login"]
                repo = index["name"]
                url = index["url"]
                watchers = index["subscribers_count"]
                stars = index["stargazers_count"]

                response = requests.get('http://api.github.com/repos/' + user + '/' + repo + '/languages',
                auth=('nicole-k-r', os.environ['OAUTH']))

                # Sort languages
                lang_list = userFunc.order_language_use(json.loads(response.content))
                print(lang_list)
                json_data.append({
                    "repo": repo,
                    "user": user,
                    "url": url,
                    "stars": stars,
                    "watchers": watchers,
                    "languages": lang_list
                })
            except:
                continue
        
    print(json_data)
    with open('repos_formatted.json', 'w') as f:
        json.dump(json_data, f)


    

