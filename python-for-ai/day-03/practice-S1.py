# 🎓 Student Management System (Console-Based)
"""
Using everything you've learned about lists.

Features:

➕ Add Student (append)
📋 Display Students (for)
🔍 Search Student (in)
❌ Remove Student (remove)
📊 Count Students (len)
🔤 Sort Students (sort)
🔄 Reverse List (reverse)
🚪 Exit Program

This project will combine almost every list concept into one application.

"""
students = []

while True:
    

    print("------------------------------------------------")
    print("Welcome to the Student Management System!")
    print("press 1 to Add Student")
    print("press 2 to Display Students")
    print("press 3 to Search Student")
    print("press 4 to Remove Student")
    print("press 5 to Count Students")
    print("press 6 to Sort Students")
    print("press 7 to Reverse List")
    print("press 8 to Exit Program")
    print("------------------------------------------------")  

    choice = int(input("Enter your choice (1-8): "))
    
    if choice == 1:
        name = input("Enter the name of Student to add !")
        students.append(name)
        print(f"{name} is added to the Students List")
    elif choice == 2:
        for i in range(len(students)):
            print(f"Student {i} = {students[i]}")
    elif choice == 3:
        name = input("Enter the name of student to search !")
        if name in students:
            print(f"Student {name} is present in the list!")
        else:
            print(f"Student {name} is not present in the list!")

    elif choice == 4:
        name = input("Enter the name of student to remove !")
        if name in students:
           students.remove(name)
           print(f"Student {name} is removed from the list!")
        else:
            print(f"Student {name} is not present in the list!")
    elif choice == 5:
        print(len(students))
    elif choice == 6:
        students.sort()
        print("Students sorted!")
    elif choice == 7:
        students.reverse()
        print("List reversed!")
    elif choice == 8:
        print("Exiting the program. Goodbye!")

        


        


