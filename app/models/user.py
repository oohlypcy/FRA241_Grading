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
        self.Picture = ""  # url_for('static', filename='')

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
        Profiledict = {}
        for x, y in zip(k, column):
            Profiledict[str(y)] = str(x)
        # close connection
        c.close()
        # return the dict
        return Profiledict

    def Get_subject(self):
        pass
