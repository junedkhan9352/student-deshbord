
def course():
    print(".........add your course..........")
    print("1.full stack developer")
    print("2.cyber security")
    print("3.data scintiest")
    print("4.ai & machine learning")

    ch=int(input("enter your choice: "))
    if ch==1:
        return "full stack develovper"
    elif ch==2:    
        return "cyber securty"
    elif ch==3:
        return "data scinctiest"
    elif ch==4:    
        return "AI & Machin learning"
    elif ch>=5:
        print("invalid choice")           