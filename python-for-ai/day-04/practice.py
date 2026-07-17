def show_menu():
    print ("====================================")
    print("Student Record Management System")
    print("====================================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")
    print("====================================")

def add_student(student_records, count):
    count += 1
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter student department: ")
    cgpa = float(input("Enter student CGPA: "))

    student = {
        "Student ID": count,
        "name": name,
        "age": age,
        "department": department,
        "cgpa": cgpa
    }

    student_records.append(student)
    print("Student added successfully!")

def display_students(student_records):
    if len(student_records) == 0:
        print("No student records found.")
    else:
        print("Student Records:")
        for s in student_records:
            for key, value in s.items():
                print(f"{key}: {value}")
            print("--------------------")
def search_student(student_records):
    found = False
    search = input("Enter the name to search: ")
    for s in student_records:
        if search == s["name"]:
            print("Student record found:")
            for key , value in s.items():
                    print(f"{key} : { value}")
            found = True
    if not found:
        print("Student record not found.")

def update_student(student_records):
    found = False
    upd = input("Enter the name to update ")
    for s in student_records:
        if upd == s["name"]:
            upg_cgpa = float(input("Enter the cgpa to update "))
            s["cgpa"] = upg_cgpa
            print("CGPA updated successfully!")
            found = True
            break

    if not found:
        print("CGPA not updated due to record not found")

def delete_student(student_records):
    found = False
    del_name = input("Enter the name to delete: ")
    for s in student_records:
        if del_name == s["name"]:
            student_records.remove(s)
            print("Student record deleted successfully!")
            found = True
            break

    if not found:
        print("Student record not found. Deletion failed.")
def count_students(student_records):
    print(f"Total number of students: {len(student_records)}")

student_records = []
count = 0

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_student(student_records, count)
        count += 1
    elif choice == "2":
        display_students(student_records)
    elif choice == "3":
        search_student(student_records)
    elif choice == "4":
        update_student(student_records)
    elif choice == "5":
        delete_student(student_records)
    elif choice == "6":
        count_students(student_records)
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

