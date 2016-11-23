import mysql.connector
#conn=mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='autohome')
conn=mysql.connector.connect(user='root', password='', host='172.16.34.36', database='pi_counter')

def insertStudent(qr):
    cursor=conn.cursor()    
    query=(qr)
    cursor.execute(query)
    result=cursor.fetchone()
    print result[0]

    


conn.close()
