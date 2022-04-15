from flask import Blueprint, render_template, request, flash, redirect, url_for 
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .matching import *

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        areas = {}
        areas["Data"] = request.form['r1']
        areas["Design"] = request.form['r2']
        areas["Investigation"] = request.form['r3']
        areas["Machine"] = request.form['r4']
        areas["Problem Solving"] = request.form['r5']
        areas["Security"] = request.form['r6']
        areas["Simulation"] = request.form['r7']
        areas["Software"] = request.form['r8']
        areas["Systems"] = request.form['r9']
        areas["Users"] = request.form['r10']
        if request.form['submit1'] == 'Submit':
            values1(areas)
            return redirect(url_for('auth.question2'))

    return render_template("question1.html", user=current_user)

@auth.route('/question2', methods=['GET', 'POST'])
def question2():
    q = topS()
    if request.method == 'POST':
        areas = {}
        for key, value in q.items():
            if int(key) < 6:
                areas[value] = request.form[key]

        q2(areas)
        
        if request.form['submit2'] == 'Submit':
            return redirect(url_for('auth.question3'))

    return render_template("question2.html", query=q, user=current_user)

@auth.route('/question3', methods=['GET', 'POST'])
def question3():
    q = q3()
    if request.method == 'POST':
        temp = request.form.get('1')
        count = len(q)
        total = count * .2
        total -= 0.2
        finalR(q, temp, total)

        if request.form['submit3'] == 'Submit':
            return redirect(url_for('auth.top'))
        
        
    return render_template("question3.html", query=q, user=current_user)

@auth.route('/top', methods=['GET', 'POST'])
def top():       
    q = topC()
    return render_template("top.html", query=q, user=current_user)