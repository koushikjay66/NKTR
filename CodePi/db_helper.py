import mysql.connector
conn=mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='CSE360')

def getName(UID):
    sql = "SELECT name from student where rfid=\""+UID+"\""
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    result=cursor.fetchone()
    return result[0]

conn.close()


