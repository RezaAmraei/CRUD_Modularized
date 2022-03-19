from flask import render_template, redirect, session, request, flash, Flask
from flask_app.models.user import User
from flask_app import app

# from flask_app import app

@app.route("/")
def index():
    
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)

    return render_template("index.html", all_users = users)

@app.route('/create')
def create_user():
    return render_template('create.html')
@app.route('/c', methods=["POST"])
def create():
    data = {
        "f_name": request.form["f_name"],
        "l_name" : request.form["l_name"],
        "email" : request.form["email"]
    }
    
    User.save(data)
    return redirect('/')