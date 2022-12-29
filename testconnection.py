import pyodbc

server ='HCL-02-NEW-15\SQLEXPRESS'
database='FileSearchResult2'
username='capstone'
password='Capstone@123'

cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(cnxn)
cursor=cnxn.cursor()
print(cursor)

cursor.execute('''
                INSERT INTO FileSearchResult2_table(File_Location,SearchCount,NameOfFile)
               VALUES
               ('ro.txt',2,'suji'),
               ('E:\mainfolder\suji1\suji2\suji3',4,'demotext.txt')
                ''')
cnxn.commit()

Values=cursor.execute('select*from FileSearchResult2_table')
for i in Values:
    print(i)
