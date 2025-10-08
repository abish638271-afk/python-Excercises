class A:
    def __init__(self):
        a=50
        b=39
        print(a+b)
    
class B(A):
    def add(self):
        c=20
        d=10
        print(c-d)
        
class C(B):
    def sub2(self):
       self.add()
sub=C()
sub.sub2()              
