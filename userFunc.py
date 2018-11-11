import requests
import json
import os
# import time
import auth

os.environ['OAUTH'] = auth.auth

def get_all_repos(user):
    list_repos = []
    response = requests.get('http://api.github.com/search/repositories?q=+user:' + user + '&sort=stars',
        auth=('nicole-k-r', os.environ['OAUTH']))
    json_data = json.loads(response.content)["items"]
    for repo in json_data:
        if not repo["private"] and repo["size"] > 2:
            list_repos.append(repo["name"])
    return list_repos


def get_languages(user, repo, language_list):
    response = requests.get('http://api.github.com/repos/' + user + '/' + repo + '/languages',
        auth=('nicole-k-r', os.environ['OAUTH']))
    json_data = json.loads(response.content)

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


def get_user_rated_content(user):
    repos = get_all_repos(user)

    sorted_languages = {}
    for repo in repos:
        sorted_languages = get_languages(user, repo, sorted_languages)

    # print(sorted_languages)

    return order_language_use(sorted_languages)