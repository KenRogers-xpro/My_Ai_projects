# this program is supposed to check password validity
# it checks for the following conditions
# 1. Password should be at least 8 characters long
# 2. Password should have at least one uppercase letter
# 3. Password should have at least one digit
# Feel free to test your balls off with this code

def valid_password():
    print ("Welcome to the password validator")
    print ("-------------------------------------")

    while True:
        user_password = input("Enter your password:")

        IsEightCharacters = True
        IsDigit = True
        IsUppercase = True
        Count_Char = 0
        Count_Upper = 0
        Count_Digit = 0

        for letter in user_password:
            Count_Char = Count_Char+1
            if letter.isupper():
                Count_Upper = Count_Upper + 1


            if letter.isdigit():
                Count_Digit = Count_Digit + 1
                # print (Count_Char)
                # print (letter)

        if Count_Char >= 8:
            IsEightCharacters

        else:
            print ("Password Should Have Eight characters atleast!!!")
            IsEightCharacters = False

        if Count_Upper > 0:
            IsUppercase

        else :
            print ("Password Should Have an uppercase character atleast!!!")
            IsUppercase = False


        if Count_Digit > 0:
            IsDigit
        else:
            print ("Password Should Have one number atleast!!!")
            IsDigit = False

        if IsDigit and IsEightCharacters and IsUppercase :
            print ("Your Password is strong")
            cont = input("Would you like to test other passwords (y/n):")
            if cont == "y":
                valid_password()
            else:
                print ("Thanks for using the password validator")
                break



        # elif IsDigit and IsEightCharacters and IsUppercase=False :
        #     print ("Your Password is strong")
        else:
            print (" --------Weak password!!!!!-----------")
            print (" -------------------------------------")
            print (" Try again with a better password!!!!!")



valid_password()