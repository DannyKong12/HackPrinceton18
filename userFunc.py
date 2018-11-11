import requests
import json
import os
# import time
import auth

# user_url = ''
token = ''

def get_all_repos():
    list_repos = []
    # print("TOKEN")
    # print(token)
    response = requests.get('http://api.github.com/user/repos?' + token)
    # print(response.content)
    # json_data = json.loads(response.content)["items"]
    # print(json.loads(response.content))
    json_data = json.loads(response.content)
    # user_url = json_data["url"]
    for repo in json_data:
        if not repo["private"] and repo["size"] > 2:
            # print (repo["url"])
            list_repos.append(repo["url"])
    return list_repos


def get_languages(repo_url, language_list):
    # response = requests.get('http://api.github.com/repos/' + user + '/' + repo + '/languages',
    # print(repo_url)
    response = requests.get(repo_url+ "/languages?" + token)
    json_data = json.loads(response.content)

    # print (json_data)
    for key in json_data.keys():
        if key in language_list:
            language_list[key] = language_list[key] + 1
        else:
            language_list[key] = 1
    return language_list


def order_language_use(sorted_languages):
    ordered_list = []
    max_count = 0
    num_languages = len(sorted_languages.keys())
    for i in range(num_languages):
        for key in sorted_languages.keys():
            language_count = sorted_languages[key]
            if language_count > max_count:
                max_count = language_count
                max_language = key
        ordered_list.append(max_language)
        del sorted_languages[max_language]
        max_count = 0
    return ordered_list


def get_user_rated_content(tkn):
    global token

    token = tkn
    # print(tkn)
    repos_urls = get_all_repos()

    sorted_languages = {}
    for repo_url in repos_urls:
        sorted_languages = get_languages(repo_url, sorted_languages)

    # print(sorted_languages)

    return order_language_use(sorted_languages)