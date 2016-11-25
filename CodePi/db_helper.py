<<<<<<< HEAD
import mysql.connector

#This is for To open the Connection

def openConn():
    return mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='CSE360')


#This function is for Closing the Connection

def closeConn(connection):
    connection.close()


#This method is for getting the name from the RFID

def getName(UID):
    conn = openConn()
    sql = "SELECT name from student where rfid=\""+UID+"\""
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    result=cursor.fetchone()
    if not result:
        return "Sorry\nInvalid ID"
    else:
        res = result[0];
        closeConn(conn)
        return "Welcome\n"+res


#This method is for getting the Current Student and Current People in Room Status It uses a local Database Buit in pi

def getCurrentStatus():
    conn = mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='CSE360')


=======
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


>>>>>>> 7d39dfe55b645f3bbb0ebf2eab49bde47f466fe8
