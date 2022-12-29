import pyodbc

#connecting pycham and database using sql server
server = 'HCL-02-NEW-15\SQLEXPRESS'
database = 'filesearchresult4'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
#using exceptions to avoid exceptional errors
class alreadyexists(Exception):
    pass

class Employee_schema:
    def Employee(self):
#The try statement specifies exception handlers and/or cleanup code for a group of statements:
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
                raise alreadyexists   #If no expressions are present, raise re-raises the last exception that was active in the current scope.
        except alreadyexists:   #The except clause(s) specify one or more exception handlers.
            print("table already created")
