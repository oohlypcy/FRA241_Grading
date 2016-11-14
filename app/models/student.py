import sqlite3
from flask import url_for

#use  inheritance idiotttttttttt
#use  inheritance idiotttttttttt
# declare class
class Student:
    # when create function
    def __init__(self, id, Subject,Subject_Id):
        # declare attribute when create
        self.Subject_Id = Subject_Id
        self.id = id
        # make a dictionary
        self.Subject = Subject
        self.Cal_grade_subject = self.Cal_grade_subject() #url_for('static',filename =)
        self.Cal_grade_ave=self.Cal_grade_ave()
        self.Get_grade_mark_by_subject =self.Get_grade_mark_by_subject()
        self.work=[]

    #def Cal_grade_subject(self):
        # connect with database
        #connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        #c = connect.cursor()
        # get table column


    #def Cal_grade_ave(self):
        # connect with database
        #connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        #c = connect.cursor()

    # use  inheritance idiotttttttttt
    def Get_grade_mark_by_subject(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        #get subject
        grade_mark_by_subject = c.execute("SELECT Subject_ID = "
                           + str(self.Subject_ID) + " grade_mark = " + str(self.Work_Id))
        grade_mark_by_subject = grade_mark_by_subject.fetchone()
        #close connection
        c.close()
        #return grading 'str'
        return str(grade_mark_by_subject[0])
        c.close()

#use  inheritance idiotttttttttt
#use  inheritance idiotttttttttt
#use  inheritance idiotttttttttt
#use  inheritance idiotttttttttt
#use  inheritance idiotttttttttt