import string
import random

# --- Password Checker ---
def passchecker(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False
    has_special = False

    if len(password) < 8:
        print(" Password too short.")
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

    if not has_upper: print("Must have uppercase.")
    if not has_lower: print("Must have lowercase.")
    if not has_digit: print("Must have digit.")
    if not has_special: print("Must have special char.")
    if has_space: print("No spaces allowed.")

    if has_upper and has_lower and has_digit and has_special and not has_space and len(password) >= 8:
        print("Strong password!")
        return True
    else:
        return False

# --- Password Generator ---
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_list = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    for _ in range(length - 4):
        password_list.append(random.choice(all_chars))
    random.shuffle(password_list)
    return ''.join(password_list)

# --- User Class ---
class User:
    def __init__(self, name, account_number, password):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = 0

    def check_credentials(self, acc_no, pwd):
        return self.account_number == acc_no and self.password == pwd

    def change_password(self, new_pass):
        self.password = new_pass
        print("Password updated successfully!")

    def deposit(self, amnt):
        self.balance += amnt
        print(f"₹{amnt} deposited.")

    def withdraw(self, amnt):
        if amnt <= self.balance:
            self.balance -= amnt
            print(f"₹{amnt} withdrawn.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        print(f" Balance: ₹{self.balance}")

# --- ATM Class ---
class ATM:
    def __init__(self):
        self.user_db = {}  # key: account_number, value: User object
        self.logged_in_user = None

    def create_account(self):
        print(" Create New Account")
        name = input("Enter your name: ")
        acc_no = input("Create a 4-digit account number: ")

        if acc_no in self.user_db:
            print("Account number already exists!")
            return

        choice = input("Generate password? (yes/no): ").lower()
        if choice == "yes":
            password = generate_password()
            print("Generated password:", password)
        else:
            password = input("Enter your password: ")

        if not passchecker(password):
            print("Invalid password. Try again.")
            return

        new_user = User(name, acc_no, password)
        self.user_db[acc_no] = new_user
        print("Account created successfully!")

    def login(self):
        print("\n Login to ATM")
        acc_no = input("Enter your account number: ")
        password = input("Enter your password: ")

        user = self.user_db.get(acc_no)
        if user and user.check_credentials(acc_no, password):
            print(f"Welcome, {user.name}!")
            self.logged_in_user = user
            return True
        else:
            print("Invalid credentials!")
            return False

    def show_menu(self):
        while True:
            print("""
--- ATM MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Change Password
5. Logout
""")
            choice = input("Enter choice: ")
            if choice == "1":
                self.logged_in_user.get_balance()
            elif choice == "2":
                amnt = float(input("Enter deposit amount: "))
                self.logged_in_user.deposit(amnt)
            elif choice == "3":
                amnt = float(input("Enter withdrawal amount: "))
                self.logged_in_user.withdraw(amnt)
            elif choice == "4":
                new_pass = input("Enter new password: ")
                if passchecker(new_pass):
                    self.logged_in_user.change_password(new_pass)
            elif choice == "5":
                print(" Logged out successfully.")
                self.logged_in_user = None
                break
            else:
                print("Invalid option.")

    def run(self):
        while True:
            print("""
======== ATM SYSTEM ========
1. Create Account
2. Login
3. Exit
""")
            main_choice = input("Choose option: ")
            if main_choice == "1":
                self.create_account()
            elif main_choice == "2":
                if self.login():
                    self.show_menu()
            elif main_choice == "3":
                print(" Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid option.")

# --- Run the ATM ---
atm = ATM()
atm.run()
