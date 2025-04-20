
# This program converts temperatures to either celicius or fahrenheit

def celsius():
    Cel = float(input("Enter the Celsius value: "))
    temp_Fah = (Cel * 1.8) + 32
    return temp_Fah

def fahrenheit():
    Fah = float(input("Enter the Fahrenheit value: "))
    cel_temp = (Fah - 32)/1.8
    return cel_temp

def main():
    print ("Welcome to The best Temperature converting program ")
    print ("---------------The temperature in balls------------")

    
    while True:
        print ("1. Fahrenheit")
        print ("2. Celsius")
        print ("3. Exit")
        option = int (input("What do you want to convert:"))

        
        if option == 1:
            while True:
                print ("You are converting from Celsius to Fahrenheit:")
                Ans = celsius()
                print (f"The temperature in Fahrenheit is {Ans}F")
                Continue = input ("Do you want to continue (y/n):")
                if Continue == "y":
                    print ("Welcome again----")

                elif Continue == "n":
                    print ("Am so glad i served you Hope to see you back bye !!------")
                    break

                else :
                    print ("invalid input !!!!!!!!! you MotherFucker!!!!!!!")

        elif option == 2:
            
            print ("You are converting from Fahrenheit to Celcius:")
            Ans = fahrenheit()
            print (f"The temperature in Celsius is {Ans}C")
            Continue = input ("Do you want to continue (y/n):")
            if Continue == "y":
                print ("Welcome again----")

            elif Continue == "n":
                print ("Am so glad i served you Hope to see you back bye !!------")
                break

            else :
                print ("invalid input !!!!!!!!! you MotherFucker!!!!!!!")

        elif option == 3:
            print ("Thank you for passing by see you soon bye ==========!!!!!!")
            break

        else :
            print (" !!!! Invalid choice !!!!! What is wrong with you motherFucker")

main()















                
