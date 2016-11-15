from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User
from app.models.subject import Subject
from app.models.submitWork import submitWork
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
    g.id = url_user_id
    g.user = User(g.id)
    g.subject_list = g.user.Subject['current']
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
    g.subject = sorted(g.subject)
    #sent work data to html
    g.work = []
    g.address = []
    g.status = []
    for subject in g.subject:
        data =[]
        for work in subject.get_work():
            # check work from submit work
            try :
                k = submitWork(work[2], year, work[0], g.user.id)
                g.address.append(k.Address)
                g.status.append("send")
            # work doesn't submit
            except Exception:
                g.address.append(None)
                g.status.append("not send")
            g.work.append(work)


    g.lenght = range(len(g.work))

    return render_template("HTML_assignment.html")


@Homepage.route('/Score')
def CurrentScore(url_user_id):
    year = datetime.date.today()
    if year.month <= 4:
        year = int(str(year.year + 542)[2:4])
    else:
        year = int(str(year.year + 543)[2:4])

    g.id = url_user_id
    g.user = User(g.id)
    #get subject
    g.subject = []
    g.work = []
    g.subject_list = g.user.Subject['current']
    g.subject_list=sorted(g.subject_list)
    for subject in g.subject_list :
        # g.subject.append(subject.get_work())
        for work in subject.get_work():
            if work[0] not in g.subject:
                # get subject id 1 time / 1 subject
                g.subject.append(work[0])
            try:
                position = work[2]
                workID = work[0]
                work = submitWork(work[2],year,work[0],g.id )
                g.work.append([workID,position,work.Get_Mark()])
            except Exception:
                g.work.append([workID,position,None])

    #create a being that process data (go get filter etc.)
    return render_template('Score.html')
