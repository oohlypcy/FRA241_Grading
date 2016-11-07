from flask import Flask,Blueprint, render_template, jsonify, json,request
import sqlite3

# create Blueprint class with name importname Blueprintfolders
Login = Blueprint('login',__name__,template_folder='',static_folder='')




#declare url route
@Login.route('/login')
# what we do in this route
def login():
    return render_template('login_from_w3.html')


@Login.route('/background_process')
def background_process():
    # import username and password from Data.db
    conn = sqlite3.connect('Data.db')  # connect Data.db
    c = conn.cursor()
    id_from_form=request.values.get('name')
    print id_from_form
    password_from_form=request.values.get('pass')
    print password_from_form
    cursor1 = c.execute("SELECT ID, Password from User WHERE ID="+str(id_from_form))
    a =cursor1.fetchone()

    if(str(a[0])==str(id_from_form) and str(a[1])==str(password_from_form) ):
        print 1
        return jsonify(authen=True)
    else:
        print 2
        return jsonify(authen=False)
#    ID = []
#    Password = []
#    for row in cursor:
#        ID.append(str(row[0]))
#        Password.append(str(row[1]))
#   return jsonify(id = ID,password = Password) #send sudo json file with id & password(don't create new files)
    

