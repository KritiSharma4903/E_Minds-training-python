class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.showA()
obj.showB()
obj.showC()
