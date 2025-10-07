class car:
    def __init__(self,brand):
        self.brand=brand
        
c=car("Toyata")
print(c.brand)

class bank:
    def __init__(self):
        self.balance=1000
    def get_balance(self):
        return self.balance
b=bank()
print(b.get_balance())
print(b.balance)
