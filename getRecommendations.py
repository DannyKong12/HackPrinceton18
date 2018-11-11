import json

def get_score(repo_obj, user_languages):
    score = 0
    score_stars = repo_obj["stars"] / 10000
    if score_stars > 10:
        score_stars = 10
    
    score_watchers = repo_obj["watchers"] / 1000
    if score_watchers > 10:
        score_watchers = 10
    
    # Check for matches of languages
    score_lang = 0
    for count, lang in enumerate(user_languages):
        for count1, lang1 in enumerate(repo_obj["languages"]):
            if lang == lang1:
                print ("match")
                score_lang += (10 - count) + (10 - count1)
    if score_lang > 50:
        score_lang = 50
    elif score_lang < 0:
        score_lang = 0


    print(score_stars + score_watchers + score_lang)
    return (score_stars + score_watchers + score_lang)


def top10(lang_list):
    scores = []
    with open('repos_formatted.json', 'r') as f:
        data = json.load(f)
        for repo in data:
            score = get_score(repo, lang_list)
            scores.append({
                "score": score,
                "url": repo["url"],
                "languages": repo["languages"],
                "repo": repo["repo"]
            })

    # find top 10
    top10 = []
    max_score = 0
    max_elem = {}
    used_names = []
    for i in range(10):
        for score_elem in scores:
            print(used_names)
            if (score_elem["score"] > max_score) and (score_elem["repo"] not in used_names):
                max_score = score_elem["score"]
                max_elem = score_elem
        top10.append({"url": max_elem["url"], "languages": max_elem["languages"]})
        used_names.append(max_elem["repo"])
        max_score = 0
    return top10
