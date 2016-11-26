from flask import Flask, Blueprint, render_template, g, request, json, jsonify, url_for
import sqlite3
from app.models.user import User
from app.models.subject import Subject
from app.models.submitWork import submitWork
from app.models.work import Work
import datetime
from operator import itemgetter

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
    lecturer = []
    g.lecturer = []
    g.data = []
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    g.subject_list = g.user.Subject['current']
    for i in g.subject_list:
        c.execute("SELECT ID, Subject_ID from Enrol WHERE Subject_ID = ? AND Subject_Year = ? AND Enrol_Type = 'teacher' ",(i.data['Subject_ID'],i.data['Year']))
        lecturer.append(c.fetchall())
        c.execute("SELECT WorkID from work WHERE Year = ? AND Subject_ID = ? ",(i.data['Year'],i.data['Subject_ID']))
        g.data.append([len(c.fetchall()),i.data['Subject_ID']])

    for i in lecturer:
        user = User(i[0][0])
        user = user.Profile['Title'] + user.Profile['Name'] + " " + user.Profile['Surname']
        g.lecturer.append([user,i[0][1]])


    return render_template('sub.html')


@Homepage.route('/Work')
def CurrentWork(url_user_id):
    year = datetime.date.today()
    if year.month <= 4:
        Year = int(str(year.year + 542)[0:4])
    else:
        Year = int(str(year.year + 543)[0:4])
    # year.time

    g.user = User(url_user_id)
    g.subject = g.user.Subject['current']
    g.subject = sorted(g.subject)
    # sent work data to html
    g.work = []
    g.address = []
    g.status = []
    for subject in g.subject:
        data = []
        for work in sorted(subject.get_work(), key=itemgetter(2)):
            # check work from submit work
            try:
                # k = submitWork(work[2], year, work[0], g.user.id)
                g.address.append(str(
                    url_for('classpage.Subject_work_score', url_Subject_id=work[0], url_Year=Year, work_id=work[2],
                            url_user_id=g.user.id)))
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
        year = int(str(year.year + 542)[0:4])
    else:
        year = int(str(year.year + 543)[0:4])

    g.id = url_user_id
    g.user = User(g.id)
    # get subject
    g.subject = []
    g.work = []
    g.fullmark = []
    g.subject_list = g.user.Subject['current']
    g.subject_list = sorted(g.subject_list)
    g.total_mark = []
    for subject in g.subject_list:
        total = 0
        full_total = 0
        # g.subject.append(subject.get_work())
        for work in sorted(subject.get_work(), key=itemgetter(2)):
            fullmark = Work(work[0], year, work[2])
            if work[0] not in g.subject:
                # get subject id 1 time / 1 subject
                g.subject.append(work[0])
            try:
                position = work[2]
                workID = work[0]
                work = submitWork(work[2], year, work[0], g.id)
                total = total + int(work.Get_Mark()[0])
                g.work.append([workID, position, work.Get_Mark(), fullmark.Get_fullmark()])
            except Exception:
                g.work.append([workID, position, [0,], fullmark.Get_fullmark()])
                total = total + 0
            full_total = full_total + fullmark.Get_fullmark()
        g.total_mark.append([subject.Subject_Id, int(total), int(full_total)])
    # create a being that process data (go get filter etc.)
    g.subject = sorted(g.subject)
    return render_template('Score.html')
