import sqlite3

class Data:
    def __init__(self):    
        """ for make table and input manual data """
        conn = sqlite3.connect('Data.db') #connect db name Data.db
        print "Connect : pass"
        c= conn.cursor()    #prepare from modify db
    
        # create table name user
        try :
            c.executescript("""
            CREATE TABLE `User` (
              `ID` bigint(20) NOT NULL,
              `Password` varchar(45) NOT NULL,
              `Title` varchar(45) DEFAULT NULL,
              `Name` varchar(45) DEFAULT NULL,
              `Surname` varchar(45) DEFAULT NULL,
              `E-mail` varchar(45) DEFAULT NULL,
              `Role` varchar(45) DEFAULT NULL,
              `Faculty` varchar(45) DEFAULT NULL,
              `Major` varchar(45) DEFAULT NULL,
              `Enrol-Year` varchar(45) DEFAULT NULL,
              `Picture` varchar(45) DEFAULT NULL
            )""")
        except Exception:
            print "Table User has created"
    
    
        # create table name Enrol
        try :
            c.executescript("""CREATE TABLE `Enrol` (
              `ID` bigint(11) NOT NULL,
              `Subject_ID` varchar(45) NOT NULL,
              `subject_Year` int(11) NOT NULL
            )""")
        except Exception:
            print "Table Enrol has created"
    
    
        # create table name Groups
        try:
            c.executescript("""
            CREATE TABLE `Groups` (
              `Subject_ID` varchar(45) NOT NULL,
              `Year` int(11) NOT NULL,
              `WorkID` int(11) NOT NULL,
              `ID` bigint(11) NOT NULL
            )""")
        except Exception:
            print "Table Groups has created"
    
    
        # create table name media
        try :
            c.executescript("""
            CREATE TABLE `media` (
              `Subject_ID` varchar(45) NOT NULL,
              `Year` int(11) NOT NULL,
              `File_name` varchar(45) DEFAULT NULL,
              `time` varchar(45) DEFAULT NULL,
              `address` varchar(45) DEFAULT NULL,
              `ID` bigint(45) DEFAULT NULL
            )""")
        except Exception:
            print "Table media has created"
    
    
        #create table name subject
        try:
            c.executescript("""
            CREATE TABLE `subject` (
              `Subject_ID` varchar(45) NOT NULL,
              `Year` int(11) NOT NULL,
              `Description` varchar(45) DEFAULT NULL,
              `FullMark` int(11) DEFAULT NULL,
              `Grading` varchar(45) DEFAULT NULL
            )""")
        except Exception:
            print "Table Subject has created"
    
    
        #create table name Submitwork
        try:
            c.executescript("""
            CREATE TABLE `SubmitWork` (
              `Subject_ID` varchar(45) NOT NULL,
              `Year` int(11) NOT NULL,
              `WorkID` int(11) NOT NULL,
              `ID` bigint(20) NOT NULL,
              `Address` varchar(45) DEFAULT NULL,
              `Status` varchar(45) DEFAULT NULL,
              `Mark` varchar(45) DEFAULT NULL
            )""")
        except Exception:
            print "Table Submit work has created"
    
        #create table name work
        try :
            c.executescript("""
            CREATE TABLE `work` (
              `Subject_ID` varchar(45) NOT NULL,
              `Year` int(11) NOT NULL,
              `WorkID` int(11) NOT NULL,
              `Deadlines` varchar(45) DEFAULT NULL,
              `status` varchar(45) DEFAULT NULL,
              `type` varchar(45) DEFAULT NULL,
              `FullMark` varchar(45) DEFAULT NULL,
              `Grading` varchar(45) DEFAULT NULL,
              `lim_member` int(11) DEFAULT NULL
            )""")
        except Exception:
            print "Table Work has created"
        c.close()


    # insert data in User table
    def UserInsert(self,ID, Password, Title, Name, Surname, E_mail, Role, Faculty, Major, Enrol_Year, Picture): #ID and Password aren't NULL
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enrol-Year`, `Picture`) VALUES
        (?,?,?,?,?,?,?,?,?,?,?);""",(ID, Password, Title, Name, Surname, E_mail, Role, Faculty, Major, Enrol_Year, Picture))
        conn.commit()  # save data into db
        c.close()
    # insert data in Enrol table
    def EnrolInsert(self,ID,Subject_ID,Subject_Year): #not NULL all
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `Enrol` (`ID`, `Subject_ID`, `subject_Year`) VALUES
        (?, ?, ?);""",(ID,Subject_ID,Subject_Year))
        conn.commit()  # save data into db
        c.close()
    #insert data in Groups table
    def GroupInsert(self,Subject_ID,Year,WorkID,ID): #not NULL all
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `Groups` (`Subject_ID`, `Year`, `WorkID`, `ID`) VALUES
         (?,?,?,?);""",(Subject_ID,Year,WorkID,ID))
        conn.commit()  # save data into db
        c.close()
    #insert data in media table
    def mediaInsert(self,Subject_ID,Year,Description,FullMark,Grading): #Subject_ID and Year aren't NULL
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `media` (`Subject_ID`,`Year`,`Description`,`FullMark`,`Grading`) VALUES
         (?,?,?,?,?);""",(Subject_ID,Year,Description,FullMark,Grading))
        conn.commit()  # save data into db
        c.close()
    #insert data in subject table
    def subjectInsert(self,Subject_ID, Year, Description, FullMark, Grading): #Description, FullMark and Grading default are NULL
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `subject` (`Subject_ID`, `Year`, `Description`, `FullMark`, `Grading`) VALUES
        (?,?,?,?,?);""",(Subject_ID,Year,Description,FullMark,Grading))
        conn.commit()  # save data into db
        c.close()
    #insert data in Submitwork table
    def SubmitworkInsert(self,Subject_ID, Year, WorkID, ID, Address, Status, Mark): #Address, status and Mark default are NULL
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `Submitwork` (`Subject_ID`, `Year`, `WorkID`, `ID`, `Address`, `Status`, `Mark`) VALUES
        (?,?,?,?,?,?,?);""",(Subject_ID, Year, WorkID, ID, Address, Status, Mark))
        conn.commit()  # save data into db
        c.close()
    #insert data in work table
    def workInsert(self,Subject_ID, Year, WorkID, Deadlines, status, type, FullMark, Grading, lim_member): #Subject_ID, Year, WorkID aren't NULL
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute("""INSERT INTO `work` (`Subject_ID`, `Year`, `WorkID`, `Deadlines`, `status`, `type`, `FullMark`, `Grading`, `lim_member`) VALUES
        (?,?,?,?,?,?,?,?,?);""",(Subject_ID, Year, WorkID, Deadlines, status, type, FullMark, Grading, lim_member))
        conn.commit()  # save data into db
        c.close()



    # UserInsert(ID='58340500017',Password='Boomming1*',Title='Mr.',Name='Chaiyaporn',Surname='Boonyasathian',E_mail='chaiya45689@gmail.com',Role='student',Faculty='FIBO',Major='robotic and automation',Enrol_Year='58',Picture=None) #insert User
    # subjectInsert(Subject_ID='FRA222',Year='59',Description=None,FullMark=None,Grading=None) #insert subject
    # workInsert(Subject_ID='FRA221',Year='59',WorkID='6') # insert work
    # EnrolInsert('58340500017','FRA221','59')
    # GroupsInsert(Subject_ID='FRA421',Year='59',WorkID='0001',ID='58340500017') #insert Groups

    # c.executescript("""DELETE FROM Enrol WHERE ID = '58340500017'""")
    # EnrolInsert(ID='58340500005',Subject_ID='FRA241',Subject_Year='59')
    # c.executescript("""DELETE FROM subject WHERE Subject_ID='FRA241'""")
    # subjectInsert(Subject_ID='FRA241',Year='59',Description=None,FullMark='100',Grading=None)
    # workInsert(Subject_ID='FRA221',Year='59',WorkID='0001',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA221',Year='59',WorkID='0002',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA221',Year='59',WorkID='0003',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    #
    # workInsert(Subject_ID='FRA222',Year='59',WorkID='0001',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA222',Year='59',WorkID='0002',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA222',Year='59',WorkID='0003',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    #
    # workInsert(Subject_ID='FRA241',Year='59',WorkID='0001',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA241',Year='59',WorkID='0002',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    # workInsert(Subject_ID='FRA241',Year='59',WorkID='0003',Deadlines=None,status=None,type=None,FullMark=None,Grading=None,lim_member=None)
    #
    # SubmitworkInsert(Subject_ID='FRA241',Year='59',WorkID='00001',ID='58340500005',Address=None,Status=None,Mark='10')
    # SubmitworkInsert(Subject_ID='FRA241',Year='59',WorkID='00002',ID='58340500005',Address=None,Status=None,Mark='15')

    # c.execute("UPDATE User SET Picture ='Untitled.png' WHERE ID ='58340500005'")

    def edit(self,code):
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        c.execute(str(code))
        conn.commit()

        c.close()

    def show(self):
        print("-----------User-----------")
        conn = sqlite3.connect("Data.db")
        c = conn.cursor()
        cursor = c.execute("SELECT ID, Password, Title, Name, Surname, Role, Faculty, Major, Picture from User") #choose table for search data
        for row in cursor:
            print "ID = ", row[0]
            print "Password = ", row[1]
            print "Title = ", row[2]
            print "Name = ", row[3]
            print "Surname = ", row[4]
            print "Role = ", row[5]
            print "Faculty = ", row[6]
            print "Major =",row[7]
            print "Picture = ",row[8]
            print "***************"

        print("-----------Enrol-----------")
        cursor = c.execute("SELECT ID, Subject_ID, Subject_Year from Enrol")  # choose table for search data
        for row in cursor:
            print "ID = ", row[0]
            print "Subject_ID = ", row[1]
            print "Subject_Year = ", row[2]
            print "***************"

        print("-----------Groups-----------")
        cursor = c.execute("SELECT Subject_ID, Year, WorkID, ID from Groups")
        for row in cursor:
            print "Subject_ID = ", row[0]
            print "Year = ", row[1]
            print "WorkID = ", row[2]
            print "ID = ", row[3]
            print "***************"

        print("-----------media-----------")
        cursor = c.execute("SELECT Subject_ID, Year  from media")  # choose table for search data
        for row in cursor:
            print "Subject_ID = ", row[0]
            print "Year = ", row[1]
            print "***************"

        print("-----------subject-----------")
        cursor = c.execute("SELECT Subject_ID, Year, Description,FullMark, Grading from subject")
        for row in cursor:
            print "Subject ID = ",row[0]
            print "Year = ",row[1]
            print "Description = ",row[2]
            print "FullMark = ",row[3]
            print "Grading = ",row[4]
            print "***************"

        print("-----------SubmitWork-----------")
        cursor = c.execute("SELECT Subject_ID, Year, WorkID, ID, Address, Status, Mark from SubmitWork")
        for row in cursor:
            print "Subject ID = ",row[0]
            print "Year = ",row[1]
            print "WorkID = ",row[2]
            print "ID = ",row[3]
            print "Address = ",row[4]
            print "Status = ",row[5]
            print "Mark = ",row[6]
            print "***************"

        print("-----------work-----------")
        cursor = c.execute("SELECT Subject_ID, Year, WorkID, Deadlines, status, FullMark, lim_member from work")
        for row in cursor:
            print "Subject ID = ",row[0]
            print "Year = ",row[1]
            print "WorkID = ",row[2]
            print "Deadline = ",row[3]
            print "status = ", row[4]
            print "FullMark = ", row[5]
            print "lim_member = ", row[6]
            print "***************"

        print("-----------enrol-----------")
        cursor = c.execute("SELECT ID, Subject_ID, subject_year from Enrol")
        for row in cursor:
            print "ID = ",row[0]
            print "Subject ID = ",row[1]
            print "Subject year = ",row[2]
        print "***************"

        # c.executescript("""DELETE  FROM User WHERE ID = '58340500000' AND Password = 'asdf'""")  # delete data in table subject
        # c.execute("UPDATE User SET ID = '58340500000' WHERE Role ='teacher'")
        # conn.commit()
        c.close()

# c.executescript("""DROP TABLE User""") #delete table
# c.executescript("""DELETE FROM subject WHERE Subject_ID = 'FRA142'""") #delete data in table subject
# c.executescript("""DELETE FROM work WHERE Subject_ID ='FRA222'""") #delete work

a = Data()

# a.edit("DELETE FROM Enrol WHERE ID = '58340500000'")#can do all code with SQL
# a.EnrolInsert('58340500000','FRA241','59')
# a.UserInsert('wanway','password','Ms.','wanway','oneway','wanway@test.com','teacher','FIBO','robotic & automation','59','teacher1.png')
a.show()


# teacher id = '58340500000' <> password = 'password'