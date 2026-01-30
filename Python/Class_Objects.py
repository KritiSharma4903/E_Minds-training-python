class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks 

    def add_marks(self,marks):
        self.marks = marks

    def is_passed(self):
        if self.marks >= 40:
            return "Passed"
        else:
            return "Fail"
        
    def display_details(self):
        print("Name: ", self.name)
        print("roll_no: ", self.roll_no)
        print("marks: ", self.marks)
        print("Result: ", self.is_passed())

# s = Student()
s = Student("kriti", 5, 38)

s.add_marks(78)

s.display_details()






