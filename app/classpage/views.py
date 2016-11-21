from flask import Flask, Blueprint, render_template, g, request, json, jsonify
import sqlite3
from app.models.user import User
from app.models.submitWork import  submitWork
from app.models.work import Work

from app.models.subject import Subject

# create Blueprint class with name importname Blueprintfolders
classpage = Blueprint('classpage', __name__, url_prefix="/<url_user_id>/<url_Subject_id>/<url_Year>",
                      template_folder='', static_folder='')


@classpage.url_value_preprocessor
def class_process(endpoint, url_Subject_id):
    g.id = url_Subject_id['url_user_id']
    g.Subject_id = url_Subject_id['url_Subject_id']
    g.Year = url_Subject_id['url_Year']
    g.user = User(g.id)
    g.work = Work()

@classpage.route('/')
def Subjects(url_Subject_id, url_Year,url_user_id):
    return render_template('sub-1.html')


@classpage.route('/work')
def Subject_work(url_Subject_id, url_Year,url_user_id):
    g.user = User(url_user_id)
    g.subject = Subject(url_Subject_id, url_Year)
    g.subjectwork = g.subject.get_work()
    # sent work data to html
    return render_template("HTML_assignment1.html")


@classpage.route('/Score')
def Subject_Score(url_Subject_id, url_Year,url_user_id):
    g.SubjectID = url_Subject_id
    g.year = url_Year
    g.UserID = url_user_id
    g.user = User(g.UserID)
    subject = Subject(g.SubjectID, g.year)
    subjectWork = subject.get_work()
    g.work = []
    g.all_user_ID = []
    if g.user.Profile['Role'] == 'teacher':
        g.workID = []
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        all_user_ID = c.execute("SELECT ID FROM Enrol WHERE Subject_ID = ? AND  subject_Year = ?",
                                (g.SubjectID, g.year))
        all_user_ID = all_user_ID.fetchall()
        for x in all_user_ID:
            if str(x[0]) != str(g.UserID):
                g.all_user_ID.append(x[0])
        c.close()
        for x in subjectWork:
            for selectUser in g.all_user_ID:
                submitwork = submitWork(x[2], g.year, g.SubjectID, selectUser)
                work = Work(g.SubjectID, g.year, x[2])
                g.work.append([selectUser, x[2], submitwork.Mark, work.Fullmark])
                if [x[2], work.Fullmark] not in g.workID:
                    g.workID.append([x[2], work.Fullmark])

        return render_template("Score2.html")

    else:
        for x in subjectWork:
            submitwork = submitWork(x[2], g.year, g.SubjectID, g.UserID)
            work = Work(g.SubjectID, g.year, x[2])
            g.work.append([x[2], submitwork.Mark, work.Fullmark])
        return render_template("Score2.html")

@classpage.route('/<work_id>/score')
def Subject_work_score(url_Subject_id, url_Year,url_user_id,work_id):
    g.work_id=work_id
    connect = sqlite3.connect('Data.db')
    g.id = url_user_id
    c= connect.cursor()
    g.user = User(url_user_id)
    g.Subject_id = url_Subject_id
    g.Year = url_Year
    if g.user.Profile['Role']=='teacher':
        ID_student = c.execute("SELECT ID from Enrol WHERE  Subject_ID =  ? AND Subject_Year = ?",(url_Subject_id,url_Year))
        g.student1 = []
        g.student2 = []
        g.student3 = []
        g.single_score = []
        g.group_user = []
        ID_student1 = ID_student.fetchall()
        #find group_limit
        group_limit = c.execute("SELECT lim_member from Work WHERE Subject_ID =  ? AND Year = ? AND WorkID = ?",(url_Subject_id,url_Year,g.work_id))
        g.group_limit = group_limit.fetchone()[0]
        for row in ID_student1:

            sudent = User(str(row[0]))

            if sudent.Profile['Role'] == 'student':
                NAME_student = c.execute("SELECT ID,Name from User WHERE  ID =" + str(row[0]))
                NAME_student = NAME_student.fetchall()
                # non group work
                single_score_student = c.execute("SELECT Mark from SubMitWork WHERE  ID = ? AND Subject_ID = ?",
                                             (str(row[0]), url_Subject_id))
                single_score_student = single_score_student.fetchall()
                # ID_student = ID_student.fetchall()
                try :
                    g.single_score.append(str(single_score_student[0][0]))
                except Exception:
                    g.single_score.append(None)
                g.student1.append(str(NAME_student[0][1]))
                g.student2.append(str(row[0]))

                #group work
                g.group_user.append(g.work_id)
                group_ID_student = c.execute("SELECT ID from Groups WHERE ID = ? AND Subject_ID = ? AND Year = ? AND WorkID = ?",(str(row[0]),g.Subject_id,g.Year,g.work_id))
                group_ID_student = group_ID_student.fetchone()
                try :
                    g.group_user[g.work_id].append(str(group_ID_student[0]))
                except :
                    pass

        print g.group_user

        g.a = range(len(g.student2))

        c.close()


        return render_template("score1.html",std2=map(json.dumps, g.student2))
    else:
        g.score = c.execute("SELECT * from SubmitWork WHERE  Subject_ID =  ? AND Year = ? AND ID = ? AND WorkID = ?",
                            (url_Subject_id, url_Year, url_user_id, work_id))
        g.score = g.score.fetchone()
        if g.score != None:
            g.score=g.score[6]
        return render_template("score1.html")

@classpage.route('/insert_mark')
def insert_mark(url_Subject_id, url_Year,url_user_id):
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form = request.values.get('id')
    score_from_form = request.values.get('score')
    subject_id_from_form = url_Subject_id
    year_from_form = url_Year
    work_id_from_form = request.values.get('work_id')
    fullMark = Work(subject_id_from_form,year_from_form,work_id_from_form)
    submit = c.execute("SELECT Status FROM SubmitWork WHERE Subject_ID = ? AND Year = ? AND WorkID = ? AND ID = ?",(subject_id_from_form,year_from_form,work_id_from_form,id_from_form))
    submit = submit.fetchone()
    print submit
    if int(score_from_form) <= int(fullMark.Fullmark):
        if submit != None:
            c.execute("UPDATE SubmitWork SET Mark = ? WHERE Subject_ID = ? AND Year = ? AND ID = ? AND WorkID = ? ",
                    (score_from_form, subject_id_from_form, year_from_form, id_from_form, work_id_from_form))
        else:

            c.execute("""INSERT INTO `SubmitWork` (`Subject_ID`, `Year`, `WorkID`, `ID`, `Address`, `Status`, `Mark`) VALUES
                   (?,?,?,?,?,?,?);""", (subject_id_from_form, year_from_form, work_id_from_form, id_from_form, 'http://google.com', 'sent', score_from_form))

    conn.commit()
    c.close()
    return jsonify(authen=True)
