#Create Account or Login
# ATM program that allows users to create an account, login, check balance, deposit, and withdraw money.
# The program uses a dictionary to store user accounts and their balances.
# The program also includes a simple menu system for user interaction.
# The program is designed to be user-friendly and easy to navigate.
# The program uses functions to organize the code and make it more modular.
import random

print ("----Welcome to MyATM!----")
print ("-------------------------")

def create_account():
    #Create a user name
    #Create a password
    #Email address
    #Account number

    Full_name = input("Enter your full name: ")
    username = input("What is your desired username: ")
    password = input("Enter a password: ")
    email = input("Enter your email address: ")

    # Generate a random 10-digit number
    random_account_number = random.randint(10**9, 10**10 - 1)
    #print(f"Your randomly generated 10-digit number is: {random_account_number}")

    # Create a dictionary to store the account information
    User_Account = {
        "Full name": Full_name,
        "Username": username,
        "Password": password,
        "Email": email,
        "Account number": random_account_number,
        "Balance": 0.0
    }
    print("Account created successfully!")
    print(f"Your account number is: {random_account_number}")
  

    return User_Account

def login(accounts):
    #Login to your account
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for account in accounts:
        if account["Username"] == username and account["Password"] == password:
            print("Login successful!")
            return account

    print("Invalid username or password. Please try again.")
    return None

def display():
    print ("----Account infomation----")
    print (f"Full Name : {account_info['Full name']}")
    print (f"User Name : account_info[Username]")
    print (f"Email : account_info[Email]")
    print (f"Account Number : account_info[Account number]")
    print (f"Account Balance : account_info[]")
    print ("-------------------------")
    print ("----Account infomation----")


def account_info ():
    #Display account information
    def change_password(account):
        #Change password
        new_password = input("Enter a new password: ")
        account["Password"] = new_password
        print("Password changed successfully!")

    def change_email(account):
        #Change email address
        new_email = input("Enter a new email address: ")
        account["Email"] = new_email
        print("Email address changed successfully!")    

            

    return display()
def check_balance(account):
    #Check account balance
    print(f"Your current balance is: UGX {account['Balance']:.2f}")

def deposit(account):
    #Deposit money into account
    amount = float(input("Enter the amount to deposit: UGX "))
    if amount > 0:
        account["Balance"] += amount
        print(f"UGX {amount:.2f} deposited successfully!")
    else:
        print("Invalid deposit amount. Please try again.")

def withdraw(account):
    #Withdraw money from account
    amount = float(input("Enter the amount to withdraw: UGX "))
    if 0 < amount <= account["Balance"]:
        account["Balance"] -= amount
        print(f"UGX {amount:.2f} withdrawn successfully!")
    else:
        print("Invalid withdrawal amount. Please try again.")   

#main function
def main():
    accounts = []  # List to store user accounts
    while True:
        print("\n----ATM Menu----")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_info = create_account()
            accounts.append(account_info)
        elif choice == "2":
            account = login(accounts)
            if account:
                while True:
                    print("\n----Account Menu----")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Change Password")
                    print("5. Change Email Address")
                    print("6. Display Account Information")
                    print("7. Logout")
                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        check_balance(account)
                    elif account_choice == "2":
                        deposit(account)
                    elif account_choice == "3":
                        withdraw(account)
                    elif account_choice == "4":
                        change_password(account)
                    elif account_choice == "5":
                        change_email(account)
                    elif account_choice == "6":
                        display()
                    elif account_choice == "7":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Thank you for using MyATM!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main ()
