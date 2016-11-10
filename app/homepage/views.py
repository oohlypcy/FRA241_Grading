from flask import Flask,Blueprint, render_template,g,request,json,jsonify
import sqlite3
from app.models.user import User
# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage',__name__,url_prefix="/<url_user_id>",template_folder='',static_folder='')

#still figuring it
@Homepage.url_value_preprocessor
def user_id(endpoint,url_user_id):
    # from what i test url_user_id is a dictionary containing 'url_user_id' key with id value
    print url_user_id['url_user_id']
    g.id = url_user_id['url_user_id']
    g.user = User(g.id)
    connect = sqlite3.connect('Data.db')
    # create a being that process data (go get filter etc.)
    c = connect.cursor()
    # get table column
    tableField = c.execute("PRAGMA table_info(User)")
    tableField = tableField.fetchall()
    g.show_list = []
    g.picture = ""
    for x in tableField:
        if str(x[1]) == "Picture" :
            g.picture = 'picture.jpg'
        elif  str(x[1]) == "Password" :
            pass
        else:
            g.show_list.append(str(x[1]))
    c.close()
    connect= sqlite3.connect('Data.db')
    d = connect.cursor()
    wiz = d.execute("SELECT * from Enrol WHERE ID =" + str(g.id) +" AND subject_Year = 59")
    liz=wiz.fetchone()
    print(liz)
    wiz = d.execute("SELECT * from Enrol WHERE ID =" + str(g.id) +" AND subject_Year = 59")
    liz=wiz.fetchall()
    print(liz)

#Homepage route
@Homepage.route('/Home')
def Home(url_user_id):
    return render_template("template.html")

#see current subject route
@Homepage.route('/Subject')
def CurrentSubject(url_user_id):
    return "boo"

@Homepage.route('/Work')
def CurrentWork(url_user_id):
    return render_template("HTML_assignment.html")

@Homepage.route('/Score')
def CurrentScore(url_user_id):
    return "boo"