print("Dear User, \nIt is advisable that you insert at least a student's three names...")

students = []

def add_student():
    student_name = input("Enter Student Name: ")
    student_age = input("Enter Student Age: ")
    student_class = input("Enter Student Class: ")

    if student_name in  students:
        print("This name already exists!")
    else:
        students.append(student_name + " : " + student_age + " : " + student_class)
        print(student_name + " has been added successfully")

def remove_student():
    student_name = input("Enter Student Name: ")
    student_age = input("Enter Student Age: ")
    student_class = input("Enter Student Class: ")
    
    if student_name not in students:
        print(student_name + " Not Found!")
    else:
        students.remove(student_name + " : " + student_age + " : " + student_class)
        print("Delete Successful!" + student_name + " has been removed!")

def view_students():
    for student in students:
        print(student)

is_active = True

while is_active:
    try:
        print("")
        print("1. Add Students")
        print("2. Remove Students")
        print("3. View all Students")
        print("4. Exit App")

        print("")

        choice = input("Select an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("Exiting application... ")
            is_active = False
        else:
            print("Invalid Selection!")
    except ValueError:
        print("Invalid Parameters!")