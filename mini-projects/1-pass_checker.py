import string

def passchecker():
    password = input("Enter your password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False
    has_special = False

    if len(password) < 8:
        print(" Password length is too short (minimum 8 characters).")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            has_space = True
        elif char in string.punctuation:
            has_special = True

    if has_upper == False:
        print(" Password must contain at least one uppercase letter.")
    if has_lower == False:
        print(" Password must contain at least one lowercase letter.")
    if has_digit == False:
        print(" Password must contain at least one digit.")
    if has_special == False:
        print(" Password must contain at least one special character.")
    if has_space == True:
        print(" Password must NOT contain spaces.")

    if has_upper == True and has_lower == True and has_digit == True and has_special == True and has_space == False and len(password) >= 8:
        print(" Strong password!")

passchecker()
