
#create the connector object
'''import mysql.connector
try:
    conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="sriram")
    print('connection success')
except:
    print('connection failure')

cur=conn.cursor()

cur.execute("show tables")
res=cur.fetchall()
for x in res:
    print(x)
conn.close()'''
#select * command
import mysql.connector
try:
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='sriram')
    print('connection success')

except:
    print('connection failed')
cur=conn.cursor()
'''cur.execute('select * from students')
res=cur.fetchall()
for x in res:
    print(x)
conn.close()'''

try:
    cur.execute("select * from students")
    res=cur.fetchall()
    print(str(res)+'\n\n')

    for x in res:
        print ("hello "+str(x[1]) +" your id is "+ str(x[0]))
except:
    print("something went wrong")
    
        
