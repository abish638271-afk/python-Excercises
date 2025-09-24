lp=""
while(lp!="q"):
    a=int(input("A:"))
    b=int(input("B:"))
    operation=input("add/sub/mul/div:")
    def calculator(a,b):
        if(operation=="+"):
            print(a+b)
        elif(operation=="-"):
            print(a-b)
        elif(operation=="*"):
            print(a*b)
        elif(operation=="/"):
            if(b==0):
                print("invalid number")
            else:
                print(a/b)
        else:
            print("invalid")

    calculator(a,b)
    lp=input("Quit or Again :")