import os

def add_student(student_id :str , student_name :str , age :int , department : str , cgpa :float):
    if os.path.exists("students.txt"):
        with open("students.txt" , "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if student_id == parts[0].strip() and student_name.lower() == parts[1].strip().lower():
                    print(f"Student with ID {student_id} already exists.")
                    return

    with open("students.txt" , "a") as file:
        file.write(f"{student_id} | {student_name} | {age} | {department} | {cgpa}\n")
        print(f"Student {student_name} added successfully!")

   

def display_students():
    found = False
    with open("students.txt" , "r") as file:
        for line in file:
            print(line.strip())
            found = True
    if not found:
        print("No students found.")

def search_student(student_id :str):
    found = False
    with open("students.txt" , "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if student_id == parts[0].strip():

                print(line.strip())
                found = True
                break
    if not found:
        print(f"Student with ID {student_id} not found.")

#update just the cgpa of the student
def update_student_cgpa(student_name :str , new_cgpa :float):
    found = False
    with open("students.txt" , "r") as file:
        lines = file.readlines()
    
    with open("students.txt" , "w") as file:
        for line in lines:
            parts = line.strip().split("|")
            if student_name.lower() == parts[1].strip().lower():
                parts[4] = str(new_cgpa)
                found = True
            file.write("|".join(parts) + "\n")
    
    if found:
        print(f"Student {student_name}'s CGPA updated to {new_cgpa}.")
    else:
        print(f"Student {student_name} not found.")

def delete_student(student_name :str):
    found = False
    with open("students.txt" , "r") as file:
        lines = file.readlines()
    
    with open("students.txt" , "w") as file:
        for line in lines:
            parts = line.strip().split("|")
            if student_name.lower() != parts[1].strip().lower():
                file.write(line)
            else:
                found = True
    
    if found:
        print(f"Student {student_name} deleted successfully.")
    else:
        print(f"Student {student_name} not found.")



while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student CGPA")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        department = input("Enter student department: ")
        cgpa = float(input("Enter student CGPA: "))
        add_student(student_id, student_name, age, department, cgpa)
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_id = input("Enter student ID to search: ")
        search_student(search_id)
    elif choice == "4":
        update_name = input("Enter student name to update CGPA: ")
        new_cgpa = float(input("Enter new CGPA: "))
        update_student_cgpa(update_name, new_cgpa)
    elif choice == "5":
        delete_name = input("Enter student name to delete: ")
        delete_student(delete_name)
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        