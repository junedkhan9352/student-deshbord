import json
from ..log.log import log_error
def getdata():
   try: 
      with open("students/data/data.json", "r") as file:
        data= json.load(file)
        return data
   except Exception as e:
      log_error(e)

      
      

def putdata(data):
    try:
        with open("students/data/data.json","w")as file:
           json.dump(data,file,indent=4)
    
    except Exception as e:
       log_error(e)
       print("try agian")        