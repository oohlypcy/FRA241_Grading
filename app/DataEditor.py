import sqlite3

""" for make table and input manual data """
conn = sqlite3.connect('Data.db') #connect db name Data.db
print "Connect : pass"
c= conn.cursor()    #prepare from modify db

# create table name user

# c.executescript("""DROP TABLE User""") #delete table
# c.executescript("""DELETE FROM subject WHERE Subject_ID = 'FRA142'""") #delete data in table subject
# c.executescript("""DELETE FROM work WHERE Subject_ID ='FRA222'""") #delete work

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


# create table name Group
try:
    c.executescript("""
    CREATE TABLE `Group` (
      `Subject_ID` varchar(45) NOT NULL,
      `Year` int(11) NOT NULL,
      `WorkID` int(11) NOT NULL,
      `ID` bigint(11) NOT NULL
    )""")
except Exception:
    print "Table group has created"


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


# insert data in User table
def UserInsert(ID, Password, Title, Name, Surname, E_mail, Role, Faculty, Major, Enrol_Year, Picture): #ID and Password aren't NULL
    c.execute("""INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enrol-Year`, `Picture`) VALUES
    (?,?,?,?,?,?,?,?,?,?,?);""",(ID, Password, Title, Name, Surname, E_mail, Role, Faculty, Major, Enrol_Year, Picture))

# insert data in Enrol table
def EnrolInsert(ID,Subject_ID,Subject_Year): #not NULL all
    c.execute("""INSERT INTO `Enrol` (`ID`, `Subject_ID`, `subject_Year`) VALUES
    (?, ?, ?);""",(ID,Subject_ID,Subject_Year))

#insert data in Group table
def groupInsert(Subject_ID,Year,WorkID,ID): #not NULL all
    c.execute("""INSERT INTO `group` (`Subject_ID`, `Year`, `WorkID`, `ID,) VALUES
     (?,?,?,?)""",(Subject_ID,Year,WorkID,ID))

#insert data in media table
def mediaInsert(Subject_ID,Year,Description,FullMark,Grading): #Subject_ID and Year aren't NULL
    c.execute("""INSERT INTO `media` (`Subject_ID`,`Year`,`Description`,`FullMark`,`Grading`) VALUES
     (?,?,?,?,?)""",(Subject_ID,Year,Description,FullMark,Grading))

#insert data in subject table
def subjectInsert(Subject_ID, Year, Description, FullMark, Grading): #Description, FullMark and Grading default are NULL
    c.execute("""INSERT INTO `subject` (`Subject_ID`, `Year`, `Description`, `FullMark`, `Grading`) VALUES
    (?,?,?,?,?);""",(Subject_ID,Year,Description,FullMark,Grading))

#insert data in Submitwork table
def subjectInsert(Subject_ID, Year, WorkID, ID, Address, Status, Mark): #Address, status and Mark default are NULL
    c.execute("""INSERT INTO `Submitwork` (`Subject_ID`, `Year`, `WorkID`, `ID`, `Address`, `Status`, `Mark`) VALUES
    (?,?,?,?,?,?,?);""",(Subject_ID, Year, WorkID, ID, Address, Status, Mark))

#insert data in work table
def workInsert(Subject_ID, Year, WorkID, Deadlines, status, type, FullMark, Grading, lim_member): #Subject_ID, Year, WorkID aren't NULL
    c.execute("""INSERT INTO `work` (`Subject_ID`, `Year`, `WorkID`, `Deadlines`, `status`, `type`, `FullMark`, `Grading`, `lim_member`) VALUES
    (?,?,?,?,?,?,?,?,?);""",(Subject_ID, Year, WorkID, Deadlines, status, type, FullMark, Grading, lim_member))


# UserInsert(ID='58340500005',Password='Boomming2*',Title='Mr.',Name='Kitti',Surname='Pongaksorn',E_mail='bosskitti7983@gmail.com',Role='student',Faculty='FIBO',Major='robotic and automation',Enrol_Year='58',Picture=None) #insert User
# subjectInsert(Subject_ID='FRA142',Year='59',Description=None,FullMark=None,Grading=None) #insert subject
# workInsert(Subject_ID='FRA221',Year='59',WorkID='6') # insert work
# EnrolInsert('58340500017','FRA221','59')


conn.commit() #save data into db
print("-----------User-----------")
cursor1 = c.execute("SELECT ID, Password from User") #choose table for search data
for row in cursor1:
    print "ID = ", row[0]
    print "Password = ", row[1]
print("-----------subject-----------")
cursor2 = c.execute("SELECT Subject_ID, Year, Description,FullMark, Grading from subject")
for row in cursor2:
    print "Subject ID = ",row[0]
    print "Year = ",row[1]
    print "Description = ",row[2]
    print "FullMark = ",row[3]
    print "Grading = ",row[4]
print("-----------work-----------")
cursor3 = c.execute("SELECT Subject_ID, Year, WorkID, FullMark from work")
for row in cursor3:
    print "Subject ID = ",row[0]
    print "Year = ",row[1]
    print "WorkID = ",row[2]
    print "FullMark = ",row[3]
print("-----------enrol-----------")
cursor4 = c.execute("SELECT ID, Subject_ID, subject_year from Enrol")
for row in cursor3:
    print "ID = ",row[0]
    print "Subject ID = ",row[1]
    print "Subject yaer = ",row[2]

cursor1.close()
cursor2.close()
cursor3.close()
cursor4.close()