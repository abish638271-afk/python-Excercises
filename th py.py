name=input("Enter the name:")
age=int(input("Enter the age:"))
a=int(input("Enter the mark:"))
b=int(input("Enter the mark:"))
c=int(input("Enter the mark:"))
print("Name:",name)
print("age:",age)

d=a+b+c
print("Total mark:",d)
ave=d//3
print("Average:",ave)
if(ave >85 and ave<100):
    print("first class")
elif(ave >65and ave<84):
    print("second class")
elif(ave >50and ave>64):
    print("third class")
elif(ave <50):
    print("fail")
else:
    print("Enter the valid mark")
        
        
