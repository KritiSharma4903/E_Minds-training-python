class GrandParent:
    def house(self):
        print("GrandParent has a house")

class Parent(GrandParent):
    pass

class child(Parent):
    pass

c = child()
c.house()
