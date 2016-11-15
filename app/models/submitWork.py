import sqlite3
import datetime
from flask import url_for


class submitWork:
    def __init__(self, Work_ID, Year, Subject_Id, ID):
        self.Subject_Id = Subject_Id
        self.Year = Year
        self.WorkID = Work_ID
        self.ID = ID
        self.submit_date = self.Get_submit_date()
        self.Mark = self.Get_Mark()
        self.Address = self.Get_address()
        self.Status = self.Get_status()

    def Get_member_list(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get user ID in same workID
        member_list = c.execute("SELECT ID from SubmitWork WHERE WorkID = "
                                + str(self.WorkID) + " AND Year = " + str(self.Year)
                                + " AND Subject_ID = " + str(self.Subject_Id))
        member_list = member_list.fetchone()
        # close connection
        c.close()
        # return id [list]
        return member_list

    def Get_deadline(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get deadline
        member_list = c.execute("SELECT Deadlines from work WHERE WorkID = "
                                + str(self.WorkID) + " AND Year = " + str(self.Year) +
                                " AND Subject_ID = " + str(self.Subject_Id))
        deadline = member_list.fetchone()
        # close connection
        c.close()
        # return deadline 'str'
        return str(deadline[0])

    def Get_Mark(self):
        # mark = []
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get mark
        mark = c.execute("SELECT Mark from SubmitWork WHERE WorkID = ? AND ID = ? AND Year = ? AND Subject_ID = ?"
                         ,(str(self.WorkID),str(self.ID) ,str(self.Year),str(self.Subject_Id)))
        mark = mark.fetchone()
        # close connection
        c.close()
        # return mark [list]
        return mark



    def Get_submit_date(self,date):
        time = datetime.datetime.now()
        date = [str(time.day),str(time.month),str(time.year)]

        #return day month year
        return date
        # return self.submit_date

    def Get_status(self):
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()
        # get status from work id &subject id
        status = c.execute(
            "SELECT status from SubmitWork WHERE WorkID = ? AND Year = ?  AND Subject_ID = ?",(str(self.WorkID),
                                                                            str(self.Year), str(self.Subject_Id)))
        status = status.fetchone()
        # close connection
        c.close()
        # return status 'str'
        return str(status[0])

    def Get_address(self):  # address
        connect = sqlite3.connect("Data.db")
        c = connect.cursor()

        # get address of work
        work_address = c.execute("SELECT Address from SubmitWork WHERE WorkID = ? AND Year = ?  AND Subject_ID = ?"
                                 ,(str(self.WorkID),str(self.Year),str(self.Subject_Id)))
        work_address = work_address.fetchone()
        # close connection
        c.close()
        # return address 'str'
        # print self.workID,self.Year,self.Subject_Id,work_address
        return work_address[0]

    def Upload(self, repository, name):  # address
        # connect = sqlite3.connect("Data.db")
        # c = connect.cursor()
        # # get address of work
        # # if change address finish > true
        # try :
        #     # change address at workid & subjectid
        #     c.execute("UPDATE User SET Address = " + str(address) + " WHERE WorkID = "+ str(self.WorkID)+
        #               " AND Subject_ID = " + str(self.Subject_Id))
        #     # close connection
        #     c.close()
        #     return True
        # # if change address finish > false
        # except Exception:
        #     # close connection
        #     c.close()
        #     return False
        pass

    def Download(self):
        # self.address
        pass
