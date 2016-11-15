from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User
from app.models.submitWork import  submitWork


from app.models.subject import Subject

# create Blueprint class with name importname Blueprintfolders
classpage = Blueprint('classpage', __name__, url_prefix="/<url_user_id>/<url_Subject_id>/<url_Year>",
                      template_folder='', static_folder='')


@classpage.url_value_preprocessor
def class_process(endpoint, url_Subject_id):
    g.id = url_Subject_id['url_user_id']
    g.Subject_id = url_Subject_id['url_Subject_id']
    g.Year = url_Subject_id['url_Year']


@classpage.route('/')
def Subjects(url_Subject_id, url_Year,url_user_id):
    return render_template('sub-1.html')


@classpage.route('/work')
def Subject_work(url_Subject_id, url_Year,url_user_id):

    g.user = User(url_user_id)
    g.subject = Subject(url_Subject_id, url_Year)
    g.subjectwork = g.subject.get_work()

    # sent work data to html
    g.work = []
    g.address = []
    g.status = []
    for work in g.subjectwork:
        # check work from submit work
        try:
            k = submitWork(work[2], g.subject.Year, g.subject.Subject_Id, g.user.id)
            g.address.append(k.Address)
            g.status.append("send")
        # work doesn't submit
        except Exception:
            g.address.append(None)
            g.status.append("not send")
    g.lenght = range(len(g.subjectwork))
    print g.address
    print g.subjectwork

    return render_template("HTML_assignment.html")


@classpage.route('/Score')
def Subject_Score(url_Subject_id, url_Year,url_user_id):



    return render_template("Score.html")

@classpage.route('/<work_id>/score')
def Subject_work_score(url_Subject_id, url_Year,url_user_id,work_id):
    return 'boo'
