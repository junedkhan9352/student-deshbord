from ..file.filehandling import*
def login():

    data=getdata()
    while True:
            e=input("enter a email:")
            p=input("enter your password: ")

            count=1
            try:
                for i in data:
                        if e==i["email"] and p==i["password"]:
                                count=0
                        break


                if count==0:
                    print("==========login sucessfully===========")
                    print(i)
                else: 
                    print("____________invalid___________") 
                
            except Exception as e:
                  print("login nhi ho sakta ")
    