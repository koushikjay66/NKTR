import requests
def getCourse():
    slot = requests.get("http://192.168.1.116/NKTR/getCourseid/getcourse.php")
    if slot.status_code!=200:
        return "error"
    else:
       return slot.content

def getDate():
    date=requests.get("http://192.168.1.116/NKTR/getCourseid/getDate.php")
    return date.content
