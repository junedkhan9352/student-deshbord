from ..log.log import log_error
def valid_email(dict):
    try:
         
        while True:
            name = input("enter your name: ")
            if len(name)>=2 and name.isalpha():
                dict["name"] = name
                break
            else:
                print("invalid name")    
        while True:
                email=input("enter a email: ")
                if '@' in email and 'gmail.com' in email:
                    dict["email"]=email
                    break
                else:
                    print("invalid email try again")
                    

        while True:
                password=input("enter a password: ")
                if len(password)>4:
                    dict["password"]=password
                    break
                else:
    
                    print("invalid password")    
        
    except Exception as e:
        log_error(e)
    
    