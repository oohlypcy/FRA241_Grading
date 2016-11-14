from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User
from app.models.subject import Subject
import datetime
# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage', __name__, url_prefix="/<url_user_id>", template_folder='', static_folder='')


# still figuring it
@Homepage.url_value_preprocessor
def user_id(endpoint, url_user_id):
    g.id = url_user_id['url_user_id']


# Homepage route
@Homepage.route('/Home')
def Home(url_user_id):
    g.id = url_user_id
    g.user = User(g.id)
    connect = sqlite3.connect('Data.db')
    # create a being that process data (go get filter etc.)
    c = connect.cursor()
    # get table column
    tableField = c.execute("PRAGMA table_info(User)")
    g.show_list = ['ID', 'name', 'E-mail', 'Role', 'Faculty', 'Major', 'Enrol-Year']
    c.close()
    return render_template("template.html")


# see current subject route
@Homepage.route('/Subject')
def CurrentSubject(url_user_id):
    return render_template('sub.html')


@Homepage.route('/Work')
def CurrentWork(url_user_id):
    year = datetime.date.today()
    if year.month <= 4:
        year = int(str(year.year +542)[2:4])
    else :
        year = int(str(year.year +543)[2:4])

    g.user = User(url_user_id)
    g.subject = g.user.Subject['current']
    print g.subject
    g.subject = sorted(g.subject)
    g.work = []
    # for subject in g.subject:
    #     work = Subject(subject,year)
    #     g.work.append(work.get_work())
    print g.work
    return render_template("HTML_assignment.html")


@Homepage.route('/Score')
def CurrentScore(url_user_id):
    g.id = url_user_id
    g.user = User(g.id)
    g.subject_list = g.user.Subject['current']
    g.subject_list=sorted(g.subject_list)
    #create a being that process data (go get filter etc.)
    return render_template('Score.html')
