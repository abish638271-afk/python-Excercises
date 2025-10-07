height=float(input("Enter the height"))
weight=float(input("Enter the weight"))
def calc():
    bm1=(weight/height**2)
    bm2=float(input
              
    print ("your bmi is",bmi)

    if bmi<=18.4:
        print("Under weight")
    elif bmi>=18.5 and bmi<=24.9:
        print("Normal weight")
    elif bmi>=25.0 and bmi<=39.9:
        print("average weight")
    else:
        print("obesity")
