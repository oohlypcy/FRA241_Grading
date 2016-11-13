from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User

# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage', __name__, url_prefix="/<url_user_id>", template_folder='', static_folder='')


# still figuring it
@Homepage.url_value_preprocessor
def user_id(endpoint, url_user_id):
    pass


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
    return "boo"


@Homepage.route('/Work')
def CurrentWork(url_user_id):
    print url_user_id
    g.user = User(url_user_id)
    g.subject = ''
    return render_template("HTML_assignment.html")


@Homepage.route('/Score')
def CurrentScore(url_user_id):
    #g.id = url_user_id
    #g.user = User(g.id)
    #connect = sqlite3.connect('Data.db')
    # create a being that process data (go get filter etc.)
    #c = connect.cursor()
    #g.subject_list = c.execute('SELECT * from ')
    return render_template('score.html')
