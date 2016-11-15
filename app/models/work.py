import sqlite3
from flask import url_for
from app.models.submitWork import submitWork


# declare class
class Work:
    # when create function
    def __init__(self, Subject_ID, year, Work_ID):
        # declare attribute when create
        self.Subject_ID = Subject_ID
        self.year = year
        self.Work_Id = Work_ID
        self.Type = ""
        self.Date_check = ""
        self.status=self.Get_status()
        self.submit_work = self.Get_submit_work()
        self.Deadline = self.Get_deadline()
        self.Fullmark = self.Get_fullmark()
        self.grad = self.Get_grad()

    def Get_deadline(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get deadline
        member_list = c.execute("SELECT Deadlines from work WHERE WorkID = ?  AND Year = ?  AND Subject_ID = ? ",
                                (str(self.Work_Id),str(self.year),str(self.Subject_ID)))
        deadline = member_list.fetchone()
        # close connection
        c.close()
        # return deadline 'str'
        return str(deadline[0])

    def Get_fullmark(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get fullmark
        fullmark = c.execute("SELECT FullMark from work WHERE Subject_ID = ? AND Year = ? AND WorkID = ?"
                             ,(str(self.Subject_ID),str(self.year),str(self.Work_Id)))
        fullmark = fullmark.fetchone()
        # close connection
        c.close()
        # return fullmark of work 'int'
        return int(fullmark[0])

    def Get_status(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get status
        status = c.execute("SELECT status from work WHERE Subject_ID = ? AND Year = ? AND WorkID = ? ",
                           (str(self.Subject_ID),str(self.year),str(self.Work_Id)))
        status = status.fetchone()
        # close connection
        c.close()
        # return status 'str'
        return str(status[0])

    def Get_submit_work(self):
        # connect = sqlite3.connect("Data.db")
        # c = connect.cursor()
        # # get submit work
        # # failed
        # submit_work = c.execute("SELECT .. from SubmitWork WHERE Subject_ID = "
        #                         + str(self.Subject_ID) + "AND Year = " + str(self.year) +
        #                         "AND WorkID = " + str(self.Work_Id))
        # Submit_Work = {}
        # for x in submit_work.fetchall():
        #     Submit_Work[str(x[3])] = submitWork(self.Work_Id, self.Subject_ID, self.year, str(x[3]))
        # # close connection
        # c.close()
        # # return status [list]
        # return submit_work
        pass

    def Get_grad(self):
        # connect = sqlite3.connect("Data.db")
        # c = connect.cursor()
        # # get grad
        # grad = c.execute("SELECT Garding from work WHERE Subject_ID = ? AND Year = ? AND WorkID = ?"
        #                  ,(str(self.Subject_ID),str(self.year),str(self.Work_Id)))
        # grad = grad.fetchone()
        # # close connection
        # c.close()
        # # return grad 'str'
        # return str(grad[0])
        pass
    def Mark_decending(self):
        # get mark as key then use sortbykey u canuse map lambda whatever
        pass
