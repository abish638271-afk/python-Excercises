import random
def game():
    a=random.randint(1,10)
    attempt=3
    while attempt>=0:
        b=int(input("Enter the number :"))
        if(b==a):
            print("You got the Correct answer")
            break
        elif(a>b):
           print("it is low")
        elif(a<b):
            print("it is high")
        else:
            print("invalid number")
        attempt-=1
        if attempt==0:
            print("try again")
        else:
            print("you have",attempt,"attempts left")
            print(" ")
        if(attempt==0 or b==a):
            inp=input("continue(c) or exit(e)")
            if inp=="e":
                break
            else:
                attempt=3
                
        
   
    