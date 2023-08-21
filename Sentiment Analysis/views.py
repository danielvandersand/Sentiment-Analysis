from flask import Flask, Blueprint, render_template, redirect, url_for, request
import ratings
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

views = Blueprint(__name__, 'views')



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@views.route('/')
def home():
    return render_template('index.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    return render_template('login.html')


@views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        #print(username)
        
        if password == confirm_password:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.login'))
        else:
            return "Passwords do not match. Please try again."
    #print('hello')
    return render_template('signup.html')
        


    



@views.route('/search/<search>')
def profile(search):
    percentage_list = ratings.get_ratings(str(search))
    subjectivity_rating = percentage_list[0]
    num_positive = percentage_list[2]
    return render_template('result.html', percentage1=subjectivity_rating, percentage2=num_positive)
