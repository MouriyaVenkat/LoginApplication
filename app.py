from flask import (Flask, render_template, request, redirect, session)

app = Flask(__name__)
app.secret_key = 'helloheyeveryonekeepthisassecert'

user = {"username": "sarvi", "password": "@123"} #we will get the username and password of the the user from the html form and check if they match. If match is found, we will create a session which will have the information for the user.

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('/dashboard')

        return "<h1>Incorrect username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")