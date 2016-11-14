import sqlite3
from flask import url_for
from flask import url_for,g,Blueprint,render_template
# declare class
class Subject:
    # when create function
    def __init__(self,Subject_Id,Work,Id,Subject,Work_Id):
        # declare attribute when create
        self.Subject_Id = Subject_Id
        self.Work=Work
        # make a dictionary
        self.Id = Id
        self.Subject = Subject
        self.Work_Id = Work_Id
        self.mean=self.Cal_mean()
        self.grade_mark_by_subject=self.Get_grade_mark_by_subject()
        self.mark=self.Assign_mark()
        self.TA=self.Assign_TA()
        self.work_status=self.Assign_work_status()
        self.student_profile=self.View_student_profile()

    def Cal_mean(self):

        #connect = sqlite3.connect('Data.db')
        #c = connect.cursor()
        #all_score = c.execute("Select student_ID =")
        #all_student = Stusent_ID
        #mean = all_score/all_student

    def Get_grade_mark_by_subject(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        #get subject
        grade_mark_by_subject = c.execute("SELECT Subject_Id = "
                           + str(self.Subject_Id) + " grade_mark = " + str(self.Work_Id))
        grade_mark_by_subject = grade_mark_by_subject.fetchone()
        #close connection
        c.close()
        #return grading 'str'
        return str(grade_mark_by_subject[0])

    def Assign_mark(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        #get subject
        self.Mark = input(" Assign_mark_here :")
        Assign_mark = c.execute("SELECT Subject = "
                           + str(self.Subject) + "SELECT Student_Id = "
                           + str(self.Student_Id) + " Work = " + str(self.Work)+ "Mark ="(self.Mark))
        Assign_mark = Assign_mark.fetchone()

        #close connection
        c.close()
        #return grading 'str'
        return float(Assign_mark[0])

    def Assign_TA(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        #get subject
        self.TA = input(" Assign_TA_here :")
        Assign_TA = c.execute("SELECT Subject = "
                           + str(self.Subject)+  "SELECT Student_Id = "
                           + str(self.Student_Id) + "TA ="(self.TA))
        Assign_TA = Assign_TA.fetchone()

        #close connection
        c.close()
        #return grading 'str'
        return str(Assign_TA[0])

    def Assign_work_status(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        #get subject
        print("Work_status\n")
        print("input 1 = send\n")
        print("input 0 = Doesn't send\n")
        print("input 2 = Over time send\n")
        self.work_status = input(" Assign_work_status_here :")
        if(self.work_status == 1):
            self.status = str("finish")
        elif (self.work_status == 0):
            self.status = str("Doesn't send")
        elif (self.work_status == 2):
            self.status = str("Over time send")
        else:
            print("Please input 0,1 and 2")

        Assign_work_status = c.execute("SELECT Subject_Id = "
                           + str(self.Subject_Id) + "Work_status ="(self.status))
        Assign_work_status = Assign_work_status.fetchone()

        #close connection
        c.close()
        #return grading 'str'
        return str(Assign_work_status[0])


