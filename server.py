# from flask import Flask
# app = Flask(__name__)
# from app import routes
from flask import Flask
import requests
import json
import userFunc

app = Flask(__name__, template_folder='.')

@app.route("/user/<user_name>")
def auth(user_name):
    print(user_name)
    response = requests.get("https://api.github.com/users/" + user_name)
    print(response.content)
    if (response.content.message == "Not Found"):
        return "User does not exits"
    else:
        return "User exists"

@app.route("/get_recommendations/<user>")
def get_recommendations(user):
    rated_content = userFunc.get_user_rated_content(user)
    return json.dumps(rated_content)
    # Get content from json



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)