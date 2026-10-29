import datetime
from ..file.filehandling import*
from ..validation.validation import valid_email
from ..course.course import course
from..log.log import log_error
import uuid
def signup():
    try:    
        dict={}
        dict["id"]=uuid.uuid4().hex[:4]
        
        valid_email(dict)
        dict["mobile_no"]=input("enter your mobile no.")
        qualification=[]
        while True:
            q=input("enter your qualification:")
            qualification.append(q)
            choice=input("do you want to add new qualifictaion(y/n)")
            if choice=="n":
                break
        dict["qualification"]=qualification
        dict["course"]=course()
        now=datetime.datetime.now()
        date=now.strftime("%d/%m/%y")
        dict["date"]=date
        data=getdata()
        data.append(dict)
        putdata(data)
        print()
        print("----------course added succesfully----------")

        print("=======signup succesfull========")
    except Exception as e:
        log_error(e)
        print("signup nhi ho sakta ")
        