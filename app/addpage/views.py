from flask import Flask, Blueprint, render_template, g, request, json, jsonify, url_for
import sqlite3
from app.models.user import User
from app.models.subject import Subject
from app.models.submitWork import submitWork
from app.models.work import Work
from app.DataEditor import Data
import datetime

# create Blueprint class with name importname Blueprintfolders
Addpage = Blueprint('Addpage', __name__, url_prefix="/<url_user_id>", template_folder='', static_folder='')


@Addpage.url_value_preprocessor
def addpage(endpoint, url_user_id):
    g.id = url_user_id['url_user_id']
    g.user = User(url_user_id['url_user_id'])


@Addpage.route('/<url_Subject_id>/<url_Year>/add_work')
def add_assignment(url_user_id, url_Subject_id, url_Year):
    return 'boo'


@Addpage.route('/add_subject')
def add_subject(url_user_id):
    return render_template('teacher_add_subject.html')


@Addpage.route('/<url_Subject_id>/<url_Year>/add_student')
def add_student(url_user_id, url_Subject_id, url_Year):
    g.year = url_Year
    g.subject_id = url_Subject_id
    g.id = url_user_id
    conn = sqlite3.connect('Data.db')
    g.current = 'student'
    currentAcademicYear = datetime.date.today()
    if currentAcademicYear.month <= 4:
        currentAcademicYear = currentAcademicYear.year + 542
    else:
        currentAcademicYear = currentAcademicYear.year + 543
    g.YEAR = [x + currentAcademicYear for x in range(0, 3)]
    print g.YEAR
    currentAcademicYear = str(int(str(currentAcademicYear)[2:4]))
    c = conn.cursor()
    subject_list = c.execute("SELECT Subject_ID from subject WHERE  Year =  ? ", (currentAcademicYear,))
    g.subject_list = subject_list.fetchall()
    people = c.execute("SELECT ID from Enrol WHERE subject_Year =  ? AND Subject_ID = ? AND Enrol_Type = ? ",
                       (g.year, g.subject_id, 'student')).fetchall()
    g.people = [int(x[0]) for x in people]
    print people
    c.close()
    print g.subject_list
    return render_template('teacher_add_TA.html')


@Addpage.route('/<url_Subject_id>/<url_Year>/add_TA')
def add_TA(url_user_id, url_Subject_id, url_Year):
    g.year = url_Year
    g.subject_id = url_Subject_id
    g.id = url_user_id
    g.current = 'TA'
    conn = sqlite3.connect('Data.db')
    currentAcademicYear = datetime.date.today()
    if currentAcademicYear.month <= 4:
        currentAcademicYear = currentAcademicYear.year + 542
    else:
        currentAcademicYear = currentAcademicYear.year + 543
    g.YEAR = [x + currentAcademicYear for x in range(0, 3)]
    print g.YEAR
    currentAcademicYear = str(int(str(currentAcademicYear)[2:4]))
    c = conn.cursor()
    subject_list = c.execute("SELECT Subject_ID from subject WHERE  Year =  ? ", (currentAcademicYear,))
    g.subject_list = subject_list.fetchall()
    people = c.execute("SELECT ID from Enrol WHERE subject_Year = ? AND Subject_ID = ? AND Enrol_Type = ? ",
                       (g.year, g.subject_id, 'teacher')).fetchall()
    print people
    g.people = [int(x[0]) for x in people]
    print people
    c.close()
    print g.subject_list
    return render_template('teacher_add_TA.html')


@Addpage.route('/add_works')
def add_works(url_user_id):
    subject = User(url_user_id)
    subject_sub = subject.Subject['current']
    subject_id = []
    for x in subject_sub:
        subject_id.append(x.Subject_Id)
    g.math = len(subject_id)
    g.subject_id =  subject_id
    return render_template('teacher_add_works.html')

@Addpage.route('/sub_add_works')
def sub_add_works(url_user_id, url_Subject_id, url_Year):
    subsubject_from_form = request.values.get('subsubject')
    subtypework_from_form = request.values.get('subtypework')
    subgroup_from_form = request.values.get('subgroup')
    subdetail_from_form = request.values.get('subdetail')
    subdate_from_form = request.values.get('subdate')
    subtime_from_form = request.values.get('subtime')
    return render_template('teacher_add_works.html')

@Addpage.route('/<url_Subject_id>/<url_Year>/<work_id>/manage_group')
def manage_group(url_user_id, url_Subject_id, url_Year, work_id):
    g.user = User(url_user_id)
    if g.user.Profile['Role'] == 'student':
        return render_template('student_grouping.html')
    else:
        return render_template('grouping.html')


@Addpage.route('/Add_subject_db')
def Add_subject_db(url_user_id):
    Subjectid_from_form = request.values.get('subcode')
    Subject_name_from_form = request.values.get('subname')
    Subject_detial_from_form = request.values.get('subdetial')
    grading_from_form = request.values.get('subref')
    sec_from_form = request.values.get('section')
    year_from_form = request.values.get('year')
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    a = c.execute("SELECT * from subject WHERE Subject_ID = ? AND Year = ?",(str(Subjectid_from_form), str(year_from_form[2:4])))
    a = a.fetchone()
    if a==None:
        c.execute("""INSERT INTO 'subject' (`Subject_ID`, `Year`, `Description`, `FullMark`, `Grading` , `Name` ) VALUES
        (?,?,?,?,?,?);""",(Subjectid_from_form,year_from_form,Subject_detial_from_form,'100',grading_from_form,Subject_name_from_form))
        c.execute("""INSERT INTO 'Enrol' (`ID`, `Subject_ID`, `subject_Year`,`Enrol_Type`,`SECTION`) VALUES
        (?, ?, ?, ?, ?);""", (
            url_user_id, Subjectid_from_form, year_from_form, 'teacher',None))
        conn.commit()
        c.close()
        return jsonify(authen=True)
    else:
        return jsonify(authen=False)


@Addpage.route('/get_TA')
def get_TA(url_user_id):
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    return jsonify(authen=True)


@Addpage.route('/<url_Subject_id>/<url_Year>/delpeople')
def removeperson(url_user_id, url_Subject_id, url_Year):
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form = request.values.get('id')
    print id_from_form
    k = c.execute("SELECT * from Enrol WHERE ID = ? AND Subject_ID = ? AND subject_Year = ?",
                  (id_from_form, url_Subject_id, url_Year))
    if k.fetchone() != None:
        c.execute("""DELETE FROM Enrol WHERE ID = ? AND Subject_ID = ? AND subject_Year = ?""",(id_from_form, url_Subject_id, url_Year))
        conn.commit()
        c.close()
        conn.close()
        return jsonify(authen=True)
    else:
        return jsonify(authen=False)


@Addpage.route('/<url_Subject_id>/<url_Year>/addpeople')
def addperson(url_user_id, url_Subject_id, url_Year):
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form = request.values.get('id')
    from_from_form = request.values.get('from')
    if from_from_form == 'TA':
        z='teacher'
    else:
        z='student'
    print id_from_form
    print from_from_form
    k=c.execute("SELECT * from Enrol WHERE ID = ? AND Subject_ID = ? AND subject_Year = ?",(id_from_form,url_Subject_id,url_Year))
    h=c.execute("SELECT * from User WHERE ID = "+str(id_from_form)).fetchone()
    if h==None:
        return jsonify(authen=False)
    if k.fetchone() == None:
        c.execute("""INSERT INTO 'Enrol' (`ID`, `Subject_ID`, `subject_Year`,`Enrol_Type`,`SECTION`) VALUES
                (?, ?, ?, ?, ?);""", (
            id_from_form, url_Subject_id, url_Year, z,
            'A'))
        conn.commit()
        c.close()
        conn.close()
        return jsonify(authen=True)
    else:
        return jsonify(authen=False)
