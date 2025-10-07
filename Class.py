class student:
    def read(self,roll,name):
        roll=int(input("Enter the roll:"))
        name=input("Enter the name:")
        self.roll=roll
        self.name=name
        print("Student read")
    def write(self):
        print("student roll :",self.roll)
        print("student name :",self.name)
        print("Student write")

s1=student()
s2=student()
s1.read(12,"kumar")
s1.write()
s2.read(13,"selvi")
s2.write()