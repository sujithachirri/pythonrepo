import pyodbc

#connecting sql server to database and pycham
#here we create table in pycham and table will create in database
server = 'HCL-02-NEW-15\SQLEXPRESS'
database = 'filesearchresult4'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
#to avoid exceptional errors we use exceptions here
class alreadyexists(Exception):
    pass

class Employee_schema:
    def Employee(self):
        try:
            details=cursor.execute('''select *from employee_table''')
            if(not (details)):
                query_2=cursor.execute(''' use filesearchresult4''')
                query_3=cursor.execute('''create table employee_table
                (
                 nameofemployee varchar(50),
                 salary int,
                 project varchar(50)
                )
                ''')
                query_1=cursor.execute(''' select *from employee_table ''')
                cnxn.commit()
            else:
                raise alreadyexists
        except alreadyexists:
            print("table already created")

# obj=Employee_schema()
# obj.Employee()
