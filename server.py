# from flask import Flask
# app = Flask(__name__)
# from app import routes
from flask import Flask, redirect, render_template, request
import requests
import json
import os

token = ""

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
    code = request.args.get('code')
    token = requests.post('https://github.com/login/oauth/access_token?client_id='
    + os.environ['ID'] + '&client_secret=' + os.environ['S'] + '&code=' + code).text
    return token


@app.route("/user/<user_name>")
def auth(user_name):
    print(user_name)
    response = requests.get("https://api.github.com/users/" + user_name)
    print(response.content)
    if (response.content.message == "Not Found"):
        return "User does not exits"
    else:
        return "User exists"

# Add other routes here

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
