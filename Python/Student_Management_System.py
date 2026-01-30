class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"
    
class StudentManagement:
    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        student = Student(roll, name, marks)

        with open("student.txt","r") as file:
            file.write(str(student)+ "\n")

        print("Student added successfully \n")


    def view_student(self):
        try:
            with open("student.txt", "r") as file:
                print("\n Roll | Name | Marks")
                for line in file:
                    roll, name, marks = line.strip().split(",")
        except FileNotFoundError:
            print("No student record found\n")


sms = StudentManagement()

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_student()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")






# # Creating objects
# s1 = Student("Rahul", 101, 35)
# s2 = Student("Anita", 102, 78)

# # Updating marks
# s1.add_marks(45)

# # Displaying student details
# s1.display_details()
# s2.display_details()