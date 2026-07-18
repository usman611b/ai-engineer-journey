#String mini project
password = input("Enter your password: ")
is_digit = False
is_upper = False
is_lower = False

for i in password:
    if i.isdigit():
        is_digit = True
    if i.isupper():
        is_upper = True
    if i.islower():
        is_lower = True

if is_digit and is_upper and is_lower and len(password) >= 8:
    print("Password is valid.")
else:
    print("Password is not valid.")

#Email Validator
cont = False
string = False


email = input("Enter your email: ")
at = email.find("@")
dot = email.rfind(".")

username = email[:at]
domain = email[at+1:dot]
domain_extension = email[dot+1:]


if email.count("@") == 1 and email.count(".") >= 1:
    cont = True

if   len(username) > 0 and len(domain) > 0 and len(domain_extension) >= 2:
    string = True

    
   

if cont and string:
    print("Email is valid.")
else:
    print("Email is not valid.")

