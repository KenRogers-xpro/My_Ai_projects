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
    print(f"Your randomly generated 10-digit number is: {random_account_number}")
create_account()

