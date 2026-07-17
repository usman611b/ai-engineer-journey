student_records = []
count = 0

while True:
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
    choice = input("Enter your choice (1-7): ") 
    if choice == "1":
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
    elif choice == "2":
        if len(student_records) == 0:
            print("No student records found.")
        else:
            print("Student Records:")
            for s in student_records:
                for key, value in s.items():
                    print(f"{key}: {value}")
                print("--------------------")
    elif choice == "3":
        found = False
        search = input("Enter the name to search")
        for s in student_records:
            if search == s["name"]:
                print("Student record found:")
                for key , value in s.items():
                        print(f"{key} : { value}")
                        found = True
        if not found:
            print("Student record not found.")
    elif choice == "4":       
        found = False
        upd = input("Enter the name to update ")
        for s in student_records:
                    if upd == s["name"]:
                        upg_cgpa = input("Enter the cgpa to update ")
                        s["cgpa"] = upg_cgpa
                        print("CGPA updated successfully!")
                        found = True
                        break

        if not found:
            print("CGPA not updated due to record not found")
    elif choice == "5":
        found = False
        del_stu = input("Enter the name to delete ")
        for s in student_records:
            if del_stu == s["name"]:
                student_records.remove(s)
                print("Student record deleted successfully!")
                found = True
                break

        if not found:
            print("Student record not found.")

    elif choice == "6":
        print(f"Total number of students: {len(student_records)}")

    elif choice == "7":
        print("Exiting the program.")
        break



