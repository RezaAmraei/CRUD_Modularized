from flask import render_template, redirect, session, request, flash, Flask
from flask_app.models.user import User
from flask_app import app

# from flask_app import app
@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    
    # call the get all classmethod to get all friends
    users = User.get_all()
   

    return render_template("index.html", all_users = users)

@app.route('/create')
def create_user():
    return render_template('create.html')

@app.route('/c', methods=["POST"])
def create():
    data = {
        "f_name": request.form["f_name"],
        "l_name" : request.form["l_name"],
        "email" : request.form["email"],
        
    }
    
    User.save(data)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    print("-----------", user, '-----------')
    return render_template("edit.html", user=user)

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show_user(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template('show.html', user = user)

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')