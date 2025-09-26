import Numbergame
print("welcome to game !")
while True:
    pas=1234
    pas=int(input("Enter the password :"))
    if(pas!=1234):
        print("Enter the valid password")
    else:
        print("correct correct password")
        Numbergame.game()
        break
