import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HCL-02-NEW-15\SQLEXPRESS;'
                      'Database=FileSearchResults;' 
                      'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('''
                INSERT INTO FileSearchResults_table (File_Location,SearchCount,NameOfFile)
                VALUES
                ("E:\mainfolder\suji1\suji2\suji3\demotext.txt")
                "E:\mainfolder\suji1\suji2\suji3\suji4\suji5\roo23\mini1\min.txt.txt"
                ''')
conn.commit();
cursor.execute('Select* From filesearchresults_table')
# file_input='demotext.txt'
# for i in cursor: