# from flask import Flask
# app = Flask(__name__)
# from app import routes
from flask import Flask, redirect, render_template, request, url_for
import requests
import json
import userFunc
import os
import getRecommendations

token = ""
import convertRepo
# import getRecommendations


app = Flask(__name__, template_folder='.')

@app.route("/")
def landing():
    return render_template('templates/index.html')

@app.route('/button')
def button():
    print('asdf')
    return redirect("https://github.com/login/oauth/authorize?client_id=fec9d1b58f144ff37ff4")

@app.route('/callback')
def authenticate():
    # print("HELLO WORLD")
    global token
    code = request.args.get('code')
    token = requests.post('https://github.com/login/oauth/access_token?client_id='
    + os.environ['ID'] + '&client_secret=' + os.environ['S'] + '&code=' + code).text
    # print("TOKEN___")
    # print(token)
    return redirect(url_for("get_recommendations"))


@app.route("/user/<user_name>")
def auth(user_name):
    # print(user_name)
    response = requests.get("https://api.github.com/users/" + user_name)
    # print(response.content)
    if (response.content.message == "Not Found"):
        return "User does not exits"
    else:
        return "User exists"

@app.route("/get_recommendations/")
def get_recommendations():
    # print("HERE")
    # print(token)
    rated_content = userFunc.get_user_rated_content(token)
    # print(rated_content)

    # convertRepo.convert_stored_repos() # Used just for converting

    top10 = getRecommendations.top10(rated_content)
    print(top10)
    return json.dumps(top10)
    # return "Hello World"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
