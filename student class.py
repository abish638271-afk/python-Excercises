class student:
    def read(self,roll,name,math,comp,phys):
        self.roll=roll
        self.name=name
        self.math=math
        self.comp=comp
        self.phys=phys
    def cal(self):
        self.total=self.math+self.comp+self.phys
        self.ave=self.total/3
         
    def disp(self):
        print("student roll is :",self.roll)
        print("student name is :",self.name)
        print("total mark :",self.total)
        print("average mark:",self.ave)
students=[]
for i in range(3):
    print("Enter the details of students",i+1:")
    roll=int(input("Enter the roll:"))
    name=input("Enter the name :")
    math=int(input("Enter the mark: "))
    comp=int(input("Enter the mark: "))
    phys=int(input("Enter the mark: "))
    marks=[]
    for j in range(3):
        marks=int(input("Enter the marks"))
        marks.append(marks)
        
    students=student(name,marks)
    students.append(student)

print("\n student.report:")
for student in students:
    student.display

        
