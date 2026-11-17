
class student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks

    def display(self):
        print("Student name =", self.name)
        print("Student USN =", self.usn)
        print("Student marks =", self.marks)


class studentmanagement:
    def __init__(self):
        self.student = []

    # Add student
    def add_student(self):
        usn = input("Enter the USN: ")

        for s in self.student:
            if s.usn == usn:
                print("USN already exists!")
                return

        name = input("Enter the name: ")
        marks = float(input("Enter the marks: "))

        s = student(name, usn, marks)
        self.student.append(s)

        print("Student added successfully!!")

    # View all students
    def view_student(self):
        if len(self.student) == 0:
            print("Students not found!!")
            return

        print("\n----- STUDENT DETAILS -----")

        for s in self.student:
            s.display()
            print("--------------------------")

    # Search student
    def search_student(self):
        usn = input("Enter the USN: ")

        for s in self.student:
            if s.usn == usn:
                print("\nStudent found!")
                s.display()
                return

        print("Student not found!")

    # Delete student
    def delete_student(self):
        usn = input("Enter the USN of the student: ")

        for s in self.student:
            if s.usn == usn:
                self.student.remove(s)
                print("Student removed successfully!")
                return

        print("Student not found!")


# Main program
sm = studentmanagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sm.add_student()

    elif choice == 2:
        sm.view_student()

    elif choice == 3:
        sm.search_student()

    elif choice == 4:
        sm.delete_student()

    elif choice == 5:
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
