print ("Welcome to the Pay Slip")
print ("-------------------------")

teacher_name = input ("Lectuerer's Name :")
fuculty = input ("Enter Lectuerer's faculty :")
hours = int(input("Enter the amount  :"))

def GrossPay ():
    payPerHr = 50000
    return hours * payPerHr

def deduction ():
    Nssf = GrossPay() * 0.15
    Sacco = GrossPay() * 0.05
    return Nssf + Sacco

def finalPay ():
    return GrossPay() - deduction()

def display ():
    print (f"Lecturer's Name : {teacher_name}")
    print (f"Lecturer's Faculty : {fuculty}")
    print (f"  --Gross Pay : {GrossPay()}")
    print (f"  --Deduction : {deduction()}")
    print (f"Final Pay : {finalPay()}")

display()


