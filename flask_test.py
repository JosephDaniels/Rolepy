import random

from flask import Flask, jsonify, request, session, redirect


app = Flask(__name__)
app.secret_key = b'this should a random string to encrypt the sessions'


home_html = "home.html"

chat_html = "chat.html"

login_html = "login.html"

all_responses = ""

@app.route('/do_login/', methods=['POST'])
def do_login():
    session['user'] = request.json["user"]
    session['pass'] = request.json["pass"]
    return jsonify("success")

@app.route('/logout')
def do_logout():
    # remove the username from the session if it's there
    user = session['user']
    print ("You were logged out.")
    session.pop('user', None)
    return """
    <html>
    <body>
    Thank you %s for coming to our Rolepy Server.
    Click here to return to the main page.
    <a href="http://LOCALHOST:5000"> here </a>
    </body>
    </html>
    """ % user

@app.route('/')
def home_page():
    return open(home_html).read()

@app.route('/echo/', methods=['POST'])
def echo():
    try:
        username = session['user']
    except:
        return jsonify("Sorry, you are not logged in.")
    if username:
        global all_responses
        answer = request.json['something']
        all_responses += username + " says: " + answer+"\n"
        return jsonify(all_responses)

@app.route("/login/")
def login():
    return open(login_html).read()

@app.route("/chat/")
def chat():
    return open(chat_html).read()

if __name__ == "__main__":
    app.run(debug = True)
