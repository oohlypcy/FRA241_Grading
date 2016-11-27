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
    print id_from_form
    print password_from_form
    cursor1 = c.execute("SELECT ID, Password from User WHERE ID=" + str(id_from_form))
    a = cursor1.fetchone()
    c.close()
    if (str(a[0]) == str(id_from_form) and str(a[1]) == str(password_from_form)):
        return jsonify(authen=True)
    else:
        return jsonify(authen=False)

@Login.route('/register')
def register():

    return render_template('add_user.html')

@Login.route('/register_process')
def register_process():
    #ID ,Password,Title,Name,Surname,E-mail,Role,Faculty,Major,Enrol-Year, Picture
    ID = request.values.get('ID')
    Password = request.values.get('Password')
    Title = request.values.get('Title')
    Name = request.values.get('Name')
    Surname = request.values.get('Surname')
    Email = request.values.get('Email')
    Role = request.values.get('Role')
    Faculty = request.values.get('Faculty')
    Major = request.values.get('Major')
    enrol = request.values.get('Enrolyear')
    Picture = request.values.get('Picture')
    key = request.values.get('Key')
    connect = sqlite3.connect("Data.db")
    c = connect.cursor()
    print "check0"
    print Title
    print key
    print Name
    print Role
    if (Role == "teacher" and key == 'access'):
        c.execute("""INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enrol-Year`, `Picture`) VALUES
                (?,?,?,?,?,?,?,?,?,?,?);""",
                  (ID, Password, Title, Name, Surname, Email, Role, Faculty, Major, enrol, Picture))
        print "check1"
        connect.commit()
        c.close()
        return jsonify(authen=True)
    elif Role == "student":
        c.execute("""INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enrol-Year`, `Picture`) VALUES
                        (?,?,?,?,?,?,?,?,?,?,?);""",
                  (ID, Password, Title, Name, Surname, Email, Role, Faculty, Major, enrol, Picture))
        print "check2"
        connect.commit()
        c.close()
        return jsonify(authen = True)
    else :
        return jsonify(authen = False)
# ID = []
#    Password = []
#    for row in cursor:
#        ID.append(str(row[0]))
#        Password.append(str(row[1]))
#   return jsonify(id = ID,password = Password) #send sudo json file with id & password(don't create new files)




