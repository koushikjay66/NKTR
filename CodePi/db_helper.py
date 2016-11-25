import mysql.connector

#This is for To open the Connection

def openConn():
    return mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='CSE360')
def openlocal():
    return mysql.connector.connect(user='root', password='root', host='localhost', database='pi_counter')

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

def getRoomtatus():
    conn = openlocal()
    #Remember There is no null check. So it cant be Null Means This value will always be set.
    sql = "SELECT rfid, ir FROM counter WHERE id = '13101206'"
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    result=cursor.fetchone()
    if not result:
        return "Error\nConcact for Help"
    else:
        rfid = result[0]
        ir=result[0]
        closeConn(conn)
        return "Attendace: "+str(rfid)+"\nIn Room: "+str(ir)



def updateRFIDCount():
    conn = openlocal()
    sql = "UPDATE counter SET rfid=rfid+1 WHERE id='13101206'"
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    conn.commit()
    closeConn(conn)



def decreaseIRCount():
    conn = openlocal()
    sql = "UPDATE counter SET ir=ir+1 WHERE id='13101206'"
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    conn.commit()
    closeConn(conn)


def increaseIRCount():
    conn = openlocal()
    sql = "UPDATE counter SET ir=ir-1 WHERE id='13101206'"
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    conn.commit()
    closeConn(conn)


def resetCount():
    conn = openlocal()
    sql = "UPDATE counter SET ir=0, rfid=0 WHERE id='13101206'"
    cursor=conn.cursor()    
    query=(sql)
    cursor.execute(query)
    conn.commit()
    closeConn(conn)

              
resetCount()

    
