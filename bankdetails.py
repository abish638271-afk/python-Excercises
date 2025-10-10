import json
import os
DATA_FILE ="bankdetails.json"

details={}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as f:
            return json.load(f)
        return{}
def add_account():
    name=int(input("Enter your pin : "))
    if name in details:
        print("Account with name:",name,"already exists")
    else:
        pin=int(input("Enter Your pin : "))
        balance=float(input("Enter Initial balance: "))
        details[name]={'pin':pin,'balance':balance}
        with open(DATA_FILE, 'w')as f:
            json.dump(details,f)
        print("account for :",name,"added successfully.")
        return details 
    print(load_data())
    print(add_account())
    print("Program started successfully!")