import requests
def getCourse():
    slot = requests.get("http://172.16.34.36/NKTR/getCourseid/getcourse.php")
    if slot.status_code!=200:
        return "error"
    else:
       print slot.content
       return slot.content

def getDate():
    date=requests.get("http://172.16.34.36/NKTR/getCourseid/getDate.php")
    print date
    return date.content
#getCourse()
