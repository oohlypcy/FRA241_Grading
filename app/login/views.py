from flask import Flask, Blueprint, render_template, jsonify, json, request
import sqlite3

# create Blueprint class with name importname Blueprintfolders
Login = Blueprint('login', __name__, template_folder='', static_folder='')


# declare url route
@Login.route('/login')
# what we do in this route
def login():
    return render_template('login_from_w3.html')


@Login.route('/background_process')
def background_process():
    # import username and password from Data.db
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form = request.values.get('name')
    password_from_form = request.values.get('pass')
    cursor1 = c.execute("SELECT ID, Password from User WHERE ID=" + str(id_from_form))
    a = cursor1.fetchone()
    c.close()
    if (str(a[0]) == str(id_from_form) and str(a[1]) == str(password_from_form)):
        return jsonify(authen=True)
    else:
        return jsonify(authen=False)


# ID = []
#    Password = []
#    for row in cursor:
#        ID.append(str(row[0]))
#        Password.append(str(row[1]))
#   return jsonify(id = ID,password = Password) #send sudo json file with id & password(don't create new files)

@Login.route('/insert_mark')
def insert_mark():
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form = request.values.get('id')
    score_from_form = request.values.get('score')
    subject_id_from_form = request.values.get('subject_id')
    year_from_form = request.values.get('year')
    work_id_from_form = request.values.get('work_id')
    c.execute("UPDATE SubmitWork SET Mark = ? WHERE Subject_ID = ? AND Year = ? AND ID = ? AND WorkID = ? ",
              (score_from_form, subject_id_from_form, year_from_form, id_from_form, work_id_from_form))
    return jsonify(authen=True)