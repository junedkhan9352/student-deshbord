from..file.filehandling import getdata
def search():
    print("1. Name to search: ")
    print("2. Email to search: ")
    print("3. course to search: ")

    ch =int(input("Enter your choice: "))

    if ch == 1:
        name=input("enter a name: ")
        data = getdata()
        for i in data:
            if i["name"] == name:
                print(i)
                break
              
        else:
            print("=====invalid name=====")  

    elif ch==2:
         email=input("enter a email: ")
         data = getdata()
         for i in data: 
            if i["email"]==email:
                print(i)
                break
         else:
            print("-----invalid student-----")
    elif ch==3:
        course=input("enter a course: ")
        data = getdata()
        for i in data:
            if i["course"]==course:
                print(i)
                break
        else:
            print("=====search un succesfull======")