import students
def main():
    while True: 
        print("-----------student menu-----------")
        print("1.signup")
        print("2.login")
        print("3.search")
        print("4.exit")
        while True:
            ch=int(input("enter your choice: "))
            if ch==1:
                students.signup()
            elif ch==2:
                students.login()
            elif ch==3:
                students.search()
            elif ch>=4:    
                print("invalid choice")            
            break
         
main()
