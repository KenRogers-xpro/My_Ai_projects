students_accounts =[{"Name":"Ken", "StdNumber":"1234"}]
# print(students_accounts)

def check_name():
    std_number  = input("Enter student number : ")

    for Student in students_accounts:
        if Student["StdNumber"] == std_number:
            name = Student["Name"]
            print (f"The name is {name}")
            return Student

    print ("Student doesn't exist!!!!")   
    return None 
def login():
    std_name = input("Enter student's Name :")
    std_number = input("Enter student number :")

    for student in students_accounts:
        if (student["StdNumber"] == std_number):
            print ("welcome, you have successfully logged in")
            return student

    print("Invalid student")
    return None
    

def create_account():
    std_name = input("Enter student's Name :")
    std_number = input("Enter student number :")
    std_email = input("Enter student's email :")
    index_number = input("Enter student's Index number :")

    for Student in students_accounts:
        if std_number == Student["StdNumber"]:
            print("Already registered !!!! just Login")
            login()
            
    
    student = {
        "Name": std_name,
        "StdNumber": std_number,
        "Email": std_email,
        "StdIndex": index_number
    }
    students_accounts.append(student)
    print ("You are successfully registered you can now login")
    print (students_accounts)
    login()


    #This program is supposed to deal with dictionaries
print ("what do you want to do (choose the options below) ")
print ("1.Login (1)")
print ("2.register (2)")
print ("3.Check name (3)")
action = int (input("enter here: "))
if (action == 1):
    login()

elif (action == 3):
    check_name()    
else:
    create_account()







