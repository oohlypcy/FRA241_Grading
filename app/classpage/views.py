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
    print g.subjectwork
    # sent work data to html
    return render_template("HTML_assignment1.html")


@classpage.route('/Score')
def Subject_Score(url_Subject_id, url_Year,url_user_id):



    return render_template("Score.html")

@classpage.route('/<work_id>/score')
def Subject_work_score(url_Subject_id, url_Year,url_user_id,work_id):
    connect = sqlite3.connect('Data.db')
    g.id = url_user_id
    c= connect.cursor()
    g.user = User(url_user_id)
    if g.user.Profile['Role']=='student':
        ID_student = c.execute("SELECT ID from Enrol WHERE  Subject_ID =  ? AND Subject_Year = ?",(url_Subject_id,url_Year))
        g.student1 = []
        g.student2 = []
        g.student3 = []
        g.single_score = []
        ID_student1 = ID_student.fetchall()
        for row in ID_student1:
            NAME_student = c.execute("SELECT ID,Name from User WHERE  ID =" + str(row[0]))
            NAME_student = NAME_student.fetchall()
            print NAME_student
            single_score_student = c.execute("SELECT Mark from SubMitWork WHERE  ID = ? AND Subject_ID = ?",(str(row[0]),url_Subject_id) )
            single_score_student = single_score_student.fetchall()

            # ID_student = ID_student.fetchall()
            g.single_score.append(str(single_score_student[0][0]))
            g.student1.append(str(NAME_student[0][1]))
            g.student2.append(str(row[0]))
        g.a = range(len(g.student2))
        c.close()
        return render_template("score1.html")
    else:
        return 'boo'