# 📂 File Handling in Python
"""Today is exciting because until now, every program you've written forgets everything when it closes.

Example:

students = []

You add:

Usman
Ali
Ahmed

Then you close the program.

Open it again...

students = []

Everything is gone. 😅"""

"""🤔 Why?

Because variables live in RAM (memory).

RAM is temporary.

When the program ends:

RAM → ❌ Cleared
💡 Solution?

Store data in a file.

Example:

students.txt

Inside:

Usman
Ali
Ahmed

Even if you restart your computer...

The file is still there."""

"""🧠 Think Like a Developer

Without files:

Program
    │
    ▼
Memory
    │
Program Ends
    │
Everything Lost


With files:

Program
    │
    ▼
students.txt
    │
Program Ends
    │
File Still Exists ✅"""

# Types of Files
"""There are two types of files:
1️⃣ Text Files (e.g., .txt, .csv, .json)
2️⃣ Binary Files (e.g., .jpg, .png, .mp3)"""

""" we'll use

Text Files (.txt)

Examples:

notes.txt
students.txt
todo.txt
passwords.txt"""

#The open() Function
from genericpath import exists


file = open("students.txt") # Think of it like opening a notebook.If the notebook is closed...You can't read it.

# File Modes

#There are four you'll use 95% of the time.

#Mode	Meaning
#"r"	Read
#"w"	Write
#"a"	Append
#"x"	Create


#1️⃣ Read Mode
file = open("students.txt", "r") #Meaning:📖 I only want to read.Cannot write.

#Write Mode
file = open("students.txt", "w") #Meaning: ✍️ Write to the file.

#⚠ Important

#If the file already contains:

"""Usman
Ali
Ahmed"""

# After

open("students.txt","w") 

#Everything is erased  .

# 3️⃣ Append Mode
file = open("students.txt","a") #Meaning: Don't erase. Just add new data.

#Before:

#Usman
#Ali

#After appending

#Ahmed

#Result:

#Usman
#Ali
#Ahmed

# 4️⃣ Create Mode
open("students.txt","x") # Creates a new file. If the file already exists... Python gives an error.

# Last Step: Closing Files

#Always close the file.

file.close()

#Think of it like saving Word documents.

"""🧠 Easy Memory Trick
r = Read

w = Wipe + Write

a = Add

x = Create"""

# code 

file = open("students.txt" , "r")

file.read()
file.close()

file = open("students.txt" , "r")
print(file.read())

file = open("students.txt" , "r")
print(file.read(5)) #Reads first 5 characters

file = open("students.txt" , "r")
print(file.readline()) #Reads first line

file = open("students.txt" , "r")
print(file.readlines()) #Reads all lines and returns a list

file = open("students.txt" , "r")
for line in file:
    print(line)

file = open("students.txt" , "w")
file.write("New student: Sarah")
file.close()

file = open("students.txt" , "a")
file.write("\nNew student: John")
file.close()

file = open("students.txt" , "w")
file.write("New student: Ahmed ")
file.close()

file = open("students.txt" , "r")
print(file.read())

file.close()

msg = input("Enter your Notes: ")

file= open("notes.txt" , "a")
file.write(msg + "\n")
file.close()

print("Notes saved successfully!")

file = open("notes.txt" , "r")
print(file.read())
file.close()

name = input("Enter your name: ")
notes = input("Enter your notes: ")

file = open("notes.txt" , "a")
file.write(f"{name}: {notes}\n\n")
file.close()

print("Notes saved successfully!")

file = open("notes.txt" , "r")
print(file.read())
file.close()

#👨‍💻 Professional Way — with open()

#Instead of:

file = open("notes.txt", "r")

print(file.read())

file.close()

#Professionals write:

with open("notes.txt", "r") as file:
    print(file.read())

#Notice: No close().

#Python automatically closes the file.

#Why use with?

#Imagine this code:

file = open("notes.txt")

# Error happens here

file.close()

#If an error occurs before close(), the file may remain open.

#With:

"""with open("notes.txt") as file:"""

#Python guarantees the file is closed automatically.

#This is why almost every modern Python project uses with.

with open ("notes.txt", "a") as file:
    file.write("New note: Remember to drink water.\n")

with open ("notes.txt", "r") as file:
    print(file.read())

