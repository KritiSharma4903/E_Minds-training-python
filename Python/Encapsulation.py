class student:
    def __init__(self):
        self.marks = 0

    def set_marks(self,marks):
        if marks >= 0:
            self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
s1 = student()
s1.set_marks(85)

print("Marks: ", s1.get_marks())


