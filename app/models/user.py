import sqlite3
from flask import url_for


# declare class
class User:
    # when create function
    def __init__(self, id):
        # declare attribute when create
        self.id = id
        # make a dictionary
        self.Profile = self.Get_profile()
        self.Subject = ""
        self.Picture = self.Get_picture() #url_for('static',filename =)

    def Get_profile(self):
        # connect with database
        connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        c = connect.cursor()
        # get table column
        tableField = c.execute("PRAGMA table_info(User)")
        tableField = tableField.fetchall()
        column = []
        for x in tableField:
            column.append(str(x[1]))
        # get profile data
        mydata = c.execute("SELECT * from User WHERE ID =" + str(self.id))
        k = mydata.fetchone()
        # make it into dict
        Profiledict = {'name':str(k[2])+str(k[3])+" "+str(k[4])}
        for x, y in zip(k, column):
            Profiledict[str(y)] = str(x)
        # close connection
        c.close()
        # return the dict
        return Profiledict

    def Get_picture(self):
        # connect with database
        connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        c = connect.cursor()
        cursor = c.execute("SELECT ID, Picture from User WHERE ID="+str(self.id))
        cursor = cursor.fetchone()
        c.close()
        if cursor[1]!='':
            return url_for('static',filename=str(cursor[1]))
        else:
            return url_for('static',filename='default1.jpg')


    def Get_subject(self):
        connect = sqlite3.connect('Data.db')
        c= connect.cursor()
        cursor = c.execute("SELECT Year from subject WHERE ID = "+str(self.id))
        cursor = cursor.fetchone()

        c.close()

