import sqlite3
from flask import url_for,g,Blueprint,render_template
score = Blueprint('score',__name__,url_prefix="/<url_user_id_>",template_folder='',static_folder='')

conn=sqlite3.connect('Data.db')
c=conn.cursor()

@score.url_value_preprocessor
def user_id2(endpoint,url_user_id_):
    ID_student = c.execute("SELECT ID from Enrol WHERE  Subject_ID =  'FRA222' AND Subject_Year = '59'")
    g.student1=[]
    g.student2=[]
    ID_student1 = ID_student.fetchall()

    print ID_student1
    for row in ID_student1:
        NAME_student = c.execute("SELECT ID,Name from User WHERE  ID ="+str(row[0]))
        NAME_student =  NAME_student.fetchall()
        print NAME_student
        #ID_student = ID_student.fetchall()
        g.student1.append(str(NAME_student[0][1]))
        g.student2.append(str(row[0]))
    g.a=range(len(g.student2))
    g.ig=url_user_id_['url_user_id_']
#score route
@score.route('/rScore')
def scores(url_user_id_):
    return render_template("score2.html")

