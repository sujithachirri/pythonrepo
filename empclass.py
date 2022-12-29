import pyodbc
import empschema

#connecting pycharm and database using sql server
server = 'HCL-02-NEW-15\SQLEXPRESS'
database = 'filesearchresult4'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
#using exception to avoid exceptional errors
class Existing(Exception):
    pass

class Employeeid:
        Bonus=2
        Project=['python','c','java']
        def __init__(self,nameofemployee,salary,project):
            self.nameofemployee=nameofemployee
            self.salary=salary
            self.project=project
        def display_employee(self):
            query = ''' 
                    INSERT INTO employee_table (nameofemployee, salary, project)
                    VALUES
                    ('{0}',{1},'{2}')  '''
            insertQuery = query.format(self.nameofemployee,self.salary,self.project)

            print(insertQuery)
            cursor.execute(insertQuery)
            query5=cursor.execute('''select *from employee_table''')
            cnxn.commit()

        def update_salary(self,update_salary,nameofemployee):
            try:   #The try statement specifies exception handlers and/or cleanup code for a group of statements:
                self.update_salary=update_salary
                self.nameofemployee=nameofemployee
                if self.update_salary!=self.salary:
                    query6 = '''
                        update employee_table SET salary='{0}' WHERE nameofemployee='{1}'
                        '''
                    update_query6 =query6.format(self.update_salary,self.nameofemployee)
                    cursor.execute(update_query6)
                    cursor.commit()
                else:
                    raise Existing
            except Existing:  #The except clause(s) specify one or more exception handlers.
                print("no change in your salary")
        def change_project(self,project,nameofemployee):
            self.project=project
            self.nameofemployee=nameofemployee
            if self.project in self.Project:
                if self.project==self.Project:
                    print("project already exists ")
                else:
                    query8='''
                           update employee_table SET Project='{0}' WHERE nameofemployee='{1}'
                    '''
            else:
                print("project is not in the list")
        def Add_bonus(self,bonus,nameofemployee):
            self.bonus=bonus
            self.nameofemployee=nameofemployee
            if self.bonus==self.Bonus:
                self.salary=self.salary+self.salary*self.bonus
                query9='''
               update employee_table SET salary='{0}' WHERE nameofemployee='{1}'
               '''
                change_query=query9.format(self.salary,self.nameofemployee)
                cursor.execute(change_query)
                cursor.commit()
            else:
                self.salary=self.salary+self.salary*self.Bonus
                query12='''
                update employee_table SET Bonus='{0}' WHERE nameofemployee='{1}'
                '''
                change_query12 = query12.format(self.salary, self.nameofemployee)
                cursor.execute(change_query12)
                cursor.commit()
        def display_details(self):
            query15='''select *from employee_table WHERE nameofemployee='{0}' '''
            query13=query.format(self.nameofemployee)
            values=cursor.execute(query13)
            for details in values:
                print("nameofemployee:{0}  salary:{1}  Project:{2}".format(details.nameofemployee,details.salary,details.Project))

obj=Employeeid('rohi',40000,'c')
ob1=empschema.Employee_schema()
ob1.Employee()
obj.display_employee()
obj.update_salary(35000,'rohith')
obj.change_project('java','mini')
obj.Add_bonus(2,'rohi')







